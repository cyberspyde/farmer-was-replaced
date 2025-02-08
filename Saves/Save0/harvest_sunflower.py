x = get_pos_x()
y = get_pos_y()
harvested = []
measures = []
move_to_start(x, y)
max_measure = 0
finishedHarvest = True
while True:
	for k in range(get_world_size()):
		for i in range(get_world_size()):
			if get_entity_type() != Entities.Sunflower and finishedHarvest == True:
				plant(Entities.Sunflower)
			if measure() != None and measure() not in measures and measure() != max_measure:
				measures.append(measure())
			move(East)
		move(North)
	
	max_measure = max(measures)
	for t in range(len(measures)):
		for k in range(get_world_size()):
			for i in range(get_world_size()):
				if measure() == max_measure:
					harvest()
				move(East)
			move(North)
		measures.remove(max_measure)
		if len(measures) != 0:
			max_measure = max(measures)
	measures = []
	max_measure = 0
		
	