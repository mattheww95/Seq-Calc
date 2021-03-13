import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
        name="Crispy-Cody-Mattheww95",
        version="0.0.1",
        author="Matthew Wells",
        author_email="",
        description="A small script to calculate breadth of coverage",
        long_description=long_description,
        long_description_content_type="text/markdown",
        classifiers=["Programming Language::Python::3"],
        install_requires=['pysam', 'pandas'],
        python_requires=">=3.6",
		scripts=['bin/crispy_cody'],
		zip_safe=False
		)
