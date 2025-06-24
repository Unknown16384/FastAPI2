from fastapi import APIRouter
from fastapi_cache.decorator import cache
from session import connect
from database import Sellers

sellers = APIRouter()
@sellers.get('')
@cache(expire=30)
def show():
    return connect.session.query(Sellers).all()
@sellers.get('/{sell_id}')
@cache(expire=30)
def show(sell_id):
    return connect.session.query(Sellers).get(sell_id)
@sellers.put('/{sell_id}/update')
def update(sell_id, name):
    seller = connect.session.query(Sellers).get(sell_id)
    if seller:
        seller.Name = name
        connect.session.commit()
    return seller
