world_size = get_world_size()
x = get_pos_x()
y = get_pos_y()
current_time = get_time()
move_to_start(x, y)

while True:
	for i in range(world_size):
		moving(East, 1)
		harvest()
	moving(North, 1)