AutoTest
==============

## Pre-install
        
      sudo apt-get install python-virtualenv
      virtualenv venv
      source /venv/bin/activate
      pip install -r requirement.txt
      
## Ubuntu environment needed(optional)
  
    sudo apt-get install xvfb
    wget -N http://chromedriver.storage.googleapis.com/{Chrome_version}/chromedriver_linux64.zip
    unzip chromedriver_linux64.zip
    chmod +x chromedriver

    sudo mv -f chromedriver /usr/local/share/chromedriver
    sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
    sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
    
## Usage
- LongRun.py can perform automated testing
- withProcessing.py can use with processing by TCP/IP Socket
