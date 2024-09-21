from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import tensorflow as tf
import joblib

# Inicializar la app de FastAPI
app = FastAPI()

# Cargar el modelo entrenado
model = tf.keras.models.load_model('airline_passengers_lstm.h5')

# Definir el formato de entrada de datos
class PassengerData(BaseModel):
    sequence: list

# Función para ajustar la secuencia a la longitud esperada por el modelo
def adjust_sequence_length(sequence, expected_length=12):
    if len(sequence) < expected_length:
        # Si la secuencia es más corta, la rellenamos con ceros al principio
        sequence = [0] * (expected_length - len(sequence)) + sequence
    elif len(sequence) > expected_length:
        # Si es más larga, la recortamos
        sequence = sequence[:expected_length]
    return sequence

# Ruta para realizar predicciones
@app.post("/predict")
async def predict(data: PassengerData):
    try:
        # Ajustar la secuencia a la longitud esperada
        adjusted_sequence = adjust_sequence_length(data.sequence)

        # Convertir la secuencia ajustada en un array de numpy y añadir una dimensión extra para LSTM
        input_data = np.array(adjusted_sequence).reshape(1, len(adjusted_sequence), 1)

        # Realizar predicción
        prediction = model.predict(input_data)

        # Devolver la predicción
        return {"predicted_value": float(prediction[0][0])}
    except Exception as e:
        return {"error": f"Ocurrió un error al procesar la solicitud: {e}"}

