from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='TextJustify',
    version='0.0.3',
    description='A text justify package',
    long_description=open('README.md').read() + '\n\n' +
    open('Changelog.txt').read(),
    url='',
    author='MH Habib',
    author_email='mhrahman7096@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='justify',
    packages=find_packages(),
    install_requires=['']
)
