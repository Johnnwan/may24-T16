from flask import Flask, request, render_template
from model import Model
from input_processing import format_model_inputs

app = Flask(__name__)

# Method 1: Via HTML Form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_input = dict(request.form)
        # print(form_input)
        model_inputs=format_model_inputs(form_input)
        print(model_inputs)
        prediction = Model().predict(model_inputs)
        return render_template('index.html', prediction=prediction)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True,port=5002)
