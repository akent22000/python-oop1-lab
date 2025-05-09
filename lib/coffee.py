#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price
    
    ##get
    @property
    def size(self):
        return self._size

    ##get
    @size.setter
    def size(self, size):
        if size == "Small" or size == "Medium" or size == "Large":
            # breakpoint()
            self._size = size
            print(size)
        else:
            # breakpoint()
            print(
                "size must be Small, Medium, or Large"
            )

    # @classmethod - ob oriented go back to lessons
    # revist instance lesson

    def tip(self):
        self.price += 1
        print("This coffee is great, here’s a tip!")
