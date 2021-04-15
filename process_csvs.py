import requests
import os, uuid
import pandas as pd
from datetime import datetime, timedelta
import io


from get_csv import get_pickup


local_path = "./data"


def pickup_csv():

    csv = get_pickup(1, "current")
    csv2 = get_pickup(2, "current")
    csv3 = get_pickup(1, "previous")
    csv4 = get_pickup(2, "previous")

    local_file_name = f"CurrentMonth.csv"
    local_file_name2 = f"LastMonth.csv"

    upload_file_path = os.path.join(local_path, local_file_name)
    upload_file_path2 = os.path.join(local_path, local_file_name2)

    df = pd.read_csv(
        io.StringIO(csv.decode("utf-8")), skiprows=5, header=0, engine="python"
    )
    df.rename(columns={"Unnamed: 15": "Qty"}, inplace=True)
    df = df[["Part Number", "Qty"]]
    df.drop(df.tail(1).index, inplace=True)

    df2 = pd.read_csv(
        io.StringIO(csv2.decode("utf-8")), skiprows=5, header=0, engine="python"
    )
    df2.rename(columns={"Unnamed: 21": "Qty"}, inplace=True)
    df2 = df2[["Part Number", "Qty"]]
    df2.drop(df2.tail(1).index, inplace=True)
    df = df.append(df2)

    df3 = pd.read_csv(
        io.StringIO(csv3.decode("utf-8")), skiprows=5, header=0, engine="python"
    )
    df3.rename(columns={"Unnamed: 15": "Qty"}, inplace=True)
    df3 = df3[["Part Number", "Qty"]]
    df3.drop(df3.tail(1).index, inplace=True)

    df4 = pd.read_csv(
        io.StringIO(csv4.decode("utf-8")), skiprows=5, header=0, engine="python"
    )
    df4.rename(columns={"Unnamed: 21": "Qty"}, inplace=True)
    df4 = df4[["Part Number", "Qty"]]
    df4.drop(df4.tail(1).index, inplace=True)
    df3 = df3.append(df4)

    df.to_csv(
        upload_file_path,
        index=False,
        header=True,
        quotechar='"',
    )

    df3.to_csv(
        upload_file_path2,
        index=False,
        header=True,
        quotechar='"',
    )