package learningjournal.scala.experiments
import org.slf4j.LoggerFactory


object TupleRead{  
    def main(args:Array[String]){  
        var tupleValues = tupleFunction()
        val logger = LoggerFactory.getLogger(getClass.getSimpleName)
        logger.info("Hey")
        println("Iterating values: ")  
        tupleValues.productIterator.foreach(println)
    }  
    def tupleFunction()={  
        var tuple = (1,2.5,"India")  
        tuple  
    }  
}  