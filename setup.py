from setuptools import setup, find_packages

setup(name='pyscores',
      version='0.2',
      description='Football (soccer) scores in your command line',
      url='https://github.com/conormag94/pyscores',
      author='Conor Maguire',
      author_email='conormag94@gmail.com',
      license='MIT',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'scores=pyscores.__main__:main'
          ]
      },
      install_requires=[
          'click==5.1',
          'requests==2.8.1',
          'tabulate==0.7.5',
          'termcolor==1.1.0'
      ])
