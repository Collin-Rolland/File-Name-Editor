# File-Name-Editor

Hello,

This is a custom script that I developed during my internship at Electrex Inc, using Python.

The script is designed to changes the file names in a production folder that Electrex uses to make the names more uniform, as there were many entry errors over the years. The company needed these file names uniform and consistent in order to use in further developmental projects. I learned many things throughout this process, Stack Overflow was often used as a reference as I met many challenges along the way.

The company will automate this script to run every night, to get rid of any entry error in their production folders.

Here is the link to the script:

Here is a folder of similar file names I was trying to fix, test the script out:

# Problems Encountered

The file names had many random characters inserted that had nothing to do with the production names of these files. Each file name has a seven digit number that starts with a nine, a Revision number (although this could be blank and that should be defined with a dash), and potentially a VCN number at the end. 

The first function I created replaced any special characters and placed a space between each of the aforementioned parts of the file name. The problem with this was that some of those special characters are needed in the file names. For example, as mentioned before if there are no revisions done, that is shown with a dash after the 'Rev' string. So I had to write a program to add that back, but only in places were a revision had been done. This was a huge challenge as there is no straightforward way to add the dash back in, considering that the 'Rev' string is in the middle of the file name and that the names had been entered with so much variety.

I solved this problem with creating multiple regualar expressions to solve it. I added a dash anytime there were two spaces after the 'Rev' string, this did its job but also added dashes in places where they weren't supposed to be. More expressions were created to get rid of those unneccasary dashed. There are many more instances of similar hurdles I had to face. The main thing I learned in this project was that sometimes it takes multiple steps to solve one simple problem.
