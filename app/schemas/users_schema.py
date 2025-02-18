from marshmallow import Schema, fields, validate
from datetime import datetime

class UsersSchema(Schema):
    first_name= fields.String(required=True)
    last_name= fields.String(required=False)
    user_name = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
    isActive = fields.Boolean(required=False, default=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    
users_schema = UsersSchema()
