from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.staticfiles import StaticFiles

app = FastAPI()

class MatricesInput(BaseModel):
    matriz1: List[List[int]]
    matriz2: List[List[int]]

@app.post("/matrices")
async def sumar_matrices(datos: MatricesInput):
    try:
        matriz1 = datos.matriz1
        matriz2 = datos.matriz2
        
        resultado = [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]
        
        print(resultado)
        return resultado
    except Exception as e:
        print(e)
        return {"error": "Ocurrió un error"}

app.mount("/", StaticFiles(directory="public", html=True))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=4600)
