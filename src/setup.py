from setuptools import setup, find_packages

DESCRIPTION = 'An app with some funny scripts.'

setup(
    name='fools',
    version='1.12',
    author="walper",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'opencv-python',
        'pytube',
        'moviepy',
        'flask',
        'pillow',
        'moviepy'
    ],
    keywords=[
        "toolsbox",
        "tools",
        "youtube",
        "download",
        "meme",
        "walper"
    ],
    entry_points={
        'console_scripts': [
            'fools = fools.main:start',
            'afools = fools.main:cli'
        ],
    },
)