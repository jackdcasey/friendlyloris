import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="friendlyloris",
    version="1.0.1",
    author="Jack Casey",
    author_email="jackdcasey@gmail.com",
    description="A Slow Loris package for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jackdcasey/friendlyloris",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords=['slowloris', 'http', 'https', 'dos', 'testing']
)