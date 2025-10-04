import imgkit 
from html_content import get_image_content
import datetime as dt

config = imgkit.config(wkhtmltoimage=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe")
options = {
        "enable-local-file-access": ""
}

def generate(name, position, team):
    date = dt.datetime.now().strftime("%B %d, %Y")
    img = "C:/Users/ABC/Documents/acm-automation/images/letterhead.png"
    html = get_image_content(name, position, team, date, img)
    imgkit.from_string(html, "./images/final.png", config=config, options=options)

generate("Zain Khan", "Head", "Event Management")