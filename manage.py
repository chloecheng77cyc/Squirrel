#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import pandas as pd

def main():
    cmd, path = sys.argv[1], sys.argv[2]
    if cmd == 'import_squirrel_data':
        df = pd.read_csv(path)
    elif cmd == 'export_squirrel_data':
        df.to_csv(path)
    else:
        raise Exception("Error: Unrecognized Command: {}".format(cmd))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'squirrel.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
