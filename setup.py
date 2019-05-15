from setuptools import setup, find_packages

setup(name='demojipy',
      version='1.2.0a',
      license='MIT',
      description='Python API Wrapper for DiscordEmoji',
      author='Algueem',
      url='https://github.com/Algueem/DiscordEmojiPy',
      keywords=['pydemoji', 'discordemoji'],
      install_requires=[
          'requests'
      ],
      packages=find_packages(),
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Programming Language :: Python :: 3.6",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent"
      ]
      )
