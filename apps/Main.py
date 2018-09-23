#!/usr/bin/env python
# <editor-fold desc="Imports">
import os
import smtplib
import sys
from email import encoders

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sys.path.append(os.path.join(os.path.dirname(__file__), '../functions'))
import other

sys.path.append(os.path.join(os.path.dirname(__file__), '../config'))
import settings

# </editor-fold>
logger = other.start_logger('main')
logger.info('>> Create new mail with backup')
data_folder = './data/'
text = 'Done creating of backup and attach it to this mail.\nList of attached files:\n'
# <editor-fold desc="Zip all data">
folders = other.read_folders()
for id_ in folders:
    filename_ = other.zip_backup(folders[id_]['folder'], data_folder, folders[id_]['archive'])
    text += '* ' + filename_ + '\n'
# </editor-fold>
text += 'Kind regards\nPawel'
# <editor-fold desc="Connect to SMTP server">
logger.info('Connect to SMTP server ' + settings.SMTP_SERV + ':' + str(settings.SMTP_PORT))
smtpserver = smtplib.SMTP(settings.SMTP_SERV, settings.SMTP_PORT)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(settings.SMTP_USER, settings.SMTP_PSWD)
# </editor-fold>
# <editor-fold desc="Send Email with data">
logger.info('Create email to ' + settings.EMAIL_TO)
msg = MIMEMultipart()
msg['Subject'] = '[' + settings.SUBJECT_TOPIC + '] Backup'
msg['From'] = settings.SMTP_USER
msg['To'] = settings.EMAIL_TO
logger.info('Add attachments')
for file_ in other.listdir(data_folder):
    with open(data_folder + file_, "rb") as file__:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file__.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename=" + file_)
        msg.attach(part)
msg.attach(MIMEText(text, 'plain'))
logger.info('Send email')
smtpserver.sendmail(settings.SMTP_USER, [settings.EMAIL_TO], msg.as_string())
smtpserver.quit()
# </editor-fold>
# <editor-fold desc="Remove all files from data folder">
for file in other.listdir(data_folder):
    logger.info('Remove archive ' + file)
    os.remove(data_folder + file)
# </editor-fold>
logger.debug('Done')
