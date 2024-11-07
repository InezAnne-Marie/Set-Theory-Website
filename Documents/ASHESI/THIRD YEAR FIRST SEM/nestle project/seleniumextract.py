import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Ensure VADER is set up
nltk.download("vader_lexicon")
sid = SentimentIntensityAnalyzer()

# Set up WebDriver with Service
driver_path = r"C:\Users\Skippy\Documents\ASHESI\THIRD YEAR FIRST SEM\nestle project\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Logging in
print("Logging into LinkedIn...")
driver.get("https://www.linkedin.com/login")
time.sleep(400)  # Give yourself time to log in manually

# Navigate to search results
driver.get("https://www.linkedin.com/search/results/content/?keywords=Nestle")
print("Navigated to LinkedIn search results for 'Nestle'")
time.sleep(30)  # Wait for the page to load

# Find posts and start scraping
print("Finding posts on the page...")
posts = driver.find_elements(
    By.CLASS_NAME, "your-target-class"
)  # Replace with actual class name

# Initialize an empty list to store the extracted text and sentiment scores
linkedin_data = []

# Loop through each post and extract the text content
for post in posts:
    try:
        # Extract the main text content of the post
        # Replace 'post-content-class' with the actual class name for the post content on LinkedIn
        text = post.find_element(By.CLASS_NAME, "post-content-class").text

        # Calculate the sentiment score using VADER
        sentiment_score = sid.polarity_scores(text)["compound"]

        # Print feedback
        print(
            "Extracted Post:", text[:50], "..."
        )  # Print first 50 characters of the post
        print("Sentiment Score:", sentiment_score)

        # Append the text and sentiment score as a dictionary to the linkedin_data list
        linkedin_data.append({"text": text, "sentiment": sentiment_score})

    except Exception as e:
        # If there's an error (like an element not found), print it and continue
        print("Error while extracting post:", e)

# Check how many posts were scraped
print("Total posts scraped:", len(linkedin_data))

# Save to CSV and confirm
linkedin_df = pd.DataFrame(linkedin_data)
linkedin_df.to_csv("linkedin_sentiments.csv", index=False)
print("Data saved to 'linkedin_sentiments.csv'")

# Close the WebDriver session
driver.quit()
