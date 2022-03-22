class SingleOrigin:
    def __init__(self, origin, roast, processing, notes, inStock):
        self.origin = origin
        self.roast = roast
        self.processing = processing
        self.notes = notes
        self.inStock = inStock

class SignatureBlend:
    def __init__(self, name, roast, inStock):
        self.name = name
        self.roast = roast
        self.inStock = inStock
