# Ideate2D 
## Important 
This software requires pygame to work. Pygame can be installed according the website: [GettingStarted - pygame wiki](https://www.pygame.org/wiki/GettingStarted) 

Information on the liabilities taken for this software and terms and conditions can be found at the bottom of the README.md file supplied with this software, and at https://github.com/shashankraocoding/Ideate2D. This software is distributed under the same license as Pygame (the  [GNU LGPL version 2.1](https://www.gnu.org/copyleft/lesser.html), also supplied with this software). 

## Video Guides Coming Soon!! 

## About 
### What You See Is What You Get
Ideate2D holds this moto at its core. You design what you want without worrying about the basics, like scaling or image management, gravity, object physics, or any of the other million things you'd rather leave to us. The end product is exactly as it appears to you in the editor. 

### Control-freak? Laissez-faire? 
Are other game engines not giving you enough control over your game? Or perhaps working with a framework is *too* low level. Ideate2D offers the middle ground. You code what you want only if you want to code it. With a modularity-first focus, each individual object can be made as complex or as simple as you want - without touching anything other than python! 

Want to use other libraries? Just use them like normal, and they (should) work with Ideate2D seamlessly! 

## Design Philosophy 

> [!Key] 
> When it really comes down to it, a game is just a simulation. The game author sets up the game world, but what happens next is up to the player. 

This is the theory behind Ideate2D. You setup the game world, and the player takes it from there. You can be as specific or vague as you like. 

# Making Levels 
### 3 objects to make anything 
Ideate2D keeps it simple: everything can be made with these 3 objects: 
1. Static Objects 
2. Dynamic Objects 
3. Illusory Objects 

#### Static Objects 
As the name implies, they are static. More specifically, **no external forces** can act on them. That said, they can be moved (example, a moving platform) if explicitly made to do so using [Special Functions](https://github.com/ShashankRaoCoding/Ideate2D/tree/main?tab=readme-ov-file#special-functions). 

#### Dynamic Objects: 
External forces, including being pushed by the player, are enabled! 

#### Illusory Objects: 
These are the juicy ones! Arguably the most important of the 3, and the most customizable. 

An illusory object is, as the name implies, like an illusion. The player can see them (if they aren't given an invisible image), and can walk through them, but can neither push them, nor is obstructed by them. What's the point? They can be used to trigger events! 

If given the appropriate [Special Functions](https://github.com/ShashankRaoCoding/Ideate2D/tree/main?tab=readme-ov-file#special-functions), an illusory object can detect when a player passes through it to start an event. Alternatively, use it to add cosmetic features, such as a background, trees, or bushes, etc. 

#### Custom Objects: 
If you want to make an object of your own, just go to datastructures/objects.py and define an object. Note that it **must** inherit from the '*object_template*' object already provided in the same file. 

### Special Functions 
Every object in Ideate2D has a special function. This special function is called once every game loop cycle. By default, this is set to do nothing. However, you can code these functions however you like. For example, a player object might have the special function 'handle_inputs' to move the player according to the inputs. 

Just code your special function in datastructures/specials.py as a function. It must take its associated object as the only argument. Once done, the level editor will automatically detect the function. Now you can assign it to an object in the level editor! 
## Liability
This project, Ideate2D, was developed as an experimental tool and is provided on an "as-is" basis. While every effort has been made to ensure the accuracy and reliability of the functions and tools provided, no guarantees or warranties are given regarding their performance, correctness, or fitness for a particular purpose.

Important Disclaimers:

- Use at Your Own Risk 
- No Warranty: The author, and any contributors to this repository are not responsible for any errors, omissions, or damages resulting from the use or misuse of the software.
- By using this software, you agree to assume all risks associated with its use.
