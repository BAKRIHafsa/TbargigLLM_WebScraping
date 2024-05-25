from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import google.generativeai as genai
import os

def scrapeDataFromCat0(link,categorie) : 
  driver = webdriver.Chrome()
  titres={}
  liens={}
  imgsSources={}
  dates={}
  contenus={}
  auteurs={}
  resumes={}
  try:
    
    driver.get(link)
 
    #FIND THE CARDS
    main_content = driver.find_element(By.CLASS_NAME, "main-content") 
    posts_row = main_content.find_element(By.CSS_SELECTOR, "body > main > section.container-fluid.section")
   
    for i in range(1,3) :
        card = posts_row.find_element(By.CSS_SELECTOR, f"body > main > section.container-fluid.section > div > div.loop-category > div.posts-categoy.row.row-cols-1.row-cols-md-3 > div:nth-child({i})")
        overlay_card = card.find_element(By.CSS_SELECTOR, f"body > main > section.container-fluid.section > div > div.loop-category > div.posts-categoy.row.row-cols-1.row-cols-md-3 > div:nth-child({i}) > div" )
        cover = overlay_card.find_element(By.CSS_SELECTOR, f"body > main > section.container-fluid.section > div > div.loop-category > div.posts-categoy.row.row-cols-1.row-cols-md-3 > div:nth-child({i}) > div > div")

        #Extract the titles
        card_body = cover.find_element(By.CLASS_NAME, "card-body")
        card_details = card_body.find_element(By.CLASS_NAME, "card-details")
        card_title = card_details.find_element(By.CLASS_NAME, "card-title")
        titres[str(i)] = card_title.text
      

        #Extract the links to the article
        card_img = cover.find_element(By.CLASS_NAME, "card-img-top")
        link_tag = card_img.find_element(By.TAG_NAME, "a")
        link_ = link_tag.get_attribute("href")
        liens[str(i)] = link_

        #Extract the images of the articles
        img_class = link_tag.find_element(By.CLASS_NAME, "ratio-medium")
        img_tag = img_class.find_element(By.TAG_NAME, "img")
        img_src = img_tag.get_attribute("src")
        imgsSources[str(i)] = img_src

        #Extract the date : 
        card_text = card_body.find_element(By.CLASS_NAME, "card-text")
        date_card = card_text.find_element(By.CLASS_NAME, "date-card")
        date_article = date_card.find_element(By.CSS_SELECTOR, f"body > main > section.container-fluid.section > div > div.loop-category > div.posts-categoy.row.row-cols-1.row-cols-md-3 > div:nth-child({i}) > div > div > div.card-body > div > div > span > small")
        dates[str(i)] = date_article.text

        #Extract content + author
        driver.get(link_)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.container-fluid.main-content")))
        class1 = driver.find_element(By.CSS_SELECTOR, "body > div.container-fluid.main-content")
        class2 = class1.find_element(By.ID, "posts")
        class3 = class2.find_element(By.ID, "main-page-content")
        class4 = class3.find_element(By.CLASS_NAME, "row-content")
        class5 = class4.find_element(By.CLASS_NAME, "article-container")
        class6 = class5.find_element(By.CLASS_NAME, "apost")
        article = class6.find_element(By.CLASS_NAME, "article-content")
        contenus[str(i)] = article.text


        #Résumé du Contenu
        genai.configure(api_key=os.environ["API_KEY"])
        model = genai.GenerativeModel('gemini-pro')
        text = article.text
        response_translation = model.generate_content("translate this into english : " +  text)
#print(response_translation.text)
        response_summary = model.generate_content("summarize this  : " +  response_translation.text)
#print(response_summary.text)
        response = model.generate_content("translate this into arabic  : " +  response_summary.text)
        print("le résumé est : ", response.text)
        resumes[str(i)]=response.text


        author_ = class6.find_element(By.CLASS_NAME, "author")
        author__ = author_.find_element(By.TAG_NAME, "a")
        authorName = author__.get_attribute("text")
        auteurs[str(i)] = authorName

      
        #Return to the main page
        driver.get(link)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        main_content = driver.find_element(By.CLASS_NAME, "main-content") 
        posts_row = driver.find_element(By.CSS_SELECTOR, "body > main > section.container-fluid.section")
        
  except Exception as e:
    print(f"Error: {e}")
  # Close the WebDriver
  driver.quit()
  return titres, liens, imgsSources, dates, contenus, auteurs, categorie, resumes





def scrapeDataFromCat1(link, categorie) : 
  driver = webdriver.Chrome()
  titres={}
  liens={}
  imgsSources={}
  dates={}
  contenus={}
  auteurs={}
  resumes={}
  try:
    
    driver.get(link)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    #FIND THE CARDS
    posts_row = driver.find_element(By.CSS_SELECTOR, " #main-page-content > div.posts-categoy.row")
   

   
    for i in range(1,3) :
        card = posts_row.find_element(By.CSS_SELECTOR, f"#main-page-content > div.posts-categoy.row > div:nth-child({i})")
        overlay_card = card.find_element(By.CSS_SELECTOR, f"#main-page-content > div.posts-categoy.row > div:nth-child({i}) > div" )
        cover = overlay_card.find_element(By.CSS_SELECTOR, f"#main-page-content > div.posts-categoy.row > div:nth-child({i}) > div > div")

        #Extract the titles
        card_body = cover.find_element(By.CLASS_NAME, "card-body")
        card_details = card_body.find_element(By.CLASS_NAME, "card-details")
        card_title = card_details.find_element(By.CLASS_NAME, "card-title")
        titres[str(i)] = card_title.text

        #Extract the links to the article
        card_img = cover.find_element(By.CLASS_NAME, "card-img-top")
        link_tag = card_img.find_element(By.TAG_NAME, "a")
        link_ = link_tag.get_attribute("href")
        liens[str(i)] = link_

        #Extract the images of the articles
        img_class = link_tag.find_element(By.CLASS_NAME, "ratio-medium")
        img_tag = img_class.find_element(By.TAG_NAME, "img")
        img_src = img_tag.get_attribute("src")
        imgsSources[str(i)] = img_src

        #Extract the date : 
        card_text = card_body.find_element(By.CLASS_NAME, "card-text")
        date_card = card_text.find_element(By.CLASS_NAME, "date-card")
        date_article = date_card.find_element(By.CSS_SELECTOR, f"#main-page-content > div.posts-categoy.row > div:nth-child({i}) > div > div > div.card-body > div > div > span > small")
        dates[str(i)] = date_article.text

        #Extract content + author
        driver.get(link_)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.container-fluid.main-content")))
        class1 = driver.find_element(By.CSS_SELECTOR, "body > div.container-fluid.main-content")
        class2 = class1.find_element(By.ID, "posts")
        class3 = class2.find_element(By.ID, "main-page-content")
        class4 = class3.find_element(By.CLASS_NAME, "row-content")
        class5 = class4.find_element(By.CLASS_NAME, "article-container")
        class6 = class5.find_element(By.CLASS_NAME, "apost")
        article = class6.find_element(By.CLASS_NAME, "article-content")
        contenus[str(i)] = article.text


        #Résumé du Contenu
        genai.configure(api_key=os.environ["API_KEY"])
        model = genai.GenerativeModel('gemini-pro')
        text = article.text
        response_translation = model.generate_content("translate this into english : " +  text)
#print(response_translation.text)
        response_summary = model.generate_content("summarize this  : " +  response_translation.text)
#print(response_summary.text)
        response = model.generate_content("translate this into arabic  : " +  response_summary.text)
        print("le résumé est : ", response.text)
        resumes[str(i)]=response.text

        author_ = class6.find_element(By.CLASS_NAME, "author")
        author__ = author_.find_element(By.TAG_NAME, "a")
        authorName = author__.get_attribute("text")
        auteurs[str(i)] = authorName


        #Return to the main page
        driver.get(link)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        posts_row = driver.find_element(By.CSS_SELECTOR, " #main-page-content > div.posts-categoy.row")


  except Exception as e:
    print(f"Error: {e}")
  # Close the WebDriver
  driver.quit()
  return titres, liens, imgsSources, dates, contenus, auteurs, categorie, resumes





