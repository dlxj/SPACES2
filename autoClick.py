# windows
# pip install pygetwindow==0.0.1
# pip install pyautogui===0.9.0

import pyautogui as pygui
import time

print( pygui.position() )

while True:
    pygui.moveTo(555,555,15)
    # time.sleep(10)
    pygui.moveTo(333,333,15)
    # time.sleep(10)
    pygui.moveTo(666,666,15)
    # time.sleep(10)

    pygui.moveTo(1711,184,15) # win10 colab busy button
    pygui.click(x=1711, y=184, clicks=2, interval=10, button='left') # # win10 colab busy button


"""
for chrome - f12

# start()开始
# stop()结束

function getElementByXpath(path) {
       return document.evaluate(path, document, null, 
       XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}
 
function reconnect(){
	  console.log('working')
	  getElementByXpath("//div[@id='top-toolbar']/colab-connect-button").click()
}
var a = setInterval(reconnect, 1*60*1000);
function stop(){
	 clearInterval(a)
}
function start(){
	 a = setInterval(reconnect, 1*60*1000);
}
"""