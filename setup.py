from setuptools import setup, find_packages

setup(
    name="diabetes_tracker",
    version="0.1.0",
    description="A CLI tool to log and visualize blood sugar and insulin data.",
    author="Aimen Aberra",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "tabulate",
        "plotext"
    ],
    entry_points={
        "console_scripts": [
            "diabetes-tracker=diabetes_cli.main:main"
        ]
    },
    python_requires=">=3.7",
)