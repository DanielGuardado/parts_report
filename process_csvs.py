import requests
import os, uuid
import pandas as pd
from datetime import datetime, timedelta


from get_csv import get_pickup, get_pickup_prev


local_path = "./data"


def pickup_csv():

    csv = get_pickup(1)
    local_file_name = f"PickupReport2.csv"
    upload_file_path = os.path.join(local_path, local_file_name)

    with open(upload_file_path, "wb") as file:
        file.write(csv)

    df = pd.read_csv(upload_file_path, skiprows=5, header=0, engine="python")
    df.rename(columns={"Unnamed: 0": "test", "Unnamed: 15": "Qty"}, inplace=True)
    df = df[["Part Number", "Qty"]]
    df.drop(df.tail(1).index, inplace=True)
    print(df)

    df.to_csv(
        upload_file_path,
        index=False,
        header=True,
        quotechar='"',
    )


def pickup_csv2():

    csv = get_pickup(2)
    local_file_name = f"PickupReport2.csv"
    upload_file_path = os.path.join(local_path, local_file_name)

    with open(upload_file_path, "wb") as file:
        file.write(csv)

    df = pd.read_csv(upload_file_path, skiprows=5, header=0, engine="python")
    df.rename(columns={"Unnamed: 0": "test", "Unnamed: 21": "Qty"}, inplace=True)
    df = df[["Part Number", "Qty"]]
    df.drop(df.tail(1).index, inplace=True)
    print(df)

    df.to_csv(
        upload_file_path,
        index=False,
        header=True,
        quotechar='"',
    )


# def pickup_csv_prev():

#     csv = get_pickup_prev(1)
#     local_file_name = f"PickupReportPrev.csv"
#     upload_file_path = os.path.join(local_path, local_file_name)

#     with open(upload_file_path, "wb") as file:
#         file.write(csv)

#     df = pd.read_csv(upload_file_path, skiprows=5, header=0, engine="python")
#     df.rename(columns={"Unnamed: 0": "test", "Unnamed: 15": "Qty"}, inplace=True)
#     df = df[["Part Number", "Qty"]]
#     df.drop(df.tail(1).index, inplace=True)
#     print(df)

#     df.to_csv(
#         upload_file_path,
#         index=False,
#         header=True,
#         quotechar='"',
#     )