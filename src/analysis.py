def average_price(df):

    result = (
        df.groupby("neighbourhood_group")["price"]
        .mean()
        .sort_values(ascending=False)
    )

    return result


def occupancy_rate(df):

    df["occupancy_rate"] = (365 - df["availability_365"]) / 365

    result = (
        df.groupby("neighbourhood_group")["occupancy_rate"]
        .mean()
        .sort_values(ascending=False)
    )

    return result


def most_expensive(df):

    return (
        df.groupby("neighbourhood")["price"]
        .mean()
        .sort_values(ascending=False)
        .head(5)
    )


def most_demanded(df):

    return (
        df.groupby("neighbourhood")["number_of_reviews"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )