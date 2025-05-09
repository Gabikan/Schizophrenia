# Schizophrenia Diagnosis Prediction

Dieses Projekt wurde im Rahmen des Moduls LB 259 an der Berufsfachschule BBB durchgeführt. Ziel war es, mit Hilfe von Machine Learning ein Modell zu entwickeln, das basierend auf Patientendaten vorhersagen kann, ob eine Person an Schizophrenie erkrankt ist.

## 🔍 Projektbeschreibung

Der Datensatz enthält demografische, klinische und soziale Merkmale von über 10.000 Patientinnen und Patienten. Die Aufgabe bestand darin, aus diesen Daten ein Klassifikationsmodell zu erstellen, das die Spalte `Diagnosis` (0 = nicht schizophren, 1 = schizophren) vorhersagt.

## 🧠 Verwendete Technologien

- Python 3
- pandas, numpy
- scikit-learn
- matplotlib
- Jupyter Notebook

## 📂 Notebooks

- `data_analysis.ipynb` – Erste Analyse und Vorbereitung der Daten
- `model_final.ipynb` – Modellaufbau, Training und erste Vorhersagen
- `evaluation.ipynb` – Modellbewertung (Feature Importance, Confusion Matrix, Sensitivität, Spezifität)

## 📊 Ergebnis

Das finale Modell basiert auf einem Random Forest Classifier und erreicht eine Genauigkeit von **100 %** auf den Testdaten. Sowohl Sensitivität als auch Spezifität liegen bei 1.00, was auf eine sehr gute Trennung zwischen den Klassen hinweist.

## 🔐 Datenschutz

Die verwendeten Daten sind anonymisiert und wurden ausschließlich zu Lernzwecken genutzt. Persönlich identifizierbare Informationen wurden entfernt oder pseudonymisiert.

## ▶️ Ausführen

1. Repository klonen oder herunterladen
2. Sicherstellen, dass `schizophrenia_dataset_cleaned.csv` im gleichen Ordner liegt
3. Jupyter Notebook starten:
   ```
   jupyter notebook
   ```
4. Nacheinander öffnen:
   - `model_final.ipynb`
   - `evaluation.ipynb`

## ✍️ Autor

Gabriel Zefaj  
Berufsfachschule BBB, 2025
