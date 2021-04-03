from setuptools import setup, find_packages

setup(
    name='openitcr',
    version='0.0.1',
    description='Open Information Technology Classroom',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown; charset=UTF-8",
    url='https://github.com/larryw3i/openitcr',
    download_url='https://github.com/larryw3i/openitcr',
    project_urls={
        'Code': 'https://github.com/larryw3i/openitcr',
        'Issue tracker': 'https://github.com/larryw3i/openitcr/issues',
        'Documentation': 'https://github.com/larryw3i/openitcr/docs/docs.md',
    },
    author='larryw3i',
    author_email='',
    license='GPL-3.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.7',
    scripts=['openitcr/bin/openitcr'],
)
