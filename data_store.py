import sqlalchemy as sq
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

metadata=MetaData()
Base=declarative_base()

class Viewed (Base):
    __tablename__='viewed'

    profile_id=sq.Column(sq.Integer, primary_key=True)
    worksheet_id=sq.Column(sq.Integer, unique=True)
    engine=create_engine(db_url_object)
    Session=sessionmaker(bind=engine)
    session=Session()
    to_bd=Viewed(profile_id=123, worksheet_id=3221)
    session.add(to_bd)

    engine=create_engine(db_url_object)
    Session=sessionmaker(bind=engine)
    session=Session()
    session.commit()
    from_bd=session.quaery(Viewed).filter(Viewed.profile_id==123).all()