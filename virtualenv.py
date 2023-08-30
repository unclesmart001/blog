'''
A virtual envt is used to control installation of python libraries with diff. versions in diff. projects.

We use the library "virualenv" which is an external python library.

Steps of using a virtual envt:
1. Creating a virtual envt
-When starting a project we create its virtual envt. where we will have its libraries.

2. Once we have the envt created, whenever we want to open and run the project we activate its evnt .

3. We r only ready to install libraries in the envt.
NB: When we install libraries to the envt , we will always b able to access them and use them but only when we have activated the envt.
If the envt is not activated our system will not b able to access and use the installed libraries ; so we should not forget to activate our envt.

INSTALLING VIRTUAL ENVT
cmd: pip install virtualenv

CREATING A NEW ENVT
cmd: python -m venv projectnameenv

ACTIVATING THE ENVT
ON WINDOWS GIT BASH
cmd: source projectnameenv/Scripts/activate
NB:This works when the envt is in ur present working directory.

ON LINUX
cmd: source projectnameenv/bin/activate

'''