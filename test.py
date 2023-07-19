import pdfkit
#import weasyprint


path_to_file = 'trial.html'





options = {
    'margin-top': '0',
    'margin-right': '0',
    'margin-bottom': '0',
    'margin-left': '0'
}

pdfkit.from_file(path_to_file, 'out.pdf', options=options)



# weasyprint.HTML(path_to_file).write_pdf('output.pdf')
