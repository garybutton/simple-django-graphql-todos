# Really simple todo api using Graphene
 
## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Queries

[/graphiql](http://localhost:8080/graphiql)

### Create todo

```
mutation MyMutation {
  createTodo(input:{clientMutationId:"a", title:"Test Todo", description:"Testing"}) {
    todo {
      id
      title
      description
    }
    ok
  }
}
```

### Get todos

```javascript
{
  todoList: allTodos {
    totalCount
    edges {
      node {
        title
        description
      }
    }
  }
}
```

## Sources

[Graphene](http://graphene-python.org/)