# Al final esto es un copy paste de la ultima seccion, probably les diga que hay que usar ese para que no se compliquen demasiado si no saben python.
# AL igual, todo lo que sea programar que pregunten que tampoco pasa nada

class NanoPortal(BaseModel):
  attack: str = Field(description="(Respuesta de aprox 10 palabras) Haz un ataque de mimos, el corazon del enemigo quedara expuesto")
  defend: str = Field(description="(Respuesta de aprox 10 palabras) Cambias las reglas del juego, ahora el daño recibido se convierte en vida para ti. Esto es la ley Pulpi!")
  parry: str = Field(description="(Respuesta de aprox 10 palabras) Paraliza al enemigo a base de ternura, convierte el daño enemigo en poder Pulpito!")


pj = ChatOpenAI(model="gpt-4o-mini").with_structured_output(NanoPortal)
prompt = """
Es tu momento de luchar! Eres un peluche pulpito! Utiliza tus ataques de forma creativa para matar al enemigo!""" # ... La creatividad se la dejo a ellos xD

# description="Este personaje es un hechicero de tamaño nano atomico que es capaz de crear portales para atacar a sus enemigos"

response = pj.invoke(prompt)

print("Ataque: ", response.attack, "\n")
print("Defensa: ", response.defend, "\n")
print("Contraataque: ", response.parry)