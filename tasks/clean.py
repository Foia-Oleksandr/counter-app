import shutil, os

[shutil.rmtree(p, ignore_errors=True) for p in (
    'build',
    'dist',
    'src/counter_app/ui_gen',
    'src/counter_app/web_view_gen',
    'src/web_viewer/node_modules',
    'src/web_viewer/web_dist',
)]

for p in (
        'src/web_viewer/package-lock.json',
        'src/counter_app/_version.py',
        'counter-app.spec'
):
    if os.path.exists(p):
        os.remove(p)