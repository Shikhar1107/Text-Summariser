import setuptools

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Text-Summariser",
    version="0.0.1",
    author="Shikhar1107",
    author_email="shikharjul01@gmail.com",
    description="A small text-summariser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Shikhar1107/Text-Summariser",
    project_urls={
        "Bug Tracker": "https://github.com/Shikhar1107/Text-Summariser/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
    )
