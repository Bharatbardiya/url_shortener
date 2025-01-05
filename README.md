# URL Shortener Service

This project is a simplified URL shortener service that allows users to shorten URLs, track the number of accesses, and handle expired URLs. The service also supports setting an expiration date for shortened URLs. [hosted link](http://216.48.189.196/)

## Features

- **URL Shortening**: Allows users to input a long URL and get a unique shortened version.
- **Expiration Date**: Users can set an expiration date for a shortened URL. Once expired, the URL will no longer be accessible.
- **Access Count**: Tracks and displays how many times a shortened URL has been accessed.
- **Error Handling**: Gracefully handles invalid URLs, duplicate submissions, non-existent short URLs, and expired URLs.

## Setup Instructions

Follow the steps below to set up the project locally.

### 1. Clone the Repository

Clone the project repository to your local machine:

```bash
git clone https://github.com/Bharatbardiya/url_shortener
cd url_shortener
```

### 2. Set Up a Python Virtual Environment
Make sure you have a Python virtual environment set up outside of the project folder. If you don't have one, you can create and activate it with the following commands:

```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
```
### 3. Install Dependencies
Install the required Python packages using requirements.txt:

```bash
pip install -r requirements.txt
```
### 4. Apply Migrations
Run the following commands to apply the migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Set Up Cron Jobs (For Deployment)
To automate the cleanup of expired URLs, you need to set up a cron job. Run the following command to add the cron job:

```bash
python manage.py crontab add
```
This will schedule the cleanup task to run at regular intervals.

### 6. View Cron Jobs
To check the current cron jobs set up on your system, run:

```bash
python manage.py crontab show
```
### 7. Run the Cleanup Task Manually
If you want to run the cleanup task manually, you can use this command:

```bash
python manage.py cleanup_urls
```
This will remove any expired URLs that are no longer accessible.

### 8. Run the Application
To start the application locally, run:

```bash
python manage.py runserver
```
Now you can access the URL shortener service at http://127.0.0.1:8000/.

## Hosted URL
You can also try the live version of the URL shortener service here:
[URL Shortener - Live](http://216.48.189.196/)

## Handling Expired or Non-Existent URLs
If a shortened URL has expired or does not exist, the service will return an appropriate error message, such as "URL not found" or "URL has expired."

## Conclusion
This project provides a basic but functional URL shortener service with the option to track URL access counts and set expiration dates for the shortened URLs. It includes the necessary error handling for edge cases like invalid URLs and expired links.
