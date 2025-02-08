world_size = get_world_size()
while True:
	move(North)
	for i in range(world_size):
		harvest()
		move(East)