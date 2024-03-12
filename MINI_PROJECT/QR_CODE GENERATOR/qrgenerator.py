import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "www.linkedin.com/in/shubham-nikam-2b8887286"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("shubhamlinkedin.svg", scale = 8) 
