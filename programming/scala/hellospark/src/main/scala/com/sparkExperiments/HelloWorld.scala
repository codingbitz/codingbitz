package com.sparkExperiments

import org.apache.log4j.{Level, Logger}
import org.apache.spark.storage.StorageLevel
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import scala.collection.mutable.ListBuffer
import scala.collection.immutable.ListMap

object HelloWorld {

  def main(args: Array[String]) {

    Logger.getLogger("org").setLevel(Level.ERROR)
    val conf = new SparkConf().setAppName("HelloWorld").setMaster("local[1]")
    val sc = new SparkContext(conf)
    val fileTxt = "data/word_count.txt"
    val wordCounts = sc.textFile(fileTxt)
                       .flatMap(line => line.split(" "))
                       .filter(x => x.matches("[A-Za-z]+"))
                       .map(word => (word, 1))
                       .reduceByKey(_ + _, 1)
                       .map(item => item.swap)
                       .sortByKey(false)
                       .map(item => item.swap)
                       .collect()
      
    var builder = new ListBuffer[String]()
    for ((word, count) <- wordCounts) builder+=(word + " : " + count)
    println(builder.toList)
    sc.stop()
  }

}
