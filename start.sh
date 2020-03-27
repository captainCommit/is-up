#!/bin/bash
function unix_command {
  $@
  if [ $? -ne 0 ]; then
    echo "could not run $@ - abort"
    exit 1
  fi
}
echo Informer : Site Up/Down Check Tool
read -p "What link do you want to monitor now : " web
read -p "Time interval to check in minutes : " t
if [[ $number =~ ^[+-]?[0-9]*$ ]];
  then
    echo ""
elif [[ $t =~ ^[+-]?[0-9]+\.?[0-9]*$ ]]; 
  then
    echo Time entered must be greater than 1 minute
    exit 0
fi
sec=60
tnet=$((sec*t))
while true
do
  unix_command python3 isup.py --f $web &
  wait
  printf "sleeping for $tnet seconds now\n"
  printf "The process ID is  $! \nTo kill this process, Open a new terminal and type type sudo killall bash"
  sleep $tnet
done