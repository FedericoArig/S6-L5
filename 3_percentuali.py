#Calcolo delle percentuali di: tipo di presenza (On-site, remote, hybrid)
#                              tipo di impiego (full time, part time, ecc)

import pandas as pd 
from matplotlib import pyplot as plt 
#scrivo l'indirizzo del dataset da importare
file = "./data_science_salaries.csv"
dataset = pd.read_csv(file)
#calcolo le percentuali del tipo di presenza
tipo_di_presenza = dataset['work_models'].value_counts()
percentuali_tipo_presenza = [i for i in tipo_di_presenza/tipo_di_presenza.sum()*100]
#creo una lista con tutti i tipi di presenza
lista_presenze = [i for i in dataset['work_models'].unique()]

#creo con pandas un dataframe che mostri le percentuali dei tipi di presenza
df_tipo_presenza = pd.DataFrame({'Percentuale Presenza': percentuali_tipo_presenza}, index=lista_presenze)
print(df_tipo_presenza)


#calcolo le percentuali dei tipi di impiego (full-time, part-time, ecc)
tipo_di_impiego = dataset['employment_type'].value_counts()
percentuali_tipo_impiego = [i for i in tipo_di_impiego/tipo_di_impiego.sum()*100]
#creo una lista con tutti i tipi di impiego
lista_impiego = [i for i in dataset['employment_type'].unique()]

#creo con pandas un dataframe che mostri le percentuali dei tipi di impiego
df_tipo_impiego = pd.DataFrame({'Percentuale Impiego': percentuali_tipo_impiego}, index=lista_impiego)
print(df_tipo_impiego)

#creiamo i grafici a torta delle percentuali

#grafico a torta percentuale presenza
plt.pie(percentuali_tipo_presenza, labels=lista_presenze, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Assicura che il grafico sia circolare
plt.title('Distribuzione del tipo di presenza')
plt.show()
#grafico a torta percentuale impiego
plt.pie(percentuali_tipo_impiego, labels=lista_impiego, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Assicura che il grafico sia circolare
plt.legend(labels=lista_impiego, loc="best")
plt.title('Distribuzione del tipo di impiego')
plt.show()