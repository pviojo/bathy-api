from main import db
from .models import Resource


class ResourceService:

    @staticmethod
    def set_status(id, status):
        resource = ResourceService.get(id)
        if not resource:
            return None
        resource.status = status
        resource.save()
        return resource

    @staticmethod
    def get(id):
        resource = Resource.query.filter_by(id=id).first()
        return resource

    @staticmethod
    def all():
        resource = Resource.query.order_by(Resource.label).all()
        return resource
