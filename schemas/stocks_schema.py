from typing import Optional, List
from pydantic import BaseModel, EmailStr

# Request schemas
class StockResponse(BaseModel):
    ticker: str
    company_name: str
    price: float
    sector: Optional[str]
    confidence_level: int

class StockListResponse(BaseModel):
    user_id: str
    personality_type: Optional[str]
    stocks: List[StockResponse]
    count: int