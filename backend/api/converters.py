class FloatConverter:
    # The regex that matches a floating point number (positive or negative)
    regex = r'-?\d+(\.\d+)?'

    # Converts the matched string into a float
    def to_python(self, value):
        return float(value)

    # Converts the Python float back into a string for the URL
    def to_url(self, value):
        return str(value)
