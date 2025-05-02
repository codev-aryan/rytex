# Rytex AI Chatbot

A conversational AI assistant powered by Google's Gemini API with Firebase integration for chat history persistence.

![Rytex AI Logo](https://via.placeholder.com/150)

## 📖 Overview

Rytex is an intelligent chatbot application built with Streamlit and Google's Generative AI capabilities. It interprets user inputs, provides contextually relevant responses, and remembers conversation history through Firebase integration.

## ✨ Features

- 💬 Natural language understanding and generation
- 🧠 Context-aware conversations with memory
- 💻 Code generation capabilities
- 🧮 Mathematical expression evaluation
- 📅 Date and time information
- 📚 Persistent chat history using Firebase
- ⌨️ Realistic typing animation effect

## 🔧 Technology Stack

- **Frontend**: Streamlit
- **AI Engine**: Google Generative AI (Gemini 1.5 Flash)
- **Database**: Firebase Firestore
- **Language**: Python

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Google Cloud account with Gemini API access
- Firebase project with Firestore database

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/cipherex/rytex.git
   cd rytex
   ```

2. Create a virtual environment and activate it
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables
   
   Create a `.env` file in the project root with the following:
   ```
   API_KEY=your_gemini_api_key
   FIREBASE_CONFIG=path_to_your_firebase_credentials.json
   ```

### Running the Application

```bash
streamlit run main.py
```

Navigate to the URL shown in the terminal (typically http://localhost:8501) to interact with Rytex.

## 📋 Project Structure

```
rytex/
├── main.py            # Main application entry point
├── backend.py         # Core functionality and API integrations
├── requirements.txt   # Package dependencies
├── .env               # Environment variables (not tracked in git)
└── README.md          # Project documentation
```

## 🔄 How It Works

1. User starts the chat by clicking the "Start Chatting" button
2. Previous conversation history is retrieved from Firebase (if any)
3. User enters a prompt which is processed by the Gemini AI API
4. The system interprets the command and generates an appropriate response
5. Responses are displayed with a typewriter effect for a more natural experience
6. All conversations are stored in Firebase for future reference

## 📝 Response Types

Rytex can handle multiple types of requests:

- **General Chat**: Everyday conversation and assistance
- **Code Generation**: Creating code snippets in Python
- **Mathematics**: Solving mathematical expressions
- **Date/Time**: Providing current date and time information

## 🛠️ Customization

You can extend Rytex's capabilities by:

1. Adding more response types in the `process_interpreted_command` function
2. Enhancing the prompt templates for better AI understanding
3. Customizing the UI in the Streamlit interface

## 🔒 Security Notes

- Never expose your API keys or Firebase credentials in public repositories
- Consider implementing user authentication for multi-user environments
- Review Google's usage policies for the Gemini API

## 📈 Future Improvements

- [ ] Add user authentication
- [ ] Implement conversation threading
- [ ] Support file uploads for data analysis
- [ ] Add voice input/output capabilities
- [ ] Create a settings panel for customization

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Contributors

- Cipherex

## 🙏 Acknowledgments

- Google for providing the Gemini API
- Streamlit for their amazing framework
- Firebase for the database solutions

---

Made with ❤️ by Aryan