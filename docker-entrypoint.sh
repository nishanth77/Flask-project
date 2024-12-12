#!/bin/sh

flask db migrate

exec guniorn --bind 0.0.0.0:80 "app:create_app()"