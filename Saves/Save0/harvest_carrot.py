if get_ground_type() != Grounds.Soil:
	till_turf()
while True:
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