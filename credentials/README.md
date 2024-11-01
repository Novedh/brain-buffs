# Credentials Folder

## The purpose of this folder is to store all credentials needed to log into your server and databases. This is important for many reasons. But the two most important reasons is

    1. Grading , servers and databases will be logged into to check code and functionality of application. Not changes will be unless directed and coordinated with the team.
    2. Help. If a class TA or class CTO needs to help a team with an issue, this folder will help facilitate this giving the TA or CTO all needed info AND instructions for logging into your team's server.

# Below is a list of items required. Missing items will causes points to be deducted from multiple milestone submissions.

1.  Server URL or IP

    `ec2-13-57-185-95.us-west-1.compute.amazonaws.com` or `13.57.185.95`

2.  SSH username

    `ubuntu`

3.  SSH password or key.
    <br> If a ssh key is used please upload the key to the credentials folder.

    We have added CTO Anthony's key to our remote server's
    ~/.ssh/authorized_keys. Follow instructions to ssh into our server.

4.  Database URL or IP and port used.
    <br><strong> NOTE THIS DOES NOT MEAN YOUR DATABASE NEEDS A PUBLIC FACING PORT.</strong> But knowing the IP and port number will help with SSH tunneling into the database. The default port is more than sufficient for this class.

    `127.0.0.1:3306` or `localhost:3306`

5.  Database username

    `team01`

6.  Database password

    `Csc648@team01`

7.  Database name (basically the name that contains all your tables)

    `CSC648`

8.  Instructions on how to use the above information.

    To ssh into ec2 instance:

    `ssh -i path/to/your_key ubuntu@{Server URL or IP}`

    To access our MySQL database, you need to SSH into our server, and then you need to run this command.

    `mysql -u team01 -p`
    Password: `Csc648@team01`

9.  To access the Database on the localized version of this applciation you will need to create a personal .env File

    to make setting up easier we have provided a `.env.example` file in the repository

    a. create a file named `.env` in the applications folder and copy the contents of `.env.example` into it.

    b. Then enter the DB credentials
    Here’s an example of what your .env file should include:

        DBMS = 'mysql'
        DB_HOST = 'database IP'
        DB_USER_NAME = 'database username'
        DB_PASSWORD = 'database password'
        DB_DATABASE = 'database name'

# Most important things to Remember

## These values need to kept update to date throughout the semester. <br>

## <strong>Failure to do so will result it points be deducted from milestone submissions.</strong><br>

## You may store the most of the above in this README.md file. DO NOT Store the SSH key or any keys in this README.md file.
