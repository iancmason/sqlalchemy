import sqlalchemy
import sqlalchemy.orm

from db import db_folder

__engine__ = None
__factory = None

def global init(db_name: str):
    global __engine, __factory

    if __factory:
        return

    conn_str = 'sqlite:///' + db_folder.get_full_path(db_name)
    __engine = sqlalchemy.create_engine(conn_str, echo=False)
    __factory = sqlalchemy.orm.sessionmaker(bind=__engine)

def create tables():
    if not __engine:
        raise Exception("You have not called global_init()")

    # noinspection PyUnresolvedReferences
    import data.__all_models
    from data.sqlalchemybase import SqlAlchemyBase
    SqlAlchemyBase.metadata.create_all(__engine) #create all means find all the classes derived from sql alchemy base

def create_session() -> sqlalchemy.orm.Session:
    pass
