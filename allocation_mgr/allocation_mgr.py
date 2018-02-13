import logging
import random

import config
import person_mgr
import room_mgr
from file_io_handler import read_file
from room_mgr.office import Office
from room_mgr.living_space import LivingSpace

logger = logging.getLogger(__name__)


class AllocationManager:
	def __init__(self):
		self.rooms = self.get_all_rooms()

	def get_all_rooms(self):
		"""Return all rooms in db as a list"""
		return read_file(config.ROOM_FILE_NAME)

	def allocate(self, person):
		"""
		Allocates a random office and living space (depending on interest)
		to the supplied person
		:param person: a Person object (Fellow or Staff) 
		"""
		self.allocate_office(person)
		self.allocate_living_space(person)

	def allocate_office(self, person):
		"""
		"""
		office = self.get_random_office()
		if not office:
			logger.warning('There was no available office to assign to %s', person.name)
		else:
			office.add_person(person)
			person.update_office(office)

	def allocate_living_space(self, person):
		"""
		"""
		if hasattr(person, 'wants_accomodation') and person.wants_accomodation:
			living_space = self.get_random_living_space()

			if not living_space:
				logger.warning('There was no available living_space to assign to %s', person.name)
			else:
				living_space.add_person(person)
				person.update_living_space(living_space)

	def get_random_office(self):
		offices = [room for room in self.rooms if isinstance(room, Office)]
		office = None
		set_of_offices = {office.name for office in offices}
		checked_offices = {}
		# import ipdb; ipdb.set_trace()
		while office is None and checked_offices != set_of_offices:
			office = random.choice(offices)
			if office.is_full():
				office = None

		return office

	def get_random_living_space(self):
		living_spaces = [room for room in self.rooms if isinstance(room, LivingSpace)]
		living_space = None
		set_of_living_spaces = {living_space.name for living_space in living_spaces}
		checked_living_spaces = {}
		import ipdb; ipdb.set_trace()
		while living_space is None and checked_living_spaces != set_of_living_spaces:
			living_space = random.choice(living_spaces)
			if living_space.is_full():
				living_space = None

		return living_space
