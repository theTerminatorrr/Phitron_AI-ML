import pandas as pd

df = pd.DataFrame({'temperature (F)': [32, 212, 98.6, 68]})
df

df['temperature (C)'] = df['temperature (F)'].apply(lambda x: (x - 32) * 5/9)
df

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})

df

df['A'] = df['A'].apply(lambda x: x ** 0.5)

df


