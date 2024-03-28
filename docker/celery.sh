#!/bin/bash

cd src

if [[ "${1}" == "celery" ]]; then
  celery --app=message.sendmessage:celery worker -l INFO
elif [[ "${1}" == "flower" ]]; then
  celery --app=message.sendmessage:celery flower
 fi