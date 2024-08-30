import logging

class ROHCCompressor:
    def __init__(self, profile, mode):
        self.profile = profile
        self.mode = mode
        self.context = {}
        logging.info(f"ROHCCompressor initialized with profile {profile} and mode {mode}.")

    def compress(self, ip_packet):
        """Mock compression logic to simulate header compression."""
        logging.debug(f"Compressing packet: {ip_packet.hex()}")
        compressed_packet = ip_packet  # Simulating compression
        return compressed_packet

    def decompress(self, compressed_packet):
        """Mock decompression logic to simulate header decompression."""
        logging.debug(f"Decompressing packet: {compressed_packet.hex()}")
        original_packet = compressed_packet  # Simulating decompression
        return original_packet

    def context_timeout(self):
        """Reset the compression context."""
        self.context = {}
        logging.info("ROHC compression context reset.")

class ROHCProfile:
    IP = "IP"

class ROHCMode:
    UNIDIRECTIONAL = "UNIDIRECTIONAL"
    BIDIRECTIONAL = "BIDIRECTIONAL"
