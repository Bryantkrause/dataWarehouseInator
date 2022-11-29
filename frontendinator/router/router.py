class ExpenseRouter:
    route_app_label = {'expensinator', 'auth'}

    def dbdb_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_label:
            return 'expensedb'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_label:
            return 'expensedb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_label or
            obj2._meta.app_label in self.route_app_label
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_label:
            return db == 'expensedb'
        return None

# project resetish
# need to establish new non default database
# according to this it seems you cannot have a default with django
# https://stackoverflow.com/questions/63090659/django-migrate-creates-the-wrong-tables-in-second-database
# dude finish this tutorial
# https://www.youtube.com/watch?v=g-FCzzzjBWo


# class CheckerRouter:

#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == 'expensinator':
#             return 'expensedb'
#         elif model._meta.app_label == 'laborinator':
#             return 'labordb'
#         return 'default'

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == 'expensinator':
#             return 'expensedb'
#         elif model._meta.app_label == 'laborinator':
#             return 'labordb'
#         return 'default'

#     def allow_relation(self, obj1, obj2, **hints):
#         if obj1._meta.app_label == 'expensinator' or obj2._meta.app_label == 'expensinator':
#             return True
#         elif 'expensinator' not in [obj1._meta.app_label, obj2._meta.app_label]:
#             return True
#         elif obj1._meta.app_label == 'laborinator' or obj2._meta.app_label == 'laborinator':
#             return True
#         elif 'laborinator' not in [obj1._meta.app_label, obj2._meta.app_label]:
#             return True
#         return False

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label == 'expensinator':
#             return db == 'expensedb'
#         elif app_label == 'laborinator':
#             return db == 'labordb'
#         return None
