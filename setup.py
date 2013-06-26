from setuptools import setup, find_packages


setup(
    name='sentry-argstagging',
    version='0.0.1',
    description='Sentry Pulgin to set tags by using arguments of Message event.',
    author='Hiroki KIYOHARA',
    author_email='hirokiky@gmail.com',
    url='https://github.com/hirokiky/sentry_argstagging',
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
