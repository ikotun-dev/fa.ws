from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:collins2005@localhost/chatapp"
#x = 'postgresql://postgres:T8ZGn16qDBNovZdzGw6g@containers-us-west-95.railway.app:5946/railway'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


#dependency
def get_db():
    db = SessionLocal()
    try :
        yield db
    finally :
        db.close()
