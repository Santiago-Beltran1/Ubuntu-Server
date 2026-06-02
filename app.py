from flask import Flask, jsonify
import datetime

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

placas = ["AAA-000", "BBB-000","CCC-000","DDD-000","EEE-000"]

motos = ["Ducati Panigale","Honda CB500","KTM DUKE 390","NKD 125 :V","Yamaha R15"]

inventario = dict(zip(motos,placas))

@app.route('/api/registros', methods=['GET'])
def get_registros():
	return jsonify({
		"status":"online",
		"servidor": "Ubuntu de Beltran Pedraza",	
		"hora_servidor": str(datetime.datetime.now()),
		"inventario" : inventario
	})

@app.route('/api/peritajes', methods=['POST'])
def crear_peritaje():
	nuevaPlaca = "dsb-212".upper()
	placas.append(nuevaPlaca)
	return jsonify({
		"estado":"Nueva placa registrada de forma correcta",
		"la placa registrada fue: ": nuevaPlaca
	})

@app.route('/api/peritajes', methods=['GET'])
def traer_peritajes():
	return jsonify({
		"peritajes": placas
	})

@app.route('/api/inventario', methods=['GET'])
def inventariado():
	return jsonify({
		"vehiculos": len(inventario),
	        "motos_registradas": inventario
	})


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
