from time import sleep

from django.shortcuts import render
from .forms import ImageForm, HexForm

from PIL import Image, ImageColor


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        form_count = HexForm(request.POST, request.FILES)
        if form_count.is_valid() and form.is_valid():
            hex_number = '#' + form_count.cleaned_data['hex_number']
            form.save()
            img_obj = form.instance
            image = img_obj.image.url[1:]
            res = get_search_count_of_color(image, hex_number)
            return render(request, 'index.html', {'form': form, 'form_count': form_count,
                                                  'img_obj': img_obj, 'res': res})

        elif form.is_valid():
            form.save()
            img_obj = form.instance
            image = img_obj.image.url[1:]
            res = ger_count_of_color(image)
            return render(request, 'index.html', {'form': form, 'form_count': form_count,
                                                  'img_obj': img_obj, 'res': res})
    else:
        form = ImageForm()
        form_count = HexForm()
    return render(request, 'index.html', {'form': form, 'form_count': form_count})


def open_img(img_url):
    img = Image.open(img_url)
    img = img.convert("RGB")
    return img


def ger_count_of_color(image):
    image = open_img(image)

    black_color = (0, 0, 0)
    white_color = (255, 255, 255)

    black = 0
    white = 0

    for pixel in image.getdata():
        if pixel == black_color:
            black += 1
        elif pixel == white_color:
            white += 1
    if white > black:
        return 'На изображении больше белых пикселей'
    else:
        return 'На изображении больше черных пикселей'


def get_search_count_of_color(image, search_color_hex):
    image = open_img(image)
    search_color_rgb = ImageColor.getcolor(search_color_hex, "RGB")
    color_count = 0

    for pixel in image.getdata():
        if pixel == search_color_rgb:
            color_count += 1

    return f'На изображении {color_count} пикселей цвета {search_color_rgb}(RGB) / {search_color_hex}(HEX)'
