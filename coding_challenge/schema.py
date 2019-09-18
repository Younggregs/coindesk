import graphene

import challenge.schema


class Query(challenge.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)