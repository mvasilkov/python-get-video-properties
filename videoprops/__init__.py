from collections import namedtuple
from functools import lru_cache
import json
from os import access, chmod, R_OK
from os.path import isfile
from pathlib import Path
import platform
from shutil import which
from subprocess import check_output
import sys

_args_quiet = ('-loglevel', 'panic')
_args_print = ('-show_streams', '-print_format', 'json')

P = namedtuple('P', 'title ffprobe_args')

P_VIDEO = P('video', (*_args_quiet, '-select_streams', 'v:0', *_args_print))
P_AUDIO = P('audio', (*_args_quiet, '-select_streams', 'a:0', *_args_print))

binary_dependencies = Path(__file__).parent / 'binary_dependencies'
system = platform.system()


@lru_cache(1)
def which_ffprobe():
    if system == 'Darwin':
        a = str(binary_dependencies / 'ffprobe')
        set_executable(a)  # package built on Windows won't have executable bits set
        return a

    if system == 'Windows':
        return str(binary_dependencies / 'ffprobe.exe')

    ffprobe = which('ffprobe')
    if not ffprobe:
        raise RuntimeError('FFmpeg is not installed')

    return ffprobe


def test_requirements():
    assert sys.version_info.major == 3 and sys.version_info.minor >= 6

    version = check_output([which_ffprobe(), '-version'], encoding='utf-8')
    assert version.startswith('ffprobe version')


def get_stream_properties(movie: str, title: str, ffprobe_args):
    if not isfile(movie) or not access(movie, R_OK):
        raise RuntimeError(f'File not found or inaccessible: {movie}')

    output = check_output([which_ffprobe(), *ffprobe_args, movie], encoding='utf-8')
    props = json.loads(output)

    if 'streams' not in props or not props['streams']:
        raise RuntimeError(f'No usable {title} stream found: {movie}')

    return props['streams'][0]


def get_video_properties(movie: str):
    return get_stream_properties(movie, *P_VIDEO)


def get_audio_properties(movie: str):
    return get_stream_properties(movie, *P_AUDIO)


def pretty_print(a):
    print(json.dumps(a, indent=2))


def noexcept(fun):
    def wrapped(*args, **kwargs):
        try:
            return fun(*args, **kwargs)
        except:
            pass

    return wrapped


@noexcept
def set_executable(a):
    if system != 'Windows':
        chmod(a, 0o755)


def run(getter=get_video_properties):
    test_requirements()

    if len(sys.argv) == 2:
        pretty_print(getter(sys.argv[1]))
    else:
        print(f'Usage: {sys.argv[0]} movie.mp4')


def run2():
    run(getter=get_audio_properties)


if __name__ == '__main__':
    run()
