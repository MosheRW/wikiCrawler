import requests
from bs4 import BeautifulSoup
import bs4


def strip_slash(txt):
    txt = txt.strip('"')
    
    return txt.lstrip('/')

    """
    if txt.rfind('/') != -1:
        return txt[txt.rfind('/')+1:]
    else:
        return txt
    """
    
def strip_dots(txt):
    if txt.find('/') >= 2:
        


def pic_name(tale): 
     img_name = tale.partition('px-')
     
     if img_name.count('px-') != 0:
     #   return img_name[img_name.index('px-')+1]
        return strip_slash(img_name[img_name.index('px-')+1])
     else:
         return strip_slash(img_name[0])

"""
    there is three data-sets
    1. imgTable: contains all implementations of images 
    2. txt: contains the splited txt of the cueernt implementation
    3. tablet: contains all the images of the current type
"""
def pics_scraper(web):                                  #pics scraper
    
    soup = BeautifulSoup(web.content)

    imgTable = soup.find_all('img')

    for i in range(len(imgTable)):                      # loop over all pics links
    
        txt = str(imgTable[i])
        txt = txt.split()

        tablet = list()                                 # creat a list

    
        for x in range(len(txt)):                       # Puts the drity pics links in the temp tablet list
            if txt[x].count('//upload') != 0:
                tablet.append(txt[x])       
            
        print(tablet)
            
        for x in range(len(tablet)):
            tale = tablet[x].partition('//')
            tale = tale[tale.index('//')+1]

            tablet[x] = head + tale                    #
            tablet[x] = tablet[x].strip('"')
            
            if x == len(tablet)-1:
                
               #img_name = str(i) + '_' + str(x) + '.jpg'  
               # img_name = tale.partition('px-')
                #img_name = img_name[img_name.index('px-')+1]
                img_name = pic_name(tale)            
                img_data = requests.get(tablet[x]).content
                with open(pic_name(tale), 'wb') as handler:
                    handler.write(img_data)
      
            
        """"
            img_name = str(i) + '_' + str(x) + '.jpg'  
            img_data = requests.get(tablet[x]).content
            with open(img_name, 'wb') as handler:
                handler.write(img_data)
        """
         
            
        """
        for x in range(len(tablet)):
            tale = tablet[x].partition('//')
            tale = tale[tale.index('//')+1]

            tablet[x] = head + tale                    #
            tablet[x] = tablet[x].rstrip('"')
            print(tablet[x])

            img_name = str(i) + '_' + str(x) + '.jpg'  
            img_data = requests.get(tablet[x]).content
            with open(img_name, 'wb') as handler:
                handler.write(img_data)
        """

#################
def links_scraper(web):                                 #links scraper
    
    head = 'https://he.wikipedia.org/w'

    soup = BeautifulSoup(web.text, 'html.parser')

    table = soup.find_all('p')

    links = list()

    for i in range(len(table)): 
      
        txt = str(table[i])       
        txt = txt.split()

        tablet = list()                                 #creat a list
    
    
        for x in range(len(txt)):
            if txt[x].count("href=") != 0:              #Puts the drity links in the temp tablet list
                tablet.append(txt[x])       
    
     
          
        for x in range(len(tablet)):                    #cleaning the link
            
            tale = tablet[x].partition('/w')
            
            if tale.count('/w') != 0:
                tale = tale[tale.index('/w')+1]
        
                tablet[x] = head + tale                 #rebuild the link
                tablet[x] = tablet[x].rstrip('"')       #cleaning it again
                links.append(tablet[x])                 #adding the link to the final list
           
       

    #print(links)
    return links

###########################################################


###main

head = 'https://'

URL = 'https://he.wikipedia.org/wiki/%D7%99%D7%A9%D7%A8%D7%90%D7%9C'
web = requests.get(URL)
print(web.status_code)


pics_scraper(web)

            
    