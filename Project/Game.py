class game(): 
    def __init__(self): 
        import pygame 
        import time 
        import random 
        import sys 
        import math 
        import datastructures.specials 
        import datastructures.objects 

        import os 
        self.file_path = __file__.removesuffix("Game.py") 

        self.pygame = pygame 
        self.time = time 
        self.random = random 
        self.sys = sys 
        self.math = math 
        self.specials = datastructures.specials 
        self.objects = datastructures.objects 
        self.sprite_manager = self.objects.sprite_manager(f"{self.file_path}sprites/",self) 

    def initiate(self): 
        self.pygame.init() 
        self.display = self.pygame.display.set_mode((0,0)) 
        self.screen_width, self.screen_height = self.display.get_size() 
        self.clock = self.pygame.time.Clock() 
        self.fps = 60 
        return self 

    def run(self): 
        self.stage_id = "0" 
        self.running = True 
        while self.running: 
            self.stage_data = open(f"{self.file_path}stagedata//{self.stage_id}.txt", "r").readlines() 
            self.current_stage = self.objects.stage(game_object=self) 
            for data in self.stage_data: 
                eval(data) 
            self.stage_id = self.current_stage.run() 


game_instance = game() 
game_instance.initiate() 
game_instance.run() 
