import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv('data_science_salaries.csv')

#confronto media, min e max salari per posizione
confronto_media = df.groupby('job_title')['salary_in_usd'].describe()

print(confronto_media)

#salario medio per livello di esperienza
salario_esperienza = df.groupby('experience_level')['salary_in_usd'].mean().reset_index()
sns.barplot(data=salario_esperienza, x='experience_level', y='salary_in_usd', hue="experience_level", palette="coolwarm")
plt.xlabel('Livello di Esperienza')
plt.ylabel('Salario Medio (USD)')

plt.show()


#andamento salario del ruolo "Data Analyst " negli anni

plt.xlabel('Anno')
plt.ylabel('Salario Medio (USD)')
plt.grid(True)
data_analyst_df = df[df['job_title'] == 'Data Analyst'].copy().sort_values(by='work_year')
data_analyst_df['work_year'] = data_analyst_df['work_year'].astype(str)
sns.lineplot(data=data_analyst_df, x='work_year', y='salary_in_usd', hue='experience_level', errorbar=None, marker='o')
plt.show()

#distribuzione geografica del salorio medio di un Data Engineer anno 2023

data_engineer_2024 = df[(df['job_title'] == 'Data Engineer') & (df['work_year'] == 2023)]
d_e_media = data_engineer_2024.groupby('company_location')['salary_in_usd'].mean().sort_values().reset_index()

print(data_engineer_2024)

sns.barplot(data=d_e_media, x='company_location', y='salary_in_usd', hue="company_location", palette="coolwarm")
for idx, value in enumerate(d_e_media['company_location']):
    plt.text(idx, 1000, str(d_e_media['company_location'][idx]), ha='center', va='bottom', rotation=90)
plt.gca().set_xticklabels([])
plt.tight_layout() 
plt.grid(True, zorder=0)

plt.show()