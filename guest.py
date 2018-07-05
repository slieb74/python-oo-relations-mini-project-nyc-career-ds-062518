from invite import Invite
from review import Review

class Guest:

    _all = []

    def __init__(self, guest):
        self._guest = guest
        Guest._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @property
    def guest(self):
        return self._guest
    @guest.setter
    def guest(self, guest):
        self._guest = guest

    @classmethod
    def most_popular(cls):
        guest_list = [invite._guest for invite in Invite._all]
        guest_dict = dict.fromkeys(set(guest_list), 0)
        for guest in guest_list:
            guest_dict[guest]+=1
        return sorted(guest_dict, key = guest_dict.get, reverse = True)[:1][0]

    @classmethod
    def toughest_critic(cls):
        guest_dict = {review._guest:[] for review in Review._all}
        for review in Review._all:
            guest_dict[review._guest].append(review._rating)
        for guest, list in guest_dict.items():
            list = round((sum(list)/len(list)),2)
            guest_dict[guest] = list
        return sorted(guest_dict, key = guest_dict.get, reverse = False)[:1][0]

    @classmethod
    def most_active_critic(cls):
        guest_dict = {review._guest:0 for review in Review._all}
        for review in Review._all:
            guest_dict[review._guest] +=1
        return sorted(guest_dict, key = guest_dict.get, reverse = True)[:1][0]

    def invites(self):
        return [invite for invite in Invite._all if self == invite._guest]

    def reviews(self):
        return [review for review in Review._all if self == review._guest]

    def number_of_invites(self):
        return len(self.invites())

    def rsvp(self, invite, rsvp_status):
        if self == invite._guest:
            invite._guest._rsvp_status = rsvp_status
        return rsvp_status

    def review_recipe(self, recipe, rating, comment):
        new_review = Review(self, recipe, rating, comment)
        return [review for review in Review._all if recipe == review._recipe]

    def favorite_recipe(self):
        fav_recipe_dict = {review._recipe:0 for review in self.reviews()}
        for review in self.reviews():
            if review._rating > fav_recipe_dict[review._recipe]:
                fav_recipe_dict[review._recipe] = review._rating
        return sorted(fav_recipe_dict, key = fav_recipe_dict.get, reverse = True)[:1][0]
