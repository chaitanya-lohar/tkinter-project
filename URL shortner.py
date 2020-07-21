import pyshorteners

url=input("Enter Url----->")
shorts=pyshorteners.Shortener().tinyurl.short(url)
print(shorts)