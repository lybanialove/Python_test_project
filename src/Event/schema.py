from pydantic import BaseModel
from datetime import datetime

class CreateEventSchema(BaseModel):
    name: str
    description: str
    uniq_code:str
    start_at: datetime