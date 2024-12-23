document.addEventListener("DOMContentLoaded", () => {
    const apiUrl = "http://127.0.0.1:8000";

    // Elements
    const leftAction = document.querySelector(".col-left.action");
    const leftGeneration = document.querySelector(".col-left.generation");
    const leftHealth = document.querySelector(".left-health");

    const rightAction = document.querySelector(".col-right.action");
    const rightGeneration = document.querySelector(".col-right.generation");
    const rightHealth = document.querySelector(".right-health");

    const judgeText = document.querySelector(".judge p");
    const roundNumber = document.querySelector(".round h2");
    const startButton = document.querySelector(".button h2");

    const leftState = document.querySelector(".state.left");
    const rightState = document.querySelector(".state.right");

    let currentRound = 1;

    // Reinicia la animación de un elemento
    function restartAnimation(element, animationClass) {
        if (!element) return;
        element.classList.remove(animationClass);
        void element.offsetWidth; // Fuerza reflujo
        element.classList.add(animationClass);
    }
    function updateHealthBar(healthElement, healthValue) {
        if (healthValue > 75) {
            healthElement.style.backgroundColor = "green";
        } else if (healthValue > 25) {
            healthElement.style.backgroundColor = "orange";
        } else {
            healthElement.style.backgroundColor = "red";
        }
    }

    function animateJudgeText() {
        judgeText.style.color = "red";
        judgeText.style.fontSize = "48px";
        setTimeout(() => {
            judgeText.style.color = "rgb(248, 237, 85)";
            judgeText.style.fontSize = "45px";
        }, 400); // Reset style after 500ms
    }
    function animateState(stateElement) {
        stateElement.style.color = "cyan";
        stateElement.style.fontSize = "32px";
        setTimeout(() => {
            stateElement.style.color = "white";
            stateElement.style.fontSize = "30px";
        }, 400); // Reset style after 400ms
    }
    
    // Actualiza la interfaz con animaciones sincronizadas
    function updateUI(data) {
        const { actions, observations, status } = data;

        // Paso 1: Muestra las acciones
        leftAction.textContent = status.player1.action;
        rightAction.textContent = status.player2.action;
        restartAnimation(leftAction, "fade-up");
        restartAnimation(rightAction, "fade-up");

        // Paso 2: Muestra las generaciones después de 1 segundo
        setTimeout(() => {
            leftGeneration.textContent = actions[0];
            rightGeneration.textContent = actions[1];
            restartAnimation(leftGeneration, "fade-in");
            restartAnimation(rightGeneration, "fade-in");
        }, 1000);

        // Paso 3: Cambia el texto del juez y actualiza las barras de salud después de 2 segundos
        setTimeout(() => {

            judgeText.textContent = observations;

            if (status.player1.health <= 0) {
                judgeText.textContent = 'GANADOR "Yellow-Team"';
            }

            if (status.player2.health <= 0) {
                judgeText.textContent = 'GANADOR "Red-Team"';
            }
            animateJudgeText();

            leftHealth.style.width = `${status.player1.health}%`;
            leftHealth.textContent = `Health: ${status.player1.health}`;

            rightHealth.style.width = `${status.player2.health}%`;
            rightHealth.textContent = `Health: ${status.player2.health}`;
            updateHealthBar(rightHealth, status.player2.health)
            updateHealthBar(leftHealth, status.player1.health)
        }, 2000);
        // restartAnimation(leftHealth, "health-bar");
        // restartAnimation(rightHealth, "health-bar");

        // Actualiza el estado de los jugadores
        setTimeout(() => {
            if (status.player1.status && status.player1.status !== "None") {
                leftState.textContent = status.player1.status;
                animateState(leftState);
            } else {
                leftState.textContent = "Neutral"; // Oculta el estado si es "None"
            }

            if (status.player2.status && status.player2.status !== "None") {
                rightState.textContent = status.player2.status;
                animateState(rightState);
            } else {
                rightState.textContent = "Neutral"; // Oculta el estado si es "None"
            }
        }, 3000);

    }

    // Comprueba si el juego ha terminado
    async function checkGameEnded() {
        const response = await fetch(`${apiUrl}/game/ended`);
        const data = await response.json();
        return data.ended;
    }

    // Ejecuta un paso del juego
    async function executeStep() {
        try {
            startButton.textContent = "Cargando...";

            const ended = await checkGameEnded();
            if (ended) {
                judgeText.textContent = "Game has ended!";
                startButton.textContent = "Restart";
                return;
            }

            const response = await fetch(`${apiUrl}/game/step`, { method: "POST" });
            const data = await response.json();

            updateUI(data);

            currentRound += 1;
            roundNumber.textContent = currentRound;

            startButton.textContent = "Step";
        } catch (error) {
            console.error("Error executing game step:", error);
            startButton.textContent = "Step";
        }
    }

    // Reinicia el juego
    async function restartGame() {
        try {
            const response = await fetch(`${apiUrl}/game/restart`, { method: "POST" });
            if (!response.ok) {
                throw new Error("Failed to restart the game");
            }

            judgeText.textContent = "Game restarted!";
            startButton.textContent = "Step";
            roundNumber.textContent = "1";
            currentRound = 1;

            leftAction.textContent = "";
            leftGeneration.textContent = "";
            rightAction.textContent = "";
            rightGeneration.textContent = "";
            leftHealth.style.width = "100%";
            leftHealth.textContent = "Health: 100";
            rightHealth.style.width = "100%";
            rightHealth.textContent = "Health: 100";
        } catch (error) {
            console.error("Error restarting game:", error);
        }
    }

    startButton.addEventListener("click", () => {
        if (startButton.textContent === "Restart") {
            restartGame();
        } else {
            executeStep();
        }
    });
});
