# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n_to=None, s_to=None, w_to=None, e_to=None, items=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.w_to = n_to
        self.e_to = s_to
        self.items = items