from googletrans import Translator
import googletrans
translator = Translator()
# out = translator.translate('Can I meet the doctor Now?',dest='hi')
# print(out.text)

responses = {
    'can i see the doctor now?': 'Doctor is available Monday->Friday, 10.00am - 9.00pm. Thankyou!'
}

user_input = input('You: ')
# Detection:
out = translator.detect(user_input)
# print(out.lang)
print('USER data >> ',user_input)
print('DETECTED LANGUAGE IS:',googletrans.LANGUAGES[out.lang])
eng_text= translator.translate(user_input,dest='en').text.lower()
print('TO eng >>: ',eng_text)

if eng_text in responses:
    get_response = responses[eng_text]
    print('AskMe!: ',translator.translate(get_response,dest=out.lang).text)


'''
क्या मैं अब डॉक्टर से मिल सकता हूँ?

res: डॉक्टर उपलब्ध है सोमवार->शुक्रवार, सुबह 10.00 बजे - रात 9.00 बजे। शुक्रिया!
Hindi : Can i see the doctor now?

എനിക്ക് ഇപ്പോൾ ഡോക്ടറെ കാണാൻ കഴിയുമോ?

res: തിങ്കൾ->വെള്ളി, രാവിലെ 10.00 മുതൽ രാത്രി 9.00 വരെ ഡോക്ടറുടെ സേവനം ലഭ്യമാണ്. നന്ദി!
Malayalam : Can i see a doctor now?

'''


# translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')
# for translation in translations:
#     print(translation.origin, ' -> ', translation.text)
