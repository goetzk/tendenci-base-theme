import subprocess

subprocess.check_call(['python', 'manage.py',  'loaddata', 'themes/tendenci2018/apps/boxes/fixtures/willow-default-boxes.json'])
subprocess.check_call(['python', 'manage.py',  'loaddata', 'themes/tendenci2018/apps/forms-builder/forms/fixtures/willow_default_forms.json'])
subprocess.check_call(['python', 'manage.py',  'loaddata', 'themes/tendenci2018/apps/navs/fixtures/nav.json'])