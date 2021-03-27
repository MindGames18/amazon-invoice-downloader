# amazon-invoice-downloader
Simple py script to help download invoice from your past orders in amazon

# Dependency
Selenium
Chrome Driver (included v89)

# Configurations (config.py)
username : Amazon username (usually email id)
password : Amazon password
pages : Number of pages from order hstory to download invoices

# ReadME 
Defaults all downloads to your downloads folders 
invoices are named invoice.pdf and increments (invoice(2).pdf and so on...)
Sleeps included to prevent too many requests