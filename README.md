# 🤖 E-Commerce Customer Support Chatbot

## 🎯 **The Problem**

E-commerce customers often need quick assistance with common questions about:

* 📦 Order status and tracking
* 🔄 Returns and refunds
* 🛍️ Products and purchases
* 💬 General customer support

Handling every customer query manually can be time-consuming and may result in delays.

## 💡 **The Solution**

An AI-powered customer support chatbot that uses the **Llama 3** language model to:

* 💬 **Answer customer queries** with helpful responses
* 🤝 **Assist customers** with common support requests
* 🔒 **Request order numbers** before handling order-status queries
* 📝 **Record conversations** for monitoring and improvement
* ⚡ **Provide fast responses** through a local AI model

## ✨ **Key Features**

### 💬 **Customer Support**

* Interactive terminal-based chatbot
* Answers customer questions
* Professional and polite responses
* Responses limited to under 100 words

### 🧠 **AI-Powered Responses**

* Uses the **Llama 3** language model
* Powered locally through **Ollama**
* Maintains conversation context
* Uses a system prompt to control chatbot behaviour

### 📝 **Conversation Logging**

* Records customer messages
* Records chatbot responses
* Includes timestamps
* Saves conversations to `chat_log.txt`

### 🔐 **Order Support**

* Requests an order number before checking order status
* Helps prevent incomplete order-status requests
* Provides appropriate responses when information is unavailable

## 🛠️ **Technologies Used**

* **Language:** Python
* **AI Model:** Llama 3
* **AI Framework:** Ollama
* **Libraries:** Python `ollama`, `datetime`
* **Logging:** Text file (`chat_log.txt`)
* **Development Environment:** VS Code
* **Version Control:** Git & GitHub

## 🚀 **How to Run**

### 1. Install Ollama

Install Ollama on your computer.

### 2. Download Llama 3

```bash
ollama pull llama3
```

### 3. Install the Python Library

```bash
pip install ollama
```

### 4. Run the Chatbot

```bash
python chatbot.py
```

### 5. Exit the Chatbot

Type:

```text
exit
```

## 📁 **Project Structure**

```text
Chat-bot/
└── chatbot.py
```

The `chat_log.txt` file is created automatically when the chatbot is used.

## 📈 **Future Improvements**

* 🌐 Web-based chatbot interface
* 🔐 Customer authentication
* 📦 Real-time order tracking
* 🗄️ Database integration
* 👨‍💼 Human-agent escalation
* 📊 Customer satisfaction analytics
* ☁️ Cloud deployment and scalability


## 👤 **Author**

**Naledi Kodisang**
