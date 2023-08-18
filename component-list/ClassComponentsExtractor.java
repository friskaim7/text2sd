import com.github.javaparser.StaticJavaParser;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.VariableDeclarator;
import com.github.javaparser.ast.expr.AnnotationExpr;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.nio.file.FileVisitOption;
import java.nio.file.FileVisitResult;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.ArrayList;
import java.util.EnumSet;
import java.util.List;

public class ClassComponentsExtractor {
    public static void main(String[] args) throws IOException {
        final String REPO_ROOT_PATH = "E:/Work/Maucash/Repos/21-repos/";
        String outputFilename = "component-list/out/output1.txt";

        String[] inputFileNames = findJavaFiles(REPO_ROOT_PATH);
        System.out.println("inputFileNames.length = " + inputFileNames.length);

        // Create parent directories for the output file
        File outputFile = new File(outputFilename);
        outputFile.getParentFile().mkdirs();

        for (String input : inputFileNames) {
            System.out.println(input);

            try (PrintStream printStream = new PrintStream(new FileOutputStream(outputFilename, true))) {
                File file = new File(input);
                CompilationUnit cu = StaticJavaParser.parse(file);
                System.setOut(printStream);

                System.out.println("**********************************************");
                System.out.println("Filename: " + input);

                ClassVisitor classVisitor = new ClassVisitor();
                cu.accept(classVisitor, null);

                List<String> classNames = classVisitor.getClassNames();
                for (String className : classNames) {
                    System.out.println("-----------------------");
                    System.out.println("Class Name: " + className);

                    cu.getClassByName(className).ifPresent(classOrInterfaceDeclaration -> {
                        System.out.println("Methods in " + className + ":");
                        for (MethodDeclaration method : classOrInterfaceDeclaration.getMethods()) {
                            System.out.println("Method Name: " + method.getNameAsString());
                            List<AnnotationExpr> annotations = method.getAnnotations();
                            System.out.println("Annotations: ");
                            for (AnnotationExpr annotation : annotations) {
                                System.out.println(annotation);
                            }

                            // Retrieve information about variables within the method
                            System.out.println("Variables: ");
                            method.getBody().ifPresent(body -> {
                                body.findAll(VariableDeclarator.class).forEach(variable -> {
                                    String variableName = variable.getNameAsString();
                                    String variableType = variable.getTypeAsString();
                                    System.out.println(variableName + "\t|" + variableType);
                                });
                            });
                        }
                    });
                }

                // List<String> classNames = classVisitor.getClassNames();
                // for (String className : classNames) {
                // System.out.println("Class Name: " + className);
                // }

                // List<MethodDeclaration> methods = cu.findAll(MethodDeclaration.class);
                // for (MethodDeclaration method : methods) {
                //     System.out.println("-----------------------");
                //     System.out.println("Method Name: " + method.getNameAsString());

                //     List<AnnotationExpr> annotations = method.getAnnotations();
                //     System.out.println("Annotations: ");
                //     for (AnnotationExpr annotation : annotations) {
                //         System.out.println(annotation);
                //     }

                //     // Retrieve information about variables within the method
                //     System.out.println("Variables: ");
                //     method.getBody().ifPresent(body -> {
                //         body.findAll(VariableDeclarator.class).forEach(variable -> {
                //             String variableName = variable.getNameAsString();
                //             String variableType = variable.getTypeAsString();
                //             System.out.println(variableName + "\t|" + variableType);
                //         });
                //     });
                // }
            } catch (Exception e) {
                System.out.println("Failed to parse: " + input);
            }
        }

        System.out.println("Output has been written to " + outputFilename);
    }

    public static String[] findJavaFiles(String rootFolderPath) throws IOException {
        final List<String> javaFilePathList = new ArrayList<>();
        Path start = Paths.get(rootFolderPath);
        Files.walkFileTree(start, EnumSet.noneOf(FileVisitOption.class), Integer.MAX_VALUE,
                new SimpleFileVisitor<Path>() {
                    @Override
                    public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) {
                        if (file.toString().endsWith(".java")) {
                            javaFilePathList.add(file.toString());
                        }
                        return FileVisitResult.CONTINUE;
                    }
                });

        return javaFilePathList.toArray(new String[0]);
    }

    public static class ClassVisitor extends VoidVisitorAdapter<Void> {
        private List<String> classNames = new ArrayList<>();

        @Override
        public void visit(ClassOrInterfaceDeclaration cls, Void arg) {
            super.visit(cls, arg);
            classNames.add(cls.getNameAsString());
        }

        public List<String> getClassNames() {
            return classNames;
        }
    }
}