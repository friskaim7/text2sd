# User Guideline

## code2diagram
### Prerequisites
- plantuml-((version)).jar files

### How To Use
1. Open command prompt in working-folder directory*
2. Compile the extractor program
> javac -cp lib\plantuml-1.2023.10.jar -d code2diagram\classes\ code2diagram\String2Diagram.java
3. Run the program
> java -cp .;lib\plantuml-1.2023.10.jar;code2diagram\classes String2Diagram

## Transformer
### Prerequisites
- jackson-databind-((version)).jar

### How To Use
1. Open command prompt in working-folder directory*
2. Compile the extractor program
> javac -cp lib\jackson-databind-2.15.2.jar -d code2diagram\classes\ code2diagram\Transformer.java
3. Run the program
> java -cp .;lib\jackson-databind-2.15.2.jar;code2diagram\classes Transformer

***
 *Powershell didn't work for .jar file