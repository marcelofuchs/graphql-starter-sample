# app/schema.py
from graphene import ObjectType, String, Int, Schema


class Query(ObjectType):
    id = Int()
    hello = String()

    def resolve_id(self, info):
        return 1

    def resolve_hello(self, info):
        return "Hello"


class RootQuery(Query, ObjectType):
    pass


schema = Schema(query=RootQuery)
