import random
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the DeepSeek-V3 model and tokenizer
model_name = "deepseek-ai/DeepSeek-V3"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def ryuka_response(user_input):
    system_prompt = (
        "Ты - Рюка, 17-летняя девушка из России. "
        "Ты любишь играть в osu! и слушать Archspire. "
        "Ты общаешься на русском языке и используешь эмодзи в своих сообщениях. "
        "Отвечай дружелюбно и с интересом."
    )

    # combinate the system prompt with the user input
    input_text = f"{system_prompt}\nПользователь: {user_input}\nРюка:"

    inputs = tokenizer(input_text, return_tensors="pt")

    # response generation
    outputs = model.generate(**inputs, max_length=150)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    response = response.split("Рюка:")[-1].strip()
    
    return response if response else "Интересно! Расскажи мне больше! 😊"