from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='radiofrance_api',
    packages=find_packages(include=['radiofrance_api']),
    version='0.0.0',
    author='jcoin',
    license='MIT',
    description='API for OpenAPI Radiofrance',
    url="https://github.com/jcoin/radiofrance-api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires=">=3.7",
    project_urls={
        'Documentation': 'https://developers.radiofrance.fr/',
        'Source': 'https://github.com/jcoin/radiofrance-api',
    },
)