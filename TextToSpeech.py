import win32com.client as wc
name = ["Aman", "Anurag", "Jishan", "Abhay","Himanshu"]
speaker = wc.Dispatch("SAPI.SpVoice")
for i in name:
    print(f"Hello! {i}")
    speaker.Speak(f"Hello! {i}")


    
