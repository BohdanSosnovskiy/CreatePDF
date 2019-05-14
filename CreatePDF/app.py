import requests
import cairosvg
from flask import Flask, Response, request, render_template
from bs4 import BeautifulSoup
from weasyprint import HTML, CSS

APP = Flask(__name__)

WSGI_APP = APP.wsgi_app
LINK = 'https://www.work-nest.com/jobs/'

@APP.route('/')
def index():
    return "Hello World!"

@APP.route('/new', methods=['GET', 'POST'])
def new_page():
    return render_template('index.html')

@APP.route('/create_pdf')
def create_pdf(): 
    html = Parse()
    cairosvg.svg2pdf(url='E:\graduatecap.svg', write_to='E:\image.pdf')
    HTML(string=html).write_pdf('E:\weasyprint-website.pdf')
    return html

def Parse():
    r = requests.get(LINK)
    soup = BeautifulSoup(r.text, 'html.parser')
    result = ''
    elements = soup.find_all('section', class_='opening-section-2')
    for element in elements:
        result = result + str(element)

    return result

if __name__ == '__main__':
    APP.run()
