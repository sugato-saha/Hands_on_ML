from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
rooms_ix, bedrooms_ix, population_ix, households_ix = 3,4,5,6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room =  True) : # no *args or *kwargs
        self.add_bedrooms_per_room = add_bedrooms_per_room
    def fit(self, X, y = None) :
        return self # nothing to do in this case
    def transform(self, X):
        rooms_per_household = X[:,rooms_ix] / X[:,households_ix]
        population_per_household = X[:,population_ix] / X[:,households_ix]
        if (self.add_bedrooms_per_room == True):
            bedrooms_per_room = X[:,bedrooms_ix] / X[:,rooms_ix]
            return np.c_[X,rooms_per_household,population_per_household,bedrooms_per_room]
        else:
            return np.c_[X,rooms_per_household,population_per_household]