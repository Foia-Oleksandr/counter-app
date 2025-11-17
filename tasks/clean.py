import shutil, os

[shutil.rmtree(p, ignore_errors=True) for p in (
    'build',
    'dist',
    'src/counter_app/ui_gen')]

os.remove('counter-app.spec') if os.path.exists('counter-app.spec') else None
