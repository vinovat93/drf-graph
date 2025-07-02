# drf-graph
django-restframework-graph


Minified Queries:

```query{users{id,username,firstName,lastName,plan}}```

```query{user(id:"1"){id,username,firstName,lastName}}```

```query{apps{name}}```

Minified Mutations:

```mutation{createApp(name:"Test Post from GraphQL",userId:1){app{id}}}```

```mutation{updateUserPlan(planId:2,userId:1){user{id,firstName}}}```

```mutation{downgradePlan(userId:1){user{id,firstName,plan}}}```

```mutation{upgradePlan(userId:1){user{id,firstName,plan}}}```