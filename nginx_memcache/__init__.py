VERSION = (0, 1)


def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[1]:
        version = '%s.%s' % (version, VERSION[1])
    return version
