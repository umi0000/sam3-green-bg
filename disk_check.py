import os
import sys
import site
import tempfile
import sysconfig
import subprocess

print("python:", sys.version)
print("sys.prefix:", sys.prefix)
print("temp dir:", tempfile.gettempdir())
print("site-packages:", sysconfig.get_paths().get("purelib"))

try:
    out = subprocess.check_output([sys.executable, "-m", "pip", "cache", "dir"], text=True)
    print("pip cache:", out.strip())
except Exception as e:
    print("pip cache error:", e)

for key in ["TMPDIR", "TEMP", "TMP", "PIP_CACHE_DIR", "XDG_CACHE_HOME", "HF_HOME", "TORCH_HOME"]:
    print(f"{key}={os.environ.get(key)}")