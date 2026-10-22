Aim
To implement a Hadoop MapReduce program for counting the frequency of words in text data
stored in HDFS.
Learning Objectives
Students should be able to:
● Explain the MapReduce programming model.
● Store input files in HDFS.
● Implement Mapper and Reducer functions.
● Execute a MapReduce job.
● Analyze the generated output.
Background
MapReduce processes large datasets in two major stages.
Map Stage
The Mapper reads the input and produces intermediate key-value pairs:

(word,1)

Reduce Stage
The Reducer receives each word and its list of counts, then calculates the total:

(word,[1,1,1])→(word,3)
The final output contains each word and its frequency.

Requirements
● Prepare a text input file.
● Create an input directory in HDFS.
● Upload the file to HDFS.
● Implement the Mapper.
● Implement the Reducer.
● Execute the MapReduce job.
● Display the output from HDFS.
Suggested Procedure
1. Install or configure Hadoop.
2. Start the required Hadoop services.
3. Create a text file containing multiple lines.
4. Create an input directory in HDFS.
5. Upload the text file to HDFS.
6. Implement the Mapper and Reducer.
7. Compile or package the program.
8. Execute the MapReduce job.
9. View the output directory.
10. Verify the word frequencies manually for a small input.
Expected Input
A text file containing words, sentences, or paragraphs.
Expected Output
A list of words with their frequency counts.
Example format:
cloud 3
data 5
system 2