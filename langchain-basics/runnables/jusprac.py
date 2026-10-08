from abc import ABC, abstractmethod


class XYZ(ABC):
    print("wrfrwf")
    pass


a = XYZ()
print(type(a))


class MNO(XYZ):
    pass
    print("wrfrwf")


a = MNO()
print(type(MNO))
