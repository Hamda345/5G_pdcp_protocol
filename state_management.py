import logging

class PDCPState:
    def __init__(self):
        self.states = {}
        logging.info("PDCPState manager initialized.")

    def save_state(self, identifier, state):
        """Save the state of a particular PDCP session."""
        self.states[identifier] = state
        logging.debug(f"State saved for {identifier}. State: {state}")

    def load_state(self, identifier):
        """Load the state of a particular PDCP session."""
        state = self.states.get(identifier, None)
        logging.debug(f"Loaded state for {identifier}: {state}")
        return state

    def reset_state(self, identifier):
        """Reset the state of a particular PDCP session."""
        if identifier in self.states:
            del self.states[identifier]
            logging.info(f"State reset for {identifier}.")

    def reset_all_states(self):
        """Reset all saved states."""
        self.states.clear()
        logging.info("All PDCP states have been reset.")
