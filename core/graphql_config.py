from ariadne import (
    make_executable_schema,
    load_schema_from_path,
    MutationType,
    QueryType,
)
from ariadne_jwt import (
    resolve_verify,
    resolve_refresh,
    resolve_token_auth,
    jwt_schema,
    GenericScalar,
)
from .resolvers import backend_version
from customers.resolvers import query as customer_query, mutation as customer_mutation

core_type_defs = load_schema_from_path("core/schema.graphql")
customer_type_defs = load_schema_from_path("customers/schema.graphql")
jwt_type_defs = jwt_schema

core_query = QueryType()
core_query.set_field("backendVersion", backend_version)

core_mutation = MutationType()
core_mutation.set_field("verifyToken", resolve_verify)
core_mutation.set_field("refreshToken", resolve_refresh)
core_mutation.set_field("tokenAuth", resolve_token_auth)

schema = make_executable_schema(
    [core_type_defs, customer_type_defs, jwt_type_defs],
    [core_query, customer_query],
    [core_mutation, customer_mutation],
    GenericScalar,
)
