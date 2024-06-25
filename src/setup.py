from setuptools import setup, find_packages

setup(
    name='ftools',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'opencv-python'
    ],
    entry_points={
        'console_scripts': [
            'ftools = ftools.main:start',
        ],
    },
)