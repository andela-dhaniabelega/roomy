from room_mgr.living_space import LivingSpace
from room_mgr.office import Office

def create_room(arguments):
	options = {'room_type', 'room_name'}
	args = {}
	for each in options:
		args[each] = arguments['<{0}>'.format(each)]

	rooms = []
	for name in args['room_name']:
		if args['room_type'] == 'office':
			rooms.append(Office(name=name))
		else:
			rooms.append(LivingSpace(name=name))

	return rooms
