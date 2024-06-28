from flask import render_template, request, redirect, url_for, current_app

@current_app.route('/')
def index():
    return render_template('index.html')

@current_app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        rating = request.form['rating']
        price = request.form['price']

        conn = current_app.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO shoppers (name, location, rating, price) VALUES (%s, %s, %s, %s)",
                      (name, location, rating, price))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('index'))

    return render_template('register.html')

@current_app.route('/shoppers')
def shoppers():
    conn = current_app.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM shoppers WHERE busy=0")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('shoppers.html', shoppers=data)

@current_app.route('/select_shopper/<int:id>')
def select_shopper(id):
    conn = current_app.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE shoppers SET busy=1 WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('shoppers'))
