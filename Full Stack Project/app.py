from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query', '').lower()
    conn = sqlite3.connect('stations.db')
    cur = conn.cursor()
    cur.execute("SELECT name, address, battery_types FROM stations WHERE LOWER(city) LIKE ? OR pincode LIKE ?", (f'%{query}%', f'%{query}%'))
    results = cur.fetchall()
    conn.close()
    return jsonify([{'name': row[0], 'address': row[1], 'battery_types': row[2]} for row in results])

if __name__ == '__main__':
    app.run(debug=True)
