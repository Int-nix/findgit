from setuptools import setup

setup(
    name="gitfind",
    version="1.0.0",
    py_modules=["gitfind"],  # must match your .py file name
    entry_points={
        'console_scripts': [
            'gitfind=gitfind:main',  # command name = gitfind
        ],
    },
    author="Owen Ainslie",
    description="Find all Git repositories on your system easily.",
    python_requires='>=3.7',
)
