class NameNotFoundException(Exception):
    """Triggered when a flavor of chocolate isn't found in the chocolate
    flavor enum"""
    def __init__(self, message='Flavor not found in list of available flavors'):
        self.message = message
        super().__init__(self.message)
