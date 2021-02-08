import setuptools

from setuptools.command.install import install
with open("README.md", "r") as fh:
    long_description = fh.read()


class CustomInstallCommand(install):
    def run(self):
        import os

        if not os.path.exists("./CurveMatchingPython.o"):
            print("Compiling Libraries ...")
            res = os.system(" g++ -std=c++17 ./CLibrary/main.cpp -o ./CurveMatchingPython/CurveMatchingPython.o -O3 -Wall -DNDEBUG")
            if res == 0:
                print("Compilation Successful")
            else:
                raise ValueError("Compilation Error")

        install.run(self)


setuptools.setup(
    name="CurveMatchingPython",
    version="1.1.7",
    author="Edoardo Ramalli",
    author_email="edoardo.ramalli@polimi.it",
    description="Python wrapper for CurveMatching  DOI=10.1016/j.combustflame.2016.03.019",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    install_requires=['numpy'],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    cmdclass={
        'install': CustomInstallCommand,
    },
    package_data={'CurveMatchingPython': ['./CurveMatchingPython.o']},

    include_package_data=True,
)
