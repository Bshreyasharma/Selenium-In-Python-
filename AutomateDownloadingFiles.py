from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
df_file= pd.read_csv('training_data_classification_labels.csv')
chromeOptions = Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory":"G:\BrainClassification\ANew"})
driver = webdriver.Chrome("./CromeDriver/chromedriver_win32/chromedriver.exe",chrome_options=chromeOptions)
driver.get("http://miccai2019-data.eastus.cloudapp.azure.com/CPM-RadPath_2019_Training_Data/Radiology/")
print(driver.title)
file_list=list(df_file['CPM_RadPath_2019_ID'])
current_File='CPM19_CBICA_AMN_1'
index_current = file_list.index('CPM19_CBICA_AMN_1')
#Download the file
for file_name in range(index_current+1,len(file_list)):
    filename = file_list[file_name]
    path_link = filename + '/'
    flair_image = filename + "_flair.nii.gz"
    t1_image = filename + "_t1.nii.gz"
    t1ce_image = filename + "_t1ce.nii.gz"
    t2_image = filename + "_t2.nii.gz"

    driver.find_element_by_link_text(path_link).click()
    driver.implicitly_wait(7)
    driver.find_element_by_link_text(flair_image).click()
    driver.implicitly_wait(7)
    driver.find_element_by_link_text(t1_image).click()
    driver.implicitly_wait(7)
    driver.find_element_by_link_text(t1ce_image).click()
    driver.implicitly_wait(7)
    driver.find_element_by_link_text(t2_image).click()
    driver.execute_script("window.history.go(-1)")


#To download the link