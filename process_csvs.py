import requests
import os, uuid
import pandas as pd
from datetime import datetime, timedelta
import io
import pyodbc
import config
from sqlalchemy import event
import sqlalchemy
import urllib

from get_csv import get_pickup


local_path = "./data"


def pickup_csv():
    csv = get_pickup(1, "current")
    csv2 = get_pickup(2, "current")
    csv3 = get_pickup(1, "previous")
    csv4 = get_pickup(2, "previous")

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

    conn = pyodbc.connect(config.connection)
    cursor = conn.cursor()
    cursor.fast_executemany = True

    db_params = urllib.parse.quote_plus(config.connection)
    engine = sqlalchemy.create_engine(
        "mssql+pyodbc:///?odbc_connect={}".format(db_params)
    )

    df.to_sql(
        "PartsReportCurrent", engine, index=False, if_exists="replace", schema="dbo"
    )
    df3.to_sql(
        "PartsReportPrevious", engine, index=False, if_exists="replace", schema="dbo"
    )