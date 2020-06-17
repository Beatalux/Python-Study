import os
import csv
import requests
from bs4 import BeautifulSoup
from save import save_to_file

os.system("clear")
alba_url = "http://www.alba.co.kr"
#page_num=0
extract=1
#place, title,time,pay,date
def brandpage(url):
  albas=[]
  request_job=requests.get(url)
  soup=BeautifulSoup(request_job.text, "html.parser")
  before_table=soup.find("div",{"class":"goodsList goodsJob"})
  try:
    table=before_table.find("table")
  except AttributeError:
    print("nothing to show")
    return
  rows=table.find_all("tr")[1:]
  for row in rows:
    global extract
    try: items=row.find_all("td")
    except AttributeError: continue
    else:
      if extract%2==1:
        try:
          place=items[0].text
          title=items[1].find("span",{"class":"company"}).text
          time=items[2].text
          pay=items[3].text
          date=items[4].text
        except IndexError: 
          alba={0,0,0,0,0}
          continue
        #print(place,title,time)

        if place and title and time and pay and date:
          alba={
            'place':place,
            'title':title,
            'time':time,
            'pay':pay,
            'date':date
          }
          #print(alba)
          albas.append(alba)
      extract+=1
  return albas
    
  
  #pages=soup.find("span",{"class":"page"})
 
  
  #change page
  #for page in pages.find_all('a'):
  #  if page.has_attr('href'):
  #    link=page.attrs['href']

  #if len(link)!=page_num:
  #  brandpage(link[page_num])



request = requests.get(alba_url)
soup = BeautifulSoup(request.text, "html.parser")
albas=[]
company_title,brand,companies=[],[],[]


superbrand=soup.find("div",{"id":"MainSuperBrand"})
for_row=superbrand.find("div",{"class":"first impact"})

for href in superbrand('a'):
  if href.has_attr('href'):
    if "http://" not in (str(href.attrs['href'])):
      continue
    #brands.add(href.attrs['href'])
    brand.append(href.attrs['href'])
    #brand=href.attrs['href']
    
    if len(brand)%2==0:
      continue
    company=href.find('span',{'class':'company'})
 
    if '>' in company.text:
      continue
    company_title.append(company.text)
    #print(company.text)
    compan={
      'link':href.attrs['href'],
      'company':company.text
    }
  
    companies.append(compan)
    #print(compan)
    

#print('check loop')
for i in companies:
  goto=i.get('link')
  comp_name=i.get('company')
  print(goto)
  alba_lst=brandpage(goto+"/job/brand/")
  #if alba_lst==None:
    #continue
  save_to_file(alba_lst,comp_name)