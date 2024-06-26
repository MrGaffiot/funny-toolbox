from setuptools import setup, find_packages

setup(
    name='ftools',
    version='a0.6',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'opencv-python',
        'pytube',
        'moviepy',
        'flask'
    ],
    entry_points={
        'console_scripts': [
            'ftools = ftools.main:start',
        ],
    },
)