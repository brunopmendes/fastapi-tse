from fastapi import FastAPI
from http import HTTPStatus
from services.consulta import get_candidates


app = FastAPI()

@app.get("/healthcheck")
def health_check():
    return {"Status": HTTPStatus.OK}


@app.get("/consultar_candidatos/ano/{ano}/uf/{uf}/municipio/{municipio}/cargo/{cargo}")
def consultar_candidatos(ano: str, uf: str, municipio: str, cargo: str):
    candidates = get_candidates(year=ano, uf=uf, municipality=municipio, position=cargo) 
    return [candidate.dict() for candidate in candidates]

