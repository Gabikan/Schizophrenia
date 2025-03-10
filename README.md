# Schizophrenia

https://www.kaggle.com/datasets/asinow/schizohealth-dataset

## Beschreibung des Datensatzes
Dieser Datensatz enthält Informationen, die im Rahmen einer Studie zu Schizophrenie-Patientinnen und -Patienten erhoben wurden. Enthalten sind demografische Merkmale (Alter, Geschlecht), klinische Befunde
(Diagnosekriterien, Symptomausprägungen) sowie Angaben zu Behandlungen und Outcomes. Insgesamt umfasst der Datensatz über 10.000 Einträge, wobei jede Zeile eine Patientin bzw. einen Patienten repräsentiert. Die Felder
können sowohl kontinuierliche (z.B. Alter) als auch kategorische Daten (z.B. Geschlecht, Diagnoseart) umfassen. Ziel ist es, aus diesen Daten mit Verfahren des maschinellen Lernens Vorhersagen über Behandlungserfolg
oder Rückfallrisiken treffen zu können.

## Datenschutz und Maßnahmen
Die Originaldaten wurden von den Erstellern anonymisiert, indem direkte Personenbezüge wie Name, genaue Adresse oder Geburtsdatum entfernt wurden. Zusätzlich werden einzelne klinische Werte nur in aggregierter oder
pseudonymisierter Form zur Verfügung gestellt. Während meiner eigenen Arbeit mit dem Datensatz achte ich darauf, keine neuen Rückschlüsse auf reale Personen zu ermöglichen. Auch wird der Datensatz nur für Forschungs
und Lernzwecke genutzt und nicht kommerziell weiterverbreitet. 

## Spalten und Beschreibungen

Patient_ID – Eindeutige Kennung, die jedem Patienten zugewiesen wurde

Age (Alter) – Alter des Patienten (zwischen 18 und 80)

Gender (Geschlecht) – 0: Weiblich, 1: Männlich

Education_Level (Bildungsniveau) – 1: Primarschule, 2: Sekundarstufe I, 3: Sekundarstufe II, 4: Universitätsabschluss, 5: Postgraduale Ausbildung

Marital_Status (Familienstand) – 0: Ledig, 1: Verheiratet, 2: Geschieden, 3: Verwitwet

Occupation (Beschäftigung) – 0: Arbeitslos, 1: Berufstätig, 2: Pensioniert, 3: Student

Income_Level (Einkommensniveau) – 0: Niedrig, 1: Mittel, 2: Hoch

Living_Area (Wohngebiet) – 0: Ländlich, 1: Städtisch

Diagnosis (Diagnose) – 0: Nicht schizophren, 1: Schizophren

Disease_Duration (Krankheitsdauer) – Dauer der Erkrankung bei Schizophrenie-Patienten (1–40 Jahre)

Hospitalizations (Krankenhausaufenthalte) – Anzahl der Krankenhausaufenthalte (zwischen 0 und 10 für Schizophrenie-Patienten)

Family_History (Familiäre Vorgeschichte) – 0: Nein, 1: Ja (genetische Veranlagung)

Substance_Use (Substanzgebrauch) – 0: Nein, 1: Ja (Tabak, Alkohol oder andere Substanzen)

Suicide_Attempt (Suizidversuch) – 0: Nein, 1: Ja

Positive_Symptom_Score (Positiver Symptomwert) – Wertebereich 0 bis 100 (höhere Werte weisen auf mehr Symptome hin)

Negative_Symptom_Score (Negativer Symptomwert) – Wertebereich 0 bis 100 (höhere Werte weisen auf mehr negative Symptome hin)

GAF_Score (Global Assessment of Functioning) – Wertebereich 0 bis 100 (niedrigere Werte bedeuten schlechtere Funktionsfähigkeit)

Social_Support (Soziale Unterstützung) – 0: Gering, 1: Mittel, 2: Hoch

Stress_Factors (Stressfaktoren) – 0: Gering, 1: Mittel, 2: Hoch

Medication_Adherence (Therapietreue) – 0: Gering, 1: Mittel, 2: Gut
