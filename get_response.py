from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
torch.manual_seed(0)

path = 'openbmb/MiniCPM-2B-dpo-fp16'
tokenizer = AutoTokenizer.from_pretrained(path)
model = AutoModelForCausalLM.from_pretrained(path, torch_dtype=torch.float16, device_map='cuda', trust_remote_code=True)

def get_response(text) -> str:
    response, _ = model.chat(tokenizer, text, temperature=0.5, top_p=0.95, repetition_penalty=1.02)
    return response