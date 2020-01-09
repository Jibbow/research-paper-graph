from flask_restplus import Namespace, fields

class ReferenceDto:
    api = Namespace('reference', description='Manage references')
    reference = api.model('reference', {
        'from_paper': fields.String(required=True, description='referencing paper'),
        'to_paper': fields.String(required=True, description='referenced paper'),
    })