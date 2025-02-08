start_time = get_time()
harvest_count = 0
x = get_pos_x()
y = get_pos_y()
move_to_start(x, y)
if get_ground_type() != Grounds.Soil:
	till_turf()
while True:
	if num_items(Items.Pumpkin_Seed) < 2000:
		trade_pumpkin(2000)
	else:
		for k in range(get_world_size()):
			for i in range(get_world_size()):
				plant(Entities.Pumpkin)
				move(East)
			move(North)
		harvest_count += 1
		
		if harvest_count % 5 == 0:
			harvest()