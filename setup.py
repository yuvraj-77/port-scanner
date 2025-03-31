from setuptools import setup, find_packages # type: ignore

setup(
    name="advanced-port-scanner",
    version="1.0.0",
    description="A highly advanced modular port scanner and wireless attack tool",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "nmap",
        "requests",
        "shodan",
        "tk",
    ],
    entry_points={
        "console_scripts": [
            "advportscan=main:main",
        ],
    },
    python_requires='>=3.7',
)
