# <editor-fold desc="Imports">
import json
import logging
import os
import sys
from contextlib import closing
from datetime import datetime
from zipfile import ZIP_DEFLATED
from zipfile import ZipFile

sys.path.append(os.path.join(os.path.dirname(__file__), '../config'))


# </editor-fold>
# <editor-fold desc="Start logger service">
def start_logger(filename=''):
    log = logging.getLogger('main')
    log.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s | %(levelname)-5.5s | %(message)s', '%Y-%m-%d %H:%M:%S')
    if filename:
        handler = logging.FileHandler(os.path.join(os.path.dirname(__file__), '../logs/' + filename + '.log'))
        handler.setFormatter(formatter)
        log.addHandler(handler)
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        log.addHandler(handler)
    return log


logger = start_logger()


# </editor-fold>
# <editor-fold desc="Read settings from config/folder.json file (folders to backup)">
def read_folders():
    try:
        with open(os.path.join(os.path.dirname(__file__), '../config/folders.json')) as file:
            data = json.load(file)
    except FileNotFoundError:
        logger.critical('Settings (folders.json) not reader, error with file')
        data = {}
    return data


# </editor-fold>
# <editor-fold desc="List all files in selected directory without UNIX hidden (starting with dot)">
def listdir(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f


# </editor-fold>
# <editor-fold desc="Create ZIP archive of folder with all subfolders recursively">
def zip_backup(folder_backup, folder_temp, zip_file):
    assert os.path.isdir(folder_backup)
    filename = zip_file + '_' + str(datetime.now().strftime('%Y-%m-%d_%H-%M')) + '.zip'
    logger.info('Create archive ' + filename + ' from folder ' + folder_backup)
    with closing(ZipFile(folder_temp + filename, 'w', ZIP_DEFLATED)) as z:
        for root, dirs, files in os.walk(folder_backup):
            for fn in files:
                absfn = os.path.join(root, fn)
                zfn = absfn[len(folder_backup) + len(os.sep):]
                z.write(absfn, zfn)
    return filename

# </editor-fold>
