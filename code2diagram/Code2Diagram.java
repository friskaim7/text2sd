import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.io.OutputStream;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

import net.sourceforge.plantuml.FileFormat;
import net.sourceforge.plantuml.FileFormatOption;
import net.sourceforge.plantuml.SourceStringReader;

/**
 * a
 */
public class Code2Diagram {
    public static void main(String[] args) {
        String source = "@startuml\n";
        source += "Bob -> Alice : hello\n";
        source += "@enduml\n";

        SourceStringReader reader = new SourceStringReader(source);
        final ByteArrayOutputStream os = new ByteArrayOutputStream();

        try {
            // Write the first image to "os"
            String desc = reader.generateImage(os, new FileFormatOption(FileFormat.SVG));
            os.close();

            // The XML is stored into svg
            final String svg = new String(os.toByteArray(), Charset.forName("UTF-8"));

            // Save the SVG to a file
            saveSvgToFile(svg, "code2diagram/out/output.svg");
        } catch (IOException e) {
            // Handle the exception here
            e.printStackTrace();
        }
    }

    private static void saveSvgToFile(String svgContent, String fileName) throws IOException {
        Path filePath = Paths.get(fileName);
        Files.write(filePath, svgContent.getBytes(Charset.forName("UTF-8")));
        System.out.println("SVG saved to: " + filePath.toAbsolutePath());
    }
}