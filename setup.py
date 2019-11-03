from setuptools import setup, find_packages


with open('README.md', 'r') as fp:
    long_desc = fp.read()


with open('requirements.txt', 'r') as fp:
    requirements = fp.readlines()


setup(name='demojipy',
      version='3.0.0',
      license='MIT',
      description='Python Wrapper for DiscordEmoji API',
      long_description=long_desc,
      long_description_content_type="text/markdown",
      author='Algueem',
      url='https://github.com/Algueem/DiscordEmojiPy',
      keywords=['pydemoji', 'discordemoji'],
      install_requires=[
          requirements
      ],
      packages=find_packages(),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Programming Language :: Python :: 3.6",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent"
      ]
      )
