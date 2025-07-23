import uuid

class MCPMessage:
    def __init__(self, sender, receiver, type, trace_id=None, payload=None):
        self.sender = sender
        self.receiver = receiver
        self.type = type
        self.trace_id = trace_id or str(uuid.uuid4())
        self.payload = payload or {}
