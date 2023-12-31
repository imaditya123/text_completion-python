import torch
from pytorch_transformers import GPT2Tokenizer, GPT2LMHeadModel

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

def token_tensor(text, model):

    indexed_tokens = tokenizer.encode(text)
    tokens_tensor = torch.tensor([indexed_tokens])
    model.eval()

    tokens_tensor = tokens_tensor.to(device)
    model.to(device)

    with torch.no_grad():
        outputs = model(tokens_tensor)
        predictions = outputs[0]

    predicted_index = torch.argmax(predictions[0, -1, :]).item()
    predicted_text = tokenizer.decode(indexed_tokens + [predicted_index])

    return predicted_text

def predict(text):
    a = []
    for i in range(10):
        a.append(token_tensor(text, model))
        text = a[i]
    return a[9].strip()




