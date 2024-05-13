from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
import uvicorn
from typing import Optional




app = FastAPI()

filmes = [
    {
        'id':1,
        'titulo': "O Poderoso Chefão",
        'Diretor': "francis Ford Copoola",
        'Ano': 1972
    },
    {
        'id': 2,
        'titulo': "O guarda costa",
        'Diretor': "Mick Jackson",
        'Ano': 1993
    },
    {
        'id': 3,
        'titulo': "Pulp Fiction",
        'Diretor': "Tarantino",
        'Ano': 1994
    },
]



@app.get("/")
def home():
    return "Welcome, Seja Bem vindo, Acueillir - API Funcionando"


# Consultar - Check
@app.get("/filmes")
def obter_filmes():
    return JSONResponse(content=filmes)

# Check by id - Consultar por id 
@app.get("/filmes/{filme_id}")
def obter_filme_id(filme_id: int):
    for filme in filmes:
        if filme['id'] == filme_id:
            return filme                        # else was breaking line and loop
    return JSONResponse(content={"mensagem": "Filme não encontrado"}, status_code=404)

# Editar - Edit
@app.put("/filmes/add/{i}")
def editar_filme_id(i:int, titulo: Optional[str]= None, diretor: Optional[str]= None, ano: Optional[int]= None):
    for filme in filmes:
        if filme[id] == i:
            if titulo:
                filme['titulo'] = titulo
            if diretor:
                filme['Diretor'] = diretor
            if ano:
                filme['Ano'] = ano
            return {"mensagem": "Filme editado com sucesso!"}
        
    return JSONResponse(content={"mensagem": "Filme&ID não encontrado!"})



# Deletar - Delete 
@app.delete("/filmes/{d}")
def excluir_filme(d: int):
    for index, filme in enumerate(filmes):
        if filme.get(id) == d:
            del filmes[index]

    return JSONResponse(content=filmes)


    
# localhost 
if __name__ == "__main__":
    uvicorn.run(app, port=8000)

