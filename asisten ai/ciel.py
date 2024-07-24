import speech_recognition as srec
import pyttsx3 as pyt

def perintah():
    mendengar = srec.Recognizer()  # untuk mengambil atribut dari object srec
    with srec.Microphone() as source:  # untuk memasukan suara sebagai perintah
        print("listening.....")
        mendengar.pause_threshold = 0.9
        suara = mendengar.listen(source)
        try:
            print("processing.....")
            layanan = mendengar.recognize_google(suara)
            print(layanan)
        except srec.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            layanan = ""
        except srec.RequestError as e:
            print(f"Could not request results; {e}")
            layanan = ""
        except Exception as e:
            print(f"An error occurred: {e}")
            layanan = ""
        return layanan
    
def run_ciel():
    layanan = perintah()
    if layanan:
        print(f"Command received: {layanan}")
    
run_ciel()
