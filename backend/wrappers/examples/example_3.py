# Al final esto es un copy paste de la ultima seccion, probably les diga que hay que usar ese para que no se compliquen demasiado si no saben python.
# AL igual, todo lo que sea programar que pregunten que tampoco pasa nada

class NanoPortal(BaseModel):
  attack: str = Field(description="(Respuesta de aprox 10 palabras) Ataca a tu enemigo causando daño instantaneo y paralisis")
  defend: str = Field(description="(Respuesta de aprox 10 palabras) Prepara un bonificador para ti y vuelvete invisible antes de que te ataque")
  parry: str = Field(description="(Respuesta de aprox 10 palabras) Realiza un contrataque al enemigo aprovechando que este expuesto envenenando su corazon")


pj = ChatOpenAI(model="gpt-4o-mini").with_structured_output(NanoPortal)
prompt = """
Es tu momento de luchar! Eres una botellita de pociones de minecraft. Cuando te ataquen, mete un estado aleatorio a tu enemigo!""" # ... La creatividad se la dejo a ellos xD

# description="Este personaje es un hechicero de tamaño nano atomico que es capaz de crear portales para atacar a sus enemigos"

response = pj.invoke(prompt)

print("Ataque: ", response.attack, "\n")
print("Defensa: ", response.defend, "\n")
print("Contraataque: ", response.parry)