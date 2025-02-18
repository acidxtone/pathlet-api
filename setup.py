from setuptools import setup, find_packages

setup(
    name="pathlet",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'flask==3.1.0',
        'flask-cors==4.0.2',
        'gunicorn==23.0.0',
        'setuptools==69.2.0',
        'wheel==0.43.0',
        'numpy==1.24.3',
        'scipy==1.10.1',
        'pandas==2.0.1',
        'transformers==4.41.2',
        'torch==2.1.2',
        'python-dotenv==1.0.1',
    ],
    python_requires='>=3.12',
    extras_require={
        'dev': [
            'pytest==8.3.4',
            'flask-limiter==3.5.0',
        ]
    },
    entry_points={
        'console_scripts': [
            'pathlet=backend.app:main',
        ],
    },
)
