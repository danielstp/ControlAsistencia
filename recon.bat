#@echo off

python manage.py migrate djangocms_text_ckeditor
python manage.py migrate filer
python manage.py migrate easy_thumbnails
python manage.py migrate event_rsvp
python manage.py migrate calendarium
python manage.py migrate cms
python manage.py migrate menus
python manage.py migrate djangocms_style
python manage.py migrate djangocms_column
python manage.py migrate djangocms_file
python manage.py migrate djangocms_flash
python manage.py migrate djangocms_googlemap
python manage.py migrate djangocms_inherit
python manage.py migrate djangocms_link
python manage.py migrate djangocms_picture
python manage.py migrate djangocms_teaser
python manage.py migrate djangocms_video
python manage.py migrate reversion
