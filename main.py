from packet_process import PDCP
from compression import ROHCProfile, ROHCMode
from state_management import PDCPState
from control_pdu import ControlPDU
from timers import PDCPTimers

def main():
    # Initialize PDCP components
    pdcp = PDCP(profile=ROHCProfile.IP, mode=ROHCMode.UNIDIRECTIONAL)
    state_manager = PDCPState()
    control_pdu_handler = ControlPDU()
    timer_manager = PDCPTimers()

    # Set security parameters
    pdcp.initialize_security(bearer=1, direction=0)  # Example parameters

    # Start a timer for demonstration
    timer_manager.start_timer('example_timer', 10)  # Start a 10-second timer

    # Example IP packet (mock data)
    ip_packet = b'\x45\x00\x00\x28\x00\x00\x40\x00\x40\x06\xb1\xe6\xc0\xa8\x00\x68\xc0\xa8\x00\x01'
    sn_length = 12  # Example sequence number length

    # Process the IP packet into a PDCP PDU
    print("\n--- Processing IP Packet ---")
    pdcp_pdu = pdcp.process_packet(ip_packet, sn_length)

    # Simulate receiving the PDCP PDU
    print("\n--- Processing Received PDCP PDU ---")
    original_ip_packet = pdcp.process_received_packet(pdcp_pdu, sn_length)
    print("Original IP Packet:", original_ip_packet)

    # Demonstrate state saving and loading
    state_manager.save_state('session_1', pdcp.get_state_info())
    loaded_state = state_manager.load_state('session_1')
    print("\nLoaded State:", loaded_state)

    # Demonstrate control PDU handling
    print("\n--- Control PDU Handling ---")
    control_pdu = control_pdu_handler.create_control_pdu(control_type=1, payload=b'\x01\x02\x03')
    control_pdu_info = control_pdu_handler.parse_control_pdu(control_pdu)
    print("Control PDU Info:", control_pdu_info)

    # Check if the timer has expired
    if timer_manager.check_timer('example_timer'):
        print("\nTimer 'example_timer' has expired.")
    else:
        print("\nTimer 'example_timer' is still active.")

if __name__ == "__main__":
    main()
