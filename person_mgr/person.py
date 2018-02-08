class Person:
  def __init__(self, name, staff_no):
    self.name = name
    self.staff_no = staff_no
    self._office = None

  def __repr__(self):
    return 'Person(name={0}, staff_no={1})'.format(self.name, self.staff_no)

  def __str__(self):
    return '{0} : {1} : {2}'.format(self.name, self.staff_no, self._office)

  def update_office(self, office):
    """Updates person's office
    :param office: an Office instance
    :return None:
    """
    if isinstance(office, Office):
      self._office = office
    else:
      raise TypeError('Expected Office Type, got {0}'.format(type(office)))
