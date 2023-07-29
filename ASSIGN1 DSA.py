#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

data = {
    'ship_mode': ["Same Day", "First Class", "Standard Class", "Second Class"],
    'sales': [100, 200, 300, 400],
    'profit': [20, 30, 40, 50]
}

df = pd.DataFrame(data)

def calculate_surcharge(ship_mode):
    if ship_mode == "Same Day":
        return 0.2
    elif ship_mode == "First Class":
        return 0.1
    elif ship_mode == "Standard Class":
        return 0.05
    else:
        return 0


df['surcharge'] = df['ship_mode'].apply(calculate_surcharge)

df['total_cost'] = (df['sales'] - df['profit']) * (1 + df['surcharge'])


print(df)


# In[4]:
#2WAY

import pandas as pd
data = {
    'sales': [100, 200, 150, 300],
    'profit': [20, 30, 25, 40],
    'ship_mode': ['Same Day', 'Standard Class', 'First Class', 'Second Class']
}


df = pd.DataFrame(data)

def calculate_surcharge(ship_mode):
    if ship_mode == 'Same Day':
        return 0.2
    elif ship_mode == 'First Class':
        return 0.1
    elif ship_mode == 'Standard Class':
        return 0.05
    else:
        return 0

df['surcharge'] = df['ship_mode'].apply(calculate_surcharge)

df['total_cost'] = (df['sales'] - df['profit']) * (1 + df['surcharge'])

print(df)


# In[ ]:




