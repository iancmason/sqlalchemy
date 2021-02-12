import sqlalchemy as sa

from data.sqlalchemybase import SqlAlchemyBase

class Scooter(SqlAlchemyBase):
    __tablename__ = 'scooters'    

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date = sa.Column(sa.DateTime)
    vin = sa.Column(sa.String)
    model = sa.Column(sa.String)
    battery_level = sa.Column(sa.Integer)

    # TODO: Relationships
