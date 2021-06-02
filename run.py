import os
import sys

migrations_list = ['makemigrations', 'migrate']

def handle_settings(debug):
    settings_file = 'main.settings'
    if not os.environ.get('DJANGO_SETTINGS_MODULE'):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_file)
    else:
        temp = os.environ.pop('DJANGO_SETTINGS_MODULE')
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_file)

def main(argument=None, debug=False):
    handle_settings(debug)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    if not argument:
        argument = sys.argv
    execute_from_command_line(argument)

def run(Flag, cmd_lis=None, **kwargs):
    if Flag:
        # with migration_handling
        return handle_migrations(cmd_lis, **kwargs)
    if cmd_lis:
        command = ['manage.py']
        sync = kwargs.pop('syncdb', False)
        if sync and cmd_lis[0] == 'migrate':
            cmd_lis += ['--run-syncdb']
        command += cmd_lis
    else:
        command = None
    main(command, **kwargs)


def handle_migrations(cmd_lis, **kwargs):
    global migrations_list
    if len(cmd_lis) < 1:
        raise ValueError("Missing commands in command list")
    for _cmd in migrations_list:
        run(False, [_cmd], **kwargs)
    run(False, cmd_lis, **kwargs)


if __name__ == '__main__':
    # _debug = False
    _debug = True
    # _handle_migrations = False
    _handle_migrations = True
    _run_syncdb = False

    # cmd = ['check']

    # cmd = ['collectstatic']
    # cmd = ['shell']  # !!!> change to emulate terminal
    # cmd = ['startapp', 'Comment']  # ['startapp', 'name-of-app']

    # cmd = ['flush']
    # cmd = ['createsuperuser']  # !!!> change to emulate terminal
    cmd = ['runserver']
    if _debug:
        if _run_syncdb:
            run(_handle_migrations, cmd, debug=_debug, syncdb=_run_syncdb)  # to run a single command
        else:
            run(_handle_migrations, cmd, debug=_debug)  # to run a single command
    else:
        run(_handle_migrations, cmd)