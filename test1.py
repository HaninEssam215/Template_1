import pdfkit
import base64

path_to_file = 'trial.html'

# Open the HTML file in read mode
with open(path_to_file, 'r') as file:
    # Read the contents of the file
    html_content = file.read()

# Read the image file and encode it as base64
with open('Namnlos.png', 'rb') as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

# Replace the "{{ encoded_image }}" placeholder in the HTML content with the actual base64-encoded image data
html_content = html_content.replace("{{ encoded_image }}", f"data:image/png;base64,{encoded_image}")

# Write the modified HTML content to a new HTML file
modified_html_file = 'modified_trial.html'
with open(modified_html_file, 'w') as file:
    file.write(html_content)


options = {
    'margin-top': '0',
    'margin-right': '0',
    'margin-bottom': '0',
    'margin-left': '0'
}

# Convert the modified HTML file to PDF using pdfkit
output_pdf = 'output.pdf'
pdfkit.from_file(modified_html_file, output_pdf, options=options)
