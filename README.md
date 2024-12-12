# AIA-Battleground-Backend
![image](https://github.com/user-attachments/assets/b3e8f897-bf80-4586-840d-bac09119097e)

<div align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
</div>

### Main Components

- **Backend**: Contains the game logic and AI analyzer.
  - `app.py`: Main backend server.
  - `analyser.py`: File to modify the guided prompt of the analyzer.
  - `game.py`: Initial game configuration and mechanics.
  - `wrappers/character_wrapper.py`: Defines fighters and their attributes.
  - `wrappers/examples`: Examples of customized fighters.

- **Frontend**: Graphical interface accessible via a web browser.
  - `index.html`: Main game page.
  - `media/`: Contains images and videos used in the design.
  - `scripts/`: Contains `script.js` for frontend functionality.
  - `styles/`: Contains `styles.css` for visual styling.

- **scripts/setup.sh**: Script to set up project dependencies.

## Installation

### Prerequisites

- Python 3.10 or higher.
- Web browser (Firefox, Chrome, Edge, etc.).
- Some python libraries such as langchain, colorama, etc. (requirements.txt not defined yet)
### Initial Setup

1. Clone this repository:
   ```bash
   git clone <REPOSITORY_URL>
   cd AIA-Battleground-Backend
   ```

2. Run the `setup.sh` script to link the PYTHONPATH:
   ```bash
   source scripts/setup.sh
   ```
   This script must be run in every new terminal session or added to the `~/.bashrc` file for automation.

   To add it to bashrc:
   ```bash
   echo "source $(pwd)/scripts/setup.sh" >> ~/.bashrc
   ```

## Usage

### Starting the Server

1. Launch the backend on port 8000:
   ```bash
   uvicorn backend.app:app --port 8000
   ```

2. Launch the frontend server on port 5500:
   ```bash
   cd frontend
   python -m http.server 5500
   ```

### Accessing the Game

Open a web browser and visit:
- `http://localhost:5500` to access the frontend.

### Game Customization

1. **AI Analyzer**: Modify the `backend/analyser.py` file to adjust the guided prompt as needed for the event.
2. **Game Parameters**: Edit the `backend/game.py` file to change initialization values and game mechanics.
3. **Fighters**: Modify or add fighters in `backend/wrappers/character_wrapper.py`. Each fighter must define a `response` variable with `attack`, `defend`, and `parry` attributes.
4. **Visual Appearance**: Edit the `frontend/index.html` file and resources in the `media/` folder to customize names, images, and backgrounds.

### Examples

Preconfigured fighter examples (`example_1.py`, `example_2.py`, etc.) are included in the `wrappers/examples/` folder and can be used directly in battles.

## Contributing

We welcome contributions to the project! Please open an issue or pull request in the repository if you have suggestions or improvements.
