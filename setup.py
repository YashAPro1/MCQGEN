from setuptools import find_packages,setup

setup(
    name='Multiple Choice Question Generator',
    version='0.0.1',
    author='Yashkumar Dubey',
    author_email='ydubey7979@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)