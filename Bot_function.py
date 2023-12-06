import translate

def Translate(post,lang):
    translator = translate.Translator(to_lang=lang)
    lang_post =  translator.translate(post)
    return lang_post

