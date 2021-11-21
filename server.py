from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'super duper secret' 

@app.route('/')
def counter():
    if 'count' not in session:
        session['count'] = 0
    if 'visits' not in session:
        session['visits'] = 0
    session['count'] += 1
    session['visits'] += 1
    return render_template('counter.html')

@app.route('/add_two')
def add_two():
    session['count'] += 1
    return redirect('/')

@app.route('/add_custom', methods=['POST'])
def add_custom():
    session['count'] += int(request.form['custom_step']) - 1
    return redirect('/')

@app.route('/destroy_session')
def reset():
    session['count'] = 0
    session['visits'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)