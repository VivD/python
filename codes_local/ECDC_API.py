import numpy as np
import matplotlib.pyplot as plt
import requests
import json
from datetime import datetime

url      = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"
r        = requests.get(url)
data     = json.loads(r.text)
cont     = 0
i        = 0
v_c      = str('US')
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
    if items['geoId'] == v_c:
        cont        = cont + 1
        i           = cont - 1
        t[i]        = datetime.strptime(items['dateRep'], '%d/%m/%Y')
        c[i]        = items['cases']
        d[i]        = items['deaths']
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
plt.legend(['US Total Cases'])
plt.xlabel('Dates')
plt.xticks(rotation=45)

ax2=plt.subplot(3,1,2, sharex=ax1)
ax2.grid(True)
plt.plot(date,deth,'b-',linewidth=2)
annot_max(date,deth)
plt.legend(['US Total Deaths'])
plt.xlabel('Dates')
plt.xticks(rotation=45)

ax3=plt.subplot(3,1,3, sharex=ax1)
ax3.grid(True)
plt.plot(date,actv,'b-',linewidth=2)
annot_max(date,actv)
plt.legend(['US Total Active'])
plt.xlabel('Dates')
plt.xticks(rotation=45)

plt.show()