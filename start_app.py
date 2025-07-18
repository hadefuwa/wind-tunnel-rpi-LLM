import subprocess
import sys
import time

# Start Streamlit with automated responses
process = subprocess.Popen([
    sys.executable, "-m", "streamlit", "run", "app.py"
], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Send empty line to skip email prompt
process.stdin.write("\n")
process.stdin.flush()

print("Starting Streamlit app...")
print("App should be available at http://localhost:8501")

# Keep the process running
try:
    process.wait()
except KeyboardInterrupt:
    process.terminate()
    print("\nApp stopped.")
