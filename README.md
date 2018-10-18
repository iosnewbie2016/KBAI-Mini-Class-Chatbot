## Project 1 for CS-4635 : Mini Class Chatbot

Read Project1_KevinKusuma for Project Description and Report.

### Requirements

Python 3.6 or above

## To run 
```
python AgentGrader.py

## Autograder Output

```
in results.log
---------------

when is the project due|project|DUEDATE|project|DUEDATE1|1.0|1.0
when is the project released|project|RELEASEDATE|project|DUEDATE2|2.0|1.0
how much is the project worth|project|WEIGHT|project|DUEDATE3|3.0|1.0
where do I turn in my project|project|PROCESS|project|DUEDATE4|4.0|1.0
where is the project specification|project|PROCESS|project|DUEDATE5|5.0|1.0
how long do we have to complete a project|project|DURATION|project|DUEDATE6|6.0|1.0

count,object,datatype
6|6.0|1.0
------------------------------------------------------------------------------------------------------
 
 | is a delimiter. 

count,object,datatype
6       |   6.0   |  1.0

count = total # of questions
object = # of correct object matches
datatype = # of correct datatype matches

                          |     ground truth        |   student agent     |
question                  |  object   |  requested  |  object | requested | question # | object match | request match
when is the project due   |  project  |  DUEDATE    | project | DUEDATE   |     1      |      1.0     |     1.0
```


