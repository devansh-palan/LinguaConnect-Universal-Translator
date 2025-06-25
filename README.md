
# 🌐 LinguaConnect: Universal Translator

**LinguaConnect** is a multilingual text translation web app powered by [Hugging Face Transformers](https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt) and built with [Streamlit](https://streamlit.io/). It leverages the `facebook/mbart-large-50-many-to-many-mmt` model to provide high-quality translations across **50+ languages**.

---

## 🚀 Features

- 🌍 Supports 50+ languages for both input and output.
- ⚡ GPU acceleration (if available) for faster translation.
- 🧠 Uses mBART-50, a state-of-the-art multilingual translation model.
- 🖥️ User-friendly Streamlit interface.
- ✅ Error handling and translation status feedback.

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/linguaconnect.git
   cd linguaconnect
   ```

2. **Install dependencies**
   It is recommended to use a virtual environment.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run main.py
   ```

---

## 📦 Requirements

- Python 3.8+
- `transformers`
- `torch`
- `streamlit`

---

## 🌐 Supported Languages

The app supports all 50+ languages available in `mbart-large-50`. Example codes include:

- English: `en_XX`
- French: `fr_XX`
- Hindi: `hi_IN`
- Chinese: `zh_CN`
- Spanish: `es_XX`
- ... and many more!

Full list is in the language dropdowns in the app.

---

## 💬 Usage

1. Enter the text you want to translate.
2. Select source and target languages from the dropdowns.
3. Click **Translate** and get your result instantly!

Example:
> “Hello, how are you?” → Source: `en_XX`, Target: `fr_XX`  
> **Output**: “Bonjour, comment vas-tu ?”

---


## 📜 License

MIT License
