from setuptools import find_packages, setup

setup(
    name = 'zomato-bot',
    version= '0.0.1',
    author= 'sunny savita',
    author_email= 'sunny.savita@gmail.com',
    packages= find_packages(),
    install_requires = ["chainlit","notebook","ipywidgets","tqdm","python-dotenv","langchain-google-genai"]

)