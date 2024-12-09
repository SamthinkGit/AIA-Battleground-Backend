from backend.wrappers.character_wrapper import p1_wrapper, p2_wrapper
from backend.analyser import combat
from dataclasses import dataclass
from typing import Optional


@dataclass
class Player:
    health: float = 100
    status: Optional[str] = None
    action: callable
    status: str = ""

    def action(self):
        return self.action()


class Game:

    def __init__(self):
        self.player1 = Player(action=p1_wrapper)
        self.player2 = Player(action=p2_wrapper)

    def step(self):
        msg1, action_1 = self.player1.action()
        msg2, action_2 = self.player2.action()
        status = [self.player1.status, self.player2.status]
        print(f"Actions: {action_1}, {action_2}")

        dmg_1, dmg_2, obs, sts1, sts2 = combat(action_1, action_2, *status)
        self.player1.health -= dmg_1
        self.player2.health -= dmg_2
        self.player1.health = min(self.player1.health, 100)
        self.player2.health = min(self.player2.health, 100)
        self.player1.status = sts1
        self.player2.status = sts2
        print(f"Obs: {obs}")

        return {
            "actions": [action_1, action_2],
            "observations": obs,
            "status": {
                "player1": {
                    "health": self.player1.health,
                    "status": self.player1.status,
                    "action": msg1,
                },
                "player2": {
                    "health": self.player2.health,
                    "status": self.player2.status,
                    "action": msg2,
                },
            },
        }

    def summary(self):
        print("\n" + "=" * 10 + "Player 1" + "=" * 10)
        print(self.player1)
        print(f"-> [{self.player1.status}]")
        print("\n" + "=" * 10 + "Player 1" + "=" * 10)
        print(self.player2)
        print(f"-> [{self.player2.status}]")

    def has_ended(self):
        return self.player1.health < 0 or self.player2.health < 0


if __name__ == "__main__":
    game = Game()
    while True:
        input("STEP?")
        game.step()
        game.summary()
