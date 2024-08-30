import logging

class ControlPDU:
    def create_control_pdu(self, control_type, payload):
        """Create a Control PDU."""
        header = bytearray()
        header.append(control_type)
        logging.debug(f"Creating Control PDU with type {control_type} and payload {payload.hex()}.")
        return header + payload

    def parse_control_pdu(self, control_pdu_bytes):
        """Parse a Control PDU."""
        control_type = control_pdu_bytes[0]
        payload = control_pdu_bytes[1:]
        logging.debug(f"Parsed Control PDU: type {control_type}, payload {payload.hex()}.")
        return {'control_type': control_type, 'payload': payload}
