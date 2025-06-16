Name: Hülya Ceren Lüleci  
University: Ankara Bilim University  
Department: Computer Engineering, 2nd Year  

Project: Stanford Code In Place 2025 Final Project  
Title: SnackLotl — A Visual Underwater-Themed Game

Demo Video  
-----------
You can watch the gameplay demo here:  
https://www.youtube.com/watch?v=R3J9KMKOv78

You can see the official project showcase here:
https://codeinplace.stanford.edu/2025/showcase?project=HL1F0C4hRXgDOMGyyfM0oOrkzI13


Overview:
---------
SnackLotl is a underwater-themed mini-game where you control a cute pink axolotl swimming near the ocean floor.  
The goal is simple: collect as many snacks (shrimp and fish) as possible, while avoiding toxic jellyfish that cost you lives.

## Key Features

- AI-generated, colorful visuals (Craiyon & DALL·E)  
- Background music and sound effects  
- Real-time scoring and responsive keyboard controls  
- 3-life system — lose a life when hitting a toxin  
- Game Over screen with Restart and Quit options  
- Intuitive keyboard movement (A/D or arrow keys)  
- Simple frame-by-frame animation and clean transitions 


This project was created as the final project for Stanford University's **Code in Place 2025** course.

Development  
-----------  
- Code editor: Visual Studio Code  
- Version control: Git (hosted on GitHub)  
- The full commit history is available in this repository  
- Demo recorded with OBS Studio

How to Run:
-----------
1. Requirements:
   - Python 3.x must be installed.
   - Install the `pygame` library:
     (pip install pygame)
     pip install -r requirements.txt

     
2. Run the game:
  - Open a terminal or command prompt.

  - Navigate to the project directory:
    - cd Stanford_CodeInPlace_AxolotlGame

      - python main.py
    

File Structure:
---------------
- `main.py`            : Main game loop: initializes window, loads assets, runs game logic  
- `logic.py`           : Core logic: collisions, score, lives
- `player.py`          : Axolotl player class and movement
- `food.py`            : Food and toxin item logic 
- `assets/`            
  - `axolotl_1.png`          : Player sprites (Craiyon)
  - `axolotl_2.png`          
  - `axolotl_3.png`          
  - `axolotl_4.png`          
  - `food_shrimp.png`      : Edible item (Craiyon)
  - `food_fish.png`        : Edible item (Craiyon)
  - `food_toxin.png`       : Harmful item (Craiyon)
  - `background.jpg`       : Underwater background (DALL·E)
  - `music.ogg`            : Background music track (looped, sourced from OpenGameArt.org) 

Features:
---------
- Custom axolotl character: AI-generated pink axolotl sprite
- Simple controls: Use arrow keys or A/D to move left and right
- Falling items: Random food and toxin items drop from the top
- Scoring system: Gain points by catching shrimp or fish
- Lives system: Lose a life when hitting a toxin — 3 strikes and it's game over
- Game Over screen: Includes options to restart or quit
- High-quality visuals: All assets designed with an underwater, pastel-colored theme
- Simple animation and responsive controls

Credits:
--------
- Game Design & Development: Hülya Ceren Lüleci  
- Visual Assets: Generated using Craiyon & DALL·E  
- Audio: Background music from OpenGameArt.org  
- Image Editing: Paint and Fotor (PNG cleanup and cutouts, minor image edits) 

Known Issues:
-------------
- Missing or renamed asset files may cause the game to crash  
- Screen scaling may not be optimal on ultra-wide or very small displays  
- Not compatible with touchscreens or mobile devices  

License:
--------
This project was created for educational and demonstration purposes only.  
All assets and code are owned by the creator and are shared under fair use for non-commercial, personal, and academic use.
