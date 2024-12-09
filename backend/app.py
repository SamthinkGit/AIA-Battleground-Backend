from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.game import Game
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # Permite solicitudes desde cualquier origen. Cambia esto por el dominio específico en producción
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los encabezados
)

game = Game()


class StepResponse(BaseModel):
    actions: list
    observations: str
    status: dict


@app.post("/game/step", response_model=StepResponse)
def game_step():
    """
    Execute one step in the game and return the result.
    """
    if game.has_ended():
        raise HTTPException(status_code=400, detail="Game has already ended.")
    return game.step()


@app.get("/game/ended")
def game_ended():
    """
    Check if the game has ended.
    """
    return {"ended": game.has_ended()}

@app.post("/game/restart")
def game_restart():
    global game
    game = Game()  # Reinicia el estado del juego
    return {"message": "Game restarted"}