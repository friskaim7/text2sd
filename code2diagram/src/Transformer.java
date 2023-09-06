import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Transformer {
    public static void main(String[] args) {
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
}
