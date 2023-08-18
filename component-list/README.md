# User Guideline

## JDepend
### Prerequisites
- jdepend-((version)).jar files

### How To Use
1. Open command prompt from jdepend root folder*
2. Run this command
> java -cp jdepend-2.9.5.jar jdepend.textui.JDepend "((classes folder))" > ((output filename)).txt

## Javaparser
### Prerequisites
- javaparser-core-((version)).jar files

### How To Use
1. Open command prompt in working-folder directory*
2. Compile the extractor program
> javac -cp lib\javaparser-core-3.25.4.jar -d component-list\classes\ component-list\ClassComponentsExtractor.java
3. Run the program
> java -cp .;lib\javaparser-core-3.25.4.jar;component-list\classes ClassComponentsExtractor

***
 *Powershell didn't work for .jar file