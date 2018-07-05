from review import Review
class Recipe:

    _all = []

    def __init__(self, recipe):
        self._recipe = recipe
        Recipe._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @property
    def recipe(self):
        return self._recipe
    @recipe.setter
    def recipe(self, recipe):
        self._recipe = recipe

    @classmethod
    def top_three(cls):
        recipe_rating_dict = {review._recipe:[] for review in Review._all}
        for review in Review._all:
            recipe_rating_dict[review._recipe].append(review._rating)
        for recipe,list in recipe_rating_dict.items():
            list = round((sum(list)/len(list)),2)
            recipe_rating_dict[recipe] = list
        return sorted(recipe_rating_dict, key = recipe_rating_dict.get, reverse = True)[:3]

    @classmethod
    def bottom_three(cls):
        recipe_rating_dict = {review._recipe:[] for review in Review._all}
        for review in Review._all:
            recipe_rating_dict[review._recipe].append(review._rating)
        for recipe,list in recipe_rating_dict.items():
            list = round((sum(list)/len(list)),2)
            recipe_rating_dict[recipe] = list
        return sorted(recipe_rating_dict, key = recipe_rating_dict.get, reverse = False)[:3]

    def reviews(self):
        return [review for review in Review._all if self ==  review._recipe]
    def top_five_reviews(self):
        review_dict = {review: review._rating for review in  self.reviews()}
        return sorted(review_dict, key = review_dict.get, reverse = True)[:5]
