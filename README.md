# NotificationProject




Installation
============
You will need to install next packages, some might be already installed in your system

1. gi: __`sudo apt install python-gi`__
2. notify: __`sudo apt install gir1.2-notify-0.7`__
3. mpg123: __`sudo apt install mpg123`__                   
4. beautifoulsoup4: __`sudo apt-get install python3-bs4`__    
5. lxml: __`sudo apt-get install python3-lxml`__         

Service automatization
======================

How to create the service:

1. Give permissions: __`chmod +x service_maker.py`__
2. Run script: __`sudo ./service_maker.py`__ 
3. Delete service: __`./clean.sh`__  

<b>WARNING</b>: ```service_maker.py``` is not yet ready, don't use untill this message is gone!!!

Original Developers
-------------------

 * Mateescu Pavel-Vlad - [Pvl26](https://github.com/Pvl26)
 * Dutica Maria-Diana - [DianaDutica](https://github.com/DianaDutica)

Contribute
==========

Any contribution is welcome. The current problems are:

..* notifyapp.service generated by ```service_maker.py``` has an error.

Feel free to make any other contribution, if you want to merge it to our repo, just make a pull request.