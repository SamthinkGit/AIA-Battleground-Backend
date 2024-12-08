import random
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI


def p1_wrapper():
    print = lambda *args, **kwargs: None

    # ===================================== WRAPPER ==================================
    # Al final esto es un copy paste de la ultima seccion, probably les diga que hay que usar ese para que no se compliquen demasiado si no saben python.
    # AL igual, todo lo que sea programar que pregunten que tampoco pasa nada

    class NanoPortal(BaseModel):
        attack: str = Field(
            description="(Respuesta de aprox 10 palabras) Aprovecha el mareo y las formas de los portales para hacer daño a tu enemigo."
        )
        defend: str = Field(
            description="(Respuesta de aprox 10 palabras) Usar portales para prevenir un ataque que pueda venir de algun enemigo!"
        )
        parry: str = Field(
            description="(Respuesta de aprox 10 palabras) Aprovecha para contraatacar con la habilidad mas original y creativa que veas posible con tus habilidades!"
        )

    pj = ChatOpenAI(model="gpt-4o-mini").with_structured_output(NanoPortal)
    prompt = """
    Es tu momento de luchar! Utiliza tus portales para atacar al enemigo y cortarle en sus puntos mas debiles. Manten invocando portales para
    esquivar los posibles ataques y si lo ves apropiado, haz un portal al vacio para pillar desprevenido a tu enemigo"""  # ... La creatividad se la dejo a ellos xD

    description = "Este personaje es un hechicero de tamaño nano atomico que es capaz de crear portales para atacar a sus enemigos"

    response = pj.invoke(prompt)

    print("Ataque: ", response.attack, "\n")
    print("Defensa: ", response.defend, "\n")
    print("Contraataque: ", response.parry)
    # ==================================================================================

    return choice(response)     


def p2_wrapper():
    print = lambda *args, **kwargs: None

    # ===================================== WRAPPER ==================================
    # Al final esto es un copy paste de la ultima seccion, probably les diga que hay que usar ese para que no se compliquen demasiado si no saben python.
    # AL igual, todo lo que sea programar que pregunten que tampoco pasa nada

    class ShadowDancer(BaseModel):
        attack: str = Field(
            description="(Respuesta de aprox 10 palabras) Usa sombras para confundir al enemigo y atacar rápidamente."
        )
        defend: str = Field(
            description="(Respuesta de aprox 10 palabras) Usa tu escudo y curate lo mas rapido posible."
        )
        parry: str = Field(
            description="(Respuesta de aprox 10 palabras) Desvía el ataque y responde con un golpe en las sombras."
        )

    pj = ChatOpenAI(model="gpt-4o-mini").with_structured_output(ShadowDancer)
    prompt = """
    Eres un maestro de las sombras. Usa tu habilidad para atacar desde ángulos inesperados, confundir a tus enemigos y mantenerte siempre fuera de su alcance. Si te ves acorralado, desaparece en las sombras y vuelve a aparecer en el lugar más inesperado para contraatacar con precisión quirúrgica.
    """

    description = "Este personaje es un ninja que utiliza las sombras como extensión de su cuerpo para atacar y defenderse."

    response = pj.invoke(prompt)

    print("Ataque: ", response.attack, "\n")
    print("Defensa: ", response.defend, "\n")
    print("Contraataque: ", response.parry)


    # ==================================================================================

    return choice(response)


def choice(response):
    return random.choice([("Attack", response.attack), ("Defend", response.defend), ("Parry", response.parry)])
