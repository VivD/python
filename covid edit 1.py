import numpy as np
import matplotlib.pyplot as plt
import requests
import json
import time
from datetime import datetime
from tkinter import *
from PIL import ImageTk,Image

a=Tk()
a.title('COVID-19')
#a.geometry('600x600')
lbl=Label(text='CHOOSE THE COUNTRY').pack()#grid(row=1,column=1)
#########
time.perf_counter()
url      = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"
r        = requests.get(url)
time.perf_counter()

#set width and height

canvas=Canvas(a,width=1200,height=600)

#give this image path. image should be in png format.

#Example: "C:\\Users\\ASUS\\OneDrive\\Pictures\\image.png"

image=ImageTk.PhotoImage(Image.open("C:\\Users\\vivian.dsouza\\OneDrive - Dana Incorporated\\Documents\\Python\\codes\\Corona.png"))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()
#############   
#res=[]
#for items in data['records']:
    #res.append(items['countriesAndTerritories'])
    
#country = [] 
#[country.append(x) for x in res if x not in country]


#print(country)


##
def show():
    time.perf_counter()
    con=clicked.get()
    print(con)
    #url      = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"
    #r        = requests.get(url)
    data     = json.loads(r.text)


    cont     = 0
    i        = 0
    t        = {}
    c        = {}
    d        = {}
    case     = np.array([])
    date     = np.array([])
    deth     = np.array([])
    actv     = np.array([])

    def annot_max(x,y, ax=None):
       xmax = x[np.argmax(y)]
       ymax = y.max()
       text= "x={:.3f}, y={:.3f}".format(xmax, ymax)
       if not ax:
         ax=plt.gca()
       bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
       arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60")
       kw = dict(xycoords='data',textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
       ax.annotate(text, xy=(xmax, ymax), xytext=(0.94,0.96), **kw)
   
    for items in data['records']:
         if items['countriesAndTerritories'] ==clicked.get():
                #v_c=items['geoId'] 
                #for items in data['records']:
                   #if items['geoId'] == v_c:
                      cont        = cont + 1
                      i           = cont - 1
                      t[i]        = datetime.strptime(items['dateRep'], '%d/%m/%Y')
                      c[i]        = items['cases_weekly']
                      d[i]        = items['deaths_weekly']
                      date        = np.append(date, t[i])
                      case        = np.append(case, int(c[i]))
                      deth        = np.append(deth, int(d[i]))
     
    n    = case.size
    date = np.flipud(date)
    case = np.flipud(case)
    deth = np.flipud(deth)
    actv = case - deth
    

    for l in range(n-1):
       case[l+1] = case[l] + case[l+1]
       deth[l+1] = deth[l] + deth[l+1]
       actv[l+1] = actv[l] + actv[l+1]
    
    ax1=plt.subplot(3,1,1)
    ax1.grid(True)
    plt.plot(date,case,'b-',linewidth=2)
    annot_max(date,case)
    plt.legend(["%s ,Total Cases" %clicked.get()])
    plt.xlabel('Dates')
    plt.xticks(rotation=45)

    ax2=plt.subplot(3,1,2, sharex=ax1)
    ax2.grid(True)
    plt.plot(date,deth,'b-',linewidth=2)
    annot_max(date,deth)
    plt.legend(['%s Total Deaths' %clicked.get()])
    plt.xlabel('Dates')
    plt.xticks(rotation=45)

    ax3=plt.subplot(3,1,3, sharex=ax1)
    ax3.grid(True)
    plt.plot(date,actv,'b-',linewidth=2)
    annot_max(date,actv)
    plt.legend(['%s Total Active' %clicked.get()])
    plt.xlabel('Dates')
    plt.xticks(rotation=45)

    plt.show()

 
#####
clicked=StringVar()
drop=OptionMenu(a,clicked,'Afghanistan','Angola','Albania', 'Andorra', 'Algeria', 'Anguilla', 'Antigua_and_Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bonaire, Saint Eustatius and Saba', 'Bosnia_and_Herzegovina', 'Botswana', 'Brazil', 'British_Virgin_Islands', 'Brunei_Darussalam', 'Bulgaria', 'Burkina_Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape_Verde', 'Cases_on_an_international_conveyance_Japan', 'Cayman_Islands', 'Central_African_Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Congo', 'Costa_Rica', 'Cote_dIvoire', 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech_Republic', 'Democratic_Republic_of_the_Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican_Republic', 'Ecuador', 'Egypt', 'El_Salvador', 'Equatorial_Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Faroe_Islands', 'Fiji', 'Finland', 'France', 'French_Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea_Bissau', 'Guyana', 'Haiti', 'Holy_See', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle_of_Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'New_Caledonia', 'New_Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North_Macedonia', 'Northern_Mariana_Islands', 'Norway', 'Oman', 'Pakistan', 'Palestine', 'Panama', 'Papua_New_Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto_Rico', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint_Barthelemy', 'Saint_Kitts_and_Nevis', 'Saint_Lucia', 'Saint_Vincent_and_the_Grenadines', 'San_Marino', 'Saudi_Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra_Leone', 'Singapore', 'Sint_Maarten', 'Slovakia', 'Slovenia', 'Somalia', 'South_Africa', 'South_Korea', 'Spain', 'Sri_Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Thailand', 'Timor_Leste', 'Togo', 'Trinidad_and_Tobago', 'Tunisia', 'Turkey', 'Turks_and_Caicos_islands', 'Uganda', 'Ukraine', 'United_Arab_Emirates', 'United_Kingdom', 'United_Republic_of_Tanzania', 'United_States_of_America', 'United_States_Virgin_Islands', 'Uruguay', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Zambia', 'Zimbabwe',).pack()#grid(row=1,column=2)
button=Button(a,text="show",command=show).pack()#grid(row=1,column=3)
####
time.perf_counter()


 




a.mainloop()
