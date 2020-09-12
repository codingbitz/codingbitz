Running Steps:

Install SBT plugin in VS Code/IntelliJ, connect to the windows directory in WSL-2(works fine in VS/not tested in IntelliJ) where dev is happening.

check for ScalaVersion:

sbt scalaVersion

sbt compile

sbt "runMain com.sparkExperiments.HelloWorld" > to pick right main class

Expected Output:

List(Spark : 6, and : 6, a : 5, Apache : 5, on : 4, data : 3, for : 3, can : 3, of : 3, it : 2, Runs : 2, You : 2, in : 2, using : 2, the : 2, SQL : 2, libraries : 2, And : 1, high : 1, is : 1, its : 1, run : 1, seamlessly : 1, parallel : 1, operators : 1, same : 1, standalone : 1, interactively : 1, Ease : 1, offers : 1, DAG : 1, over : 1, easy : 1, execution : 1, hundreds : 1, make : 1, engine : 1, from : 1, other : 1, these : 1, performance : 1, use : 1, physical : 1, you : 1, that : 1, or : 1, build : 1, achieves : 1, times : 1, to : 1, including : 1, analytics : 1, cluster : 1, query : 1, MLlib : 1, batch : 1, both : 1, streaming : 1, Access : 1, machine : 1, unified : 1, combine : 1, powers : 1, stack : 1, Hadoop : 1)

git add <FileName>

git commit -m <commit_msg>

git push origin <branch>

Load the data file

split it based on search string

filter out numbers

count occurance

sort by value

convert to list
