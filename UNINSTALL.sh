#!/bin/bash

if [ -f /usr/bin/white-rabbit ]
  then
    sudo rm /usr/bin/white-rabbit
    echo "White Rabbit has been Successfully Uninstalled!"
  else
    echo "White Rabbit is Not Installed!"
fi
