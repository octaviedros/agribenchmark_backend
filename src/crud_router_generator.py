import uuid
from typing import List, Type

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlmodel import Session as SQLSession
from sqlmodel import SQLModel, select

from src.models import GeneralFarm


def get_session():
    from src.database import engine  # Adjust import as necessary
    with SQLSession(engine) as session:
        yield session

def create_crud_router(model: Type[SQLModel], session: Session = Depends(get_session)):
    router = APIRouter()

    @router.post("/", response_model=model)
    def create_item(item: model, session: Session = Depends(get_session)):
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

    @router.get("/{item_id}", response_model=model)
    def read_item(item_id: str, session: Session = Depends(get_session)):
        item = session.exec(select(model).where(model.id == item_id)).first()
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item
    
    @router.head("/{item_id}")
    def head_item(item_id: str, session: Session = Depends(get_session)):
        item = session.exec(select(model).where(model.id == item_id)).first()
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return {"ok": True}
    
    @router.get("/by_general_id/{general_id}", response_model=List[model])
    def read_items_by_general_id(general_id: str, session: Session = Depends(get_session)):        
        items = session.exec(select(model).where(model.general_id == general_id)).all()
        farm_data = session.exec(select(GeneralFarm).where(GeneralFarm.general_id == general_id)).first()
        # check if general_id is a scenario other than Baseline
        if farm_data.scenario_name != "Baseline" and items == []:
            # get the Baselines general_id
            baseline_general_id = session.exec(select(GeneralFarm).where((GeneralFarm.scenario_name == "Baseline") & (GeneralFarm.farm_id == farm_data.farm_id))).first().general_id
            # get the Baseline items
            baseline_items = session.exec(select(model).where(model.general_id == baseline_general_id)).all()
            # update the general_id column of all entries in the baseline_items list, and also create new uuid4s for the id columns
            for item in baseline_items:
                item.general_id = general_id
                item.id = str(uuid.uuid4())
            return baseline_items
        if not items:
            raise HTTPException(status_code=404, detail="No items found")
        return items

    @router.get("/", response_model=List[model])
    def read_items(session: Session = Depends(get_session)):
        items = session.exec(select(model)).all()
        return items

    @router.put("/{item_id}", response_model=model)
    def update_item(item_id: str, item: model, session: Session = Depends(get_session)):
        db_item = session.exec(select(model).where(model.id == item_id)).first()
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        update_data = item.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_item, key, value)
        session.add(db_item)
        session.commit()
        session.refresh(db_item)
        return db_item

    @router.delete("/{item_id}")
    def delete_item(item_id: str, session: Session = Depends(get_session)):
        item = session.exec(select(model).where(model.id == item_id)).first()
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        session.delete(item)
        session.commit()
        return {"ok": True}

    return router
