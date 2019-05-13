from setuptools import setup, find_packages

setup(
    name="hello-world",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["hello-world = hello_world.hello:main"]},
    install_requires=["Flask"],
)