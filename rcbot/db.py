from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



engine = create_engine('sqlite:///ryancreamer.db')
Base = declarative_base()


class Video(Base):
    __tablename__ = 'video'
    id=Column(Integer, primary_key=True)
    video_id = Column(String)
    title=Column(String)
    thumbnail=Column(String)
    url=Column(Integer)

    def save(self):
        if self.id == None:
            session.add(self)
        return session.commit()


def get_video(**kwargs):
    return session.query(Video).filter_by(**kwargs).first()



Session = sessionmaker()
Session.configure(bind=engine)

Base.metadata.create_all(engine)

session = Session()
