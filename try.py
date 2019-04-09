import sys

arg1 = sys.argv[1]
main_player = arg1 #'James Harden'

line_number = 0
for line in sys.stdin:
	line_number = line_number + 1
	if line_number == 1:
		continue
	line = line.strip()
	l = line[line.index('m'): ].split(',')
	result = l[0]
	closest_def_dist = l[1]
	player_name = l[-1]
	player_name = player_name.strip().title()
	l2 = line.split(',')
	shot_dist = l2[2]
	if shot_dist == '':
		shot_dist = 0.0
	shot_clock = l2[3]
	if shot_clock == '':
		shot_clock = 0.0
	if player_name == main_player:
		key = str(shot_dist) + ',' + str(closest_def_dist)
		value = str(shot_clock) + ',' + str(result)
		print '%s\t%s' % (key, value)

for line in sys.stdin:
	temp_a, temp_b = line.split('\t')
	result, closest_def_dist = temp_a.split(',')
	shot_dist, shot_clock = temp_b.split(',')
	shot_dist = float(shot_dist)
	closest_def_dist = float(closest_def_dist)
	shot_clock = float(shot_clock)
	result = result.strip()
	out = (shot_dist, closest_def_dist, shot_clock, result)
	print('%s' % (out, ))