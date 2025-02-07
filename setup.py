from setuptools import setup  # type: ignore

# todo: add/remove/think about this list
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Games/Entertainment",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: pygame",
    "Programming Language :: Python :: 3",
]

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="pymunk",
    url="http://www.pymunk.org",
    author="Victor Blomqvist",
    author_email="vb@viblo.se",
    version="6.5.1",  # remember to change me for new versions!
    description="Pymunk is a easy-to-use pythonic 2d physics library",
    long_description=long_description,
    packages=["pymunk", "pymunk.tests", "pymunk.examples"],
    include_package_data=True,
    license="MIT License",
    classifiers=classifiers,
    python_requires=">=3.6",
    # Require >1.14.0 since that (and older) has problem with returing structs from functions.
    install_requires=["cffi >= 1.15.0"],
    cffi_modules=["pymunk/pymunk_extension_build.py:ffibuilder"],
    extras_require={
        "dev": ["pyglet < 2.0.0", "pygame", "sphinx", "aafigure", "wheel", "matplotlib"]
    },
    test_suite="pymunk.tests",
)
