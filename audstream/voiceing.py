import pyaudio
import wave
import time
import threading

from colorama import Fore, Style

class AudStream:
    def __init__(self, name_of_file: str = "output.wav"):
        self.name_of_file = name_of_file
        self.recording = False
        self.thread = None
        
    def _record(self, channels: int, rate: int, record_time: int = None, start_time: int = 0):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=channels, rate=rate, input=True, frames_per_buffer=1024)
        frames = []
        print(Style.BRIGHT + Fore.GREEN + "Recording..." + Style.RESET_ALL + Fore.RESET)
        if record_time is None:
            
            while self.recording:
                data = stream.read(1024)
                frames.append(data)
                
        else:
            current_time = int(time.time())
            while current_time - start_time < record_time:
                data = stream.read(1024)
                frames.append(data)
                current_time = int(time.time())
                
            self.recording = False
            
        with wave.open(self.name_of_file, "wb") as sound_file:
            sound_file.setnchannels(channels)
            sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
            sound_file.setframerate(rate)
            sound_file.writeframes(b"".join(frames))
        
        stream.stop_stream()
        stream.close()
        audio.terminate()
        
    def start_recording(self, channels: int, rate: int, record_time: int = 5):
        if self.thread is not None or self.recording:
            return print(Style.BRIGHT + Fore.RED + "Already recording!" + Style.RESET_ALL + Fore.RESET)
        self.recording = True
        _time = int(time.time())
        self.thread = threading.Thread(target=self._record, args=(channels, rate, record_time, _time))
        self.thread.start()
        
    def stop_recording(self):
        if self.thread is None or not self.recording:
            return print(Style.BRIGHT + Fore.RED + "Not recording!" + Style.RESET_ALL + Fore.RESET)
        
        self.recording = False
        self.thread.join()
        
audio = AudStream()
audio.start_recording(2, 44100, record_time=10)