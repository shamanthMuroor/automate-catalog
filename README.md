# Automate updating catalog information
> Python script that will process the images and descriptions and then update your company's online website to add the new products.
> This was done for a coursera project 

## Summarize:

- A script that summarizes and processes sales data into different categories
- reports.py file generates a PDF report using Python
- Automatically send a PDF report by email
- health_script.py script to check the health status of the system and send an email if something goes wrong

## What does changeImage.py do?
 - It processes the images 
 - Size: Change image resolution to 600x400 pixel
 - Format: Change image format to .JPEG
 
## What does supplier_image_upload.py do?
 supplier_image_upload.py that takes the jpeg images from the specified directory that you've processed previously and uploads them to the web server catalog.
 
## What does reports.py do?
 Generates pdf report with the passed filename, title and body of pdf
 
## What does emails.py do?
 - Generates email format with the passed sender, recipient, subject, body and attachment
 - Sends the message with send_message function with message as the parameter
 
## What does report_email.py do?
  This is the file where the calls to other functions are made. Report is generated and an email is sent to the person!
 
