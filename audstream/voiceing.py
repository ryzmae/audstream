# MIT License
#
# Copyright (c) 2023 Ceeq
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pyaudio
import wave
import time
import threading

from colorama import Fore, Style

class AudStreamer:
    def __init__(self, filename: str = "output.mp3"):
        self.filname = filename
        self.recording = False
        self.thread = None
        self.audios = [
            ".aac",
            ".aiff",
            ".flac",
            ".cda",
            ".m4a",
            ".mp3",
            ".ogg",
            ".wav",
            ".wma",
            ".mp4"
        ]
        
        if not self.filname.endswith(tuple(self.audios)):
            print(Style.BRIGHT + Fore.RED + "[WARNING] Invalid file type!" + Style.RESET_ALL + Fore.RESET)
            return SystemExit
        
        
    def _record(self, channels: int, rate: int, record_time: int = None, start_time: int = 0):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=channels, rate=rate, input=True, frames_per_buffer=1024)
        frames = []
        print(Style.BRIGHT + Fore.GREEN + "[AUDSREAMER] Recording..." + Style.RESET_ALL + Fore.RESET)
        
        if record_time is None:
            while self.recording:
                data = stream.read(1024)
                frames.append(data)
                
        else:
            while self.recording and int(time.time()) - start_time < record_time:
                data = stream.read(1024)
                frames.append(data)
                
        stream.stop_stream()
        stream.close()
        audio.terminate()
        
        sound = wave.open(self.filname, "wb")
        sound.setnchannels(channels)
        sound.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound.setframerate(rate)
        sound.writeframes(b"".join(frames))
        sound.close()
        
        
    def start_recording(self, channels: int, rate: int, record_time: int = None, start_time: int = 0):
        if channels > 2:
            print(Style.BRIGHT + Fore.RED + "[WARNING] Channels must be 1 or 2!" + Style.RESET_ALL + Fore.RESET)
            return
        
        elif rate > 38400:
            print(Style.BRIGHT + Fore.RED + "[WARNING] Rate must be 38400 or lower!" + Style.RESET_ALL + Fore.RESET)
            return
        
        elif channels > 2 and rate > 38400:
            print(Style.BRIGHT + Fore.RED + "[WARNING] Channels must be 1 or 2 and rate must be 38400 or lower!" + Style.RESET_ALL + Fore.RESET)
            return
        
        self.recording = True
        self.thread = threading.Thread(target=self._record, args=(
            channels,
            rate,
            record_time,
            time.time()
            ))
        self.thread.start()
        
    def stop_recording(self):
        self.recording = False
        self.thread.join()
        print(Style.BRIGHT + Fore.GREEN + "[AUDSREAMER] Recording stopped!" + Style.RESET_ALL + Fore.RESET)
        
        if self.filname.endswith(tuple(self.audios)):
            print(Style.BRIGHT + Fore.GREEN + f"[AUDSREAMER] File saved as {self.filname}" + Style.RESET_ALL + Fore.RESET)
            return
        
        else:
            print(Style.BRIGHT + Fore.RED + "[WARNING] Cannot save the audio File!" + Style.RESET_ALL + Fore.RESET)
            
            
    def __del__(self):
        if self.recording:
            self.stop_recording()