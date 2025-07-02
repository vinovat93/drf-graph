from graphene_django import DjangoObjectType
from project.settings import PLANS, PRO, HOBBY
import graphene

from .models import User, DeployedApp


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"


class DeployedAppType(DjangoObjectType):
    class Meta:
        model = DeployedApp
        fields = "__all__"


class UpgradeApp(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, user_id):
        user = User.objects.get(pk=user_id)
        user.plan = HOBBY
        user.save()

        return UpdateUserPlanApp(user=user)


class DowngradeApp(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, user_id):
        user = User.objects.get(pk=user_id)
        user.plan = PRO
        user.save()

        return UpdateUserPlanApp(user=user)


class UpdateUserPlanApp(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)
        plan_id = graphene.ID(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, user_id, plan_id):
        user = User.objects.get(pk=user_id)
        user.plan = plan_id
        user.save()

        return UpdateUserPlanApp(user=user)


class CreateApp(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        user_id = graphene.ID(required=True)

    app = graphene.Field(DeployedAppType)

    def mutate(self, info, name, user_id):
        user = User.objects.get(pk=user_id)
        app = DeployedApp(name=name, user=user)
        app.save()
        return CreateApp(app=app)


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    apps = graphene.List(DeployedAppType)
    user = graphene.Field(UserType, id=graphene.ID(required=True))

    def resolve_user(self, info, id):
        return User.objects.get(pk=id)

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_apps(self, info):
        return DeployedApp.objects.all()


class Mutation(graphene.ObjectType):
    create_app = CreateApp.Field()
    update_user_plan = UpdateUserPlanApp.Field()
    upgrade_plan = UpgradeApp.Field()
    downgrade_plan = DowngradeApp.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
