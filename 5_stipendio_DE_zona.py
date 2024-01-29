import pandas as pd
import matplotlib.pyplot as plt

#scrivo l'indirizzo del dataset da importare
file = "./data_science_salaries.csv"

#importo il file con pandas
df = pd.read_csv(file)
print(df) #testo se l'import è avvenuto correttamente


# salario medio x anno data engineer:))

#definiamo nel dataframe il ruolo di data engineer

data_engineer_df = df[df["job_title"] == "Data Engineer"]

#calcoliamo il salario medio per anno per i data engineer

salario_medio_annuo_data_engineer = data_engineer_df.groupby(["work_year"])["salary_in_usd"].mean()

print(salario_medio_annuo_data_engineer)

# Tracciamo il grafico
plt.plot(salario_medio_annuo_data_engineer.index, salario_medio_annuo_data_engineer.values, marker='o', linestyle='-')

# Aggiungiamo etichette degli assi
plt.xlabel('Anno')
plt.ylabel('Salario medio annuo (USD)')

# Aggiungiamo titolo al grafico
plt.title('Salario medio annuo per i Data Engineer')

# Aggiungiamo la  legenda
plt.legend(['Salario medio annuo per Data Engineer'], loc='best')

# Mostra il grafico
plt.grid(True)  # Aggiungi griglia
plt.show()

#adesso trovo lo stipendio annuo del DATA ENEGINEER per location aziendale

stipendio_medio_annuo_per_zona = data_engineer_df.groupby(['company_location'])['salary_in_usd'].mean()

stipendio_medio_annuo_per_zona_ordinato = stipendio_medio_annuo_per_zona.sort_values(ascending=False)


print(stipendio_medio_annuo_per_zona_ordinato.head(10))

# Tracciamo il grafico a barre
plt.bar(stipendio_medio_annuo_per_zona_ordinato.head(10).index, stipendio_medio_annuo_per_zona_ordinato.head(10).values, color='skyblue')

# Aggiungiamo etichette degli assi
plt.xlabel('Zona Aziendale')
plt.ylabel('Stipendio medio annuo (USD)')

# Aggiungiamo titolo al grafico
plt.title('Stipendio medio annuo per zona aziendale dei Data Engineer')

# Aggiungiamo legenda
plt.legend(['Stipendio medio annuo per zona aziendale'], loc='best')

# Ruotiamo le etichette sull'asse x per una migliore leggibilità
plt.xticks(rotation=45, ha='right')

# Mostriamo il grafico
plt.grid(axis='y')  # Aggiungi griglia sull'asse y
plt.tight_layout()  # Ottimizza la disposizione degli elementi del grafico
plt.show()
