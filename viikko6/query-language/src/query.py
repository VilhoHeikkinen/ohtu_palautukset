from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class Query:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()
    
    def empty(self):
        return len(self.elements) == 0

class AllQuery:
    def build(self):
        return All()

class PlaysInQuery:
    def __init__(self, team):
        self._team = team

    def build(self):
        return PlaysIn(self._team)
    
class HasAtLeastQuery:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def build(self):
        return HasAtLeast(self._value, self._attr)
    
class AndQuery:
    def __init__(self, *queries):
        self._queries = queries

    def build(self):
        return And(self._queries)