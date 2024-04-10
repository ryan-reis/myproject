from flask import Flask, render_template

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/employee')
def employee_directory():
    return render_template('employee.html')

@app.route('/payroll')
def payroll():
    return render_template('payroll.html')

@app.route('/documents')
def documents():
    return render_template('documents.html')

if __name__ == '__main__':
    app.run(debug=True)
