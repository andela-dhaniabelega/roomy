import os
import pickle

import config
from room_mgr.living_space import LivingSpace
from room_mgr.office import Office

def create_room(arguments):
	options = {'room_type', 'room_name'}
	args = get_args(arguments, options)

	rooms = []
	for name in args['room_name']:
		if args['room_type'] == 'office':
			rooms.append(Office(name=name))
		else:
			rooms.append(LivingSpace(name=name))

	save_room(rooms)


def save_room(new_rooms):
	"""Save rooms in pb file
	:params new_rooms: a list
	"""
	import ipdb; ipdb.set_trace()

	rooms = []
	if os.path.exists(config.ROOM_FILE_NAME):
		with open(config.ROOM_FILE_NAME, 'rb') as pickle_file:
			rooms = pickle.load(pickle_file)

	rooms.extend(new_rooms)

	with open(config.ROOM_FILE_NAME, 'a+b') as pickle_file:
		pickle.dump(rooms, pickle_file)


def add_person(arguments):
	options = {'person_name', 'FELLOW', 'STAFF', 'wants_accomodation'}
	print(arguments)
	args = get_args(arguments, options)
	print(args)


def get_args(docopt_args, target_fields):
	"""
	"""
	args = {}
	for each in docopt_args:
		if strip_punctuations(each) in target_fields:
			args[strip_punctuations(each)] = docopt_args[each]
	return args


def strip_punctuations(astr):
	"""
	"""
	return astr.strip('<>|[]')
