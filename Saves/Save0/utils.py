def clear_world():
	x = get_pos_x()
	y = get_pos_y()
	move_to_start(x, y)

	for k in range(get_world_size()):
		for i in range(get_world_size()):
			moving(East, 1)
			harvest()
		moving(North, 1)

def moving(direction, n):
	for i in range(n):
		move(direction)
		
def move_to_start(x, y):
	if x != 0:
		moving(West, x)
	if y != 0:
		moving(South, y)
	
def till_soil():
	for k in range(get_world_size()):
		for i in range(get_world_size()):
			if get_ground_type() != Grounds.Turf:	
				till()
			move(East)
		move(North)
	
def till_turf():
	for k in range(get_world_size()):
		for i in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:	
				till()
			move(East)
		move(North)
		
def trade_carrot(n):
	while num_items(Items.Carrot_Seed) < n:
		trade(Items.Carrot_Seed)
		
def trade_sunflower(n):
	while num_items(Items.Sunflower_Seed) < n:
		if num_items(Items.Carrot) < n:
			harvest_carrot()
		trade(Items.Sunflower_Seed)

def trade_pumpkin(n):
	while num_items(Items.Pumpkin_Seed) < n:
		trade(Items.Pumpkin_Seed)
		
def trade_fertilizer(n):
	for k in range(n):
		trade(Items.Fertilizer)
		
def harvest_wood():
	world_size = get_world_size()
	x = get_pos_x()
	y = get_pos_y()
	current_time = get_time()
	move_to_start(x, y)
	
	while True:
		for k in range((world_size + 1) / 2):
			if can_harvest():
				harvest()
			for i in range((world_size + 1) / 2):
				if can_harvest():
					harvest()
				plant(Entities.Tree)
				moving(East, 2)	
				
			moving(North, 2)
			moving(West, 1)	
		
		moving(South, 1)
		if num_items(Items.Wood) > 2000:
			break
			
def harvest_carrot():	if get_ground_type() != Grounds.Soil:
		till_turf()
	for k in range(20):
		if num_items(Items.Wood) < 2000:
			harvest_wood()
		if num_items(Items.Carrot_Seed) < 2000:
			trade_carrot(2000)
		for k in range(get_world_size()):
			for i in range(get_world_size()):
				if can_harvest:
					harvest()
				else:
					continue
				plant(Entities.Carrots)
				move(East)
			move(North)
			
def harvest_hay():
	world_size = get_world_size()
	for k in range(2000):
		move(North)
		for i in range(world_size):
			harvest()
			move(East)
		
def harvest_pumpkin():
	x = get_pos_x()
	y = get_pos_y()
	move_to_start(x, y)
	crop_count = 0
	if get_ground_type() != Grounds.Soil:
		till_turf()
	
	while True:
		if num_items(Items.Carrot) < 2000:
			harvest_carrot()
		
		if num_items(Items.Pumpkin_Seed) < 2000:
			trade_pumpkin(2000)
		else:
			for k in range(get_world_size()):
				for i in range(get_world_size()):
					if get_entity_type() == Entities.Carrots:
						harvest()
					if get_entity_type() == Entities.Pumpkin and can_harvest():
						crop_count += 1
					plant(Entities.Pumpkin)
					move(East)
				move(North)
		if crop_count == get_world_size() * get_world_size():
			harvest()
		crop_count = 0