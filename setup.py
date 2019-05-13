import setuptools

setuptools.setup(name='demojipy',
                 version='1.0',
                 license='MIT',
                 description='Python API Wrapper for DiscordEmoji',
                 author='Algueem',
                 url='https://github.com/Algueem/DiscordEmojiPy',
                 keywords=['pydemoji', 'discordemoji'],
                 install_requires=[
                     'requests',
                     'json'
                 ],
                 packages=setuptools.find_packages()
                 )
