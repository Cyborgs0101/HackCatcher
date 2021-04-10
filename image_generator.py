from PIL import Image, ImageFont, ImageDraw

def Pil(event_name,start_date,n):
    my_image = Image.open("Imagename.ext")
    title_font = ImageFont.truetype('arial.ttf', 50)

    Event_name = event_name
    Start_date = start_date
    image_editable = ImageDraw.Draw(my_image)

    image_editable.text((100,100), Event_name, (237, 230, 211), font=title_font)
    image_editable.text((100,25), Start_date, (237, 230, 211), font=title_font)
    name = "HackerEarth_" + str(n) +".jpg"
    my_image.save(name)
