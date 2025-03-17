#Variablen
versuchsleiter:str = "Ellena Hehle"
erstellungsdatum:str = "11.03.2025"
first_experiment_id:int = 100

#10 Experimente
experimente_10 = []
for i in range(10):
    try:
        experiment_10 = { i : {
            "Versuchsleiter": versuchsleiter,
            "Erstellungsdatum": erstellungsdatum,
            "Id_Nummer": i + first_experiment_id}}
        experimente_10.append(experiment_10)
    except TypeError:
        print("Eingabe von floats und strings nicht zulässig")
        
print(experimente_10)

#5 Experimente
experimente_5 = []
for i in range(5):
    try:
        experiment_5 = { i : {
            "Versuchsleiter": versuchsleiter,
            "Erstellungsdatum": erstellungsdatum,
            "Id_Nummer": i + first_experiment_id}}
        experimente_5.append(experiment_5)
    except TypeError:
        print("Eingabe von floats und strings nicht zulässig")
        
print(experimente_5)

#wie viele Experimente mit einer geraden ID erstellt wuden
i = 0
while i <= 10:
    if (i + first_experiment_id) % 2 == 0:
        print("Experiment mit der Id_Nummer {} hat eine gerade Zahl".format(i+first_experiment_id))
    i = i+1
