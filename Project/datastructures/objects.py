''' 
The stage represents the most fundamental functional unit of the game. Eahc stage is an environment where the physics and game events take place. 
It consists of 3 types of objects: 
    1. Dynamic Objects - These are Obejcts are collideable and can move. 
    2. Static Objects - These are objects that are collideable, but cannot move 
    3. Illusory Obejcts - These objects are the same as static objects except that they are non-collideable, making them useful as event triggers 
                            or background image holders/cutscene players 
    3.5. Player Objects - These are a special instance of dynamic objects that respond to player inputs 
'''
class stage(): 
    def __init__(self,game_object): 
        self.exit_id = "" 
        self.game_object = game_object 
        self.dynamic = [] 
        self.static = [] 
        self.illusory = [] 
        self.object_lists = [self.static,self.dynamic,self.illusory] 
        self.newtonian = [] 
        self.dampable = [] 
        self.players = [] 
        self.projectiles = [] 
        self.objects = [] 
        self.gravity = 9 
        self.friction = -5 
        self.horizontal_multiplier = 2 
        self.vertical_multiplier = 2 
        self.up = [1,0,0,0] 
        self.down = [0,0,1,0] 
        self.right = [0,0,0,1] 
        self.left = [0,1,0,0] 

    def get_inputs(self): 
        return [self.game_object.pygame.event.get(),self.game_object.pygame.key.get_pressed()] 
        
    def process_special_functions(self,objectswithspecialfunctionstoprocess): 
        for object in objectswithspecialfunctionstoprocess: 
            object.special_function(object) 

    def game_close_check(self): 
        for event in self.inputs[0]: 
            if event.type == self.game_object.pygame.QUIT: 
                self.game_exit()  
            if event.type == self.game_object.pygame.KEYDOWN: 
                if event.key == self.game_object.pygame.K_ESCAPE:
                    self.game_exit()  

    def apply_gravity(self,listofobjectstoapplygravityto): 
        for object in listofobjectstoapplygravityto: 
            if object.on_ground == False: 
                object.movements[2] += self.gravity 
            elif object.last_on_ground_state == False: 
                object.movements[0] = 0 
                object.movements[2] = 0 
            else: 
                object.movements[2] = 0 

    def draw_and_tick(self,listofobjectstodrawtothescreen): 
        self.game_object.display.fill((0,0,0,255)) 
        for object in listofobjectstodrawtothescreen: 
            self.game_object.display.blit(object.current_sprite,object.position) 
            # self.game_object.pygame.draw.rect(self.game_object.display,(255,0,0),object.collision_rect) 
        self.game_object.pygame.display.update() 
        self.game_object.clock.tick(self.game_object.fps) 

    def move_objects(self,listofobjectstomove): 
        for object in listofobjectstomove:  
            object.move(object.movements) 

    def apply_friction(self,listofobjectstodampthevelocitiesof): 
        for object in listofobjectstodampthevelocitiesof: 
            for i in range(0,4): 
                if object.movements[i] != 0: 
                    object.movements[i] += self.friction 

    def on_ground_checks(self,listofobjectstocheck): 
        for object in listofobjectstocheck: 
            object.last_on_ground_state = object.on_ground  
            object.move_down() 
            collision_Object = object.check_collisions() 
            if collision_Object and collision_Object.type in ["static", "dynamic"]: 
                object.on_ground = True 
            else: 
                object.on_ground = False 
            object.move_up() 

    def game_exit(self): 
        self.game_object.pygame.quit() 
        self.game_object.sys.exit() 

    def enable_camera(self,focus): 
        offsetx = - focus.position[0] + self.game_object.screen_width/2 
        offsety = - focus.position[1] + self.game_object.screen_height/2 
        for object in self.objects: 
            object.position = [offsetx+object.position[0],offsety+object.position[1]] 
            object.update_collision_rect() 

    def game_loop(self): 
        while not(self.exit_id): 
            self.inputs = self.get_inputs() 
            self.game_close_check() 
            self.on_ground_checks(self.newtonian) 
            self.apply_gravity(self.newtonian) 
            self.apply_friction(self.dampable) 
            self.process_special_functions(self.objects) 
            self.move_objects(self.dynamic) 
            self.enable_camera(self.players[0]) 
            self.draw_and_tick(self.objects) 
        return self.exit_id 

    def run(self): 
        exit_id = self.game_loop() 
        return exit_id 

# object that handles sprites and is passed as a parameter into stage construction from where images are accessed. 
# structure: 
# each sprite group has a group name (the name of the subforlder they are stored under within 'sprites') 
# each sprite group name is the key to a value containing a list of sprite images 
# these sprites are not automatically cycled through 
class sprite_manager(): 
    def __init__(self,path,game_object) -> None: 
        import os 
        self.path = path 
        self.game_object = game_object 
        self.sprite_groups = {} 
        for sprite_group_name in os.listdir(path=path): 
            sprites_list = [] 
            for sprite_instance in os.listdir(path=path+f"{sprite_group_name}/") : 
                sprite = self.game_object.pygame.image.load(path+f"{sprite_group_name}/"+sprite_instance) 
                sprites_list.append(sprite) 
            self.sprite_groups[sprite_group_name] = sprites_list 

        pass 

class object_template(): 
    def __init__(self,size,position,type,sprite_list,special_function,stage_object): 
        self.stage_object = stage_object 
        self.stage_object.object_lists[type].append(self) 
        self.stage_object.objects.append(self) 
        self.position = position 
        self.size = size 
        self.sprite_list = sprite_list 
        self.spriteIndex = 0 
        self.current_sprite = self.stage_object.game_object.pygame.transform.scale(self.sprite_list[self.spriteIndex],self.size) 
        self.update_collision_rect() 
        self.special_function = special_function 
        self.last_on_ground_state = False 

    def update_collision_rect(self): 
        self.collision_rect = self.current_sprite.get_rect(topleft = self.position) 
        self.collision_rect.w = self.current_sprite.get_width() 
        self.collision_rect.h = self.current_sprite.get_height() 

    def check_collisions(self): 
        for object in self.stage_object.objects: 
            if ((self.collision_rect.colliderect(object.collision_rect)) and (self != object)): 
                return object 
        return False 
    
    def move(self,movements): 
        
        for i in range(0,self.stage_object.game_object.math.ceil(self.stage_object.vertical_multiplier*movements[0]/10)): 
            self.move_up() 
            collision = self.check_collisions() 
            while (collision and collision.type in ["static", "dynamic"]): 
                if collision.type == "static": 
                    self.move(self.stage_object.down) 
                    self.movements[0] = 0 
                    self.movements[2] = 0 
                elif collision.type == "dynamic": 
                    collision.move(self.stage_object.up) 
                collision = self.check_collisions() 

                    
        for i in range(0,self.stage_object.game_object.math.ceil(self.stage_object.horizontal_multiplier*movements[1]/10)): 
            self.move_left() 
            collision = self.check_collisions() 
            while (collision and collision.type in ["static", "dynamic"]): 
                if collision.type == "static": 
                    self.move(self.stage_object.right) 
                elif collision.type == "dynamic": 
                    collision.move(self.stage_object.left) 
                collision = self.check_collisions() 

        for i in range(0,self.stage_object.game_object.math.ceil(movements[2]/10)): 
            self.move_down() 
            collision = self.check_collisions() 
            while (collision and collision.type in ["static", "dynamic"]): 
                if collision.type == "static": 
                    self.move(self.stage_object.up) 
                elif collision.type == "dynamic": 
                    collision.move(self.stage_object.down) 
                collision = self.check_collisions() 

        for i in range(0,self.stage_object.game_object.math.ceil(self.stage_object.horizontal_multiplier*movements[3]/10)): 
            self.move_right() 
            collision = self.check_collisions() 
            while (collision and collision.type in ["static", "dynamic"]): 
                if collision.type == "static": 
                    self.move(self.stage_object.left) 
                elif collision.type == "dynamic": 
                    collision.move(self.stage_object.right) 
                collision = self.check_collisions() 

    def move_up(self): 
        self.position[1] -= 1 
        self.update_collision_rect() 

    def move_left(self): 
        self.position[0] -= 1 
        self.update_collision_rect() 

    def move_down(self): 
        self.position[1] += 1 
        self.update_collision_rect() 

    def move_right(self): 
        self.position[0] += 1 
        self.update_collision_rect() 

    def update_sprite(self): 
        self.current_sprite = self.stage_object.game_object.pygame.transform.scale(+1+self.sprite_list[self.sprite_list.index(self.current_sprite)]) 

class static_object(object_template): 
    def __init__(self, size, position, sprite_list, special_function, stage_object): 
        super().__init__(size, position, 0, sprite_list, stage_object.game_object.specials.static, stage_object) 
        self.type = "static" 
        self.player = False 

class dynamic_object(object_template): 
    def __init__(self, size, position, sprite_list, special_function, stage_object): 
        super().__init__(size, position, 1, sprite_list, special_function, stage_object) 
        self.type = "dynamic" 
        self.on_ground = False 
        self.player = False 
        self.movements = [0,0,0,0] 
        self.direction = 0 
        self.stage_object.newtonian.append(self) 
        self.stage_object.dampable.append(self) 

class player(dynamic_object): 
    def __init__(self, size, position, sprite_list, special_function, stage_object): 
        super().__init__(size,position,sprite_list,stage_object.game_object.specials.process_player_movements,stage_object) 
        self.double_jump = False 
        self.dash = False 
        self.jump_height = 125 
        self.max_velocity = [125,50,500,50] # W, A, S, D 
        self.movements = [0,0,0,0] 
        self.max_jump_height = 1000 
        self.direction = 0 
        self.stage_object.players.append(self) 
        self.movement_velocity = 50 
        self.player = True 
        self.stage_object.newtonian.append(self) 
        self.stage_object.dampable.append(self) 


class illusory_object(object_template): 
    def __init__(self, size, position, sprite_list, special_function, stage_object): 
        super().__init__(size, position, 2, sprite_list, special_function, stage_object) 
        self.type = "illusory" 
        self.on_ground = True 
        self.player = False 
        self.movements = [0,0,0,0] 
        self.direction = 0 