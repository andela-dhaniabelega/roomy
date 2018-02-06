import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from fellow import Fellow
from fellow import LivingSpaceRejectedException
from room_mgr.office import Office
from room_mgr.living_space import LivingSpace


class TestRooms(unittest.TestCase):
  def setUp(self):
    self.office = Office('Aso', '100', 'FL1')
    self.living_space = LivingSpace('Banku', '100', 'FL1')

  def test_update_living_space(self):
    fellow = Fellow('Dhani', 'AF26121')
    self.assertRaises(TypeError, fellow.update_living_space, self.office)

    fellow = Fellow('Dhani', 'AF26121', have_living_space=False)
    self.assertRaises(LivingSpaceRejectedException, fellow.update_living_space,self.living_space)



  def test_update_office(self):
   pass

  def tearDown(self):
    pass


if __name__ == '__main__':
  unittest.main(verbosity=2)