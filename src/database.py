from sqlmodel import SQLModel, create_engine, Session
from config import username, password, db
import inspect, sys

DATABASE_URL = f"postgresql://{username}:{password}@localhost/{db}"

engine = create_engine(DATABASE_URL)

tables = [cls_obj.__tablename__ for cls_obj in inspect.getmembers(sys.modules['src.models']) \
                    if inspect.isclass(cls_obj) and cls_obj.__module__ == 'src.models' and hasattr(cls_obj, '__tablename__')]

tables_general_id = [
    cls_obj.__tablename__
    for _, cls_obj in inspect.getmembers(sys.modules['src.models'])
    if (
        inspect.isclass(cls_obj)
        and cls_obj.__module__ == 'src.models'
        and hasattr(cls_obj, '__tablename__')
        and 'general_id' in cls_obj.__fields__
    )
]

def init_db():
    SQLModel.metadata.create_all(engine)
