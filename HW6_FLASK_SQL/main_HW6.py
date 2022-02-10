from flask import Flask

from database_handler import execute_query

from webargs import validate, fields
from webargs.flaskparser import use_kwargs

from utils import format_records

app = Flask(__name__)


@app.route("/order-price")
@use_kwargs(
    {
        "country": fields.Str(
            required=False,
            missing=None,
            validate=[validate.Regexp("^[0-9]*")])
    },
    location="query"
)
def order_price(country):
    query = "SELECT InvoiceId, UnitPrice*Quantity, BillingCountry W " \
            "FROM invoice_items " \
            "INNER JOIN invoices i USING (InvoiceId)"
    fields = {}
    if country:
        fields["BillingCountry"] = country

    if fields:
        query += " WHERE " + "".join(f"{key}=?" for key in fields.keys())

    records = execute_query(query=query, args=tuple(fields.values()))
    return format_records(records)


@app.route("/get-all-info-about-tracks")
def get_all_info_about_track():
    query = """SELECT t.TrackId, t.Name, 
    Composer, 
    Title as AlbumTitle, 
    g.Name as Genre, 
    mt.Name as MediaType, 
    Milliseconds, Bytes ,
    t.UnitPrice as Price,
    a2.Name as Artist,
    Qty, Sales
FROM tracks t 
INNER JOIN albums a USING(AlbumId)
INNER JOIN genres g USING(GenreId)
INNER JOIN media_types mt USING(MediaTypeId)
INNER JOIN artists a2 USING(ArtistId)
INNER JOIN invoice_items ii USING (TrackId)
INNER JOIN (SELECT TrackId, COUNT(TrackId) AS Qty, COUNT(TrackId) * UnitPrice AS Sales FROM invoice_items ii 
GROUP BY TrackId ) USING (TrackId)"""

    fields = {}
    records = execute_query(query=query, args=tuple(fields.values()))
    print(records)
    return format_records(records)


app.run(port=5001, debug=True)
