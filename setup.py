from setuptools import setup, find_packages

long_description = """
txsh is a dynamic wrapper around Twisted ProcessProtocol and
spawnProcess that allows you to call any program as if it were
a function and return a deferred with its exit code and output.

.. code-block:: python

        from twisted.internet import reactor
        from txsh import ls

        def my_callback(exc_info):
            print 'Exit Code:', exc_info.status
            print 'Output:', exc_info.stdout
            print 'Errors:', exc_info.stderr
            reactor.stop()

        d = ls()
        d.addCallback(my_callback)

        reactor.run()
"""


setup(
    name="txsh",
    version='0.2',
    description="Twisted Process interface",
    long_description=long_description,
    author="Nicholas Amorim",
    author_email="jonah.crawford@gmail.com",
    url="https://github.com/minskmaz/txsh",
    license="MIT",
    packages=find_packages(),
    install_requires=['twisted'],
    requires=['twisted'],
    tests_require=['twisted', 'mock'],
    keywords='twisted process shell command',
    zip_safe=False
)
