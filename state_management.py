class PDCPState:
    def __init__(self):
        self.states = {}

    def save_state(self, identifier, state):
        """Save the state of a particular PDCP session."""
        self.states[identifier] = state
        print(f"State saved for {identifier}.")

    def load_state(self, identifier):
        """Load the state of a particular PDCP session."""
        return self.states.get(identifier, None)

    def reset_state(self, identifier):
        """Reset the state of a particular PDCP session."""
        if identifier in self.states:
            del self.states[identifier]
            print(f"State reset for {identifier}.")
