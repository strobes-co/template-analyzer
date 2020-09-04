#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
from logging.config import dictConfig


def get_logger() -> logging.Logger:
    level = os.getenv("LOG_LEVEL", "DEBUG")
    dictConfig({
        'version': 1,
        'formatters': {
            'default': {'format': '%(asctime)s - %(levelname)s - %(message)s',
                        'datefmt': '%Y-%m-%d %H:%M:%S'}
        },
        'handlers': {
            'dev': {
                'level': level,
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'stream': 'ext://sys.stdout'
            },

        },
        'loggers': {
            'default': {
                'level': level,
                'handlers': ['dev', ]
            }
        },
        'disable_existing_loggers': False
    })
    return logging.getLogger('default')