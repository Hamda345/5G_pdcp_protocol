import time
import logging

class PDCPTimers:
    def __init__(self):
        """Initialize the timer manager."""
        self.active_timers = {}
        logging.info("PDCPTimers manager initialized.")

    def start_timer(self, timer_id, duration):
        """Start a timer for a given duration."""
        end_time = time.time() + duration
        self.active_timers[timer_id] = end_time
        logging.info(f"Timer '{timer_id}' started for {duration} seconds.")

    def check_timer(self, timer_id):
        """Check if the specified timer has expired."""
        if timer_id in self.active_timers:
            if time.time() >= self.active_timers[timer_id]:
                del self.active_timers[timer_id]
                logging.info(f"Timer '{timer_id}' has expired.")
                return True
            logging.debug(f"Timer '{timer_id}' is still active.")
            return False
        logging.error(f"Timer '{timer_id}' does not exist.")
        return False

    def stop_timer(self, timer_id):
        """Stop a specified timer."""
        if timer_id in self.active_timers:
            del self.active_timers[timer_id]
            logging.info(f"Timer '{timer_id}' has been stopped.")

    def pause_timer(self, timer_id):
        """Pause a specified timer."""
        if timer_id in self.active_timers:
            remaining_time = self.active_timers[timer_id] - time.time()
            self.active_timers[timer_id] = remaining_time
            logging.info(f"Timer '{timer_id}' has been paused with {remaining_time} seconds remaining.")

    def resume_timer(self, timer_id):
        """Resume a paused timer."""
        if timer_id in self.active_timers and isinstance(self.active_timers[timer_id], (int, float)):
            new_end_time = time.time() + self.active_timers[timer_id]
            self.active_timers[timer_id] = new_end_time
            logging.info(f"Timer '{timer_id}' has been resumed and will end in {self.active_timers[timer_id]} seconds.")
