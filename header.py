class PDCPHeader:
    def create_data_pdu_header(self, sn, sn_length):
        """Create a PDCP Data PDU header with sequence number and length."""
        header = bytearray()
        header.append((sn >> 8) & 0xFF)  # High byte of sequence number
        header.append(sn & 0xFF)         # Low byte of sequence number
        header.append(sn_length)          # Sequence number length
        return header

    def parse_header(self, header_bytes):
        """Parse the PDCP header to extract sequence number and length."""
        sn = (header_bytes[0] << 8) | header_bytes[1]
        sn_length = header_bytes[2]
        return {'sn': sn, 'sn_length': sn_length, 'pdu_type': 'Data'}

    def create_control_pdu_header(self, control_type):
        """Create a PDCP Control PDU header."""
        header = bytearray()
        header.append(control_type)  # Control type
        return header

    def parse_control_header(self, header_bytes):
        """Parse the Control PDU header."""
        control_type = header_bytes[0]
        return {'control_type': control_type}
