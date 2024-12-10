import random
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI


def p1_wrapper():
    print = lambda *args, **kwargs: None

    # START
    # ===================================== WRAPPER ==================================
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
    # ==================================================================================
    # END

    return choice(response)


def p2_wrapper():
    print = lambda *args, **kwargs: None

    # START
    # ===================================== WRAPPER ==================================
    class NanoPortal(BaseModel):
        attack: str = Field(description="(Respuesta de aprox 10 palabras) Dispara miel venenosa por todo el alrededor, envenenando y paralizando a todo lo que toca excepto a si mismo")
        defend: str = Field(description="(Respuesta de aprox 10 palabras) Lanza un escudo mágico que protege y le vuelve invisible, escondiendole del enemigo. El escudo también te cura y da fuerzas para atacar")
        parry: str = Field(description="(Respuesta de aprox 10 palabras) Antes de que el enemigo reaccione le ataca con millones de zarpazos por todas partes dejandole debilitado, aturdido y cegado")


    pj = ChatOpenAI(model="gpt-4o-mini").with_structured_output(NanoPortal)
    prompt = """
    Eres un guerrero mítico con el unico objetivo de derrotar a tu enemigo antes de que reaccione, curandete cuando sea necesario.
    """ # ... La creatividad se la dejo a ellos xD

    description="Eres el mejor peluche guerrero del mundo, mitad gato, mitad tortitas. "

    response = pj.invoke(prompt)

    print("Ataque: ", response.attack, "\n")
    print("Defensa: ", response.defend, "\n")
    print("Contraataque: ", response.parry)
    # ==================================================================================
    # END

    return choice(response)


def choice(response):
    return random.choice(
        [
            ("Attack", response.attack),
            ("Defend", response.defend),
            ("Parry", response.parry),
        ]
    )


# TODO: Cortar el maximo response de cada jugador
