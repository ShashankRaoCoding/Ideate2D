import tkinter as tk
from tkinter import filedialog
import os 
import sys 
import pygame 
from tqdm import tqdm 
import shankskit 

def folder_selector_ui():
    def select_folders():
        nonlocal selected_folders
        file_paths = filedialog.askdirectory()
        if file_paths:
            selected_folders.append(file_paths) 
            root.destroy()
        else:
            label_file_path.config(text="No files selected")

    selected_folders = []

    # Create the main window
    root = tk.Tk()
    root.title("File Selector")
    root.geometry("400x300")

    # Add a label
    label_instruction = tk.Label(root, text="Click the button below to select files:")
    label_instruction.pack(pady=10)

    # Add a button to select files
    btn_select_folders = tk.Button(root, text="Select Folders", command=select_folders)
    btn_select_folders.pack(pady=5)

    # Add a label to display the file paths
    label_file_path = tk.Label(root, text="No folders selected", wraplength=380, fg="blue")
    label_file_path.pack(pady=10)

    # Run the application
    root.mainloop()

    return selected_folders

class editor(): 
    def __init__(self):
        self.display = pygame.display.set_mode((0,0))
        self.gameObjects = [] 
        self.events = [] 
        self.clock = pygame.time.Clock() 
        self.fps = 60 
        self.selected = None 
        self.holdingPos = None 
        self.selection_index = 0 
        self.show = False 
        self.focus = None 
        pass
    
    def run(self): 
        self.editing = True 
        while self.editing: 
            self.handle_inputs() 
            self.wipe() 
            self.draw() 
            self.update() 

    def handle_inputs(self): 
        self.mouse_pos = pygame.mouse.get_pos() 
        for event in self.events: 
            if (event.type == pygame.QUIT): 
                pygame.quit() 
                sys.exit() 
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                if event.button == 1: # this is now working ignore this comment. 
                    for gameObjectInstance in self.gameObjects: 
                        if gameObjectInstance.getSprite().get_rect(topleft=gameObjectInstance.position).collidepoint(self.mouse_pos): 
                            self.selected = gameObjectInstance 
            elif (event.type == pygame.KEYDOWN): 
                if (event.key == pygame.K_ESCAPE): 
                    pygame.quit() 
                    sys.exit() 
                elif (event.key == pygame.K_e): 
                    self.export() 
                elif (event.key == pygame.K_d): 
                        size = (self.selected.size[0], self.selected.size[1]) 
                        self.selected = gameObject(self.mouse_pos,sprite_list=self.selected.sprite_list,type=self.selected.type,special_function_name=self.selected.special_function_name, sprite_list_name=self.selected.sprite_list_name) 
                        self.selected.size = size 
                        self.selected.resizeSprites() 
                        self.gameObjects.append(self.selected) 
                elif (event.key == pygame.K_h): 
                    self.show = not(self.show) 
                elif (event.key == pygame.K_t): 
                    import datastructures.objects 
                    self.selected.type = shankskit.select_from_list(list(shankskit.getClasses(datastructures.objects).keys())[::-1]) 
                elif (event.key == pygame.K_f): 
                    self.focus = self.selected 
                elif event.key == pygame.K_a: 
                    try: 
                        sprite_list = [] 
                        objectPosition = self.mouse_pos 
                        folders_path = folder_selector_ui() 
                        for folder_path in folders_path: 
                            for sprite_path in os.listdir(folder_path) : 
                                sprite_list.append(pygame.image.load(os.path.join(folder_path,sprite_path)) ) 
                            pathParts = folder_path.split("/") 
                            sprite_list_name = pathParts[-1+len(pathParts)]
                            self.selected = gameObject(objectPosition,sprite_list=sprite_list,type="static_object",special_function_name="static", sprite_list_name=sprite_list_name) 
                            self.gameObjects.append(self.selected) 
                    except Exception as e: 
                        print(e) 
                elif (event.key == pygame.K_q and self.selected != None): 
                    sprite_list = [] 
                    folders_path = folder_selector_ui() 
                    for folder_path in folders_path: 
                        for sprite_path in os.listdir(folder_path) : 
                            sprite_list.append(pygame.image.load(os.path.join(folder_path,sprite_path)) ) 
                        pathParts = folder_path.split("/") 
                        sprite_list_name = pathParts[-1+len(pathParts)]
                    self.selected.sprite_dict[sprite_list_name] = sprite_list 
                elif event.key == pygame.K_r: 
                    if self.selected != None: 
                        self.holdingPos = self.mouse_pos 
                elif (event.key == pygame.K_TAB and self.selected != None): 
                    import datastructures.specials 
                    self.selected.special_function_name = shankskit.select_from_list(list(shankskit.getFunctions(datastructures.specials).keys())[::-1]) 
            elif (event.type == pygame.KEYUP): 
                if event.key == pygame.K_r: 
                    self.holdingPos = None 
        
        keys_pressed = pygame.key.get_pressed() 
        if keys_pressed[pygame.K_g]: 
            if type(self.selected) == gameObject: 
                self.selected.position = self.mouse_pos 
        if keys_pressed[pygame.K_r]: 
            if self.selected != None and (self.holdingPos != None): 
                width = abs(self.holdingPos[0]-self.mouse_pos[0]) 
                height = abs(self.holdingPos[1]-self.mouse_pos[1]) 
                self.selected.size = [width, height] 
                self.selected.resizeSprites() 
        if keys_pressed[pygame.K_DOWN]: 
            for gameObjectInstance in self.gameObjects: 
                gameObjectInstance.position = [gameObjectInstance.position[0],-10+gameObjectInstance.position[1]] 
        if keys_pressed[pygame.K_UP]: 
            for gameObjectInstance in self.gameObjects: 
                gameObjectInstance.position = [gameObjectInstance.position[0],+10+gameObjectInstance.position[1]] 
        if keys_pressed[pygame.K_LEFT]: 
            for gameObjectInstance in self.gameObjects: 
                gameObjectInstance.position = [+10+gameObjectInstance.position[0],gameObjectInstance.position[1]] 
        if keys_pressed[pygame.K_RIGHT]: 
            for gameObjectInstance in self.gameObjects: 
                gameObjectInstance.position = [-10+gameObjectInstance.position[0],gameObjectInstance.position[1]] 

    def export(self): 
        try: 
            self.gameObjects.remove(self.focus) 
            stagedatafile = open("stagedata/" + str(len(os.listdir("stagedata/"))) + ".txt", "w") 
            for gameObjectInstance in self.gameObjects: 
                gameObjectSyntax = gameObjectInstance.getSyntax() 
                stagedatafile.write(gameObjectSyntax + "\n") 
                for sprite_list_name, sprite_list in gameObjectInstance.sprite_dict.items(): 
                    if os.path.exists(f"sprites/{sprite_list_name}"): 
                        pass 
                    else: 
                        os.mkdir(f"sprites/{sprite_list_name}") 
                        for sprite_index, sprite_instance in tqdm(enumerate(sprite_list)): 
                            pygame.image.save(sprite_instance,f"sprites/{sprite_list_name}/{sprite_index}.png") 
                            events = pygame.event.get() 

            gameObjectSyntax = self.focus.getSyntax() 
            stagedatafile.write(gameObjectSyntax + "\n") 
            for sprite_list_name, sprite_list in gameObjectInstance.sprite_dict.items(): 
                if os.path.exists(f"sprites/{sprite_list_name}"): 
                    pass 
                else: 
                    os.mkdir(f"sprites/{sprite_list_name}") 
                    for sprite_index, sprite_instance in tqdm(enumerate(sprite_list)): 
                        pygame.image.save(sprite_instance,f"sprites/{sprite_list_name}/{sprite_index}.png") 
                        events = pygame.event.get() 
            stagedatafile.write("self.current_stage.set_focus(self.current_stage.objects[-1+len(self.current_stage.objects)]) ") 
            self.gameObjects.append(self.focus) 
            stagedatafile.close()
        except Exception as e: 
            print(e) 

    def wipe(self): 
        self.display.fill((0,0,0,255)) 
    
    def draw(self): 
        if not(self.show): 
            for gameObject in self.gameObjects: 
                self.display.blit(gameObject.getSprite(), gameObject.position) 
        else: 
            for gameObject in self.gameObjects: 
                pygame.draw.rect(self.display,(255,0,0,255),gameObject.getSprite().get_rect(topleft=gameObject.position)) 

        if self.selected != None: 
            rect = self.selected.getSprite().get_rect(topleft=self.selected.position)
            highlight_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
            highlight_surface.fill((0, 0, 255, 128))  
            self.display.blit(highlight_surface, rect.topleft)

    def update(self): 
        self.clock.tick(self.fps) 
        pygame.display.flip() 
        self.events = pygame.event.get() 

class gameObject(): 
    def __init__(self, position, sprite_list, type, special_function_name, sprite_list_name): 
        self.type = type 
        self.special_function_name = special_function_name
        self.position = position 
        self.sprite_dict = {} 
        self.sprite_list = sprite_list 
        self.spriteIndex = 0 
        self.size = [100,100] 
        self.resizedSprites = sprite_list[0:] 
        self.resizeSprites() 
        self.sprite_dict[sprite_list_name] = sprite_list 
        self.sprite_list_name = sprite_list_name 
        pass

    def getSyntax(self):
        if self.type == "player": 
            sprite_sheet_syntax = "{'playeridleleft' : self.sprite_manager.sprite_groups['playeridleleft'],'playeridleright' : self.sprite_manager.sprite_groups['playeridleright'],'playerrunleft' : self.sprite_manager.sprite_groups['playerrunleft'],'playerrunright' : self.sprite_manager.sprite_groups['playerrunright'],}" 
        else: 
            sprite_sheet_syntax = "{" 
            for sprite_list_name, sprite_list in self.sprite_dict.items(): 
                sprite_sheet_syntax += f"'{sprite_list_name}' : self.sprite_manager.sprite_groups['{sprite_list_name}'],"
            sprite_sheet_syntax += "}" 
        return f"self.objects.{self.type}({list(self.size)}, {list(self.position)}, {sprite_sheet_syntax}, self.current_stage.game_object.specials.{self.special_function_name}, self.current_stage) "

    def resizeSprites(self): 
        for index, sprite in enumerate(self.sprite_list): 
            self.resizedSprites[index] = pygame.transform.scale(sprite,self.size) 

    def getSprite(self): 
        if self.spriteIndex < len(self.resizedSprites): 
            return self.resizedSprites[self.spriteIndex] 
        else: 
            self.spriteIndex = 0 
            return self.resizedSprites[self.spriteIndex] 

    def move(self, position): 
        self.position = position 
        pass

    def resize(self, size): 
        self.size = size 
        self.resizeSprites() 
        pass

editor_instance = editor() 
editor_instance.run() 