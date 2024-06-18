from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# OpenAI API 키 설정
# openai.api_key = "-" # 깃허브에 안올려짐

def create_chatbot(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "chat bot"},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return str(e)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    bot_response = create_chatbot(user_input)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)