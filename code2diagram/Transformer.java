import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Transformer {
    public static void main(String[] args) {
        // Specify the JSON file path and the output text file path
        // String jsonFilePath = "resource/input.json";
        // String outputFilePath = "output.txt";

        // try {
        // // Read JSON file content into a string
        // String jsonContent = new String(Files.readAllBytes(Paths.get(jsonFilePath)));

        // // Transform JSON and write the transformed content to a text file
        // String transformedContent = transformJson(jsonContent);
        // writeStringToFile(transformedContent, outputFilePath);

        // System.out.println("Transformed content written to " + outputFilePath);
        // } catch (IOException e) {
        // e.printStackTrace();
        // }
        // String json = "{\"name\": \"John\", \"age\": 30, \"city\": \"New York\"}";

        // ObjectMapper objectMapper = new ObjectMapper();
        // try {
        // JsonNode jsonNode = objectMapper.readTree(json);

        // // Start iterating through the JSON structure
        // iterateJson(jsonNode, "");
        // } catch (Exception e) {
        // e.printStackTrace();
        // }

        String jsonString = "{\"file_relative_path\": \"path/to/file\", \"package_name\": \"com.google.maps\"}";

        try {
            ObjectMapper objectMapper = new ObjectMapper();
            JsonNode jsonNode = objectMapper.readTree(jsonString);

            // Get the value of the "file_relative_path" field
            String fileRelativePath = jsonNode.get("file_relative_path").asText();

            System.out.println("file_relative_path: " + fileRelativePath);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // private static void iterateJson(JsonNode node, String prefix) {
    //     if (node.isObject()) {
    //         System.out.println(prefix + "{");
    //         for (JsonNode entry : node) {
    //             String key = entry.getKey();
    //             // String key = entry.getKey();
    //             JsonNode valueNode = entry.getValue();
    //             System.out.print(prefix + "  \"" + key + "\": ");
    //             iterateJson(valueNode, prefix + "  ");
    //         }
    //         System.out.println(prefix + "}");
    //     } else if (node.isArray()) {
    //         System.out.println(prefix + "[");
    //         for (JsonNode item : node) {
    //             iterateJson(item, prefix + "  ");
    //         }
    //         System.out.println(prefix + "]");
    //     } else if (node.isValueNode()) {
    //         System.out.println("\"" + node.asText() + "\"");
    //     }
    // }

    // private static String transformJson(String jsonContent) throws IOException {
    //     // Parse the JSON content
    //     ObjectMapper objectMapper = new ObjectMapper();
    //     JsonNode jsonNode = objectMapper.readTree(jsonContent);

    //     // Perform your transformation on the JSON data
    //     // For example, you can manipulate the JSON structure or values here
    //     // In this example, let's just add a new field to the JSON
    //     ((com.fasterxml.jackson.databind.node.ObjectNode) jsonNode).put("newField", "newValue");

    //     // Convert the transformed JSON back to a string
    //     return objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(jsonNode);
    // }

    // private static void writeStringToFile(String content, String filePath) throws IOException {
    //     Path outputPath = Paths.get(filePath);
    //     Files.write(outputPath, content.getBytes());
    // }
}
