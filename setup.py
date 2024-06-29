from setuptools import setup

setup(
    name="gitvis",
    version="0.1.0",
    description="A CLI made with Python to visualize your Git commits",
    url="https://github.com/aldinash",
    author="Aldinash Seitenov",
    author_email="aldinash.seitenov@gmail.com",
    license="MIT",
    packages=["gitvis"],
    install_requires=[
        "click>=8.1.7",
        "colorama>=0.4.6",
        "gitdb>=4.0.11",
        "GitPython>=3.1.43",
        "smmap>=5.0.1",
        "setuptools>=70.1.1",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",  # Adjust to your chosen license
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities",
    ],
    entry_points={
        "console_scripts": [
            "gitvis=gitvis.__main__:main",
        ],
    },
)
