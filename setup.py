from setuptools import find_packages, setup

name = 'DeeperBin'
requires_list = open('./requirements.txt', 'r', encoding='utf8').readlines()
requires_list = [i.strip() for i in requires_list]

setup(
    name=name,
    version='1.0.7',
    author="Bohao Zou",
    author_email='csbhzou@comp.hkbu.edu.hk',
    description="The binner to cluster contigs.",
    python_requires=">=3.9",
    packages=find_packages(),
    package_data={"": ["*"]},
    include_package_data=True,
    zip_safe=False,
    entry_points={"console_scripts": ["deeperbin=DeeperBin.main:main"]},
    install_requires=requires_list
)
