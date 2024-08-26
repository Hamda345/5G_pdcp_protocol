def start_timer(self, timer_id, duration):
    """Start a timer for a given duration."""
    end_time = time.time() + duration
    self.active_timers[timer_id] = end_time
