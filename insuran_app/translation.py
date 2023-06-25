from modeltranslation.translator import register, TranslationOptions
from insuran_app.models import *


@register(Sugurta)
class SugurtaTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
