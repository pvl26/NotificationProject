#!/bin/bash
sudo systemctl reset-failed    #  daca serviciul a dat fail

sudo systemctl stop notifyapp.service

sudo systemctl disable notifyapp.service

sudo rm /etc/systemd/system/notifyapp.service 

sudo rm /usr/local/lib/notifyapp/service_source.py

sudo rm /usr/local/lib/notifyapp/unconvinced.mp3

sudo rm /usr/local/lib/notifyapp/Icons/*

sudo rmdir /usr/local/lib/notifyapp/Icons

sudo rmdir /usr/local/lib/notifyapp/
