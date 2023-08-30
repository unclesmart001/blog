'''
WORKING WITH A requirements.txt FILE IN DJANGO
A requirements.txt file is used to store the name and version of the installed libraries.

It saves time used to install individual libraries using pip

CREATING A requirements.txt FILE AUTOMATICALLY
-Initially after installing libraries for our projects in our virtual envt , we can automatically create requirements.txt and add the required libriries and their version.

cmd: pip freeze > requirements.txt

The command above checks if there is an existing requirements.txt; if there isnt, it will create a new one, will require libraries specifications , but if there is , it will only update it to match the currently installled libraries.

INSTALLING libraries from the requirements.txt 
-After pushing your code to git , whenever you will want to retrieve it and run it from a diff. machine/cntainer, which already has python in it and has an envt, 
we acess requirements.txt file that will b part of the project retrieved from git, we then run a command that automaticallly installs all libraries stated in the requirements.txt

cmd: pip install -r requirements.txt


'''