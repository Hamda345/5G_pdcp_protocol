import json
import requests
import sys
from packet_process import PDCP
from compression import ROHCProfile, ROHCMode
from state_management import PDCPState
from control_pdu import ControlPDU
from timers import PDCPTimers

def log_data_to_api(data):
    """Log exchanged data to the MongoDB API."""
    try:
        response = requests.post('http://localhost:5000/log', json=data)
        if response.status_code == 201:
            print("Data logged successfully to MongoDB.")
        else:
            print(f"Failed to log data: {response.text}")
    except Exception as e:
        print(f"Error logging data to API: {e}")

def main(ip_packet_hex, sn_length):
    # Initialize PDCP components
    pdcp = PDCP(profile=ROHCProfile.IP, mode=ROHCMode.UNIDIRECTIONAL)
    state_manager = PDCPState()
    control_pdu_handler = ControlPDU()
    timer_manager = PDCPTimers()

    # Set security parameters
    pdcp.initialize_security(bearer=1, direction=0)

    # Start a timer for demonstration
    timer_manager.start_timer('example_timer', 10)

    # Convert hex string to bytes
    ip_packet = bytes.fromhex(ip_packet_hex)

    # Process the IP packet into a PDCP PDU
    print("\n--- Processing IP Packet ---")
    pdcp_pdu = pdcp.process_packet(ip_packet, int(sn_length))

    # Log the exchanged data
    log_data_to_api({'action': 'process_packet', 'ip_packet': ip_packet.hex(), 'pdcp_pdu': pdcp_pdu.hex()})

    # Simulate receiving the PDCP PDU
    print("\n--- Processing Received PDCP PDU ---")
    original_ip_packet = pdcp.process_received_packet(pdcp_pdu, int(sn_length))
    print("Original IP Packet:", original_ip_packet.hex())

    # Log the received data
    log_data_to_api({'action': 'process_received_packet', 'pdcp_pdu': pdcp_pdu.hex(), 'original_ip_packet': original_ip_packet.hex()})

    # Demonstrate state saving and loading
    state_manager.save_state('session_1', pdcp.get_state_info())
    loaded_state = state_manager.load_state('session_1')
    print("\nLoaded State:", loaded_state)

    # Log the state information
    log_data_to_api({'action': 'state_management', 'session': 'session_1', 'state_info': pdcp.get_state_info()})

    # Demonstrate control PDU handling
    print("\n--- Control PDU Handling ---")
    control_pdu = control_pdu_handler.create_control_pdu(control_type=1, payload=b'\x01\x02\x03')
    control_pdu_info = control_pdu_handler.parse_control_pdu(control_pdu)
    print("Control PDU Info:", control_pdu_info)

    # Log the control PDU information
    log_data_to_api({'action': 'control_pdu_handling', 'control_pdu': control_pdu.hex(), 'control_pdu_info': control_pdu_info})

    # Check if the timer has expired
    if timer_manager.check_timer('example_timer'):
        print("\nTimer 'example_timer' has expired.")
    else:
        print("\nTimer 'example_timer' is still active.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <ip_packet_hex> <sn_length>")
        sys.exit(1)
    
    main(sys.argv[1], sys.argv[2])
