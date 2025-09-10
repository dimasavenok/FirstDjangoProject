from django import forms

from catalog.models import Product

BANNED_WORDS = [
    "казино", "криптовалюта", "крипта", "биржа",
    "дешево", "бесплатно", "обман", "полиция", "радар"
]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category", "status", "price", "image"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})

    def clean_name(self):
        name = self.cleaned_data.get("name", "").lower()
        for word in BANNED_WORDS:
            if word.lower() in name:
                raise forms.ValidationError(f"Слово '{word}' - запрещено")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", "").lower()
        for word in BANNED_WORDS:
            if word.lower() in description:
                raise forms.ValidationError(f"Слово '{word}' - запрещено")
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price and price < 0:
            raise forms.ValidationError("Цена продукта не может быть отрицательной")
        return  price

    def clean_image(self):
        image = self.cleaned_data.get("image")
        try:
            if image:
                if image.size > 5*1024*1024:
                    raise forms.ValidationError("Фото не должно превышать 5мб")
                if not image.content_type in ["image/png", "image/jpeg"]:
                    raise forms.ValidationError("Допустимые форматы: jpeg/png")
            return image
        except Exception:
            pass


