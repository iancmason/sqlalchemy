import sqlalchemy
import sqlalchemy.orm

from db import db_folder

__engine__ = None
__factory = None

def global_init(db_name: str):
    global __engine, __factory

    if __factory:
        return

    conn_str = 'sqlite:///' + db_folder.get_full_path(db_name)
    __engine = sqlalchemy.create_engine(conn_str, echo=False)
    __factory = sqlalchemy.orm.sessionmaker(bind=__engine)

def create_tables():
    if not __engine:
        raise Exception("You have not called global_init()")

    # noinspection PyUnresolvedReferences
    import data.__all_models
    from data.sqlalchemybase import SqlAlchemyBase
    SqlAlchemyBase.metadata.create_all(__engine) #create all means find all the classes derived from sql alchemy base

def create_session() -> sqlalchemy.orm.Session:
    if not __factory:
        raise Exception('you have not called global_init()')

    session : Session = __factory()
    session.expire_on_commit = False
    return session
