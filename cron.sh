#!/usr/bin/env bash

if [[ $1 == "-h" ]] ; then
    echo "Cron script to automatically create backup of selected folders"
    echo "Remember to have execute rights on all files (check README.md)"
    echo ""
    echo "Usage:"
    echo "$0     | execute backup and send email"
    echo "$0  -h | show help"
fi
if [[ $# == 0 ]] ; then
    APP_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    cd ${APP_DIR}
    ./apps/Main.py
fi