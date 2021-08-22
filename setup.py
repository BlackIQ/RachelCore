from setuptools import find_packages, setup

# def parse_requirements(filename):
#     """ load requirements from a pip requirements file """
#     lineiter = (line.strip() for line in open(filename))
#     return [line for line in lineiter if line and not line.startswith("#")]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='RachelCore',
    packages=find_packages(),
    version='0.0.12',
    author='Amirhossein Mohammadi',
    license='MIT',
    author_email="amirhosseinmohammadi1380@yahoo.com",
    description="Rachel assistant core.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BlackIQ/RachelCore",
    install_requires=[
        "requests",
        "googlesearch-python"
    ]
)
