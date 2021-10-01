# AutoDelete
Python Script to automatically delete files

Start the script on a Raspberry with this line:
`sudo nohup python3 main.py &`

Execute:
`sudo crontab -e`

Add this to the File:
```@reboot sudo nohup python3 /bin/AutoDelete/main.py &```

Than restart the machine
`sudo reboot`
