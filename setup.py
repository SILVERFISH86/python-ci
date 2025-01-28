from setuptools import setup, find_packages

setup(
    name="my-python-app",  # Replace with your package name
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A brief description of your Python project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/my-python-app",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests",  # List your dependencies here
        "numpy"
    ],
    entry_points={
        "console_scripts": [
            "my-app=my_module.main:main",  # Replace with your actual module and entry function
        ],
    },
)
