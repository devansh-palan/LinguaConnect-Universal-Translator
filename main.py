from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import torch
import streamlit as st

model_name = "facebook/mbart-large-50-many-to-many-mmt"

@st.cache_resource
def load_model_and_tokenizer():
    try:
        tokenizer = MBart50TokenizerFast.from_pretrained(model_name)
        model = MBartForConditionalGeneration.from_pretrained(model_name)
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model = model.to(device)
        return tokenizer, model, device
    except Exception as e:
        st.error(f"Failed to load model or tokenizer: {e}")
        st.stop()

tokenizer, model, device = load_model_and_tokenizer()

if device.type == "cpu":
    st.warning("Running on CPU. Translation may be slow due to large model size.")

def translate_text(text, source_lang, target_lang):
    try:
        if source_lang not in tokenizer.lang_code_to_id or target_lang not in tokenizer.lang_code_to_id:
            st.error("Invalid source or target language code.")
            return None
        tokenizer.src_lang = source_lang
        encoded_text = tokenizer(text, return_tensors="pt").to(device)
        generated_tokens = model.generate(
            **encoded_text,
            forced_bos_token_id=tokenizer.lang_code_to_id[target_lang]
        )
        translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        return translated_text[0]
    except Exception as e:
        st.error(f"Translation failed: {e}")
        return None

st.title("LinguaConnect: Universal Translator")
st.markdown("Translate text in multiple languages using AI-powered models from Hugging Face!")

text = st.text_area("Enter the text to translate")

source_language = st.selectbox(
    "Select the source language",
    options=[
        "ar_AR", "cs_CZ", "de_DE", "en_XX", "es_XX", "et_EE", "fi_FI", "fr_XX", "gu_IN", 
        "hi_IN", "it_IT", "ja_XX", "kk_KZ", "ko_KR", "lt_LT", "lv_LV", "my_MM", "ne_NP", 
        "nl_XX", "ro_RO", "ru_RU", "si_LK", "tr_TR", "vi_VN", "zh_CN", "af_ZA", "az_AZ", 
        "bn_IN", "fa_IR", "he_IL", "hr_HR", "id_ID", "ka_GE", "km_KH", "mk_MK", "ml_IN", 
        "mn_MN", "mr_IN", "pl_PL", "ps_AF", "pt_XX", "sv_SE", "sw_KE", "ta_IN", "te_IN", 
        "th_TH", "tl_XX", "uk_UA", "ur_PK", "xh_ZA", "gl_ES", "sl_SI"
    ]
)

target_language = st.selectbox(
    "Select the target language",
    options=[
        "ar_AR", "cs_CZ", "de_DE", "en_XX", "es_XX", "et_EE", "fi_FI", "fr_XX", "gu_IN", 
        "hi_IN", "it_IT", "ja_XX", "kk_KZ", "ko_KR", "lt_LT", "lv_LV", "my_MM", "ne_NP", 
        "nl_XX", "ro_RO", "ru_RU", "si_LK", "tr_TR", "vi_VN", "zh_CN", "af_ZA", "az_AZ", 
        "bn_IN", "fa_IR", "he_IL", "hr_HR", "id_ID", "ka_GE", "km_KH", "mk_MK", "ml_IN", 
        "mn_MN", "mr_IN", "pl_PL", "ps_AF", "pt_XX", "sv_SE", "sw_KE", "ta_IN", "te_IN", 
        "th_TH", "tl_XX", "uk_UA", "ur_PK", "xh_ZA", "gl_ES", "sl_SI"
    ]
)

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter some text to translate.")
    else:
        with st.spinner("Translating..."):
            translation = translate_text(text, source_language, target_language)
            if translation:
                st.success("Translation successful")
                st.write(translation)

st.sidebar.header("Examples")
st.sidebar.markdown("""
**Try translating:**
- `Hello, how are you?` from `en_XX` (English) to `fr_XX` (French)
- `Bonjour, comment vas-tu ?` from `fr_XX` (French) to `en_XX` (English)
""")