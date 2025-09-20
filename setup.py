from setuptools import setup, find_packages

setup(
    name='varcross',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'astroquery',
        'astropy',
        'numpy',
        'matplotlib',
        'pandas',
        # ha kell: 'seismolab'
    ],
    author='Dóra Tarczay-Nehéz',
    description='Modular pipeline for Gaia–OGLE variable star cross-analysis',
    python_requires='>=3.7',
)
