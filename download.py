# download.py
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

model_name = "facebook/mbart-large-50-many-to-many-mmt"
save_path = "./mbart_local"

print("Downloading tokenizer...")
tokenizer = MBart50TokenizerFast.from_pretrained(model_name)
tokenizer.save_pretrained(save_path)

print("Downloading model...")
model = MBartForConditionalGeneration.from_pretrained(model_name)
model.save_pretrained(save_path)

print("Download complete. Saved to:", save_path)
