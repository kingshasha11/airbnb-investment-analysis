from sqlalchemy import create_engine
import pandas as pd

def get_engine():
    username = "root"
    password = ""
    host = "localhost"
    database = "airbnb_analysis"
    
    connection = f"mysql+pymysql://{username}:{password}@{host}/{database}"
    engine = create_engine(connection)
    return engine

if __name__ == "__main__":
    engine = get_engine()
    query = "SELECT COUNT(*) AS total_listings FROM listings;"
    df = pd.read_sql(query,engine)
    print(df)