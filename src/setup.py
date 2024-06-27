from setuptools import setup, find_packages

setup(
    name='fools',
    version='a0.8',
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
    entry_points={
        'console_scripts': [
            'fools = fools.main:start',
            'afools = fools.main:cli'
        ],
    },
)