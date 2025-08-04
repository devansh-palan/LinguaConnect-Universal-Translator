from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import torch
import streamlit as st

model_name = "facebook/mbart-large-50-many-to-many-mmt"

@st.cache_resource
def load_model_and_tokenizer():
    tokenizer = MBart50TokenizerFast.from_pretrained(model_name)
    model = MBartForConditionalGeneration.from_pretrained(model_name)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    return tokenizer, model, device

# 🟡 Force model to load immediately with spinner
with st.spinner("Loading model... This may take a few seconds."):
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

language_options = {
    "ar_AR": "Arabic (ar_AR)",
    "cs_CZ": "Czech (cs_CZ)",
    "de_DE": "German (de_DE)",
    "en_XX": "English (en_XX)",
    "es_XX": "Spanish (es_XX)",
    "et_EE": "Estonian (et_EE)",
    "fi_FI": "Finnish (fi_FI)",
    "fr_XX": "French (fr_XX)",
    "gu_IN": "Gujarati (gu_IN)",
    "hi_IN": "Hindi (hi_IN)",
    "it_IT": "Italian (it_IT)",
    "ja_XX": "Japanese (ja_XX)",
    "kk_KZ": "Kazakh (kk_KZ)",
    "ko_KR": "Korean (ko_KR)",
    "lt_LT": "Lithuanian (lt_LT)",
    "lv_LV": "Latvian (lv_LV)",
    "my_MM": "Burmese (my_MM)",
    "ne_NP": "Nepali (ne_NP)",
    "nl_XX": "Dutch (nl_XX)",
    "ro_RO": "Romanian (ro_RO)",
    "ru_RU": "Russian (ru_RU)",
    "si_LK": "Sinhala (si_LK)",
    "tr_TR": "Turkish (tr_TR)",
    "vi_VN": "Vietnamese (vi_VN)",
    "zh_CN": "Chinese (zh_CN)",
    "af_ZA": "Afrikaans (af_ZA)",
    "az_AZ": "Azerbaijani (az_AZ)",
    "bn_IN": "Bengali (bn_IN)",
    "fa_IR": "Persian (fa_IR)",
    "he_IL": "Hebrew (he_IL)",
    "hr_HR": "Croatian (hr_HR)",
    "id_ID": "Indonesian (id_ID)",
    "ka_GE": "Georgian (ka_GE)",
    "km_KH": "Khmer (km_KH)",
    "mk_MK": "Macedonian (mk_MK)",
    "ml_IN": "Malayalam (ml_IN)",
    "mn_MN": "Mongolian (mn_MN)",
    "mr_IN": "Marathi (mr_IN)",
    "pl_PL": "Polish (pl_PL)",
    "ps_AF": "Pashto (ps_AF)",
    "pt_XX": "Portuguese (pt_XX)",
    "sv_SE": "Swedish (sv_SE)",
    "sw_KE": "Swahili (sw_KE)",
    "ta_IN": "Tamil (ta_IN)",
    "te_IN": "Telugu (te_IN)",
    "th_TH": "Thai (th_TH)",
    "tl_XX": "Tagalog (tl_XX)",
    "uk_UA": "Ukrainian (uk_UA)",
    "ur_PK": "Urdu (ur_PK)",
    "xh_ZA": "Xhosa (xh_ZA)",
    "gl_ES": "Galician (gl_ES)",
    "sl_SI": "Slovenian (sl_SI)"
}

st.title("LinguaConnect: Universal Translator")
st.markdown("Translate text in multiple languages using AI-powered models from Hugging Face!")

text = st.text_area("Enter the text to translate")

source_language = st.selectbox(
    "Select the source language",
     options=list(language_options.values())
)

target_language = st.selectbox(
    "Select the target language",
     options=list(language_options.values())
)

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter some text to translate.")
    else:
        source_lang_code = [k for k, v in language_options.items() if v == source_language][0]
        target_lang_code = [k for k, v in language_options.items() if v == target_language][0]
        with st.spinner("Translating..."):
            translation = translate_text(text, source_lang_code, target_lang_code)
            if translation:
                st.success("Translation successful")
                st.write(translation)

st.sidebar.header("Examples")
st.sidebar.markdown("""
**Try translating:**
- `Hello, how are you?` from `en_XX` (English) to `fr_XX` (French)  
- `Bonjour, comment vas-tu ?` from `fr_XX` (French) to `en_XX` (English)
""")
