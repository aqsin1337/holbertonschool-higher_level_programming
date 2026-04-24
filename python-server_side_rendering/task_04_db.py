from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except Exception:
        return []

def read_csv():
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception:
        pass
    return products

def read_sql():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append(dict(row))
        conn.close()
    except Exception as e:
        print(f"Database error: {e}")
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql()
    else:
        return render_template('product_display.html', error="Wrong source")
    
    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if p['id'] == product_id]
            if not data:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Product not found")
    
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
