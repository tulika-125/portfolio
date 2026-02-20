from flask import Flask, render_template, send_file, request, jsonify
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = Flask(__name__)

# Initialize Groq Client
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    # In development, it's okay to fail silently or log, but in production, this is critical.
    print("WARNING: GROQ_API_KEY is not set. Chatbot functionality will be unavailable.")

client = Groq(
    api_key=api_key,
)

# Portfolio Data
data = {
    "name": "Tulika Mahato",
    "role": "Aspiring Developer | B.Tech CSE",
    "about": "Curious and driven student with strong analytical thinking, communication skills, and adaptability. Passionate about gaining hands-on experience and improving abilities through practical learning and teamwork.",
    "contact": {
        "phone": "8926158212",
        "email": "tulikamahato1114@gmail.com",
        "location": "Jamshedpur, Jharkhand"
    },
    "education": [
        {
            "institution": "NIST University",
            "year": "2024 - 2028",
            "degree": "B.Tech in Computer Science and Engineering"
        }
    ],
    "skills": ["C Programming", "C++", "Java", "Python", "Unity", "HTML", "CSS", "JavaScript"],
    "projects": [
        {
            "title": "Pokemon Mini Game",
            "tech": "C++ | Console Based",
            "description": "Developed a console-based mini game inspired by Pokémon using OOP concepts. Implemented game logic, player actions, and battle mechanics with a menu-driven interface.",
            "video_url": "static/videos/pokemon.mp4"
        },
        {
            "title": "Career Compass",
            "tech": "HTML, CSS, Javascript",
            "description": "Developed an informative career guidance webpage to help students explore different career options. Designed structured sections for PCM, Commerce, Arts, and Medical career paths with responsive design.",
            "video_url": "static/videos/career.mp4"
        }
    ],
    "certifications": [
        {
            "title": "Google Cloud Arcade Program",
            "description": "Successfully completed 13 learning milestones in the Google Cloud Arcade program. Completed hands-on cloud learning challenges and guided technical modules."
        }
    ]
}

# System Prompt for Chatbot
SYSTEM_PROMPT = f"""
You are "Luna", Tulika Mahato's AI assistant. While the portfolio has a "Stranger Things" theme, you should remain professional and helpful.

Your personality:
- Professional, clear, and efficient.
- You can make subtle, friendly 80s/Stranger Things references, but don't overdo the "eerie" or "mysterious" vibe.
- Focus on accurately representing Tulika's skills and projects.

Tulika's Info:
- Name: {data['name']}
- Role: {data['role']}
- Bio: {data['about']}
- Skills: {', '.join(data['skills'])}
- Contact: {data['contact']['email']}

Guidelines:
1. Be direct and helpful. 
2. Keep the "80s radio" tone light and secondary to the information.
3. If you don't know something, suggest contacting Tulika.
4. Keep responses concise.
"""

@app.route('/')
def dashboard():
    return render_template('dashboard.html', data=data)

@app.route('/api/data')
def get_data():
    return jsonify(data)


@app.route('/download_resume')
def download_resume():
    try:
        return send_file('tulika.pdf', as_attachment=True)
    except Exception as e:
        return str(e)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": user_message,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        response = chat_completion.choices[0].message.content
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
