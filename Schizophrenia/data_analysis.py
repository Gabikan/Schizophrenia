import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# 1️⃣ CSV-DATEI EINLESEN (Mit angepassten Spaltennamen)
file_path = "schizophrenia_dataset.csv"
df = pd.read_csv(file_path, encoding='utf-8', sep=',')

df.columns = [
    "Patient_ID", "Age", "Gender", "Education_Level", "Marital_Status", "Occupation", "Income_Level",
    "Living_Area", "Diagnosis", "Disease_Duration", "Hospitalizations", "Family_History", "Substance_Use",
    "Suicide_Attempt", "Positive_Symptom_Score", "Negative_Symptom_Score", "GAF_Score", "Social_Support",
    "Stress_Factors", "Medication_Adherence"
]

# 2️⃣ ERSTER ÜBERBLICK ÜBER DIE DATEN
print(df.head())  # Zeigt die ersten 5 Zeilen
print(df.info())  # Infos zu Datentypen und fehlenden Werten
print(df.describe())  # Statistische Übersicht

# 3️⃣ WELCHES FELD SOLL VORHERSAGT WERDEN?
prediction_target = "Diagnosis"  # 0: Nicht schizophren, 1: Schizophren
print(f"Wir möchten Vorhersagen für: {prediction_target}")

# 4️⃣ STATISTISCHE WERTE PRO SPALTE
print(df.describe())

# 5️⃣ HISTOGRAMM FÜR EIN WICHTIGES MERKMAL
plt.figure(figsize=(8, 5))
sns.histplot(df["Age"], bins=20, kde=True)
plt.title("Altersverteilung der Patienten")
plt.xlabel("Alter")
plt.ylabel("Anzahl")
plt.show()

# 6️⃣ OPTIONAL: SCALING EINES FELDES
scaler = MinMaxScaler()
df[["Age"]] = scaler.fit_transform(df[["Age"]])
print("Alter nach MinMax-Skalierung:")
print(df[["Age"]].head())

# Falls keine Skalierung nötig ist, begründen:
scaling_reason = "Wir haben Age skaliert, weil das Modell empfindlich auf große Wertebereiche reagieren könnte."
print(scaling_reason)

# 7️⃣ BEREINIGTE DATEN SPEICHERN
df.to_csv("schizophrenia_dataset_cleaned.csv", index=False)
print("Datei gespeichert: schizophrenia_dataset_cleaned.csv")
