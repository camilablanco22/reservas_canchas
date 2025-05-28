from rest_framework.permissions import DjangoModelPermissions


class StrictModelPermissions(DjangoModelPermissions):
    """
    Requiere que incluso para métodos GET el usuario tenga el permiso view_model.
    """
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'], #esta línea es la clave
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
