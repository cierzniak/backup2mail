# Python Backup2Mail online tool

Application to send email with data from other applications (folders). You can set everything in settings and run it with schedule in cron.

### Dependencies
* Python

### Configuration
Copy file `config/settings.ini.py` to `config/settings.py` and edit to fit your settings:

````python
# Email recipient
EMAIL_TO = 'user@example.com'

# Subject topic eg. Machine name
SUBJECT_TOPIC = 'Server'

# SMTP server
SMTP_SERV = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USER = 'user@gmail.com'
SMTP_PSWD = 'super_secret_password'
````

* `EMAIL_TO` is recipient email,
* `SUBJECT_TOPIC` is prefix of subject, eg. [Server] Backup,
* `SMTP_(...)` are settings of SMTP server like address, port, user and password.

Copy file `config/folders.ini.json` to `config/folders.json` and edit to fir your backup folders:

````json
{
  "1": {
    "folder": "/var/log",
    "archive": "system_logs"
  },
  "2": {
    "folder": "/boot",
    "archive": "boot"
  }
}
````

* `folder` points to **full** folder path and will be packed recursively with subfolders,
* `archive` is a prefix name of ZIP archive, whole filename is `prefix_date_time.zip`.

### Chmod
Allow to execute files:

````bash
cd /root/Backup
sudo chmod +x ./*.sh
sudo chmod +x ./apps/*.py
````

### Crontabź

````bash
0 1 * * 0 /root/Backup/cron.sh
````

which means to do backup every sunday at 1.00 AM
