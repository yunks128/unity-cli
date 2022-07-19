import setuptools

setuptools.setup(
  name="unity-cli",
  version="0.1.0",
  packages=['unity', 'unity.commands'],
  entry_points='''
      [console_scripts]
      unity = unity.main:cli
  ''',
  install_requires=[
    'requests',
    'click'
  ],
  python_requires='>=3.8',
)
