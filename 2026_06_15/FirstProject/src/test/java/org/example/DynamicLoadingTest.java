package org.example;

import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class DynamicLoadingTest {

    @Test
    public void dynamicLoadingExampleTest() {
        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();

        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1");

        // Trazi dugme
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(15));

        WebElement startButton = wait.until(
            ExpectedConditions.elementToBeClickable(By.xpath("//button[normalize-space()='Start']"))
        );

        startButton.click();

        WebElement result = wait.until(
                ExpectedConditions.elementToBeClickable(By.id("finish"))
        );

        String resultText = result.getText();

        Assert.assertEquals("Hello World!", resultText);

        driver.quit();
    }
}
