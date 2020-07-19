from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(file, title, add_info):
    report = SimpleDocTemplate(file)
    styles = getSampleStyleSheet()    
    report_title = Paragraph(title, styles['h1'])
    report_body = Paragraph(add_info, styles['BodyText'])
    space = Spacer(1,10)

    report.build([report_title, space, report_body, space])
    print("Report successful")

#generate_report('processed.pdf', 'Report', 'Testing')
