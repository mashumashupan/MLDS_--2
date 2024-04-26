from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io
import uvicorn
import numpy as np
import model

app = FastAPI()

@app.post("/classify-image/")
async def classify_image(file: UploadFile = File(...)):
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data))
    image = image.resize((32, 32)).convert('RGB')
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    
    predictions = model.predict(image_array)
    predicted_class = np.argmax(predictions)
    score = np.max(predictions)
    
    return {
        "predictions": [{
            "classification_results": predicted_class,
            "score": score
        }]
    }

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
