
import subprocess
import sys
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

FILE = Path(__file__).with_name("python_basics.py")
last_run = 0


def run_file():
    global last_run
    last_run = time.time()
    print("=" * 40, flush=True)
    subprocess.run([sys.executable, str(FILE)])


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if Path(event.src_path).resolve() == FILE.resolve():
            global last_run
            if time.time() - last_run > 1:
                time.sleep(0.2)
                run_file()


observer = Observer()
observer.schedule(Handler(), str(FILE.parent), recursive=False)
observer.start()

try:
    run_file()
    while True:
        time.sleep(0.2)
except KeyboardInterrupt:
    observer.stop()

observer.join()
