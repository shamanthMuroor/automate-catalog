#!/usr/bin/env python3
import os
from datetime import date

from reports import generate_report

def pdf_body(desc_dir):
    """Generating a summary with two lists, which gives the output name and weight"""
    res = []
    wt = []
    for item in os.listdir(desc_dir):
      filename=os.path.join(desc_dir,item)
      with open(filename) as f:
        line=f.readlines()
        weight=line[1].strip('\n')
        name=line[0].strip('\n')
        print(name,weight)
        res.append('name: ' +name)
        wt.append('weight: ' +weight)
        print(res)
        print(wt)
    # initializing the object
    new_obj = ""  
    # Calling values from two lists one by one.
    for i in range(len(res)):
        if res[i]:
            new_obj += res[i] + '<br />' + wt[i] + '<br />' + '<br />'
    return new_obj

if __name__=='__main__':
    user = os.getenv('USER')
    # The directory which contains all the files with data in it.
    description_directory = '/home/{}/supplier-data/descriptions/'.format(user)
    # Creating data in format "May 5, 2020"
    current_date = date.today().strftime("%B %d, %Y")
    # Title for the PDF file with the created date
    title = 'Processed Update on ' + str(current_date)  
    # calling the generate_report function 
    generate_report('processed.pdf', title, pdf_body(description_directory))
    # subject line give in assignment for email
    email_subject = 'Upload Completed - Online Fruit Store'
    # body line give in assignment for email
    email_body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    # structuring email and attaching the file. Then sending the email
    msg = generate_email("automation@example.com", "{}@example.com".format(user),
                         email_subject, email_body, "/tmp/processed.pdf")  
    send_email(msg)
