import json
from service.find_objects import find_object

json_file = "../resources/json/map.json"

if __name__ == "__main__":
    target_object = input("Inserisci il nome dell'oggetto da cercare: ")

    try:
        with open(json_file, "r") as file:
            data = json.load(file)
            result = find_object(data, target_object)
            print(result)
    except FileNotFoundError:
        print("File JSON non trovato.")
    except json.JSONDecodeError:
        print("Il file JSON non è valido.")
