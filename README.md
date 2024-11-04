# Ideate2D 
## About 
Ideate2D is a 2D game engine built on top of the pygame framework. It is designed to allow quick prototyping of 2D games while handling basic physics simulations and game-events in an implicit, and easily modifiable manner. 

## Design Philosophy 
Ideate2D approaches game making with much the same ideas of a 0 player game such as Conway's Game of Life. The game is a simulation, and the game maker only controls the starting setup of each level. Everything from there on out is largely unscripted, unless explicitly coded for by the game maker using 'special functions' (discussed in the how to use section). 
In theory, the tools provided should be able to make most 2D games, except for the most dynamic ones that modify objects with live input. For such exceptional cases, the entire engine is written in python (except dependencies) and can thus be modified by users in accordance with the license alongside the engine. 

## How to make levels 
A level editor is in the works and a basic version of it is provided under Ideate2D/Scripts/level_editor.py. Using this allows users to draw levels, and select between 3 unique object types that each interact with their environments differently. Once a level is designed, the user can export their level, and it is formatted into a text file containing instructions for the engine to contruct the level at run-time. 
The engine is also a game processing environment, and as such can be packaged with the game (licence included) for distribution. 

The basis for supporting dynamic objects that the player can interact with beyond simple collision is present in version 0.1.0, but shall be more accessible in future version via a dedicated scripting environment within the level editor. 

## How-To-Use Guide: Coming Soon 

## Liability
This project, Ideate2D, was developed as an experimental tool and is provided on an "as-is" basis. While every effort has been made to ensure the accuracy and reliability of the functions and tools provided, no guarantees or warranties are given regarding their performance, correctness, or fitness for a particular purpose.

Important Disclaimers:

- Use at Your Own Risk 
- No Warranty: The author, and any contributors to this repository are not responsible for any errors, omissions, or damages resulting from the use or misuse of the software.
- By using this software, you agree to assume all risks associated with its use.
