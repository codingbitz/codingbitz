package com.sparkExperiments

import org.apache.log4j.{Level, Logger}
import org.apache.spark.storage.StorageLevel
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import scala.collection.mutable.ListBuffer

object HelloWorld {

  def main(args: Array[String]) {

    Logger.getLogger("org").setLevel(Level.ERROR)
    val conf = new SparkConf().setAppName("HelloWorld").setMaster("local[1]")
    val sc = new SparkContext(conf)

    val wordCounts = sc.textFile("in/word_count.txt")
                       .flatMap(line => line.split(" "))
                       .filter(x => x.matches("[A-Za-z]+"))
                       .countByValue()
      
    var builder = new ListBuffer[String]()
    for ((word, count) <- wordCounts) builder+=(word + " : " + count)
    println(builder.toList)
    sc.stop()
  }

}
