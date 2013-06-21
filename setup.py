from setuptools import setup, find_packages


setup(
    name='sentry-argstagging',
    version='0.0.1',
    author='Hiroki KIYOHARA',
    author_email='hirokiky@gmail.com',
    classifiers=[
      'Development Status :: 1 - Planning',
      'Environment :: Plugins',
      'Framework :: Django',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python',
      'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=['sentry'],
    packages=find_packages(),
    entry_points={
       'sentry.plugins': [
            'pluginname = sentry_argstagging.plugin:ArgsPlugin'
        ],
    },
)
