import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

with open('./requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="traffic hcm",
    version="0.0.1",
    author="kalog.acc@gmail.com",
    author_email="kalog.acc@gmail.com",
    description="Open traffic open data",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    # install_requires=install_requires,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)