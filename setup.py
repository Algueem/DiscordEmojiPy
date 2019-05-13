import setuptools

setuptools.setup(name='demojipy',
                 version='1.1',
                 license='MIT',
                 description='Python API Wrapper for DiscordEmoji',
                 author='Algueem',
                 url='https://github.com/Algueem/DiscordEmojiPy',
                 keywords=['pydemoji', 'discordemoji'],
                 install_requires=[
                     'requests'
                 ],
                 packages=setuptools.find_packages()
                 )
