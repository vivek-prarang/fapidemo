
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ...config.settings import DATABASE_URL


# Create engine for database connection
engine = create_engine(DATABASE_URL)

# Create SessionLocal class for database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency function to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
