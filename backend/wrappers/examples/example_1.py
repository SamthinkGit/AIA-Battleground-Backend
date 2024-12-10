from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
# Al final esto es un copy paste de la ultima seccion, probably les diga que hay que usar ese para que no se compliquen demasiado si no saben python.
# AL igual, todo lo que sea programar que pregunten que tampoco pasa nada


class NanoPortal(BaseModel):
    attack: str = Field(
        description="(Respuesta de aprox 10 palabras) Lanza zarpazos gatunos agiles y rapidos, dejando heridas letales que infectan y dejan vulnerable al enemigo"
    )
    defend: str = Field(
        description="(Respuesta de aprox 10 palabras) Esquiva todos los ataques haciendo un salto gatuno rapido, dejando a tu enemigo despistado y curandote rapidamente"
    )
    parry: str = Field(
        description="(Respuesta de aprox 10 palabras) Muerde y ataca a tu enemigo antes de que ataque, anulando su ofensiva y dejandole expuesto a un remate!"
    )


pj = ChatOpenAI(model="gpt-4o-mini").with_structured_output(NanoPortal)
prompt = """
Es tu momento de luchar! Eres un mega gigante gato que tratara de atacar al enemigo rodeandole y atacandole por todos sus puntos débiles.
Trata de ser creativo y utiliza ataques de conjunto. Para defenderte utiliza secuestros al enemigo y para atacar lanza zarpazos, fuego y usa sobretodo tu agilidad
para matar al enemigo."""  # ... La creatividad se la dejo a ellos xD

# description="Este personaje es un hechicero de tamaño nano atomico que es capaz de crear portales para atacar a sus enemigos"

response = pj.invoke(prompt)

print("Ataque: ", response.attack, "\n")
print("Defensa: ", response.defend, "\n")
print("Contraataque: ", response.parry)


