import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('survey_results_public.csv')
df.head()
print(df)
df.shape
df['BetterLife'].value_counts()
print(df['BetterLife'].value_counts())
df['BetterLife'].value_counts(normalize=True)
df['MgrMoney'].value_counts(normalize=True)
print(df['MgrMoney'].value_counts(normalize=True))

