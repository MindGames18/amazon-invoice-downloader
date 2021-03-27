# Amazon Invoice Downloader - Python

Script to download invoices from Amazon.in

## Dependencies:

[Selenium]()  
[Chrome Driver v89]()

## Configurations [config.py](config.py):

`username`: Amazon.in username (usually Email ID)  
`password`: Amazon.in password  
`pages`: Number of pages from order hstory to download invoices from

## Default Behaviour:

- Defaults all downloads to your `Downloads` folders
- invoices are named `invoice.pdf` and increments (`invoice(2).pdf` and so on...)
- Sleeps included to prevent too many requests
