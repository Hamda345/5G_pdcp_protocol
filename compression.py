class ROHCCompressor:
    def __init__(self, profile, mode):
        self.profile = profile
        self.mode = mode
        self.context = {}

    def compress(self, ip_packet):
        """Mock compression logic to simulate header compression."""
        compressed_packet = ip_packet  # In a real implementation, compression would occur here
        print("Compressing packet:", ip_packet)
        return compressed_packet

    def decompress(self, compressed_packet):
        """Mock decompression logic to simulate header decompression."""
        original_packet = compressed_packet  # In a real implementation, decompression would occur here
        print("Decompressing packet:", compressed_packet)
        return original_packet

    def context_timeout(self):
        """Reset the compression context."""
        self.context = {}
        print("ROHC compression context reset.")

class ROHCProfile:
    IP = "IP"  # IP profile

class ROHCMode:
    UNIDIRECTIONAL = "UNIDIRECTIONAL"  # Unidirectional mode
    BIDIRECTIONAL = "BIDIRECTIONAL"    # Bidirectional mode
