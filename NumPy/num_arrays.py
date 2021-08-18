height = [1.87, 1.75, 1.2]
weight = [56, 58, 59]

import numpy as np

np_height = np.array(height)
np_weight = np.array(weight)

print(np_height)
print(np_weight)

bmi = np_weight / np_height * 2

print(bmi > 60)

# Students
# School@2021


import pandas as pd

dict = {
    "country": ["Burundi", "Tanzania", "Rwanda"],
    "capital": ["Bujumbura", "Dar-es-Salaam", "Kigali"],
    "population": [6.3, 15.4, 9.2],
    "area": [100.2, 303.1, 124.5]
}

brics = pd.DataFrame(dict)
print(brics)
