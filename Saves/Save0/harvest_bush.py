while True:
	for i in range(get_world_size()):
		if can_harvest:
			harvest()
		else:
			continue
		plant(Entities.Bush)
		move(East)
	move(North)
