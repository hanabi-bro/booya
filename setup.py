import setuptools

with open("README.md", "r", encoding='UTF-8') as f:
    long_description = f.read()

setuptools.setup(
    name="booya",
    version="0.0.1",
    author="hanabi-bro",
    author_email="hanabi.bro@gmail.com",
    description="test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hanabi-bro/booya",
    packages=setuptools.find_packages(),
    install_requires = [
        'psutil',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],
    # entry_points = {
    #     'console_scripts': ['forti_dff = booya.forti_diff:main']
    # },
    python_requires='>=3.9',
)
