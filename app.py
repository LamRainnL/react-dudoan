from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

# Load mô hình đã lưu
with open('model/model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        data = [int(request.form[f'question{i}']) for i in range(1, 55)]
        user_data = pd.DataFrame([data])

        # Dự đoán ngành học
        prediction = model.predict(user_data)[0]

        return render_template('result.html', prediction=prediction)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
