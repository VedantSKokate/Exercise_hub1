from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the home page
@app.route('/')
def welcome_page():
    return render_template('index.html')

# Route for page 1 that shows activities
@app.route('/page1')
def page1():
    return render_template('page1.html')

# Route for page 2
@app.route('/page2')
def page2():
    exercise_name = request.args.get('exercise_name')
    video1_url = request.args.get('video1_url')
    video2_url = request.args.get('video2_url')

    if not (exercise_name and video1_url and video2_url):
        return redirect(url_for('page1'))

    return render_template(
        'page2.html',
        exercise_name=exercise_name,
        video1_url=video1_url,
        video2_url=video2_url
    )

# Route for page 3
@app.route('/page3')
def page3():
    return render_template('page3.html')

# Route for page 4
@app.route('/page4')
def page4():
    return render_template('page4.html')

# Route for page 5
@app.route('/page5')
def page5():
    return render_template('page5.html')

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
