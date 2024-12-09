from query import Query, AllQuery, PlaysInQuery, HasAtLeastQuery, AndQuery
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self):
        self.queries = []

    def query(self):
        return self.queries
    
    def plays_in(self, team):
        self.queries.append(PlaysIn(team))
        return self
    
    def has_at_least(self, value, attr):
        self.queries.append(HasAtLeast(value, attr))
        return self
    
    def has_fewer_than(self, value, attr):
        self.queries.append(HasFewerThan(value, attr))
        return self
    
    def build(self):
        return And(self.queries)