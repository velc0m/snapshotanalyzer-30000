# before install: pipenv install -d setuptools
# for this file: pipenv run python setup.py bdist_wheel
# after this in the dist dir will be created some files.
# and can install our app as system pip3 package: pip3 install dist/snapshotsanalyzer_30000-0.1-py3-none-any.whl
# pip3 show snapshotsanalyzer_30000
# for uninstall it: pip3 uninstall snapshotsanalyzer_30000
# put snapshotsanalyzer_30000-0.1-py3-none-any.whl into AWS S3 public bucket
# can install it from AWS S3: pip3 install "url for file in the s3"

from setuptools import setup

setup(
    name='snapshotsanalyzer-30000',
    version='0.1',
    author="Litvinenka Vitali",
    description="Snapshotsanalyzer 30000 is a tool for manage AWS EC2 snapshots",
    license='GPLv3+',
    packages=['shotty'],
    url='https://github.com/velc0m/snapshotanalyzer-30000',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    '''
)
