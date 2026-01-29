# webscraper


### Webscraper is a web scraping tool that uses Selenium to scrape data from websites.
### In this project we are scraping data from quotes.toscrape.com, a website that contains quotes from famous people. Good for learning purposes.


## Steeps to run the aplication:

1. Install the environment:

```bash
cd webscraper
```

### For MAC
```bash
python3 -m venv venv && source venv/bin/activate && python -m pip install --upgrade pip
```

#### For WINDOWS

```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

### Install the requirements:
```bash
pip install -r requirements.txt
```

### If we want to run the scraper, we need to run the following command:

If you just want to run the scraper, you can run the following command:
Go to the directory where the manage.py file is located and run the following command:


```bash
cd webscraper 
cd webscraper_project
```

```bash
python3 manage.py scraper
```


For Django server:
 If we want to run the server, we need to run the following command:
 Go to the directory where the manage.py file is located and run the following command:

```bash
 cd webscraper 
 cd webscraper_project
```

```bash
 python3 manage.py runserver
```

 If we want to create a superuser, we need to run the following command:
```bash
 python3 manage.py createsuperuser
```

 Then we can access the admin panel at:

 ```bash
 http://127.0.0.1:8000/admin/
 ```

