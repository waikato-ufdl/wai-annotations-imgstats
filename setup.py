from setuptools import setup, find_namespace_packages


def _read(filename: str) -> str:
    """
    Reads in the content of the file.

    :param filename:    The file to read.
    :return:            The file content.
    """
    with open(filename, "r") as file:
        return file.read()


setup(
    name="wai.annotations.imgstats",
    description="Various sinks for generating image dataset statistics.",
    long_description=f"{_read('DESCRIPTION.rst')}\n"
                     f"{_read('CHANGES.rst')}",
    url="https://github.com/waikato-ufdl/wai-annotations-imgstats",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Programming Language :: Python :: 3',
    ],
    license='Apache License Version 2.0',
    package_dir={
        '': 'src'
    },
    packages=find_namespace_packages(where='src'),
    namespace_packages=[
        "wai",
        "wai.annotations",
    ],
    version="1.0.3",
    author='Peter Reutemann',
    author_email='fracpete@waikato.ac.nz',
    install_requires=[
        "wai.annotations.core>=0.1.1",
        "termplotlib",
    ],
    entry_points={
        "wai.annotations.plugins": [
            # sinks
            "area-histogram-is=wai.annotations.imgstats.format.areahistogram.specifier:AreaHistogramISOutputFormatSpecifier",
            "area-histogram-od=wai.annotations.imgstats.format.areahistogram.specifier:AreaHistogramODOutputFormatSpecifier",
            "label-dist-ic=wai.annotations.imgstats.format.labeldist.specifier:LabelDistributionICOutputFormatSpecifier",
            "label-dist-is=wai.annotations.imgstats.format.labeldist.specifier:LabelDistributionISOutputFormatSpecifier",
            "label-dist-od=wai.annotations.imgstats.format.labeldist.specifier:LabelDistributionODOutputFormatSpecifier",
        ]
    }
)
