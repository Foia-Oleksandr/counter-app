import shutil, os;

[shutil.rmtree(p, ignore_errors=True) for p in ('build','dist')];
os.remove('counter-app.spec') if os.path.exists('counter-app.spec') else None
