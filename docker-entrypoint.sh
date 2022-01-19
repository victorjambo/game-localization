#!/bin/sh

set -e
python app.py db upgrade

python app.py run
