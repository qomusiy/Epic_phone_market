from django import forms
from .models import Phone

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'

    def clean_maker(self):
        maker = self.cleaned_data.get('maker')
        if len(maker) < 3:
            raise forms.ValidationError("Makerni to'g'ri kirit")
        return maker
    
    def clean_year(self):
        year = self.cleaned_data.get('year')
        if year < 2000:
            raise forms.ValidationError("Yili 2000 dan kichik bo'lmasin!!")
        return year
    
    def clean_color(self):
        c = self.cleaned_data.get('color')
        if c not in ['Black', 'Blue', 'Yellow', 'Red', 'Pink', 'Gold', 'Silver', 'Green', 'Grey', 'Purple']:
            raise forms.ValidationError("Rang quydagilardan biri bo'lishi kerak 'Black', 'Blue', 'Yellow', 'Red', 'Pink', 'Gold', 'Silver', 'Green', 'Grey', 'Purple'")
        return c
    
    def clean_description(self):
        c = self.cleaned_data.get('description')
        if c in ['hell', 'shit']:
            raise forms.ValidationError("So'kinish mumkin emas!!")
        return c
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:  # 5MB in bytes
                raise forms.ValidationError("Rasm hajmi 5MB dan kam bo'lishi kerak!")
        return image



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Ismini to'ri kirit")
        return name