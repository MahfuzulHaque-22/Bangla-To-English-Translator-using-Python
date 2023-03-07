from googletrans import Translator

# Initialize the translator
translator = Translator(service_urls=['translate.google.com'])

# Define the Bangla sentence to translate
bangla_text = 'আমি বাংলায় কথা বলতে পারি'

# Detect the language of the input text
lang = translator.detect(bangla_text).lang

# If the detected language is not English, translate the text
if lang != 'en':
    translation = translator.translate(bangla_text, src=lang, dest='en')
    english_text = translation.text
else:
    english_text = bangla_text

# Print the translated text
print('Bangla Text: ', bangla_text)
print('English Text: ', english_text)
