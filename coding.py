import subprocess
import webbrowser
app = ["code", "konsole", "telegram-desktop"]
for i in range(0,3):
    try:
        subprocess.Popen([app[i]])
        print(f"Opening {app[i]}...")
    except FileNotFoundError:
        print(f"Application '{app[i]}' not found!")
webbrowser.open("https://chatgpt.com/", )
webbrowser.open("https://youtube.com/")