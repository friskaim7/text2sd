import com.github.javaparser.StaticJavaParser;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.expr.AnnotationExpr;

import java.io.File;
import java.io.IOException;
import java.util.List;

public class ClassComponentsExtractor {
    public static void main(String[] args) throws IOException {
        File file = new File("E:/Work/Maucash/Playground/ReflectionExtractor/welab-application/welab-application-api/src/main/java/com/welab/application/common/AppUtil.java");
        CompilationUnit cu = StaticJavaParser.parse(file);

        List<MethodDeclaration> methods = cu.findAll(MethodDeclaration.class);
        for (MethodDeclaration method : methods) {
            System.out.println("Method Name: " + method.getNameAsString());

            // Mengambil annotation yang digunakan dalam method
            List<AnnotationExpr> annotations = method.getAnnotations();
            for (AnnotationExpr annotation : annotations) {
                System.out.println("Annotation: " + annotation);
            }

            System.out.println("-----------------------");
        }
    }
}