class Room:
  def __init__(self, name):
    self.name = name
    self._occupants = []

  def __str__(self):
    return '{0} : {1}: {2}'.format(self.name, self.capacity, len(self._occupants))

  def __repr__(self):
    return 'Room(name={0})'.format(self.name)

  def add_person(self, person):
    if len(self._occupants) < self.CAPACITY:
      self._occupants.append(person)
    else:
      raise RoomFullException

  def remove_person(self, person):
    try:
      self._occupants.remove(person)
    except ValueError:
      raise PersonNotInRoomException

  def get_num_of_occupants(self):
    return len(self._occupants)

  def get_names_of_occupants(self):
    return [name for person.name in self._occupants]

  def is_full(self):
    if len(self._occupants) == self.CAPACITY:
      return True
    return False


class RoomFullException(Exception):
  """Raise this exception when the room is full"""


class PersonNotInRoomException(Exception):
  """Raise this exception when trying to remove an occupant
  and the occupant is not in the room
  """
