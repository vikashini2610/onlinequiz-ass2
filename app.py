from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris",
    },
    {
        "question": "What is 5 + 7?",
        "options": ["10", "12", "13", "14"],
        "answer": "12",
    },
    {
        "question": "Which programming language is known for data analysis?",
        "options": ["Java", "C++", "Python", "Ruby"],
        "answer": "Python",
    },
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        user_answers = request.form.to_dict()
        score = sum(1 for idx, q in enumerate(quiz_data) if user_answers.get(str(idx)) == q['answer'])
        return redirect(url_for('result', score=score, total=len(quiz_data)))
    return render_template('quiz.html', quiz_data=quiz_data)

@app.route('/result')
def result():
    score = int(request.args.get('score', 0))
    total = int(request.args.get('total', 1))
    return render_template('result.html', score=score, total=total)

if __name__ == '__main__':
    app.run(debug=True)
