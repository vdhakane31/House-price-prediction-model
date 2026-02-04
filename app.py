from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    display_price = None

    if request.method == 'POST':
        sqft = float(request.form['sqft'])
        rooms = int(request.form['rooms'])
        bathrooms = int(request.form['bathrooms'])

        # Simple dummy formula (replace with ML later)
        price = (sqft * 3000) + (rooms * 500000) + (bathrooms * 300000)

        if price < 10000000:
            display_price = f"{price/100000:.2f} Lakhs"
        else:
            display_price = f"{price/10000000:.2f} Crores"

        prediction = price

    return render_template(
        'index.html',
        prediction=prediction,
        display_price=display_price
    )

if __name__ == '__main__':
    app.run(debug=True)
