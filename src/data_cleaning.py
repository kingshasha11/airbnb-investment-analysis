import pandas as pd


def clean_data(df):

    df = df.drop_duplicates()

    df["reviews_per_month"] = df["reviews_per_month"].fillna(0)

    df = df[df["price"] > 0]

    df = df[df["price"] < 1000]

    df["price"] = df["price"].astype(float)

    return df