import sys, importlib
if 'ntml.app' not in sys.modules.keys():
    from uikit.app import dp
else:
    dp = importlib.reload(sys.modules['uikit.app']).dp
