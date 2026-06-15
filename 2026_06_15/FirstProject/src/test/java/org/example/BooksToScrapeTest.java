package org.example;

import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

import static java.awt.SystemColor.window;

public class BooksToScrapeTest {

    @Test
    public void openTravelCategoryAndFirstBook() {
        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();

        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(15));
        driver.get("https://books.toscrape.com/");

        // locirati kategoriju travel
        WebElement travelCategoryLink = wait.until(
                ExpectedConditions.elementToBeClickable(
                        By.xpath("//a[normalize-space()='Travel']")
                )
        );

        travelCategoryLink.click();

        // nadji prvu knjigu i klikni na nju
        WebElement firstBookLink = wait.until(
                ExpectedConditions.elementToBeClickable(
                        By.cssSelector("article.product_pod h3 a")
                )
        );

        // ocekivani naslov sa liste knjiga
        String expectedBookTitle = firstBookLink.getAttribute("title");

        // klik na knjigu
        firstBookLink.click();

        // dobavljamo h1 element
        WebElement actualBookTitle = wait.until(
                ExpectedConditions.visibilityOfElementLocated(By.cssSelector(".product_main h1"))
        );

        // Izvlacimo tekst iz h1
        String actualBookTitleValue = actualBookTitle.getText();

        Assert.assertEquals(actualBookTitleValue, expectedBookTitle);

        driver.quit();
    }

}
