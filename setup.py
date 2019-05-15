from setuptools import setup, find_packages


with open('README.md', 'r') as fp:
    long_desc = fp.read()


setup(name='demojipy',
      version='1.3.0',
      license='MIT',
      description='Python Wrapper for DiscordEmoji API',
      long_description=long_desc,
      long_description_content_type="text/markdown",
      author='Algueem',
      url='https://github.com/Algueem/DiscordEmojiPy',
      keywords=['pydemoji', 'discordemoji'],
      install_requires=[
          'requests'
      ],
      packages=find_packages(),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Programming Language :: Python :: 3.6",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent"
      ]
      )
