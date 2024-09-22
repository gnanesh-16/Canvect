from setuptools import setup, find_packages

setup(
    name='canvect',                          
    version='0.1.4',                         
    author='Gnanesh Balusa',                      
    author_email='gnaneshbalusa016g@gmail.com',   
    description='Canvect is a Python package designed for sending and managing CAN (Controller Area Network) messages related to acceleration control. It provides a simple yet flexible API for creating and dispatching CAN messages, making it ideal for applications in automotive and industrial systems where CAN communication is essential.',
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',
    url='https://github.com/gnanesh-16/Canvect',  
    packages=find_packages(),                
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',   
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',                 
    install_requires=[                       
        'python-can',
    ], #python setup.py sdist bdist_wheel, twine upload dist/*


)
