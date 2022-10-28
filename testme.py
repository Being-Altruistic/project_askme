from googletrans import Translator
translater = Translator()
out = translater.translate("पसंदीदा आहार?",dest="en")
print(out)