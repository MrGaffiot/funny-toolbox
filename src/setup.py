from setuptools import setup, find_packages

setup(
    name='ftools',
    version='a0.4',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'opencv-python',
        'pytube'
    ],
    entry_points={
        'console_scripts': [
            'ftools = ftools.main:start',
        ],
    },
)