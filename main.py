"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="AIzaSyDhlbk_wHrcsGbyVc6oOcfaaJ4L4LRc8xI")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["essay on ai"]
  },
  {
    "role": "model",
    "parts": ["## Artificial Intelligence: Reshaping Our World\n\nArtificial intelligence (AI) has transitioned from science fiction to a tangible reality, intricately woven into the fabric of our daily lives. From the algorithms curating our social media feeds to the voice assistants managing our schedules, AI's influence is undeniable and its potential, seemingly limitless. This essay explores the multifaceted landscape of AI, examining its applications, benefits, challenges, and the ethical considerations surrounding its development and deployment.\n\n**Applications Across Industries:**\n\nAI's versatility is evident in its wide range of applications across diverse sectors. In healthcare, AI algorithms analyze medical images with remarkable accuracy, aiding in early disease detection and diagnosis. The financial industry utilizes AI for fraud detection, algorithmic trading, and personalized financial advice. Manufacturing processes are becoming increasingly automated thanks to AI-powered robots and predictive maintenance systems. Even the creative industries are experiencing AI's impact, with AI tools assisting in music composition, graphic design, and content creation.\n\n**Benefits and Advancements:**\n\nThe integration of AI brings forth numerous benefits. Automation of repetitive tasks leads to increased efficiency and productivity, freeing up human workers to focus on more complex and creative endeavors. AI-powered systems can analyze vast datasets, identifying patterns and insights that would be impossible for humans to discern. This has led to breakthroughs in scientific research, weather prediction, and disaster response. Moreover, AI personalizes user experiences, tailoring products and services to individual preferences, ultimately enhancing customer satisfaction.\n\n**Challenges and Ethical Concerns:**\n\nDespite its transformative potential, AI presents significant challenges. Job displacement due to automation remains a concern, requiring proactive measures to reskill and upskill the workforce. Bias in AI algorithms, often stemming from biased training data, can lead to discriminatory outcomes and perpetuate societal inequalities. The issue of data privacy is also paramount, as AI systems often rely on vast amounts of personal data, raising concerns about its collection, storage, and use. \n\nThe development of autonomous weapons systems raises ethical questions about accountability and the potential for misuse. Ensuring the responsible development and deployment of AI is crucial, necessitating international cooperation and robust regulatory frameworks.\n\n**The Road Ahead:**\n\nAI is poised to revolutionize our world in ways we can only begin to imagine. As AI research progresses, we can expect even more sophisticated and capable systems. The key lies in harnessing the power of AI for the betterment of humanity while mitigating potential risks. Open dialogues, ethical guidelines, and continuous research are essential to ensure a future where AI complements and empowers human capabilities, leading to a more equitable and prosperous society."]
  },
  {
    "role": "user",
    "parts": ["stop"]
  },
  {
    "role": "model",
    "parts": ["Okay, I've stopped generating the essay."]
  },
])

convo.send_message("essay on israel palestine issue in 50 words")
print(convo.last.text)