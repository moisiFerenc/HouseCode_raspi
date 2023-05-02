from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('test.html')

@app.route("/checkboxes", methods=['POST'])
def handle_checkboxes():
    checkboxes_values = request.form.getlist('my_checkbox')
    for value in checkboxes_values:
        print(value)
    return ''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
