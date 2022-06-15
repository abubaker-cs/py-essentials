#!/usr/bin/env python3
# Shebang Line: For UNIX Based Systems
import platform

version = platform.python_version()


def message():
    print('This is python version {}'.format(version))


def main():
    message()


if __name__ != '__main__':
    pass
else:
    main()
