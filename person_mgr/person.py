class Person:
  def __init__(self, name, staff_no):
    self.name = name
    self.staff_no = staff_no
    self._office = None

  def update_office(self, office):
    """Updates person's office
    :param office: an Office instance
    :return None:
    """
    if isinstance(office, Office):
      self._office = office
    else:
      raise TypeError('Expected Office Type, got {0}'.format(type(office)))
