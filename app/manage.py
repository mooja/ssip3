#!/usr/bin/env python
import os
import sys

import environ

if __name__ == '__main__':
    ROOT_DIR = environ.Path(__file__) - 1  # (/a/b/myfile.py - 3 = /)
    env = environ.Env()
    environ.Env.read_env(ROOT_DIR('.env'))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', env('DJANGO_SETTINGS_MODULE'))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
