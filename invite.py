class Invite:

    _all = []

    def __init__(self, dinner_party, guest, rsvp_status = None):
        self._guest = guest
        self._dinner_party = dinner_party
        self._rsvp_status = rsvp_status
        Invite._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @property
    def guest(self):
        return self._guest
    @guest.setter
    def guest(self, guest):
        self._guest = guest

    @property
    def dinner_party(self):
        return self._dinner_party
    @dinner_party.setter
    def dinner_party(self, dinner_party):
        self._dinner_party = dinner_party

    @property
    def rsvp_status(self):
        return self._rsvp_status
    @rsvp_status.setter
    def rsvp_status(self, rsvp_status):
        self._rsvp_status = rsvp_status

    def accepted(self):
        return Guest._rsvp_status
