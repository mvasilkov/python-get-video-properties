from setuptools import find_packages, setup

if __name__ == '__main__':
    setup(
        name='get-video-properties',

        version='0.1.0',

        description='Get video properties',
        long_description='Get video properties',

        url='https://github.com/mvasilkov/python-get-video-properties',

        author='Mark Vasilkov',
        author_email='mvasilkov@gmail.com',

        license='MIT',

        classifiers=[
            'Intended Audience :: Developers',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3 :: Only',
            'Topic :: Multimedia :: Sound/Audio',
            'Topic :: Multimedia :: Video',
        ],

        keywords='ffprobe video audio',

        packages=find_packages(),
        include_package_data=True,

        entry_points={
            'console_scripts': [
                'videoprops=videoprops:run',
                'audioprops=videoprops:run2',
            ],
        },
    )
