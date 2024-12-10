# Al final esto es un copy paste de la ultima seccion, probably les diga que hay que usar ese para que no se compliquen demasiado si no saben python.
# AL igual, todo lo que sea programar que pregunten que tampoco pasa nada

class NanoPortal(BaseModel):
  attack: str = Field(description="(Respuesta de aprox 10 palabras) Aprovecha el mareo y las formas de los portales para hacer daño a tu enemigo.")
  defend: str = Field(description="(Respuesta de aprox 10 palabras) Usar portales para prevenir un ataque que pueda venir de algun enemigo!")
  parry: str = Field(description="(Respuesta de aprox 10 palabras) Aprovecha para contraatacar con la habilidad mas original y creativa que veas posible con tus habilidades!")


pj = ChatOpenAI(model="gpt-4o-mini").with_structured_output(NanoPortal)
prompt = """
Es tu momento de luchar! Utiliza tus portales para atacar al enemigo y cortarle en sus puntos mas debiles. Manten invocando portales para
esquivar los posibles ataques y si lo ves apropiado, haz un portal al vacio para pillar desprevenido a tu enemigo""" # ... La creatividad se la dejo a ellos xD

# description="Este personaje es un hechicero de tamaño nano atomico que es capaz de crear portales para atacar a sus enemigos"

response = pj.invoke(prompt)

print("Ataque: ", response.attack, "\n")
print("Defensa: ", response.defend, "\n")
print("Contraataque: ", response.parry)