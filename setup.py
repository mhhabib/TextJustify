from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='TextJustify',
    version='0.0.5',
    description='A text justify package',
    long_description=long_description + '\n\n' +
    open('Changelog.txt').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/mhhabib/TextJustify',
    author='MH Habib',
    author_email='mhrahman7096@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='justify',
    packages=find_packages(),
    install_requires=['']
)
