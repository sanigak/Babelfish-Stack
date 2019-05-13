from googletrans import Translator

translator = Translator()

ans = translator.translate('how are you doing', src='en', dest = 'de')

print(ans.text)