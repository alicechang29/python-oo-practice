class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    # TODO: consider calling count something more relevant like next_val
    def __init__(self, start):
        """Create serial generator from start number"""
        self.start = start
        self.count = self.start

    def __repr__(self):
        return f"<SerialGenerator start={self.start}, count={self.count}>"

    # TODO: make sure language is clear on what is returned
    def generate(self):
        """Increases count of serial number by 1 and returns the"""
        self.count += 1
        return self.count-1

    def reset(self):
        """Resets count of serial number to start number"""
        self.count = self.start
