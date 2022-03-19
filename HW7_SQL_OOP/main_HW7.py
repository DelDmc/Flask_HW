from flask import Flask

from database_handler import execute_query

from webargs import validate, fields
from webargs.flaskparser import use_kwargs

from utils import format_records

app = Flask(__name__)


@app.route("/stats-by-city")
@use_kwargs(
    {
        "genre": fields.Str(
            required=False,
            missing=None,
            validate=[validate.Regexp("^[0-9]*")])
    },
    location="query"
)
def stats_by_city(genre):
    query = f"""SELECT BillingCity ,COUNT(BillingCity) AS QTY 
        FROM(SELECT BillingCity FROM invoice_items ii
        INNER JOIN invoices i USING (InvoiceId)
        INNER JOIN tracks t USING (TrackId)
        INNER JOIN genres g USING (GenreId) WHERE g.Name = ?
        ORDER BY BillingCity )
        GROUP BY "BillingCity"
        ORDER BY QTY DESC
        LIMIT 1
        """
    records = execute_query(query=query,
                            args=(genre,) if genre else ("Hip Hop/Rap",))
    return format_records(records)


app.run(port=5001, debug=True)
