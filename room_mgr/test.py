import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest

from person_mgr.fellow import Fellow
from room_mgr.room import RoomFullException, PersonNotInRoomException
from room_mgr.office import Office
from room_mgr.living_space import LivingSpace


class TestRooms(unittest.TestCase):
  def setUp(self):
    self.office = Office('Aso', '100', 'FL1')
    self.living_space = LivingSpace('Banku', '100', 'FL1')

  def test_add_person(self):
    self.first_fellow = Fellow('Dhani', 'AF26121') 
    self.second_fellow = Fellow('Amaka', 'AF26122') 
    self.third_fellow = Fellow('James', 'AF26123') 
    self.fourth_fellow = Fellow('John', 'AF26124') 
    self.fifth_fellow = Fellow('Obinna', 'AF26125') 
    self.sixth_fellow = Fellow('Terso', 'AF26126')
    self.extra_fellow = Fellow('Mazi', 'AF26127')
    persons = [self.first_fellow, self.second_fellow, self.third_fellow, 
    self.fourth_fellow, self.fifth_fellow, self.sixth_fellow]
    for fellow in persons:
      self.living_space.add_person(fellow)
    with self.assertRaises(RoomFullException):
      self.living_space.add_person(self.extra_fellow)

  def test_remove_person(self):
    self.extra_fellow = Fellow('Mazi', 'AF26127') 
    self.assertRaises(PersonNotInRoomException, self.living_space.remove_person, self.extra_fellow)

  def tearDown(self):
    pass


if __name__ == '__main__':
  unittest.main(verbosity=2)