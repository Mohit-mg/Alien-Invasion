class GameStats():
    """Track statistic for Alien Invasion"""

    def __init__(self,ai_settings):
        """Initialize statistics."""
        self.ai_settings=ai_settings
        self.reset_stats()
        #Start Alien Invasionn in an Active state.
        self.game_active=True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left=self.ai_settings.ship_limit