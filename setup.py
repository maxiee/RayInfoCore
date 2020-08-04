from setuptools import find_packages, setup

setup(
    name='RayInfoCore',
    version='0.0.1',
    author='Maxiee',
    author_email='maxieewong@gmail.com',
    license='MIT',
    packages=find_packages(),
    python_requires='>=3',
    install_requires=[
        'click', 'peewee'
    ],
    entry_points='''
        [console_scripts]
        RayInfoCore=ray_info_core.cli:cli
    ''',
)