from pydantic import BaseModel

class UpdateSuperheroReq(BaseModel):
    update_params: dict