def find_object(json_data, target_object):
    rooms = json_data["rooms"]

    # Creare un dizionario per mappare le stanze in base all'ID
    room_map = {room["id"]: room for room in rooms}

    # Funzione per cercare l'oggetto nelle stanze ricorsivamente
    def search_object(current_room, path=[], visited=None):
        if visited is None:
            visited = set()
        if current_room["id"] in visited:
            return None

        visited.add(current_room["id"])
        # Aggiungi la stanza corrente al percorso
        path.append(current_room["name"])

        # Controlla se l'oggetto è presente nella stanza corrente
        if any(obj["name"] == target_object for obj in current_room["objects"]):
            return path

        # Cerca le direzioni possibili
        directions = [direction for direction in current_room if direction != "id" and direction != "name"]

        # Continua la ricerca nelle stanze adiacenti
        for direction in directions:
            next_room_id = current_room[direction]
            next_room = room_map.get(next_room_id)
            if next_room is not None:
                result = search_object(next_room, path.copy(), visited)
                if result:
                    return result

        return None

    # Inizia la ricerca dalla prima stanza
    start_room = rooms[0]
    result = search_object(start_room)

    if result:
        return " -> ".join(result)
    else:
        return "Oggetto non trovato in nessuna stanza."
