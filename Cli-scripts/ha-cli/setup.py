from setuptools import setup, find_packages

setup(
    name='ha',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ha = ha.__main__:main',
        ],
    },
    install_requires=[
        'PyYAML',
    ],
    author='Your Name',
    description='A simple Home Assistant YAML script generator CLI.',
    url='https://github.com/yourusername/ha-cli',
    python_requires='>=3.6',
)
