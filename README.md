# Real time alpaca api 
All the python scripts are loaded to check in the whether the real time data is getting fetched or not.

Zookeeper start cmd:
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

Kafka start cmd:
.\bin\windows\kafka-server-start.bat .\config\server.properties

For the Hadoop,
we use jdk 1.8 version and to run hadoop on the windows we use the following commands:
start-all.cmd
start-yarn.cmd

Now to run Apache Hive we need to start the server in the new command prompt:
StartNetworkServer -h 0.0.0.0

And now go to the C:/hive/bin path and run the command and check whether the data is processed and fetched in hive:
just type hive then the hive shell will start.

For the grafana:
run the grafana-server by running as administrator and use localhost:8080 to run your machine.
