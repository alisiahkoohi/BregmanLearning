import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

reqs = []
setuptools.setup(
    name='bregman',
    version='0.1',
    author='',
    author_email='',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/TimRoith/BregmanLearning',
    license='MIT',
    install_requires=reqs,
    packages=setuptools.find_packages()
)
