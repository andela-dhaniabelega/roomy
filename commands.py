import os
import pickle
import uuid

import config
from person_mgr.staff import Staff
from person_mgr.fellow import Fellow
from room_mgr.living_space import LivingSpace
from room_mgr.office import Office
from allocation_mgr.allocation_mgr import AllocationManager


def create_room(arguments):
	options = {'room_type', 'room_name'}
	args = get_args(arguments, options)

	rooms = []
	for name in args['room_name']:
		if args['room_type'] == 'office':
			rooms.append(Office(name=name))
		else:
			rooms.append(LivingSpace(name=name))

	save(rooms, config.ROOM_FILE_NAME)


def add_person(arguments):
	options = {'person_name', 'Fellow', 'Staff', 'y', 'n'}
	args = get_args(arguments, options)

	name = args['person_name']
	staff_no = str(uuid.uuid4())
	
	if args[config.STAFF]:
		person = Staff(name, staff_no)
	else:
		wants_accomodation = True if args['y'] else False
		person = Fellow(name, staff_no, wants_accomodation)

	AllocationManager().allocate(person)

	# TODO: Handle for cases where there are no available rooms
	
	# Add room to db
	save([person], config.PERSON_FILE_NAME)


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
