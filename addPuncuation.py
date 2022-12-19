from ppasr.utils.text_utils import PunctuationExecutor

filename = "text"
pun_executor = PunctuationExecutor(model_dir='pun_models')
result = ""
with open(filename, "r") as f:
    text = f.read(500)
    while text:
        result += pun_executor(text)
        text = f.read(500)
#print(result)
filename = "text_pun"
with open(filename, "w") as f:
    f.write(result)

