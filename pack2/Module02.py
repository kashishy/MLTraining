import math  # external linking, we have to mention the name of library
print(math.sqrt(25))
print(math.pi)

# Adding all features of math library in the program
from math import *  # internal linking
print(sqrt(16))
print(pi)


# Adding selective features of math library in the program
from math import sqrt, pi
print(sqrt(16))
print(pi)

# Nick name to Linked Library
import math as chintu  # external linking
print(chintu.sqrt(25))
print(chintu.pi)

import pack1.Module01  # custom external Linking
pack1.Module01.show(4)
pack1.Module01.sum(2, 3)
print(pack1.Module01.count)


from pack1.Module01 import *  # custom internal Linking
show(4)
sum(2, 3)
print(count)

from pack1 import Module01
Module01.show(7)
Module01.sum(3, 5)
print("Module01.count = ", Module01.count)