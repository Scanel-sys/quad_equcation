class number:

    dummy = 1

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, ln_container):
        self.long = ln_container

    def __init_casual_numb__(self, number):
        self.cas_num = number

    def info(self):
        print("number :", self.long)

    def sqrt(self):
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, number):
            return self.dummy + other.dummy

        elif isinstance(other, int):
            return self.dummy + other

        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, number):
            self.dummy += other.dummy

        elif isinstance(other, int):
            self.dummy += other

        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, number):
            return self.dummy - other.dummy

        elif isinstance(other, int):
            return self.dummy - other

        else:
            return NotImplemented

    def __isub__(self, other):
        if isinstance(other, number):
            self.dummy -= other.dummy

        elif isinstance(other, int):
            self.dummy -= other

        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, number):
            return self.dummy * other.dummy

        elif isinstance(other, int):
            return self.dummy * other

        else:
            return NotImplemented

    def __imul__(self, other):
        if isinstance(other, number):
            self.dummy *= other.dummy

        elif isinstance(other, int):
            self.dummy *= other

        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, number):
            return self.dummy / other.dummy

        elif isinstance(other, int):
            return self.dummy / other

        else:
            return NotImplemented

    def __itruediv__(self, other):
        if isinstance(other, number):
            self.dummy /= other.dummy

        elif isinstance(other, int):
            self.dummy /= other

        else:
            return NotImplemented

    def __eq__(self, other) -> bool:
        if isinstance(other, number):
            return self.dummy == other.dummy

        elif isinstance(other, int):
            return self.dummy == other

        else:
            return NotImplemented

    def __ne__(self, other) -> bool:
        if isinstance(other, number):
            return self.dummy != other.dummy

        elif isinstance(other, int):
            return self.dummy != other

        else:
            return NotImplemented

    def __lt__(self, other) -> bool:
        if isinstance(other, number):
            return self.dummy < other.dummy

        elif isinstance(other, int):
            return self.dummy < other

        else:
            return NotImplemented

    def __gt__(self, other) -> bool:
        if isinstance(other, number):
            return self.dummy > other.dummy

        elif isinstance(other, int):
            return self.dummy > other

        else:
            return NotImplemented

    def __le__(self, other) -> bool:
        if isinstance(other, number):
            return self.dummy <= other.dummy

        elif isinstance(other, int):
            return self.dummy <= other

        else:
            return NotImplemented

    def __ge__(self, other) -> bool:
        if isinstance(other, number):
            return self.dummy >= other.dummy

        elif isinstance(other, int):
            return self.dummy >= other

        else:
            return NotImplemented

    def __neg__(self):
        return -self.dummy
