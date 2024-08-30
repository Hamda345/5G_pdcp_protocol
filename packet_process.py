from header import PDCPHeader
from compression import ROHCCompressor, ROHCProfile, ROHCMode
from security import PDCPSecurity

class PDCP:
    def __init__(self, profile=ROHCProfile.IP, mode=ROHCMode.UNIDIRECTIONAL):
        self.pdcp_header = PDCPHeader()
        self.rohc_compressor = ROHCCompressor(profile, mode)
        self.security = PDCPSecurity()
        self.sn = 0  # PDCP sequence number

    def set_rohc_profile(self, profile, mode):
        """Set ROHC profile and mode."""
        self.rohc_compressor = ROHCCompressor(profile, mode)

    def initialize_security(self, bearer, direction):
        """Initialize security parameters."""
        self.security.generate_key()
        self.security.set_parameters(bearer, direction)

    def process_packet(self, ip_packet: bytes, sn_length: int) -> bytes:
        """Process and prepare a PDCP PDU from an IP packet."""
        try:
            compressed_packet = self.rohc_compressor.compress(ip_packet)
            protected_packet = self.security.protect(compressed_packet)
            pdcp_header = self.pdcp_header.create_data_pdu_header(self.sn, sn_length)
            self.sn = (self.sn + 1) % (2**sn_length)
            pdcp_pdu = pdcp_header + protected_packet
            print("Processed PDCP PDU:", pdcp_pdu)
            return pdcp_pdu
        except Exception as e:
            print(f"Error processing packet: {str(e)}")
            raise

    def process_received_packet(self, pdcp_pdu: bytes, sn_length: int) -> bytes:
        """Process the received PDCP PDU and extract the original IP packet."""
        try:
            header_info = self.pdcp_header.parse_header(pdcp_pdu[:3])
            if header_info['pdu_type'] != 'Data':
                raise ValueError("Received PDU is not a Data PDU")
            if header_info['sn_length'] != sn_length:
                raise ValueError(f"Received SN length ({header_info['sn_length']}) does not match expected SN length ({sn_length})")
            header_length = 2 if sn_length == 12 else 3
            protected_packet = pdcp_pdu[header_length:]
            unprotected_packet = self.security.unprotect(protected_packet)
            original_ip_packet = self.rohc_compressor.decompress(unprotected_packet)
            return original_ip_packet
        except Exception as e:
            print(f"Error processing received packet: {str(e)}")
            raise

    def reset_rohc_context(self):
        """Reset the ROHC context."""
        self.rohc_compressor.context_timeout()

    def get_state_info(self):
        """Get current state information of PDCP."""
        return {
            "ROHC Compressor Profile": self.rohc_compressor.profile,
            "ROHC Compressor Mode": self.rohc_compressor.mode,
            "Security Bearer": self.security.bearer,
            "Security Direction": "Uplink" if self.security.direction == 0 else "Downlink",
            "PDCP Count": self.security.count,
            "PDCP SN": self.sn
        }

