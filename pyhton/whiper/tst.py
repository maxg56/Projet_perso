import whisper  
import pyaudio
import wave
import keyboard

# Définir les paramètres d'enregistrement
FORMAT = pyaudio.paInt16  # Format du son (16-bit PCM)
CHANNELS = 1  # Nombre de canaux audio (mono)
RATE = 44100  # Taux d'échantillonnage en Hz (standard CD quality)
CHUNK = 1024  # Nombre d'échantillons par trame

# Nom du fichier de sortie MP3
output_file = "audio.mp3"

def enregistrer_audio():
    # Initialiser PyAudio
    audio = pyaudio.PyAudio()

    # Ouvrir un flux audio en lecture (input)
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print("Enregistrement en cours... Appuyez sur 'Ctrl + C' pour arrêter.")

    frames = []

    try:
        while True:
            # Lire les données audio du flux
            data = stream.read(CHUNK)
            frames.append(data)

            # Vérifier si la touche 'q' est enfoncée pour arrêter l'enregistrement
            if keyboard.is_pressed('q'):
                break
    except KeyboardInterrupt:
        pass

    print("Enregistrement terminé.")

    # Arrêter le flux audio
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Écrire les données audio dans un fichier WAV
    with wave.open(output_file, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"Le fichier {output_file} a été enregistré avec succès.")

if __name__ == "__main__":
    enregistrer_audio()
"""
model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])
"""