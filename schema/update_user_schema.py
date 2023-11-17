"""Схема для api reqres, update user"""

schema = {
    "type": "object",
    "properties": {"name": {"type": "string"}, "job": {"type": "string"}, "updatedAt": {"type": "string"}},
    "required": ["name", "job", "updatedAt"],
}
