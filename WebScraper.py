from fpdf import FPDF
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
start_time = time.time()

#Lets grab the contents of the config file
config = open("config.txt")
lines = config.readlines()
config.close()

#Now we can configure our parameters:
params = {'driver' : '', 'targetUrl' : '', 'username' : '', 'password' : '', 'images' : '', 'startImage' : '', 'dlLocation' : ''}
strings = ['driver', 'targetUrl', 'username', 'password', 'dlLocation']
for line in lines:
    if '=' in line:
        left = line.split(' =')[0]
        right = line.split(' =')[1].strip()
        if left in params and left in strings:
            params[left] = right
        elif left in params:
            params[left] = int(right)

browser = webdriver.Chrome(params['driver'])
browser.get(params['targetUrl'])
By = webdriver.common.by.By()

#Lets login!
browser.find_element_by_id("username").send_keys(params['username'])
browser.find_element_by_id("password").send_keys(params['password'])

#Since we cannot find the login button by id, lets isolate it from the list of the login forms. It should always be the 3rd element
browser.find_elements_by_class_name("form-group")[2].click()
browser.find_element(By.CSS_SELECTOR, "a[href*='/book/read']").click()

#Now we need to switch to the eReader's new tab. This should always be the 2nd tab
#but first lets wait for the tab to fully load the first image
import time
time.sleep(10) 
eReader = browser.window_handles[1]
browser.switch_to_window(eReader)

#If the user was last seen in the eReader at a different location, the eReader will prompt to start at the last image
#we want to start at the cover, so lets say no
try:
    browser.find_element_by_class_name("location-history-options-button").click()
except:
    #if its not there we don't care and just continue as normal
    pass

#Lets get our container ready for the pdf:
pdf = FPDF('P', 'mm', 'A4')
pdf.set_auto_page_break(0)

#Now that we're in the reader lets individually grab the image element, crop and save it's png and then click continue to the next image
counter = 0
while counter < (params['images'] + params['startImage']):
    if params['startImage'] <= counter:
        time.sleep(3) 
        Img = browser.find_element_by_class_name("page-" + str(counter + 1))
        im = Image.open(BytesIO(Img.screenshot_as_png))
        im = im.crop((0, 34, 743, 907))
        im.save(params['dlLocation'] + '/screenshotOfImage' + str(counter) + '.png')
        pdf.add_page()
        pdf.image(params['dlLocation'] + '/screenshotOfImage' + str(counter) + '.png', 0, 0, 231)
    browser.find_element_by_class_name("ion-ios7-arrow-right").click()
    counter += 1
    #It'll slow things down but we need to make sure that all the images are loaded before the image is taken

#Lets build the pdf!
#finally, lets save the pdf
pdf.output(params['dlLocation'] + "/Build.pdf" ,"F")

print("Build time(s): ")
print(str(time.time()-start_time) + " seconds")