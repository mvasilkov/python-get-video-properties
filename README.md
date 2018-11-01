python-get-video-properties
===

Get video properties

Installation
---

```sh
pip install -U get-video-properties
```

Usage
---

```python
from videoprops import get_video_properties

props = get_video_properties('movie.mp4')

print(f'''
Codec: {props['codec_name']}
Resolution: {props['width']}×{props['height']}
Aspect ratio: {props['display_aspect_ratio']}
Frame rate: {props['avg_frame_rate']}
''')
```

**Sample output**

```text
Codec: h264
Resolution: 1920×1080
Aspect ratio: 16:9
Frame rate: 25/1
```

Usage (audio)
---

```python
from videoprops import get_audio_properties

props = get_audio_properties('movie.mp4')

print(f'''
Codec: {props['codec_name']}
Channels: {props['channels']}
Sample rate: {props['sample_rate']}
''')
```

**Sample output**

```text
Codec: opus
Channels: 2
Sample rate: 48000
```

Command-line usage
---

```sh
videoprops movie.mp4
audioprops movie.mp4
```
