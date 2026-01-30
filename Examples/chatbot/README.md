# Streamlit Chatbot

This repository contains a simple chatbot built with Streamlit.
The main entry point is `chatbot.py`.
Below are the steps to set up the environment and run the application.

---

## Prerequisites

| Item | Minimum Version | Notes |
|------|-----------------|-------|
| Python | 3.8+ | Tested with 3.12 |
| pip | - | Comes with Python installation |
| virtualenv (optional) | - | Recommended for isolated environments |

---

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/synaptrixai/SpiLLI.git
   
   cd SpiLLI/Examples/chatbot
   ```

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   
   Step 1: Install the requirements in your terminal:

   ```bash
   pip install -r requirements.txt
   ```

   Step 2: Install SpiLLI SDK using the following:
   ```bash
   pip install --index-url https://well.synaptrix.org --upgrade SpiLLI
   ```
   Step 3: Download your encryption  pem file into the folder SpiLLI/Examples/chatbot. For instructions see the link: https://github.com/synaptrixai/SpiLLI/wiki/SpiLLI-SDK-Installation-Guide#step-2-download-a-personalized-encryption-pem-key

   ** Optionally you can install and run the chatbot directly using a docker container with the following command:
      ```bash
      docker-compose up
      ```
---

## Running the Chatbot


You can run the chatbot in your terminal using:
```bash
streamlit run chatbot.py
```

- The app will start and open a local web server (usually at `http://localhost:8501`).
- Open that URL in your browser to interact with the chatbot.

---

## Common Issues

| Issue | Fix |
|-------|-----|
| `ModuleNotFoundError` | Ensure all required packages are installed. Check `requirements.txt`. |
| Port already in use | Use `streamlit run chatbot.py --server.port 8502` to change the port. |
| PEM file missing | Download the pem file into the folder SpiLLI/Examples/chatbot. For instructions see the link: https://github.com/synaptrixai/SpiLLI/wiki/SpiLLI-SDK-Installation-Guide#step-2-download-a-personalized-encryption-pem-key|

---

## Customization

- **Changing the model**: Edit `chatbot.py` and modify the model name or parameters.
- **Adding new features**: Add widgets or callbacks in the Streamlit layout.

---

## Contributing

Feel free to open issues or pull requests. Please follow the standard Git workflow.

---

## License

MIT License – see `LICENSE` file for details.

---