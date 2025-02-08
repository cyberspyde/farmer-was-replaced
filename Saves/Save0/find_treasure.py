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

    visited = {}

    def opposite_direction(direction):
        if direction == East: return West
        elif direction == West: return East
        elif direction == North: return South
        elif direction == South: return North

    def explore_maze():
        stack = []
        start_pos = (get_pos_x(), get_pos_y())
        visited[start_pos] = {
            'walls': detect_walls(),
            'explored': []
        }
        stack.append((start_pos, None))  # (position, backtrack_direction)
        
        while stack:
            current_pos, backtrack_dir = stack[-1]
            
            # Check for treasure at current position
            if get_entity_type() == Entities.Treasure:
                harvest()
                return True
            
            # Detect walls if first visit
            if current_pos not in visited:
                visited[current_pos] = {
                    'walls': detect_walls(),
                    'explored': []
                }
            
            # Get unexplored directions
            walls = visited[current_pos]['walls']
            open_dirs = get_open_directions(walls)
            unexplored = [d for d in open_dirs if d not in visited[current_pos]['explored']]
            
            if unexplored:
                # Explore first available direction
                direction = unexplored[0]
                visited[current_pos]['explored'].append(direction)
                
                # Move to new position
                move(direction)
                new_pos = (get_pos_x(), get_pos_y())
                
                # Add new position to stack with backtrack direction
                stack.append((new_pos, opposite_direction(direction)))
            else:
                # Backtrack to previous position
                stack.pop()
                if backtrack_dir:
                    move(backtrack_dir)

    # Modified wall detection to return direction list (same as original)
    def detect_walls():
        walls = []
        for direction in [East, West, North, South]:
            if move(direction):
                walls.append("no")
                walls.append(direction)
                move(opposite_direction(direction))
            else:
                walls.append("yes")
                walls.append(direction)
        return walls

# Keep your existing get_open_directions function

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