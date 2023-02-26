# What is AudStream?

**AudStream is a simple audio streaming server written in Python.**

## Features

* **Simple** - AudStream is a simple audio streaming server written in Python. It is designed to be easy to use and easy to understand.

* **Lightweight** - AudStream is a lightweight audio streaming server written in Python. It is designed to be easy to use and easy to understand.

* **Cross-platform** - AudStream is a cross-platform audio streaming server written in Python. It is designed to be easy to use and easy to understand.

* **Open source** - AudStream is an open source audio streaming server written in Python. It is designed to be easy to use and easy to understand.

* **Free** - AudStream is a free audio streaming server written in Python. It is designed to be easy to use and easy to understand.

## Installation

### Requirements

* Python 3.6 or higher

### MacOS/Linux

```sh
pip3 install audstream
```

### Windows

```sh
pip install audstream
```

## Example Usage

```py
from audstream import AudStreamer

audio = AudStreamer(channels=1, rate=44100, record_time=10)

audio.start_recording()
```