import logging
from typing import Union

from data.database.dbhandler import DBHandler

from uuid import UUID

from fastapi import FastAPI, status, HTTPException
from fastapi.responses import RedirectResponse

from data.model import Parcel

logger = logging.getLogger(__name__)
app = FastAPI()
db_handler = DBHandler(db_name="dict", data_type=Parcel)


@app.get("/")
async def root():
    return RedirectResponse("/redoc")


@app.post("/parcel", status_code=status.HTTP_201_CREATED)
async def new_parcel(parcel: Parcel):
    logger.info(f"Creating parcel with {id = }")
    db_response: Union[Parcel, str] = db_handler.create(parcel)
    if type(db_response) is Parcel:
        return {"parcel": db_response}
    return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=db_response)


@app.get("/parcel", status_code=status.HTTP_200_OK)
async def get_parcel(target_id: UUID):
    logger.info(f"Getting parcel with id = {target_id}")
    db_response: Union[Parcel, str] = db_handler.read(target_id)
    if type(db_response) is Parcel:
        return {"parcel": db_response}
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=db_response)


@app.put("/parcel", status_code=status.HTTP_200_OK)
async def update_parcel(target_id: UUID, content: str):
    logger.info(f"Replacing the contents of parcel with id = {target_id}")
    db_response: Union[Parcel, str] = db_handler.update(target_id, content)
    if type(db_response) is Parcel:
        return {"parcel": db_response}
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=db_response)


@app.patch("/parcel", status_code=status.HTTP_200_OK)
async def update_parcel_patch(target_id: UUID, content: str):
    return update_parcel(target_id, content)


@app.delete("/parcel", status_code=status.HTTP_200_OK)
async def delete_parcel(target_id: UUID):
    logger.info(f"Deleting parcel with id = {target_id}")
    db_response = db_handler.delete(target_id)
    if type(db_response) is Parcel:
        return {"parcel": db_response}
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=db_response)
