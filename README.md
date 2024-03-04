# MRjob

This repository contains all xmk files required to configure and run hadoop successfull.

For Hadoop requirement is that JAVA shoulbe no more than version JAVA 8.

For Mac, the command that worked for me is,
brew install --cask homebrew/cask-versions/adoptopenjdk8

All hadoop jar files on MAC are stored under,
/opt/homebrew/Cellar/hadoop/3.3.6/libexec/share/hadoop/tools/lib/

Proper syntax for running mapper reducer code is,
Syntax:
Path_to_hadoop_installation hadoop jar path_to_hadoop-streaming_jar_files -files path_to_files_to_be_copied_to_distributed_cache -mapper specify_script_to_run -reducer specify_script_to_run -input path_to_hdfs_input_files -output path_to_hdfs_output_file


Example,
/opt/homebrew/Cellar/hadoop/3.3.6/libexec/bin/hadoop jar /opt/homebrew/Cellar/hadoop/3.3.6/libexec/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-files /opt/homebrew/Cellar/hadoop/mapper.py,/opt/homebrew/Cellar/hadoop/reducer.py \
-mapper mapper.py \
-reducer reducer.py \
-input /code/pg5000.txt \
-output /code/output

When you run MRjob, you will see "reading from STDIN" this output when mapper successfully sends key-value pair to reducer.

python3 m11.py cleaned_comments.csv  | python3 r11.py > output11
