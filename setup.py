from setuptools import setup, find_packages

install_requires = (
    # XXX(dmr, 2018-02-26): possibly not minimum version
    'munch>=2.2.0'
)

setup(
    name='punch-it',
    version='0.0.0',
    description='munch not fast enough? just punch.it',
    author='dmr',
    author_email='dradetsky@gmail.com',
    url='https://github.com/dradetsky/punch',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=install_requires,
    license='WTFPL',
)
