from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import csv

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://www.baseballamerica.com/draftdb/index.php')

selectYear = Select(driver.find_element_by_name('year'))
selectYear.select_by_value("2016")

selectRound = Select(driver.find_element_by_name('round'))
selectRound.select_by_index(0)

search = driver.find_element_by_id('search500')
search.click()

time.sleep(5)
tableDiv = driver.find_elements_by_class_name('column-one')

if len(tableDiv) == 1:
    print "okay"
else:
    print "keep looking"

table = tableDiv[0].find_elements_by_tag_name('table')

if len(table) == 1:
    print "OK"
else:
    print "keep looking"


evenRows = tableDiv[0].find_elements_by_class_name("evenRow")
oddRows = tableDiv[0].find_elements_by_class_name("oddRow")

allRows = evenRows + oddRows

print(len(allRows))


with open('draft.csv', 'w') as f:
    csvwriter = csv.writer(f)
    headers = ['rnd', 'pick', 'team', 'player', 'pos', 'school', 'state', 'bonus']
    csvwriter.writerow(headers)
    for row in allRows:
        columns = row.find_elements_by_tag_name('td')
        rnd = columns[0].text
        pick = columns[1].text
        team = columns[2].text
        player = columns[3].text
        pos = columns[4].text
        school = columns[5].text
        state = columns[6].text
        bonus = columns[7].text
        tempList = [rnd, pick, team, player, pos, school, state, bonus]
        csvwriter.writerow(tempList)




print("Complete")
