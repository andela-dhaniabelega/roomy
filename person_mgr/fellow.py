from person_mgr.person import Person

from room_mgr.living_space import LivingSpace


class Fellow(Person):
  def __init__(self, name, staff_no, have_living_space=True):
    super().__init__(name, staff_no)
    self.have_living_space = have_living_space
    self._living_space = None

  def update_living_space(self, living_space):
    """Updates person's living space
    :param office: a LivingSpace instance
    :return None:
    """
    if self.have_living_space:
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
