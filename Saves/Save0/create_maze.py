while True:
	for i in range(get_world_size()):
		use_item(Items.Fertilizer)
		move(East)
	move(North)