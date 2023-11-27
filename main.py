from flask import Flask, jsonify, request

app = Flask(__name__)

# Ruta principal
@app.route('/')
def root():
    return "prueba"

# Obtener un usuario por ID con parámetro opcional de query
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = {"id": user_id, "name": "luis", "telefono": "123123"}
    query = request.args.get('query')
    if query:
        user["query"] = query
    return jsonify(user), 200

# Crear un nuevo usuario con datos enviados mediante POST
@app.route("/users", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        # Verificar si se enviaron los datos necesarios
        if "id" in data and "name" in data and "telefono" in data:
            # Crear un nuevo usuario
            new_user = {
                "id": data["id"],
                "name": data["name"],
                "telefono": data["telefono"]
            }
            return jsonify(new_user), 201
        else:
            return jsonify({"error": "Datos incompletos para crear un usuario"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Actualizar un usuario existente por ID mediante el método PUT
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    try:
        data = request.get_json()
        # Verificar si se enviaron los datos necesarios para actualizar
        if "name" in data or "telefono" in data:
            # Simular la actualización del usuario
            updated_user = {
                "id": user_id,
                "name": data.get("name"),
                "telefono": data.get("telefono")
            }
            return jsonify(updated_user), 200
        else:
            return jsonify({"error": "Datos incompletos para actualizar el usuario"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Eliminar un usuario por ID mediante el método DELETE
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    # Simular la eliminación del usuario
    deleted_user = {"message": f"Usuario con ID {user_id} eliminado"}
    return jsonify(deleted_user), 200

if __name__ == "__main__":
    app.run(debug=True)