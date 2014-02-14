from setuptools import setup

setup(
    name='django-gistpage',
    version='0.0.0',
    author='Chris Chang',
    author_email='c@crccheck.com',
    url='https://github.com/texastribune/django-gistpage',
    packages=['DjangoGistServer'],
    include_package_data=True,  # automatically include things from MANIFEST.in
    install_requires=['Django>=1.6.2'],  # meh, use latest as of writing
    license='Apache License, Version 2.0',
    description='Instant Django Single Page Server',
    long_description=open('README.rst').read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
    ],
)
