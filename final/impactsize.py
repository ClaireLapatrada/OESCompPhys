from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import matplotlib.pyplot as plt
import time
import numpy as np

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://down2earth.eu/impact_calculator/planet.html?lang=en-US")
move = ActionChains(driver)
pds = []
depths = []
dias = []

search_box = driver.find_element(By.XPATH, '//*[@id="Earth"]/img')
search_box.click()
search_box = driver.find_element(By.XPATH, '//*[@id="StartButton"]')
search_box.click()
en2 = driver.find_element(By.XPATH, '//*[@id="ProjectileVelocitySlider"]')
move.click_and_hold(en2).move_by_offset(2, 0).release().perform()

for i in range(10):
    en =  driver.find_element(By.XPATH, '//*[@id="ProjectileSizeSlider"]')
    move.click_and_hold(en).move_by_offset(2, 0).release().perform()
    pd = driver.find_element(By.XPATH, '//*[@id="ProjectileValue"]')
    pds.append(int(pd.text[0:4]))
    print(f"Projectile dia: {pd.text[0:4]}")
    time.sleep(1)
    clect = driver.find_element(By.XPATH, '//*[@id="cpPjDens"]')
    clect.click()
    clect2 = driver.find_element(By.XPATH, '//*[@id="pjd_op3"]')
    clect2.click()
    time.sleep(1)
    clect = driver.find_element(By.XPATH, '//*[@id="cpTgDens"]')
    clect.click()
    clect2 = driver.find_element(By.XPATH, '//*[@id="tgd_op2"]')
    clect2.click()
    time.sleep(1)
    go = driver.find_element(By.XPATH, '//*[@id="BT_Submit"]')
    go.click()
    time.sleep(1)
    depth = driver.find_element(By.XPATH, '//*[@id="ImpactValuesTable"]/tr[1]/td[2]')
    dia = driver.find_element(By.XPATH, '//*[@id="ImpactValuesTable"]/tr[2]/td[2]')
    depths.append(int(depth.text[0:5]))
    dias.append(int(dia.text[0:6]))
    print(f"Depth: {depth.text}")
    print(f"Dias: {dia.text}")
    time.sleep(1)
    back = driver.find_element(By.XPATH, '//*[@id="BT_Back"]')
    back.click()
    time.sleep(1)
driver.close()

print(pds, depths, dias)
x = np.array([pds])
y1 = np.array([depths])
y2 = np.array([dias])

a, b = np.polyfit(x, y1, 1)
print(a,b)
print(f"{a}x + {b} where x is the diameter of the impactor")
plt.scatter(x,y1)
plt.plot(x, a*x+b)
plt.show()

a, b = np.polyfit(x, y2, 1)
print(a,b)
print(f"{a}x + {b} where x is the diameter of the impactor")
plt.scatter(x,y2)
plt.plot(x, a*x+b)
plt.show()