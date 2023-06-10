from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from undetected_chromedriver import Chrome, ChromeOptions
import time
import csv

options = ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = Chrome(options=options, executable_path=ChromeDriverManager().install())

driver.maximize_window()

component_Careers_page_URL = []
component_Careers_page_source = []
component_Application_form_URL = []
component_Job_page_URL = []
component_Jobs_page_source = []

##################################################################################################################
driver.get("https://www.ethosbc.com/")
# time.sleep(10)

Company_name = "Ethos BeathChapman"

Careers_page_URL = driver.find_elements(By.CLASS_NAME, "mayon-arrow-btn-blue")[1].find_element(By.TAG_NAME, "a").get_attribute("href")

Careers_page = driver.get(Careers_page_URL)
Careers_page_source = driver.page_source

driver.get("https://www.ethosbc.com/")
Job_page_URL = driver.find_elements(By.CLASS_NAME, "top_jobs")[0].find_element(By.TAG_NAME, "a").get_attribute("href")

Jobs_page = driver.get(Job_page_URL)
Jobs_page_source = driver.page_source

Application_form_URL = driver.find_elements(By.CLASS_NAME, "job-apply-now-link")[0].find_element(By.TAG_NAME, "a").get_attribute("href")

component_Careers_page_URL.append(Careers_page_URL)
component_Careers_page_source.append(Careers_page_source)
component_Application_form_URL.append(Application_form_URL)
component_Job_page_URL.append(Job_page_URL)
component_Jobs_page_source.append(Jobs_page_source)

dict = {'Company Name': Company_name, 'URL': "https://www.ethosbc.com/", 'Careers page URL': component_Careers_page_URL, 'Careers page source': component_Careers_page_source, 'Application form URL': component_Application_form_URL, 'Job page URL': component_Job_page_URL, 'Jobs page source': component_Jobs_page_source}
df = pd.DataFrame(dict)

df.to_csv('Result.csv', index = False)

# ############################################################################################################################

Company_name = "IGNITE"
Careers_page_URL = "https://www.igniteco.com/careers/"
Careers_page = driver.get(Careers_page_URL)
Careers_page_source = driver.page_source
Application_form_URL = "https://www.aptrack.co/uap/AAABagAPWfsCAZ7j/#apply"
Job_page_URL = "https://www.igniteco.com/job-search/"
Jobs_page = driver.get(Job_page_URL)
Jobs_page_source = driver.page_source

# Open the CSV file in append mode
with open('Result.csv', mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)

    # Write the new row to the CSV file
    writer.writerow([Company_name, "https://www.igniteco.com/", Careers_page_URL, Careers_page_source, Application_form_URL, Job_page_URL, Jobs_page_source])

########################################################################################################################################

driver.get("https://franklinsmithgroup.co.nz/")

Company_name = "Franklin Smith"

Careers_page_URL = driver.find_elements(By.CLASS_NAME, "menu-item-4018")[0].find_element(By.TAG_NAME, "a").get_attribute("href")

Careers_page = driver.get(Careers_page_URL)
Careers_page_source = driver.page_source

driver.get("https://franklinsmithgroup.co.nz/")
Job_page_URL = driver.find_elements(By.CLASS_NAME, "menu-item-4074")[0].find_element(By.TAG_NAME, "a").get_attribute("href")

Jobs_page = driver.get(Job_page_URL)
Jobs_page_source = driver.page_source

# Application_form_URL = "https://franklinsmithgroup.co.nz/jobs/maintenance-manager/"
Application_form_URL = driver.find_elements(By.CLASS_NAME, "matador-job-title")[0].find_element(By.TAG_NAME, "a").get_attribute("href")

# Open the CSV file in append mode
with open('Result.csv', mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)

    # Write the new row to the CSV file
    writer.writerow([Company_name, "https://franklinsmithgroup.co.nz/", Careers_page_URL, Careers_page_source, Application_form_URL, Job_page_URL, Jobs_page_source])

# #########################################################################################################################################


driver.get("https://www.bluefinresources.com.au/")

Company_name = "Bluefin Resources"

Careers_page_URL = driver.find_element(By.XPATH, '//*[@id="b_navigation"]/ul/li[2]/ul/li[1]').find_element(By.TAG_NAME, "a").get_attribute("href")

Careers_page = driver.get(Careers_page_URL)
Careers_page_source = driver.page_source

driver.get("https://www.bluefinresources.com.au/")
Application_form_URL = driver.find_element(By.XPATH, '//*[@id="b_navigation"]/ul/li[4]/ul/li[8]').find_element(By.TAG_NAME, "a").get_attribute("href")

Job_page_URL = "https://www.bluefinresources.com.au/advancedsearch.aspx?search=1"

Jobs_page = driver.get(Job_page_URL)
Jobs_page_source = driver.page_source

# Open the CSV file in append mode
with open('Result.csv', mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)

    # Write the new row to the CSV file
    writer.writerow([Company_name, "https://www.bluefinresources.com.au/", Careers_page_URL, Careers_page_source, Application_form_URL, Job_page_URL, Jobs_page_source])

#######################################################################################################################################

driver.get("https://www.sbrecruitment.com/")

Company_name = "SB Recruitment"

Careers_page_URL = driver.find_element(By.XPATH, '//*[@id="b_navigation"]/ul/li[2]/ul/li[1]').find_element(By.TAG_NAME, "a").get_attribute("href")

Careers_page = driver.get(Careers_page_URL)
Careers_page_source = driver.page_source

driver.get("https://www.sbrecruitment.com/")
Job_page_URL = driver.find_element(By.XPATH, '//*[@id="1049841281"]/ul/li[2]').find_element(By.TAG_NAME, "a").get_attribute("href")

Jobs_page = driver.get(Job_page_URL)
Jobs_page_source = driver.page_source

Application_form_URL = driver.find_element(By.XPATH, '//*[@id="1228438648"]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]').find_element(By.TAG_NAME, "a").get_attribute("href")

# Open the CSV file in append mode
with open('Result.csv', mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)

    # Write the new row to the CSV file
    writer.writerow([Company_name, "https://www.bluefinresources.com.au/", Careers_page_URL, Careers_page_source, Application_form_URL, Job_page_URL, Jobs_page_source])

#######################################################################################################################################

Company_name = "Fuse Recruitment"
Careers_page_URL = "https://www.fuserecruitment.com/about"
Careers_page = driver.get(Careers_page_URL)
Careers_page_source = driver.page_source
Application_form_URL = "https://www.fuserecruitment.com/job-application?jobID=18ee811b-a22e-46de-9791-2a068be5afb9"
Job_page_URL = "https://www.fuserecruitment.com/job-results"
Jobs_page = driver.get(Job_page_URL)
Jobs_page_source = driver.page_source

# Open the CSV file in append mode
with open('Result.csv', mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)

    # Write the new row to the CSV file
    writer.writerow([Company_name, "https://www.fuserecruitment.com/", Careers_page_URL, Careers_page_source, Application_form_URL, Job_page_URL, Jobs_page_source])

########################################################################################################################################

Company_name = "Core Talent"
Careers_page_URL = "https://www.coretalent.com.au/about-us/"
Careers_page = driver.get(Careers_page_URL)
Careers_page_source = driver.page_source
Application_form_URL = "https://www.aplitrak.com/?adid=ZGFubnkuc3RlcGhlbnNvbi44OTExMC42OTkxQGNvcmV0YWxlbnRhdS5hcGxpdHJhay5jb20"
Job_page_URL = "https://www.coretalent.com.au/candidates/browse-jobs/"
Jobs_page = driver.get(Job_page_URL)
Jobs_page_source = driver.page_source

# Open the CSV file in append mode
with open('Result.csv', mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)

    # Write the new row to the CSV file
    writer.writerow([Company_name, "https://www.coretalent.com.au/", Careers_page_URL, Careers_page_source, Application_form_URL, Job_page_URL, Jobs_page_source])

########################################################################################################################################

Company_name = "Healthcare Professionals Group"
Careers_page_URL = "https://www.hpgconnect.com/about"
Careers_page = driver.get(Careers_page_URL)
Careers_page_source = driver.page_source
Application_form_URL = "https://www.hpgconnect.com/job/marketing-associate-director-1/apply"
Job_page_URL = "https://www.hpgconnect.com/jobs"
Jobs_page = driver.get(Job_page_URL)
Jobs_page_source = driver.page_source

# Open the CSV file in append mode
with open('Result.csv', mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)

    # Write the new row to the CSV file
    writer.writerow([Company_name, "https://www.hpgconnect.com/", Careers_page_URL, Careers_page_source, Application_form_URL, Job_page_URL, Jobs_page_source])

########################################################################################################################################

Company_name = "Enterprise IT Resources"
Careers_page_URL = "https://www.eitr.com.au/about"
Careers_page = driver.get(Careers_page_URL)
Careers_page_source = driver.page_source
Application_form_URL = "https://www.eitr.com.au/job-application?jobID=7b8f3801-3bdb-40b2-a6ff-d87c2edea60d"
Job_page_URL = "https://www.eitr.com.au/permanent"
Jobs_page = driver.get(Job_page_URL)
Jobs_page_source = driver.page_source

# Open the CSV file in append mode
with open('Result.csv', mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)

    # Write the new row to the CSV file
    writer.writerow([Company_name, "https://www.eitr.com.au/", Careers_page_URL, Careers_page_source, Application_form_URL, Job_page_URL, Jobs_page_source])

########################################################################################################################################

Company_name = "12 Wizards"
Careers_page_URL = "No page"
# Careers_page = driver.get(Careers_page_URL)
Careers_page_source = "None"
Application_form_URL = "No page"
Job_page_URL = "No page"
# Jobs_page = driver.get(Job_page_URL)
Jobs_page_source = "None"

# Open the CSV file in append mode
with open('Result.csv', mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)

    # Write the new row to the CSV file
    writer.writerow([Company_name, "No Company", Careers_page_URL, Careers_page_source, Application_form_URL, Job_page_URL, Jobs_page_source])

########################################################################################################################################

Company_name = "ADVA Optical Networking"
Careers_page_URL = "https://www.adva.com/en/about-us/careers"
Careers_page = driver.get(Careers_page_URL)
Careers_page_source = driver.page_source
Application_form_URL = "https://www.adva.com/en/about-us/contact"
Job_page_URL = "https://www.adva.com/en/about-us/investors"
Jobs_page = driver.get(Job_page_URL)
Jobs_page_source = driver.page_source

# Open the CSV file in append mode
with open('Result.csv', mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)

    # Write the new row to the CSV file
    writer.writerow([Company_name, "https://www.adva.com/en", Careers_page_URL, Careers_page_source, Application_form_URL, Job_page_URL, Jobs_page_source])

########################################################################################################################################

Company_name = "Crunchbase"
Careers_page_URL = "https://about.crunchbase.com/about-us/careers/"
Careers_page = driver.get(Careers_page_URL)
Careers_page_source = driver.page_source
Application_form_URL = "https://www.sbrecruitment.com/job-application?jobID=6199d6b9-6267-4c81-9f6c-1073b1de92f9"
Job_page_URL = "Not jobsite"
# Jobs_page = driver.get(Job_page_URL)
Jobs_page_source = "None"

# Open the CSV file in append mode
with open('Result.csv', mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)

    # Write the new row to the CSV file
    writer.writerow([Company_name, "https://www.crunchbase.com/organization/adzonesocial", Careers_page_URL, Careers_page_source, Application_form_URL, Job_page_URL, Jobs_page_source])

########################################################################################################################################

Company_name = "AeroCRS"
Careers_page_URL = "https://www.aerocrs.com/about-aerocrs/"
Careers_page = driver.get(Careers_page_URL)
Careers_page_source = driver.page_source
Application_form_URL = "https://www.aerocrs.com/customers/start-trial/"
Job_page_URL = "Not Jobsite"
# Jobs_page = driver.get(Job_page_URL)
Jobs_page_source = "None"

# Open the CSV file in append mode
with open('Result.csv', mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)

    # Write the new row to the CSV file
    writer.writerow([Company_name, "https://www.aerocrs.com/", Careers_page_URL, Careers_page_source, Application_form_URL, Job_page_URL, Jobs_page_source])

########################################################################################################################################

Company_name = "affiliaXe"
Careers_page_URL = "https://www.affiliaxe.com/aboutus.php"
Careers_page = driver.get(Careers_page_URL)
Careers_page_source = driver.page_source
Application_form_URL = "https://www.affiliaxe.com/New-Advertiser-Signup.php"
Job_page_URL = "Not jobsite"
# Jobs_page = driver.get(Job_page_URL)
Jobs_page_source = "None"

# Open the CSV file in append mode
with open('Result.csv', mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)

    # Write the new row to the CSV file
    writer.writerow([Company_name, "https://www.affiliaxe.com/", Careers_page_URL, Careers_page_source, Application_form_URL, Job_page_URL, Jobs_page_source])

########################################################################################################################################

Company_name = "Affilomania"
Careers_page_URL = "https://www.affilomania.com/careers"
Careers_page = driver.get(Careers_page_URL)
Careers_page_source = driver.page_source
Application_form_URL = "No page"
Job_page_URL = "https://www.affilomania.com/JobDetails/12"
Jobs_page = driver.get(Job_page_URL)
Jobs_page_source = driver.page_source

# Open the CSV file in append mode
with open('Result.csv', mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)

    # Write the new row to the CSV file
    writer.writerow([Company_name, "https://www.affilomania.com/", Careers_page_URL, Careers_page_source, Application_form_URL, Job_page_URL, Jobs_page_source])

########################################################################################################################################

Company_name = "Affilroi"
Careers_page_URL = "https://home.affilroi.com/en/"
Careers_page = driver.get(Careers_page_URL)
Careers_page_source = driver.page_source
Application_form_URL = "https://home.affilroi.com/en/"
Job_page_URL = "No jobsite"
# Jobs_page = driver.get(Job_page_URL)
Jobs_page_source = "None"

# Open the CSV file in append mode
with open('Result.csv', mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)

    # Write the new row to the CSV file
    writer.writerow([Company_name, "https://home.affilroi.com/en/", Careers_page_URL, Careers_page_source, Application_form_URL, Job_page_URL, Jobs_page_source])

########################################################################################################################################

Company_name = "Agora"
Careers_page_URL = "https://www.agora.io/en/careers/"
Careers_page = driver.get(Careers_page_URL)
Careers_page_source = driver.page_source
Application_form_URL = "No page"
Job_page_URL = "No jobsite"
# Jobs_page = driver.get(Job_page_URL)
Jobs_page_source = "None"

# Open the CSV file in append mode
with open('Result.csv', mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)

    # Write the new row to the CSV file
    writer.writerow([Company_name, "https://www.agora.io/en/", Careers_page_URL, Careers_page_source, Application_form_URL, Job_page_URL, Jobs_page_source])

########################################################################################################################################

Company_name = "AIROBOTICS"
Careers_page_URL = "https://www.airoboticsdrones.com/company/"
Careers_page = driver.get(Careers_page_URL)
Careers_page_source = driver.page_source
Application_form_URL = "https://www.airoboticsdrones.com/contact-us/"
Job_page_URL = "No jobsite"
# Jobs_page = driver.get(Job_page_URL)
Jobs_page_source = "None"

# Open the CSV file in append mode
with open('Result.csv', mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)

    # Write the new row to the CSV file
    writer.writerow([Company_name, "https://www.airoboticsdrones.com/", Careers_page_URL, Careers_page_source, Application_form_URL, Job_page_URL, Jobs_page_source])

########################################################################################################################################

Company_name = "LHH"
Careers_page_URL = "https://www.lhh.com/us/en/about-us/careers/"
Careers_page = driver.get(Careers_page_URL)
Careers_page_source = driver.page_source
Application_form_URL = "https://www.lhh.com/us/en/job/oakland/accounts-payable-clerk/us_en_27_849088_2983179/"
Job_page_URL = "https://www.lhh.com/us/en/search-jobs/"
Jobs_page = driver.get(Job_page_URL)
Jobs_page_source = driver.page_source

# Open the CSV file in append mode
with open('Result.csv', mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)

    # Write the new row to the CSV file
    writer.writerow([Company_name, "https://www.ajilon.com/", Careers_page_URL, Careers_page_source, Application_form_URL, Job_page_URL, Jobs_page_source])

########################################################################################################################################

Company_name = "Akamai"
Careers_page_URL = "https://www.akamai.com/careers"
Careers_page = driver.get(Careers_page_URL)
Careers_page_source = driver.page_source
Application_form_URL = "https://www.akamai.com/why-akamai/contact-us/contact-sales"
Job_page_URL = "No jobsite"
# Jobs_page = driver.get(Job_page_URL)
Jobs_page_source = "None"

# Open the CSV file in append mode
with open('Result.csv', mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)

    # Write the new row to the CSV file
    writer.writerow([Company_name, "https://www.akamai.com/", Careers_page_URL, Careers_page_source, Application_form_URL, Job_page_URL, Jobs_page_source])

########################################################################################################################################

print('Data appended to CSV file.')