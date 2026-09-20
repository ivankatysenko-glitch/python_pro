import inspect
import math
import requests


print(inspect.getmodule(requests.get))
print(inspect.getmodule(list))
print(inspect.getmodule(math.sqrt))
