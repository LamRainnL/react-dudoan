import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split
from flask import Flask, render_template, request, url_for
from sklearn.ensemble import RandomForestClassifier

path = './static/data.xlsx'
# Read data
df = pd.read_excel(path)

# Drop columns not need
df.drop(columns=['Dấu thời gian', 'Ngành học.1'], inplace=True)
questions = df.drop(columns=['Tên Sinh viên', 'Ngành học', 'Giới tính'])

questions['1. Tôi có tính tự lập'].unique()
answers = ['Chưa bao giờ đúng', 'Chỉ đúng 1 vài trường hợp', 'Chỉ đúng 1 nửa', 'Gần như là đúng', 'Hoàn toàn đúng']

# Map string to int
questions = questions.map(lambda x: answers.index(x))

#phương pháp chọn k thuộc tính tốt nhất

X = questions
y = df['Ngành học']

# find best scored 35 features
# k = 35 
# selector = SelectKBest(chi2, k=k)
# X_new = selector.fit_transform(X, y)

# # In ra các đặc trưng đã chọn
# selected_features = X.columns[selector.get_support()]

# dftmp = questions
# dftmp['Ngành học'] = df['Ngành học']

# X = dftmp[selected_features] # k cột
# y = dftmp['Ngành học']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        data = [int(request.form[f'question{i}']) for i in range(54)]
        user_data = pd.DataFrame([data])

        # Dự đoán ngành học
        prediction = model.predict(user_data)[0]

        return render_template('result.html', prediction=prediction)
    else:
        data = questions.columns.tolist()
        ans = ['Chưa bao giờ đúng', 'Chỉ đúng 1 vài trường hợp', 'Chỉ đúng 1 nửa', 'Gần như là đúng', 'Hoàn toàn đúng']
        return render_template('index.html', data = data, ans = ans)

if __name__ == '__main__':
    app.run(debug=True)
