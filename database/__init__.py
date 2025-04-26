from sqlalchemy import create_engine, event
from sqlalchemy.orm import declarative_base, sessionmaker
SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
localSession = sessionmaker(bind=engine)
Base = declarative_base()

# включение каскадов
@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON;")
    cursor.close()

def get_db():
    db = localSession()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()