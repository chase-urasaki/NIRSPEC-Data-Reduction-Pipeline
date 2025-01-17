try:
    import imp

except ImportError: 
    import importlib
    imp = importlib

MODULES = [
    'os',
    'numpy',
    'math',
    'subprocess',
    'fnmatch',
    'logging',
    'pylab',
    'errno',
    'datetime',
    'warnings',
    'astropy',
    'scipy',
    'argparse',
    'statsmodels',
    'PIL',
    'astroscrappy']

missingModules = []


def is_missing():
    for m in MODULES:
        try:
            imp.import_module(m)
        except ImportError:
            missingModules.append(m)

    return missingModules