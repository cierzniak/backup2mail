# Python Backup2Mail online tool

Application to send email with data from other applications (folders). You can set everything in settings and run it with schedule in cron.

### Dependencies
* Bash (on Linux)
* Python

### Tested on
* Python 3.5.2 @ Windows 10
* Python 2.7.9 @ Debian Jessie

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
    * eg Linux path: `/home/user/application/logs`,
    * eg Windows path: `C:\\Users\\user\\application\\logs`,
* `archive` is a prefix name of ZIP archive, whole filename is `prefix_date_time.zip`.

### Execute rights
Allow to execute applicatyion by adding execute right in following steps:

````bash
cd /home/user/Backup
sudo chmod +x ./*.sh
sudo chmod +x ./apps/*.py
````

### Schedule
On Linux powered machine add scheduler using `crontab -e` by adding at the end of file:

````bash
0 1 * * 0 /home/user/Backup/cron.sh
````

which means to do backup every sunday at 1.00 AM.

By the way you can still just use `./apps/Main.py` to execute Backup2Mail.

### TODO
* [ ] BAT script to execute on Windows (same as cron.sh)

### Author
[Paweł Cierzniakowski](mailto:pawel@cierzniakowski.pl)
