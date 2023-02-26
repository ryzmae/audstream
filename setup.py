from setuptools import setup, find_packages

setup(
    name="audstream",
    description="A simple audio streamer for Python",
    libraries=["audstream", "wave", "pyaudio", "colorama"],
    version="0.0.1",
    py_modules=["audstream"],
    
)