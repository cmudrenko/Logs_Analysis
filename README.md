# Log Analysis Project
-Christopher Mudrenko
## Project Description:
-A large database of news information has been given by the Udacity team to create python file to interpret three different queries. This reporting tool is showing valuable information to keep relevant with top articles, authors and percentage of large cases of errors. 
#Inorder to Run
## Installing critical files
1. Install [Vagrant](https://www.vagrantup.com/)
1. Install [VirtualBox](https://www.virtualbox.org/)
1. Download the vagrant setup files from [Udacity's Github](https://github.com/udacity/fullstack-nanodegree-vm)
These files configure the virtual machine and install all the tools needed to run this project.
1. Download the database setup: [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
1. Unzip the data to get the newsdata.sql file.
1. Put the newsdata.sql file into the vagrant directory
1. Upzip as needed and copy all files into the vagrant directory into a folder called log_analysis
#### Start the Virtual Machine:
1. Open Terminal and navigate to the project folders we setup above.
1. cd into the vagrant directory
1. Run ``` vagrant up ``` to build the VM for the first time.
1. Once it is built, run ``` vagrant ssh ``` to connect.
1. cd into the correct project directory: ``` cd /vagrant/logs_analysis ```
#### Load the data into the database:
1. Launch Vagrant VM by running vagrant up, you can the log in with vagrant ssh

1. To load the data, use the command psql -d news -f newsdata.sql to connect a database and run the necessary SQL statements.


