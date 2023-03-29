from hezar import build_model, Model, Tokenizer


path = "hezarai/bert-base-fa"
tokenizer = Tokenizer.load(path)
text = tokenizer(["hello guys"], return_tensors="pt")

model = build_model("bert_lm")
outputs = model.predict(text, output_attentions=True, output_hidden_states=True)
print(outputs)

model = Model.load(path)
outputs = model.predict(text, output_attentions=True, output_hidden_states=True)
print(outputs)
