import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words,tokenize
import googletrans
from googletrans import Translator
translator = Translator()

#Checking for GPU availability
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# Creating Model
with open('intents.json','r') as f:
    intents = json.load(f)

#RETRIEVING FILE DATA
FILE = "data.pth"
data=torch.load(FILE)

input_size =data['input_size']
hidden_size =data['hidden_size']
output_size =data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']

model = NeuralNet(input_size,hidden_size,output_size).to(device)

model.load_state_dict(model_state)
model.eval()

# CHATBOT UI/UX
bot_name = "AskMe :"
print("We care 4 U! Try asking 'about' , 'languages' ")
while True:
    sentence = input('You: ')
    if sentence == 'languages':
        print('We support total of :', len(googletrans.LANGUAGES),' languages')
        for i in googletrans.LANGUAGES:
            print(googletrans.LANGUAGES[i])
    if sentence == "quit":
        break

    # Language detection
    lang_detected = translator.detect(sentence).lang
    sentence = tokenize(translator.translate(sentence,dest='en').text)


    # DEBUGGING
    print('DETECTED LANGUAGE:  ',googletrans.LANGUAGES[lang_detected])


    X=bag_of_words(sentence,all_words)
    X=X.reshape(1,X.shape[0])
    X = torch.from_numpy(X)

    output =model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    # Calculating TAG probability
    probs = torch.softmax(output,dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent['tag']:
                print(f"{bot_name}: {translator.translate(random.choice(intent['responses']),dest=lang_detected).text}")

    else:
        print(f"{bot_name}: Sorry... Can you repeat it?")