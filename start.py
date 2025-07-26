# start.py
import threading
import subprocess
import uvicorn

def run_fastapi():
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=False)

def run_chainlit():
    subprocess.run(["chainlit", "run", "chatbot/chainlit_app.py", "--host", "0.0.0.0", "--port", "8000"])

if __name__ == "__main__":
    t1 = threading.Thread(target=run_fastapi)
    t2 = threading.Thread(target=run_chainlit)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
