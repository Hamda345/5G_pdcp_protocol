class ControlPDU:
    def create_control_pdu(self, control_type, payload):
        """Create a Control PDU."""
        header = bytearray()
        header.append(control_type)
        return header + payload

    def parse_control_pdu(self, control_pdu_bytes):
        """Parse a Control PDU."""
        control_type = control_pdu_bytes[0]
        payload = control_pdu_bytes[1:]
        return {'control_type': control_type, 'payload': payload}
