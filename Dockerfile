# Use Debian base image commonly used python:3.8.2-slim
FROM python:3.8.2-slim

# Keep working directory as /usr/src/app, copy project files there
# then run setup using '3 setup.py install'

# Before installing run unit tests using
# python3 test.py