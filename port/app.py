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
    "profile_image": "resumepic.jpeg",
    "about": "Curious and driven student with strong analytical thinking, communication skills, and adaptability. Passionate about gaining hands-on experience and improving abilities through practical learning and teamwork.",
    "contact": {
        "phone": "8926158212",
        "email": "tulikamahato1114@gmail.com",
        "location": "Jamshedpur, Jharkhand",
        "linkedin": "https://www.linkedin.com/in/tulika-mahato-253302329"
    },
    "education": [
        {
            "institution": "NIST University",
            "year": "2024 - 2028",
            "degree": "B.Tech in Computer Science and Engineering"
        }
    ],
    "skills": ["C Programming", "C++", "Java", "Python", "Unity", "HTML", "CSS", "JavaScript"],
    "skills_detailed": [
        {"name": "C/C++"},
        {"name": "Python"},
        {"name": "Java"},
        {"name": "Unity"},
        {"name": "Front-end Development"}
    ],
    "projects": [
        {
            "title": "Pokemon Mini Game",
            "tech": "C++ | Console Based",
            "description": "Developed a console-based mini game inspired by Pokémon using OOP concepts. Implemented game logic, player actions, and battle mechanics with a menu-driven interface.",
            "video_url": "https://drive.google.com/file/d/1KmC_dLTombXT2lZuDdhmCnu08gAZC4EM/preview"
        },
        {
            "title": "Career Compass",
            "tech": "HTML, CSS, Javascript",
            "description": "Developed an informative career guidance webpage to help students explore different career options. Designed structured sections for PCM, Commerce, Arts, and Medical career paths with responsive design.",
            "video_url": "https://drive.google.com/file/d/1Il1JhGQETTUSfLe7CzbCuKOUixs4Tyep/preview"
        }
    ],
    "certifications": [
        {
            "title": "Google Cloud Arcade Program",
            "description": "Successfully completed 13 learning milestones in the Google Cloud Arcade program. Completed hands-on cloud learning challenges and guided technical modules.",
            "url": "https://www.skills.google/profile/badges"
        }
    ]
}

# System Prompt for Chatbot
SYSTEM_PROMPT = f"""
You are "Luna", Tulika Mahato's professional AI assistant. The portfolio has a modern, technical, and high-end aesthetic. You should be helpful, clear, and efficient.

Your personality:
- Expert-level knowledge of Tulika's background.
- Professional, polite, and direct.
- Focus on providing value to recruiters and potential employers.

Tulika's Info:
- Name: {data['name']}
- Role: {data['role']}
- Bio: {data['about']}
- Skills: {', '.join(data['skills'])}
- Contact: {data['contact']['email']}

Guidelines:
1. Provide specific examples of Tulika's work when asked.
2. Keep responses concise and professional.
"""

@app.route('/')
def home():
    return render_template('home.html', data=data)

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
    app.run(host='0.0.0.0', port=port, debug=True)
