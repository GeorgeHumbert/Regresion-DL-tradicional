# Predicción del Número de Pasajeros en Aerolíneas con una Red LSTM

Este proyecto utiliza una red LSTM (Long Short-Term Memory) para predecir el número de pasajeros mensuales en aerolíneas utilizando una serie temporal. El modelo está entrenado con el conjunto de datos `airline-passengers.csv` y se implementa una API con FastAPI para realizar predicciones en tiempo real.

## Estructura del Proyecto

El proyecto está dividido en varias fases y archivos:

- **A_Feature_Pipeline.ipynb**: Preprocesamiento de los datos, incluyendo la normalización y la transformación de la serie temporal para adaptarse a la entrada esperada por una LSTM.
- **B_Training_Pipeline.ipynb**: Entrenamiento del modelo LSTM con los datos preprocesados.
- **C_Model_Inference.ipynb**: Evaluación del modelo entrenado y prueba con nuevas secuencias para obtener predicciones.
- **API Fast**: Carpeta que contiene la implementación de la API usando FastAPI para realizar predicciones en tiempo real. El archivo principal es `app.py`.
- **airline_passengers_lstm.h5**: Archivo que contiene el modelo LSTM entrenado guardado en formato HDF5.
- **requirements.txt**: Archivo que contiene todas las dependencias necesarias para ejecutar el proyecto.

## Requisitos

Para ejecutar este proyecto, necesitas instalar los siguientes paquetes:

```bash
pip install -r requirements.txt
El archivo requirements.txt contiene:

txt
Copiar código
tensorflow==2.6.0
numpy==1.19.5
pandas==1.3.3
matplotlib==3.4.3
fastapi==0.70.0
uvicorn==0.15.0
joblib==1.1.0
Instrucciones de Ejecución
1. Preprocesamiento y Entrenamiento del Modelo
Para entrenar el modelo, sigue estos pasos:

Ejecuta el notebook A_Feature_Pipeline.ipynb para preparar los datos:

Carga del dataset airline-passengers.csv.
Normalización de los datos.
Transformación de los datos en secuencias para la entrada del modelo LSTM.
Luego, ejecuta B_Training_Pipeline.ipynb para entrenar el modelo LSTM:

El modelo LSTM está configurado con capas LSTM y Dense.
Guarda el modelo entrenado como airline_passengers_lstm.h5.
Opcionalmente, ejecuta C_Model_Inference.ipynb para probar el modelo entrenado:

Se cargan nuevas secuencias para obtener predicciones del modelo.
Se genera un gráfico que muestra el ajuste del modelo a los datos reales.
2. Implementación de la API
Una vez que hayas entrenado y guardado el modelo, puedes implementar la API para realizar predicciones en tiempo real:

Ve a la carpeta api_fast.
Asegúrate de que el archivo airline_passengers_lstm.h5 esté en el mismo directorio que el archivo app.py.
Ejecuta el siguiente comando para levantar el servidor FastAPI:
bash
Copiar código
uvicorn app:app --reload
3. Realizar Predicciones
Con el servidor FastAPI en ejecución, puedes hacer solicitudes a la API para obtener predicciones. Aquí hay un ejemplo de cómo realizar una solicitud POST con curl:

bash
Copiar código
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d "{\"sequence\": [112, 118, 132, 129, 121]}"
La API devolverá una predicción en formato JSON con el número predicho de pasajeros para el próximo mes.

Ejemplos de Uso
Ejemplo de Entrada:
json
Copiar código
{
  "sequence": [112, 118, 132, 129, 121]
}
Ejemplo de Respuesta:
json
Copiar código
{
  "predicted_value": 135.67
}
Resultados
Pérdida de Entrenamiento: 0.0019
Pérdida de Validación: 0.0014
Gráfico de Pérdida: El gráfico muestra cómo la pérdida disminuye consistentemente durante el entrenamiento y la validación.
Notas Finales
Este proyecto es un ejemplo básico de cómo usar redes neuronales LSTM para la predicción de series temporales. Se puede mejorar utilizando más datos o arquitecturas más avanzadas como GRU o Transformers.

La API puede ser fácilmente desplegada en servicios de nube como Heroku, AWS o Google Cloud.

r
Copiar código

Este archivo README incluye la estructura del proyecto, instrucciones claras sobre cómo ejecutar el código, y ejemplos de cómo interactuar con la API para realizar predicciones.
