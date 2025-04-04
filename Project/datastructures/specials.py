def process_player_movements(player_object): 
    inputs = player_object.stage_object.inputs 

    if player_object.on_ground: 
        player_object.double_jump = True 
    else: 
        player_object.movements[2] = min(player_object.movements[2],player_object.max_velocity[2])  
        player_object.direction = "2" 

    keypressed = inputs[1] 

    if (keypressed[player_object.stage_object.game_object.pygame.K_w] and player_object.on_ground): 
        player_object.movements[0] = min(player_object.movements[0] + player_object.jump_height, player_object.max_velocity[0])  
        player_object.direction = "0" 
    for event in player_object.stage_object.inputs[0]: 
        if event.type == player_object.stage_object.game_object.pygame.KEYDOWN and event.key == player_object.stage_object.game_object.pygame.K_w and player_object.double_jump and player_object.on_ground == False: 
            player_object.double_jump = False 
            player_object.movements[0] = min(player_object.movements[0] + player_object.jump_height, player_object.max_velocity[0])  
            player_object.movements[2] = 0 
            player_object.direction = "0" 
    if keypressed[player_object.stage_object.game_object.pygame.K_s]: 
        player_object.movements[2] = min(player_object.movements[2] + player_object.movement_velocity,player_object.max_velocity[2])  
        player_object.direction = "2" 
    if keypressed[player_object.stage_object.game_object.pygame.K_a]: 
        player_object.movements[1] = min(player_object.movements[1] + player_object.movement_velocity,player_object.max_velocity[1])  
        player_object.direction = "1" 
    if keypressed[player_object.stage_object.game_object.pygame.K_d]: 
        player_object.movements[3] = min(player_object.movements[3] + player_object.movement_velocity,player_object.max_velocity[3])  
        player_object.direction = "3" 

def static(game_object_instance): 
    pass # function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
# function_name
def function_name(self): 
	pass
