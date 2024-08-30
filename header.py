import logging

class PDCPHeader:
    def create_data_pdu_header(self, sn, sn_length):
        """Create a PDCP Data PDU header with sequence number and length."""
        try:
            header = bytearray([
                (sn >> 8) & 0xFF,  # High byte of sequence number
                sn & 0xFF,         # Low byte of sequence number
                sn_length          # Sequence number length
            ])
            logging.debug(f"Created data PDU header with SN: {sn}, Length: {sn_length}.")
            return header
        except Exception as e:
            logging.error(f"Error creating data PDU header: {str(e)}")
            raise

    def parse_header(self, header_bytes):
        """Parse the PDCP header to extract sequence number and length."""
        try:
            sn = (header_bytes[0] << 8) | header_bytes[1]
            sn_length = header_bytes[2]
            logging.debug(f"Parsed PDCP header -> SN: {sn}, SN Length: {sn_length}.")
            return {'sn': sn, 'sn_length': sn_length, 'pdu_type': 'Data'}
        except Exception as e:
            logging.error(f"Error parsing PDCP header: {str(e)}")
            raise

    def create_control_pdu_header(self, control_type):
        """Create a PDCP Control PDU header."""
        header = bytearray([control_type])
        logging.debug(f"Created control PDU header with Control Type: {control_type}.")
        return header

    def parse_control_header(self, header_bytes):
        """Parse the Control PDU header."""
        control_type = header_bytes[0]
        logging.debug(f"Parsed control header with Control Type: {control_type}.")
        return {'control_type': control_type}
