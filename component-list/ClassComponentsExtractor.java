import com.github.javaparser.StaticJavaParser;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.expr.AnnotationExpr;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.util.List;

public class ClassComponentsExtractor {
    public static void main(String[] args) throws IOException {
        final String REPO_ROOT_PATH = "E:/Work/Maucash/Repos/21-repos/";
        String inputFileName = "welab-application/welab-application-api/src/main/java/com/welab/application/common/AppUtil.java";
        String outputFilename = "component-list/out/" + inputFileName.replace(".java", ".txt");;

        File file = new File(REPO_ROOT_PATH + inputFileName);
        CompilationUnit cu = StaticJavaParser.parse(file);

        // Create parent directories for the output file
        File outputFile = new File(outputFilename);
        outputFile.getParentFile().mkdirs();

        try (PrintStream printStream = new PrintStream(new FileOutputStream(outputFilename))) {
            System.setOut(printStream);

            List<MethodDeclaration> methods = cu.findAll(MethodDeclaration.class);
            for (MethodDeclaration method : methods) {
                System.out.println("Method Name: " + method.getNameAsString());

                List<AnnotationExpr> annotations = method.getAnnotations();
                for (AnnotationExpr annotation : annotations) {
                    System.out.println("Annotation: " + annotation);
                }

                System.out.println("-----------------------");
            }
        }

        System.out.println("Output has been written to " + outputFilename);
    }
}