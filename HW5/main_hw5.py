import csv

from flask import Flask
import pandas as pd
import requests
from webargs import validate, fields
from webargs.flaskparser import use_kwargs

from hw5_class_file import HWProvider

app = Flask(__name__)


def get_currency_sign(currency):
    url = "https://bitpay.com/currencies"
    result = requests.get(url)
    if result.status_code != 200:  # not in(HTTPStatus.OK,)
        return Response("Error", status=result.status_code)
    result = result.json()["data"]
    for value in result:
        if value["code"] == currency:
            return value["symbol"]


def get_bitcoin_value(currency):
    url = "https://bitpay.com/api/rates"
    result = requests.get(url)
    if result.status_code != 200:
        return Response("Error", status=result.status_code)
    result = result.json()
    default_res = result[2]["rate"]
    res = str(
        next(
            (item["rate"] for item in result if item["code"] == currency),
            f" {default_res} USD",
        )
    )
    return res


@app.route("/get-bitcoin-value")
@use_kwargs({"currency": fields.Str(required=False)}, location="query")
def get_bitcoin_value_and_sign(currency):
    return f'{get_bitcoin_value(currency)} {get_currency_sign(currency)}'


@app.route("/generate-students")
@use_kwargs(
    {
        "quantity": fields.Int(
            required=True,
            validate=[validate.Range(min=1, max=1000)],
        )
    },
    location="query",
)
def generate_students(quantity):
    fake = Faker("UK")
    fake.add_provider(HWProvider)
    with open("hw5.csv", "w", newline="") as csv_file:
        fieldnames = [
            "first_name",
            "last_name",
            "email",
            "password",
            "date_of_birth"
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        for _ in range(quantity):
            writer.writerow(fake.profile_for_homework())
    filename = "hw5.csv"
    data = pd.read_csv(filename, header=None)
    return pd.DataFrame.to_html(data)


app.run(port=5001, debug=True)
