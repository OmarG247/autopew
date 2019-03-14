from setuptools import setup, find_packages
import versioneer

tests_require = ["pytest", "pytest-runner", "pytest-cov", "coverage", "codecov"]

gui_require = ["sip", "PyQt5", "PyQt5-sip"]
dev_require = [
    "pytest",
    "versioneer",
    "black",
    "nbstripout",
    "nbdime",
    "twine",
    "sphinx_rtd_theme",
    "sphinx-autodoc-annotation",
    "recommonmark",
] + tests_require


with open("README.md", "r") as src:
    LONG_DESCRIPTION = src.read()

setup(
    name="autopew",
    description="Automating target selection for laser ablation.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    version=versioneer.get_version(),
    url="https://github.com/morganjwilliams/autopew",
    author="Morgan Williams",
    author_email="morgan.williams@csiro.au",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["laser ablation", "geochemistry"],
    packages=find_packages(exclude=["test*"]),
    install_requires=["pathlib", "numpy", "scipy", "pandas", "matplotlib", "xlrd"]
    + gui_require,
    extras_require={"dev": dev_require},
    tests_require=tests_require,
    test_suite="test",
    package_data={"autopew": ["data/*"]},
    include_package_data=True,
    license="CSIRO Modifed MIT/BSD",
    cmdclass=versioneer.get_cmdclass(),
)
