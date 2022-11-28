class CheckerRouter:

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'expense':
            return 'expense'
        elif model._meta.app_label == 'labor':
            return 'labor'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'expense':
            return 'expense'
        elif model._meta.app_label == 'labor':
            return 'labor'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'expense' or obj2._meta.app_label == 'expense':
            return True
        elif 'expense' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        elif obj1._meta.app_label == 'labor' or obj2._meta.app_label == 'labor':
            return True
        elif 'labor' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'expense':
            return db == 'expense'
        elif app_label == 'labor':
            return db == 'labor'
        return None
