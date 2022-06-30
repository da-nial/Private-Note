from setuptools import find_packages, setup

setup(
    name='privatenote',
    version='1.0.0',
    packages=['privatenote'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
