from flask_login import UserMixin


class User(UserMixin):
  def __init__(self, name, password) -> None:
      self.name = name
      self.password = password

  def get_id(self):
    return self.name