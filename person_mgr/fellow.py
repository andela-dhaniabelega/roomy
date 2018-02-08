from person_mgr.person import Person

from room_mgr.living_space import LivingSpace


class Fellow(Person):
  def __init__(self, name, staff_no, wants_accomodation=True):
    super().__init__(name, staff_no)
    self.wants_accomodation = wants_accomodation
    self._living_space = None

  def __repr__(self):
    return 'Person(name={0}, staff_no={1}, wants_accomodation={2})'.format(
      self.name, self.staff_no, self.wants_accomodation)

  def __str__(self):
    return '{0} : {1} : {2} : {3}'.format(
      self.name, self.staff_no, self._office, self._living_space)

  def update_living_space(self, living_space):
    """Updates person's living space
    :param office: a LivingSpace instance
    :return None:
    """
    if self.wants_accomodation:
      if isinstance(living_space, LivingSpace):
        self._living_space = living_space
      else:
        raise TypeError('Expected LivingSpace Type, got {0}'.format(
          type(living_space)))
    else:
      raise LivingSpaceRejectedException


class LivingSpaceRejectedException(Exception):
  """Raise this exception when the fellow has indicated he doesn't want
  a living space
  """
