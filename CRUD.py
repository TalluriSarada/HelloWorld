import pandas as pd
df = pd.read_csv('survey_results_public.csv')
df.head()
print(df)
df.shape
df['BetterLife'].value_counts()
print(df['BetterLife'].value_counts())
df['BetterLife'].value_counts(normalize=True)
df['MgrMoney'].value_counts(normalize=True)
print(df['MgrMoney'].value_counts(normalize=True))
df['SocialMedia'].value_counts().plot(kind="bar")
print(df['SocialMedia'].value_counts().plot(kind="bar"))
said_no = df[df['BetterLife'] == 'No']
said_no.head(3)
said_no.shape
df['BetterLife'].value_counts()
print(df['BetterLife'].value_counts())
said_no['BetterLife'].value_counts()
print(said_no['BetterLife'].value_counts())
said_no = df[df['BetterLife'] == 'No']
#print(said_no = df[df['BetterLife'] == 'No'])
said_yes = df[df['BetterLife'] == 'Yes']
#print(said_yes = df[df['BetterLife'] == 'Yes'])
print(said_no['Age'].mean(),
      said_yes['Age'].mean(),
      said_no['Age'].median(),
      said_yes['Age'].median()
     )
over50 = df[df['Age'] >= 50]
under25 = df[df['Age'] <= 25]
print(over50['BetterLife'].value_counts(normalize=True))
print(under25['BetterLife'].value_counts(normalize=True))
print(len(over50))
print(len(under25))
#only people in India who gave the optimistic answer about the future
filtered_1 = df[(df['BetterLife'] == 'Yes') & (df['Country'] == 'India')]
print(filtered_1['BetterLife'].value_counts())
print(filtered_1['Country'].value_counts())
#more complicated drill-down Answered ‘Yes’ to the better life question
#Are over age 50  Live in India Do NOT code as a hobby
filtered = df[(df['BetterLife'] == 'Yes') & (df['Age'] >= 50) & (df['Country'] == 'India') &~ (df['Hobbyist'] == "Yes") &~ (df['OpenSourcer'] == "Never")]
filtered
#Analyzing Multi-Answer Survey Questions
df["LanguageWorkedWith"].head()
print(df["LanguageWorkedWith"].head())
python_bool = df["LanguageWorkedWith"].str.contains('Python')
python_bool.value_counts(normalize=True)
lang_lists = df["LanguageWorkedWith"].str.split(';', expand=True)
lang_lists.head()
print(lang_lists)
