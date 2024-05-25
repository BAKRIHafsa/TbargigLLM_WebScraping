import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from application.scrapingMeth import scrapeDataFromCat0, scrapeDataFromCat1



def scraping():

        # Initialize Chrome WebDriver
        driver = webdriver.Chrome()


        # Navigate to the website
        driver.get("https://www.hespress.com")
    
        # Wait for the page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        header = driver.find_element(By.CSS_SELECTOR, "body > header")
        navbar_header = header.find_element(By.CLASS_NAME, "navbar-header")
        container = navbar_header.find_element(By.CLASS_NAME, "container")
        d_flex = container.find_element(By.CLASS_NAME, "d-flex")
        header_menu_navbar = d_flex.find_element(By.CLASS_NAME, "header-menu-nav")

        #time.sleep(40)

        try:
                # Recherchez l'élément
                bouton_annuler = driver.find_element(By.ID,"notification-popover-cancel-button")
                # Cliquez sur l'élément
                bouton_annuler.click()
                print("Bouton 'Annuler' cliqué avec succès.")
        except Exception:
                # Si l'élément n'est pas trouvé, imprimez un message
                print("Bouton 'Annuler' non trouvé.")

        # Attendre que l'élément soit cliquable
        sidebar = WebDriverWait(header_menu_navbar, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > header > div.navbar-header > div > div > div.header-menu-nav > button"))
        )

        # Cliquer sur l élément
        sidebar.click()

        try:
                # Recherchez l'élément
                bouton_annuler = driver.find_element(By.ID,"notification-popover-cancel-button")
                # Cliquez sur l'élément
                bouton_annuler.click()
                print("Bouton 'Annuler' cliqué avec succès.")
        except Exception:
                # Si l'élément n'est pas trouvé, imprimez un message
                print("Bouton 'Annuler' non trouvé.")


        try:
                # Recherchez l'élément
                bouton_annuler = driver.find_element(By.CSS_SELECTOR,"#dismiss-button")
                # Cliquez sur l'élément
                bouton_annuler.click()
                print("Bouton 'Annuler' de la pub cliqué avec succès.")
        except Exception:
                # Si l'élément n'est pas trouvé, imprimez un message
                print("Bouton 'Annuler' de la pub non trouvé.")
            

        

        menu_sidebar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "menuSidebar")))
        menu_menu_sidebar = WebDriverWait(menu_sidebar, 10).until(EC.presence_of_element_located((By.ID, "menu-menu-sidebar")))
        li_elements = menu_menu_sidebar.find_elements(By.TAG_NAME, "li")
        liste_cat =[]
        found = False
        for e in li_elements : 
            if e.text == "الأقسام" :
                found=True
            if found :
                
                    index_e = li_elements.index(e)
                    li_elements = li_elements[index_e +2: index_e + 5]
                    break
            

        # la liste des catégorie                     
        # for e in li_elements :
        #     liste_cat.append(e.text) 
            

            
        #Extraction des articles des différentes catégories
        #Catégorie : رياضة
        link_a = li_elements[0].find_element(By.TAG_NAME, "a")
        link = link_a.get_attribute("href")
        listeSport = scrapeDataFromCat0(link, li_elements[0].text)

        """ #Catégorie : منوعات
        link_a = li_elements[1].find_element(By.TAG_NAME, "a")
        link = link_a.get_attribute("href")
        listeVariés = scrapingMethods.scrapeDataFromCat1(link, li_elements[1].text) """

         #Catégorie : حوادث
        link_a = li_elements[2].find_element(By.TAG_NAME, "a")
        link = link_a.get_attribute("href")
        listesAccidents = scrapeDataFromCat1(link, li_elements[2].text)

        """ #Catégorie : 24 ساعة
        link_a = li_elements[3].find_element(By.TAG_NAME, "a")
        link = link_a.get_attribute("href")
        liste24 = scrapingMethods.scrapeDataFromCat1(link, li_elements[3].text)

        #Catégorie : سياسة
        link_a = li_elements[4].find_element(By.TAG_NAME, "a")
        link = link_a.get_attribute("href")
        listePolitique = scrapingMethods.scrapeDataFromCat1(link, li_elements[4].text)

        #Catégorie : مجتمع
        link_a = li_elements[5].find_element(By.TAG_NAME, "a")
        link = link_a.get_attribute("href")
        listeSociété = scrapingMethods.scrapeDataFromCat1(link, li_elements[5].text)

        #Catégorie : جهات
        link_a = li_elements[6].find_element(By.TAG_NAME, "a")
        link = link_a.get_attribute("href")
        listeRégions = scrapingMethods.scrapeDataFromCat1(link, li_elements[6].text)

        #Catégorie : اقتصاد
        link_a = li_elements[7].find_element(By.TAG_NAME, "a")
        link = link_a.get_attribute("href")
        listeEconomie = scrapingMethods.scrapeDataFromCat1(link, li_elements[7].text)

        #Catégorie : سيارات
        link_a = li_elements[8].find_element(By.TAG_NAME, "a")
        link = link_a.get_attribute("href")
        listeVoitures = scrapingMethods.scrapeDataFromCat1(link, li_elements[8].text)

        #Catégorie : مغاربة العالم
        link_a = li_elements[9].find_element(By.TAG_NAME, "a")
        link = link_a.get_attribute("href")
        listeMarocains = scrapingMethods.scrapeDataFromCat1(link, li_elements[9].text)

        #Catégorie : السلطة الرابعة
        link_a = li_elements[10].find_element(By.TAG_NAME, "a")
        link = link_a.get_attribute("href")
        listeSalade = scrapingMethods.scrapeDataFromCat1(link, li_elements[10].text)

        #Catégorie : فن وثقافة
        link_a = li_elements[11].find_element(By.TAG_NAME, "a")
        link = link_a.get_attribute("href")
        listeArt = scrapingMethods.scrapeDataFromCat1(link, li_elements[11].text)

        #Catégorie : تمازيغت
        link_a = li_elements[12].find_element(By.TAG_NAME, "a")
        link = link_a.get_attribute("href")
        listeTamazight = scrapingMethods.scrapeDataFromCat1(link, li_elements[12].text) """ 
        
        # Wait for user input before closing the browser
        #input("Press Enter to close the browser...")

        # Close the browser
        driver.quit()

        #Add the summary Script : 


        return listeSport, listesAccidents
      
    # , listesVariée, liste24, listePolitique, listeSociété, listeRégions, listeEconomie, listeVoitures, listeMarocains, listeSalade, listeArt, listeTamazight





            
