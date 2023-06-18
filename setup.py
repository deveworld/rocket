from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name                = 'minirocket',
    version             = '0.1a1',
    description         = 'A simple python simulation of a rocket.',
    long_description    = long_description,
    long_description_content_type="text/markdown",
    author              = 'devworld',
    author_email        = 'world@worldsw.dev',
    url                 = 'https://github.com/deveworld/rocket/',
    install_requires    = [
                            'getch; platform_system == "Linux"',
                        ],
    packages            = find_packages(exclude=[]),
    keywords            = ['rocket', 'simulation', 'simple rocket', 'pypi'],
    python_requires     = '>=3.6',
    project_urls        = {
                            'Documentation': 'https://github.com/deveworld/rocket/',
                            'Source': 'https://github.com/deveworld/rocket/',
                            'Tracker': 'https://github.com/deveworld/rocket/issues',
                        },
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
                            'Development Status :: 3 - Alpha',
                            'License :: OSI Approved :: MIT License',
                            'Programming Language :: Python :: 3',
                        ],
)