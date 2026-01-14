from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name='TornPy',
  version='0.0.2',
  description='A Wrapper for the Torn API',
  author="Meaning",
  long_description=long_description,
  long_description_content_type="text/markdown",
  license="MIT",
  packages=find_packages(),
  install_requires=[
    "pydantic>=2.12.5",
    "httpx>=0.28.1",
  ],
  classifiers=[
    'Development Status :: 1 - Planning',
    'License :: OSI Approved :: MIT License',  
    'Typing :: Typed'
  ]
)
