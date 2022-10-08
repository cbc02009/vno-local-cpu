from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

import json

from fairseq.models.transformer import TransformerModel

ja2en = TransformerModel.from_pretrained(
    './fairseq/japaneseModel/',
    checkpoint_file='big.pretrain.pt',
    source_lang = "ja",
    target_lang = "en",
    bpe='sentencepiece',
    sentencepiece_model='./fairseq/spmModels/spm.ja.nopretok.model',
    # is_gpu=True
)

# ja2en.cuda()

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods = ['POST'])
@cross_origin()

def sendImage():
    data = request.get_json()
    message = data.get("message")
    content = data.get("content")

    print("this content", content)

    if (message == "translate sentences"):
        result = ja2en.translate(content)
        print(f"translation result is {result}")
        return json.dumps(result)

    if (message == "close server"):
        shutdown_server()

    # return json.dumps(content)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=14366)



# from fairseq.models.transformer import TransformerModel

# driveLocation = "/content/gdrive/MyDrive/OCR/pairseq_training/models/ja_en/base_pretrained_big"

# ja2en = TransformerModel.from_pretrained(
#     './japaneseModel/',
#     checkpoint_file='big.pretrain.pt',
#     data_name_or_path='./',
#     bpe='sentencepiece',
#     sentencepiece_model='./japaneseModel/spm.ja.nopretok.model',
# )

# ja2en.cuda()

# print(ja2en.translate("すみません"))

# japaneseFile = open("./cloverpoint.txt", "r", encoding="utf8")

# listOfJapaneseLines = []

# for line in japaneseFile:
#   listOfJapaneseLines.append(line)

# for index, line in enumerate(listOfJapaneseLines):
#   ja2en.translate(line)
#   print(index)
