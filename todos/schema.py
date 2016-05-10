import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import graphene
from graphene import relay
from graphene.contrib.django import DjangoNode, DjangoConnection
from graphene.contrib.django.debug import DjangoDebugPlugin
from graphene.contrib.django.filter import DjangoFilterConnectionField

import models


schema = graphene.Schema(name='Todo Relay Schema', plugins=[DjangoDebugPlugin()])


class Connection(DjangoConnection):
    total_count = graphene.Int()

    def resolve_total_count(self, args, info):
        return len(self.get_connection_data())


class Todo(DjangoNode):

    class Meta:
        model = models.Todo
        exclude_fields = ('created', )
        filter_fields = ('title', )

    connection_type = Connection


class Query(graphene.ObjectType):
    all_todos = DjangoFilterConnectionField(Todo)
    todo_item = relay.NodeField(Todo)
    viewer = graphene.Field('self')

    def resolve_viewer(self, *args, **kwargs):
        return self


class CreateTodo(relay.ClientIDMutation):

    class Input:
        title = graphene.String(required=True)
        description = graphene.String(required=True)

    todo = graphene.Field(Todo)
    ok = graphene.Boolean()

    @classmethod
    def mutate_and_get_payload(cls, input, info):
        title = input.get('title')
        description = input.get('description')

        todo = Todo._meta.model(title=title, description=description)
        todo.save()

        return CreateTodo(todo=todo, ok=bool(todo.id))


class Mutation(graphene.ObjectType):
    create_todo = graphene.Field(CreateTodo)


schema.query = Query
schema.mutation = Mutation
