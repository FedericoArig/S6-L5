import pandas as pd 
import matplotlib.pyplot as plt

#scrivo l'indirizzo del dataset da importare
file = "./data_science_salaries.csv"

#importo il file con pandas
dataset = pd.read_csv(file)
print(dataset) #testo se l'import è avvenuto correttamente

#usando il metodo .groupby(), calcolo lo stipendio medio (in usd) per ogni anno
stipendio_medio_per_anno = dataset.groupby('work_year')['salary_in_usd'].mean()
print(stipendio_medio_per_anno)

# Traccia il grafico
plt.plot(stipendio_medio_per_anno.index, stipendio_medio_per_anno.values, marker='o', linestyle='-')

# Aggiungi etichette degli assi
plt.xlabel('Anno')
plt.ylabel('Stipendio medio (USD)')

# Aggiungi titolo al grafico
plt.title('Stipendio medio per anno')

# Aggiungi legenda
plt.legend(['Stipendio medio per anno'], loc='best')

# Mostra il grafico
plt.grid(True)  # Aggiungi griglia
plt.show()