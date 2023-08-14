import java.lang.reflect.*;

public class MethodNamesExtractor {
    public static void main(String[] args) throws ClassNotFoundException {
        if (args.length != 1) {
            System.out.println("Usage: java MethodNamesExtractor <ClassName>");
            return;
        }

        String className = args[0];
        // // Set the classpath for the target class
        // String classPath = "com.welab.application.common";  // Update this to the appropriate path

        // // Combine the classpath with the class name to get the full path
        // String fullClassName = classPath + "." + className;

        // Load the target class
        Class<?> clazz = Class.forName(className);

        Method[] methods = clazz.getDeclaredMethods();
        System.out.println("Method names in " + className + ":");
        for (Method method : methods) {
            System.out.println(method.getName());
        }
    }
}
