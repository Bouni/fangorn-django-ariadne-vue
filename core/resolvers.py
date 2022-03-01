from ariadne import QueryType

query = QueryType()


@query.field("backendVersion")
def backend_version(*_):
    return "0.0.1"
