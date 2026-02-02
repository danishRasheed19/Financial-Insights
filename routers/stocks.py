from typing import List

from fastapi import APIRouter
from schemas.stocks_schema import StockResponse,StockListResponse
from data.stocks_data.stockBook import stocks
router = APIRouter(prefix="/stocks", tags=["stocks"])

@router.get("/expertStockList")
async def get_expert_stock_list():
    """Returns the list of stocks"""
    mapped_stocks: List[StockResponse] = []
    for stock in stocks:
        mapped_stocks.append(
            StockResponse(
                ticker=stock["ticker"],
                company_name=stock["name"],
                price=stock["price"],
                sector=stock["sector"],
                confidence_level= 90
            )
        )
    return StockListResponse(user_id="temp",personality_type="Saver",count=len(mapped_stocks), stocks=mapped_stocks)

