#Analisi delle colonne singole più interessanti

import pandas as pd 
from matplotlib import pyplot as plt 
#scrivo l'indirizzo del dataset da importare
file = "./data_science_salaries.csv"
#importo il file con pandas
dataset = pd.read_csv(file)



#Calcolo quali sono i lavori più frequenti
#il metodo .value_counts() mi ordina anche già i risultati in ordine crescente
tipo_di_lavoro = dataset['job_title'].value_counts()
print(tipo_di_lavoro.head(5))
#i 5 lavori più frequenti sono, in ordine:
# Data Engineer, Data Scientist, Data Analyst, Analytics Engineer

#Calcolo quali sono i tipi di impiego (full-time, parti-time, ecc) più frequenti
tipo_di_impiego = dataset['employment_type'].value_counts()
print(tipo_di_impiego)
#la stragrande maggioranza dei lavoratori sono full-time


#Calcolo quali sono i tipi di presenza (remoto, online, ibrido) più frequenti
tipo_di_presenza = dataset['work_models'].value_counts()
print(tipo_di_presenza)
#la maggior parte dei lavoratori è in presenza (on-site)

x_values = tipo_di_lavoro.head(5).index
y_values = tipo_di_lavoro.head(5).values

plt.bar(x_values, y_values, color='red')
# Aggiungiamo legenda
plt.legend(['tipo di lavoro'], loc='best')
plt.show()

x_values_1 = tipo_di_impiego.head(5).index
y_values_1 = tipo_di_impiego.head(5).values


plt.bar(x_values_1, y_values_1, color='red')
# Aggiungiamo legenda
plt.legend(['tipo di impiego'], loc='best')
plt.show()

x_values_2 = tipo_di_presenza.head(5).index
y_values_2 = tipo_di_presenza.head(5).values

plt.bar(x_values_2, y_values_2, color='red')
# Aggiungiamo legenda
plt.legend(['tipo di presenza'], loc='best')
plt.show()