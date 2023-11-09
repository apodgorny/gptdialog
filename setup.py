from setuptools import setup, find_packages

setup(
    name             = 'gptdialog',
    version          = '0.1',
    packages         = find_packages(),
    install_requires = [
        'requests~=2.31.0',
        'openai~=0.28.1'
    ],
    # More configurations can be added here.
)