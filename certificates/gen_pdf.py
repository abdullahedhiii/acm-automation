import pdfkit 
from html_content import get_html_content
import datetime as dt

config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')  # change path if needed
options = {
    'dpi': 129,                       # scale image to match page width
    'page-width': '8in',              # page width
    'page-height': '5.75in',          # page height
    'margin-top': '0in',              # no margins
    'margin-right': '0in',
    'margin-bottom': '0in',
    'margin-left': '0in',
    'encoding': "UTF-8",              # text encoding
    'enable-local-file-access': None, # allow local images/fonts
    'no-outline': None,               # remove bookmarks
}



def generate(name, comp):
    # date = dt.datetime.now().strftime("%B %d, %Y")
    # img = "design.png"
    html = get_html_content("certificates/pictemp.html", name, comp)
    pdfkit.from_string(html, f"certificates/certificate.pdf", options=options, configuration=config)

generate("Sameer kotwani" , "Competitive Programming")