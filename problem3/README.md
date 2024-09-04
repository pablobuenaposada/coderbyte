# Coderbyte Back-end Challenge

In the Python file, write a program to access the contents of the bucket coderbytechallengesandbox. In there there might be multiple files, but your program should find the file with the prefix __cb__, and then output the contents of that file. You should use the boto3 module to solve this challenge.

You do not need any access keys to access the bucket because it is public. This post might help you with how to access the bucket.

**Example Output**

contents of some file

**Example Output with ChallengeToken**

contents o some le


Once your function is working, take the final output string and remove any characters (case-insensitive) from it that appear in your ChallengeToken. If the new final string is empty, return the string EMPTY.

Your ChallengeToken: ifwq4d590