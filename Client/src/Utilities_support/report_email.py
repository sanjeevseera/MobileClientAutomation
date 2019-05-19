import os
import configparser
import glob
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
#from email.Utils import COMMASPACE, formatdate
from email import encoders

def email_reporter(html_report_dir):
    list_of_files = glob.glob(html_report_dir+"*.html")  # * means all if need specific format then *.html
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    config_path = "email_report.cfg"

    if not os.path.isfile(config_path):
        return "email_report.cfg, not exist in this path, reports can not be sent in mail"
    else:
        conf_data = configparser.ConfigParser()
        conf_data.read(config_path)
        conf_data_dict = {}
        for i, conf in enumerate(conf_data.sections()):
            if not ( i == 0 and conf.lower() == "configs"):
                return "configs are not provides"
            else:
                for item in conf_data.items(conf):
                    conf_data_dict[item[0]] = item[1]
                if not "sender_email" in conf_data_dict.keys():
                    return "sender_email is not configured, reports can not be sent in mail"
                elif not "sender_pass" in conf_data_dict.keys():
                    return "sender_pass is not configured, reports can not be sent in mail"
                elif not "send_to" in conf_data_dict.keys():
                    return "send_to is not configured, reports can not be sent in mail"
                elif not "subject" in conf_data_dict.keys():
                    return "subject is not configured, reports can not be sent in mail"
                else:
                    send_from = conf_data_dict["sender_email"]
                    PASSWORD = conf_data_dict["sender_pass"]
                    send_to = conf_data_dict["send_to"].split(',')
                    subject = conf_data_dict["subject"]
                    '''
                    send_from = "sanjeev.seera@gmail.com"
                    PASSWORD = "Sveejnas#5"
                    send_to = ["sanjeev.seera@gmail.com"]
                    #send_to = ["anil.punichithaya@gmail.com", "sriram.g.n@gmail.com", "sanjeev.seera@gmail.com", "sireesha.mulakala@gmail.com"]
                    subject = "Rakuten Client Automation Test Report"
                    '''
                    text = "{:*^50s}\n".format("EXECUTION STATUS")
                    server = "smtp-mail.outlook.com"
                    port = 587


                    msg = MIMEMultipart()
                    msg['From'] = send_from
                    msg['To'] = ", ".join(send_to)
                    msg['Subject'] = subject
                    with open(latest_file, "r") as data:
                        for s in data.readlines():
                            if "Status:" in s:
                                s = s.rstrip().split("</strong>")[-1][:-4]
                                sdict = {}
                                total_cases = 0
                                report_test = ""
                                for x in s.split(','):
                                    #report_test += "{0:*<25}: {1}\n".format(str(x.split(":")[0].strip()).upper(), str(x.split(":")[1].strip()))
                                    report_test += "{0}\t\t : {1}\n".format(str(x.split(":")[0].strip()).upper(), str(x.split(":")[1].strip()))
                                    sdict[x.split(":")[0].strip()] = x.split(":")[1].strip()
                                    total_cases += int(x.split(":")[1].strip())

                                if 'Pass' in sdict.keys() and total_cases == int(sdict['Pass']):
                                    text += "\nSTATUS: PASS\n\n"
                                else:
                                    text += "\nSTATUS: FAIL\n\n"
                                #text += "{0:*<25}: {1}\n".format("Total Test Cases", str(total_cases))
                                text += "{0} : {1}\n".format("Total Test Cases", str(total_cases))
                                text += report_test
                                #text += s
                                text += "\n\n{:*^50s}\n".format("EXECUTION STATUS")
                                text += "\nDetailed Report is Available in Attached HTML file"
                                break
                    print(text)
                    msg.attach(MIMEText(text))
                    with open(latest_file, "rb") as data:
                        part = MIMEBase('application', "octet-stream")
                        part.set_payload(data.read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(latest_file))
                        msg.attach(part)

                    smtp = smtplib.SMTP(server, port)
                    smtp.starttls()
                    smtp.login(send_from, PASSWORD)
                    smtp.sendmail(send_from, send_to, msg.as_string())
                    smtp.close()
        return "Report generated Successfully!!!"
