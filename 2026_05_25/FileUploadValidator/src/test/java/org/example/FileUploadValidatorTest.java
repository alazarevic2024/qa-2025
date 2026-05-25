package org.example;

import org.junit.Assert;
import org.junit.Test;

import java.io.File;

public class FileUploadValidatorTest {
    @Test
    public void testValidPDF() {
        FileUploadValidator validator = new FileUploadValidator();
        boolean result = validator.isValid("dokument.pdf", 2);
        Assert.assertTrue(result);
    }
    @Test
    public void testInvalidExtension() {
        FileUploadValidator validator = new FileUploadValidator();
        boolean result = validator.isValid("video.mp4", 2);
        Assert.assertFalse(result);
    }

    @Test
    public void testValidJPG() {
        FileUploadValidator validator = new FileUploadValidator();
        boolean result = validator.isValid("image.jpg", 2);
        Assert.assertTrue(result);
    }

    @Test
    public void testValidPNG() {
        FileUploadValidator validator = new FileUploadValidator();
        boolean result = validator.isValid("image.png", 2);
        Assert.assertTrue(result);
    }

    @Test
    public void testPDFSizeGreaterThenExpected() {
        FileUploadValidator validator = new FileUploadValidator();
        boolean result = validator.isValid("image.pdf",
                6);
        Assert.assertFalse(result);
    }

    @Test
    public void testPDFExpectedSize() {
        FileUploadValidator validator = new FileUploadValidator();
        boolean result = validator.isValid("image.pdf",
                5);
        Assert.assertTrue(result);
    }

    @Test
    public void testEmptyFileName() {
        FileUploadValidator validator = new FileUploadValidator();
        boolean result = validator.isValid("", 2);
        Assert.assertFalse(result);
    }

    @Test
    public void testNullValueForFile() {
        FileUploadValidator validator = new FileUploadValidator();
        boolean result = validator.isValid(null, 2);
        Assert.assertFalse(result);
    }

    // proveriti i negativnu velicinu fajla ili 0

}
