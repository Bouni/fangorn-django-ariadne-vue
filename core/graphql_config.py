from ariadne import QueryType, make_executable_schema, load_schema_from_path, MutationType
from ariadne_jwt import resolve_verify, resolve_refresh, resolve_token_auth, jwt_schema, GenericScalar
from customers.resolvers import all_customers, get_customer, create_customer

type_defs = [
    load_schema_from_path("core/schema.graphql"),
    load_schema_from_path("customers/schema.graphql"),
]

type_defs += [jwt_schema]

query = QueryType()
query.set_field("customers", all_customers)
query.set_field("customer", get_customer)

mutation = MutationType()
mutation.set_field("createCustomer", create_customer)
mutation.set_field('verifyToken', resolve_verify)
mutation.set_field('refreshToken', resolve_refresh)
mutation.set_field('tokenAuth', resolve_token_auth)

schema = make_executable_schema(type_defs, query, mutation, GenericScalar)
