while True:
	for k in range(get_world_size()):
		for i in range(get_world_size()):
			if can_harvest:
				harvest()
			else:
				continue
			plant(Entities.Bush)
			move(East)
		move(North)

	while True:
		if num_items(Items.Fertilizer) < 200:
			trade_fertilizer(200)
		for i in range(get_world_size()):
			use_item(Items.Fertilizer)
			move(East)
		move(North)
		if get_entity_type() == Entities.Hedge:
			break

	# Initialize a list to track visited positions
	visited_positions = []

	# Function to get the current position as a tuple (x, y)
	def get_current_position():
		return (get_pos_x(), get_pos_y())

	# Function to get open directions
	def get_open_directions(walls):
		open_directions = []
		for i in range(0, len(walls), 2):
			if walls[i] == "no":
				open_directions.append(walls[i + 1])
		return open_directions

	# Function to move the drone to a new position
	def move_to_direction(direction):
		move(direction)

	# Function to explore the maze
	def explore_maze():
		# Get the current position
		current_position = get_current_position()
		
		# Mark the current position as visited
		visited_positions.append(current_position)
		
		# Check if the drone is above a treasure
		if get_entity_type() == Entities.Treasure:
			print("Treasure found! Harvesting...")
			harvest()
			return True  # Stop exploring after harvesting
		
		# Detect walls and get open directions
		walls = detect_walls()
		open_directions = get_open_directions(walls)
		
		# Try to move in open directions
		for direction in open_directions:
			# Move in the current direction
			move_to_direction(direction)
			
			# Get the new position after moving
			new_position = get_current_position()
			
			# If the new position hasn't been visited, explore it
			if new_position not in visited_positions:
				if explore_maze():  # Recursively explore
					return True  # Stop exploring if treasure is found
			
			# If the new position has been visited or leads to a dead end, backtrack
			move_back(direction)
		
		# If no open directions lead to the treasure, backtrack
		return False

	# Function to detect walls in all directions
	def detect_walls():
		walls = []
		for direction in [East, West, North, South]:
			wall = move(direction)
			if wall == True:
				walls.append("no")  # No wall
				walls.append(direction)
				move_back(direction)  # Move back to the original position
			elif wall == False:
				walls.append("yes")  # Wall
				walls.append(direction)
		return walls

	# Function to move back to the previous position
	def move_back(direction):
		if direction == East:
			opposite_direction = West
		elif direction == West:
			opposite_direction = East
		elif direction == North:
			opposite_direction = South
		elif direction == South:
			opposite_direction = North
		move(opposite_direction)

	# Start exploring the maze
	explore_maze()