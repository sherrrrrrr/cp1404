from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that has additional charges based on fanciness."""

    flagfall = 4.50

    def __init__(self, name, fuel, price_per_km, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel, price_per_km)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the price for the taxi trip, including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"