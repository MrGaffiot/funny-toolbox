from setuptools import setup

setup(
    name='ftools',
    version='a0.1',
    py_modules=['ftools'],
    install_requires=[
        'Click',
        'cv2'
    ],
    entry_points={
        'console_scripts': [
            'ftools = main:start',
        ],
    },
)