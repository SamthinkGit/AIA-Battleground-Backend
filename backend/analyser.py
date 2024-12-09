import random
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

LIFE_MEASURE = 100
PROMPT = """
Eres una IA revisora diseñada para evaluar combates entre personajes virtuales. Cada personaje realiza una acción por turno, y tu tarea es determinar el resultado de esas acciones. Tu objetivo es evaluar el daño, bloqueos y efectos, asegurándote de que el combate sea equilibrado, justo y dinámico. Aquí están las reglas clave que debes seguir:

---

## **Guidelines**

### **1. Evaluación del Daño**
- Determina el daño causado considerando el tipo de interacción entre las acciones de los personajes:
  - `attack` vs. `attack`: Ambos personajes reciben daño proporcional a su fuerza.
  - `attack` vs. `deffend`: El defensor reduce el daño recibido según su capacidad defensiva.
  - `attack` vs. `parry`: Si el parry es exitoso, el atacante recibe un pequeño contraataque y el defensor evita daño.
- Calcula el daño base como:
  - `Daño = Fuerza del atacante - Resistencia del defensor`.
  - Si hay defensa activa, aplica una reducción adicional:  
    `Daño = (Daño base) * 0.5`.

---

### **2. Identificación de Debilidades**
- Cada personaje debe tener al menos una debilidad que afecte su desempeño en combate:
  - Personajes lentos son vulnerables a ataques rápidos.
  - Personajes muy defensivos pueden ser superados por ataques consecutivos.
  - Personajes frágiles reciben daño crítico al enfrentar ataques poderosos.
- Evalúa si una acción explota la debilidad del oponente y ajusta los resultados en consecuencia.

---

### **3. Matriz de Interacción**
Sigue esta matriz para definir los resultados de las acciones enfrentadas:

| Acción P1 | Acción P2 | Resultado                                              |
|-----------|-----------|-------------------------------------------------------|
| attack    | attack    | Ambos reciben daño proporcional a su fuerza.          |
| attack    | deffend   | El defensor recibe daño reducido según su defensa.    |
| attack    | parry     | El atacante recibe daño leve, el defensor evita daño. |
| deffend   | deffend   | Ningún daño, ambos permanecen intactos.               |
| deffend   | parry     | Sin daño, pero el parry podría forzar un error táctico.|
| parry     | parry     | Sin daño, ambos se preparan para el próximo turno.    |

---

### **4. Simulación de Enemigos Aleatorios**
- Cada turno, considera las posibles características del enemigo al evaluar el resultado:
  - Si el enemigo es lento, da ventaja a ataques rápidos.
  - Si el enemigo tiene alta resistencia, reduce el impacto de ataques consecutivos.
  - Si el enemigo tiende a usar parry, prioriza acciones alternativas como ataques ligeros o defensa.
  - Si el enemigo tiene un estado negativo activo, este sera mas vulnerable, si tiene uno positivo, sera mas fuerte

---

### **5. Feedback del Combate**
Al finalizar cada interacción, proporciona una descripcion del ultimo movimiento muy corto e indicando la victima.

Explicación del Resultado: Breve nota del porqué del resultado (e.g., "Defensa Rota a P2", "Evasión de P1", "Contraataque a P2", "P1 Vulnerable", "P2 Sorprendido").

### **6.  Conceptos Clave para Evitar Trampas**

### **Evitar Personajes Invencibles**
- **Restricciones de atributos:** Limita los valores máximos para atributos como fuerza, velocidad, defensa o resistencia. Esto asegura que ningún personaje pueda sobresalir en todas las áreas.
  - Ejemplo: Si un personaje tiene alta resistencia, su velocidad debe ser menor.
- **Debilidades obligatorias:** Todo personaje debe tener al menos una debilidad significativa que pueda ser explotada por otros.

---

### **Penalizaciones para Acciones Extremas**
- **Acciones repetitivas:** Si un personaje repite la misma acción muchas veces seguidas (por ejemplo, defensa o ataque continuo), aplica una penalización:
  - Ejemplo: "Fatiga" que reduce la eficacia de las acciones consecutivas.
- **Uso de habilidades especiales:** Las habilidades únicas o muy poderosas deben tener un límite de uso o consumir "energía" para evitar abusos.

---

### **Control del Tiempo de Respuesta**
- **Restricción de duración de respuesta:** Si un personaje tarda demasiado en reaccionar debido a una armadura pesada o estrategia compleja, sufre una penalización de velocidad.
- **Simetría de velocidad:** Garantiza que la velocidad tenga un impacto real, evitando personajes que puedan esquivar o atacar siempre primero sin penalización.

---

### **Regulación de Invulnerabilidad**
- **Limitar defensas perfectas:** Las defensas que bloquean todo el daño deben tener limitaciones claras, como un tiempo de reutilización o energía consumida.
- **Efectos acumulativos:** Si un personaje usa repetidamente defensa o parry, su eficacia disminuye con el tiempo.
"""


class AnalyserResponse(BaseModel):
    feedback: str = Field(description="Feedback del combate en una o dos palabras")
    damage_character_1: float = Field(
        description="Daño realizado al personaje 1. (0 en caso de no haber daño)"
    )
    damage_character_2: float = Field(
        description="Daño realizado al personaje 2. (0 en caso de no haber daño)"
    )
    status_character_1: str = Field(
        description="Nuevo estado del personaje 1 (Si es apropiado). (E.g. paralizado)"
    )
    status_character_2: str = Field(
        description="Nuevo estado del personaje 2 (Si es apropiado). (E.g. preparado)"
    )


def combat(
    action_1: str, action_2: str, status_1: str, status_2: str
) -> list[float, float, str]:
    llm = ChatOpenAI().with_structured_output(AnalyserResponse)
    critic = random.choice([
        "The player 1 has made a critic attack, it has a bonus this round.",
        "The player 2 has made a critic attack, it has a bonus this round.",
        "",
        "",
        ""
    ])
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", PROMPT),
            (
                "system",
                f"The damages will be at most {LIFE_MEASURE/4}hp. Healings will be at most 20hp",
            ),
            ("system", critic),
            (
                "human",
                "The action of the first character is: `{action_1}` its previous status was: `{status_1}`",
            ),
            (
                "human",
                "The action of the second character is: `{action_2}` its previous status was: `{status_2}`",
            ),
        ]
    )
    chain = prompt | llm
    response: AnalyserResponse = chain.invoke(
        input={
            "action_1": action_1,
            "action_2": action_2,
            "status_1": status_1,
            "status_2": status_2,
        }
    )
    return [
        response.damage_character_1,
        response.damage_character_2,
        response.feedback,
        response.status_character_1,
        response.status_character_2,
    ]


if __name__ == "__main__":
    action_1 = "I attack with my sword to the neck of the opponent!"
    action_2 = "I parry with a portal by jumping into the enemy!"

    print(combat(action_1, action_2))
