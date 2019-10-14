from setuptools import setup, find_packages


setup(
    name="cli-context",
    version="0.1.0",
    description="Hierarchical CLI creator",
    long_description="".join([
        "Library which supports CLI contexts for action hierarchies",
    ]),
    url="https://github.com/darkclouder/cli-context",
    author="darkclouder",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries",
    ],
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
)
