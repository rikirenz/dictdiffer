import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    user_options = [('pytest-args=', 'a', 'Arguments to pass to py.test')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        try:
            from ConfigParser import ConfigParser
        except ImportError:
            from configparser import ConfigParser
        config = ConfigParser()
        config.read("pytest.ini")
        self.pytest_args = config.get("pytest", "addopts").split(" ")

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


tests_require = [
    'pytest', 'pytest-cache', 'pytest-cov', 'pytest-pep8', 'coverage'
]

setup(
    name='dictdiffer',
    version='0.0.5.dev0',
    description='Dictdiffer is a helper module that helps you '
                'to diff and patch dictionaries',
    author='Fatih Erikli',
    author_email='info@invenio-software.org',
    url='https://github.com/inveniosoftware/dictdiffer',
    py_modules=['dictdiffer'],
    extras_require={
        "docs": ["sphinx_rtd_theme"] + tests_require,
    },
    install_requires=tests_require,
    tests_require=tests_require,
    cmdclass={'test': PyTest},
)
