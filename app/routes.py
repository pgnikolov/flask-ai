from flask import Blueprint, render_template, request, current_app
from groq import Groq

main = Blueprint('main', __name__)


def get_ai_response(user_input):
    api_key = current_app.config.get('GROQ_API_KEY')
    if not api_key:
        return "Error: API key is missing."

    client = Groq(api_key=api_key)
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            model="llama3-8b-8192",
        )

        if chat_completion.choices:
            return chat_completion.choices[0].message.content
        else:
            return "Error: No choices returned from the API."
    except Exception as e:
        return f"Error: {e}"


@main.route('/', methods=['GET', 'POST'])
def index():
    ai_response = ''
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        if user_input:
            ai_response = get_ai_response(user_input)
    return render_template('index.html', ai_response=ai_response)
