class GenericCoffee:
    def __init__(self, roast, inStock):
        self.roast = roast
        self.inStock = inStock


class SingleOrigin(GenericCoffee):
    def __init__(self, origin, roast, processing, notes, inStock):
        super().__init__(roast, inStock)

        self.origin = origin
        self.processing = processing
        self.notes = notes


class SignatureBlend(GenericCoffee):
    def __init__(self, name, roast, inStock):
        super().__init__(roast, inStock)
        self.name = name
