from fastapi import FastAPI
import uvicorn
from input import input_data
import pickle

app = FastAPI()

pickel_in = open('classifier.pkl', 'rb')
model = pickle.load(pickel_in)

@app.get('/')
def index():
    return {'message': "Hello, How's your day going?"}

@app.get("/{name}")
def get_name(name: str):
    return {f"Welcome to the Model Integration with Fast API, {name}"}

@app.post('/predict')
def predict_note(data: input_data):
    data = data.dict()
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']
    prediction = model.predict([[variance, skewness, curtosis, entropy]])
    if (prediction[0]<0.5):
        prediction = "Fake Note"
    else:
        prediction = "Its a Bank Note"
    return {
        'prediction': prediction
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)