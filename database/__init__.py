from sqlalchemy.engine import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
engine = create_engine(SQLALCHEMY_DATABASE_URI)
localSession = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    db = localSession()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()