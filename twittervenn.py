import random
import copy

import numpy
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from textblob import TextBlob
from statistweepy import models

sqrt = numpy.sqrt
helv_24 = fm.FontProperties(fname='/home/asus/Arief_tempo/new_font/HelveticaNeueBold.ttf', size = 24)
helv_15 = fm.FontProperties(fname='/home/asus/Arief_tempo/new_font/HelveticaNeueBold.ttf', size = 15)
helv_11 = fm.FontProperties(fname='/home/asus/Arief_tempo/new_font/HelveticaNeueBold.ttf', size = 11)
helv_9 = fm.FontProperties(fname='/home/asus/Arief_tempo/new_font/HelveticaNeueBold.ttf', size = 9)
leftcolor = [1, 0, 0, 1]
middlecolor = [0, 1, 0, 1]
rightcolor = [0, 0, 1, 1]
highlight1 = ('jokowi', )
highlight2 = ('prabowo', )

#dataset = models.Tweets(numpy.load('/home/asus/Arief_tempo/twitterstats/TMCPoldaMetro_1500samples_hour_min_0_16_date_11_7_2018.npy'))
dataset = models.Tweets(numpy.load('/home/asus/Arief_tempo/twitterstats/jakpost_3214samples_hour_min_20_18_date_22_6_2018.npy'))
tweets_dic = {}
tweets_dic['tweet'] = dataset
tweets_dic['text'] = [i.full_text for i in dataset]
tweets_dic['word'] = [TextBlob(i).words for i in tweets_dic['text']]
tweets_dic['stats'] = [(i.retweet_count, i.favorite_count) for i in dataset]
tweets_dic['category'] = []
for i in tweets_dic['word']:
    lower = [j.lower() for j in i]
    count = 0
    result = (False, )
    for k in highlight1:
        if k in lower:
            result = ('left', leftcolor)
            count += 1
            break
    for k in highlight2:
        if k in lower:
            result = ('right', rightcolor)
            count += 1
            break
    if count == 2:
        result = ('middle', middlecolor)
    tweets_dic['category'].append(result)
    
def distance(point1, point2):
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
    
def in_circle(point, center, radius):
    if distance(point, center) < radius-0.7:
        return True
    else:
        return False
    
def out_circle(point, center, radius):
    if distance(point, center) > radius+0.7:
        return True
    else:
        return False
    
msize = 10
def collide(rand, points):
    r = 0.4
    for i in points:
        if distance([rand[0], rand[1]], [i[0][0], i[0][1]])<2*r:
            return True
    return False

def set_point(data, center1, radius1, center2, radius2):
    points = []
    index = 0
    for i in data:
        if i[0] == 'middle':
            rand = [ random.uniform(center1[0], center2[0]), random.uniform(center1[1]-radius1, center2[1]+radius2) ]
            while (not ( in_circle(rand, center1, radius1) and in_circle(rand, center2, radius2) )) or collide(rand, points):
                rand = [ random.uniform(center1[0], center2[0]), random.uniform(center1[1]-radius1, center2[1]+radius2) ]
            points.append((rand, index))
        if i[0] == 'left':
            rand = [ random.uniform(center1[0]-radius1, center1[0]+radius1), random.uniform(center1[1]-radius1, center1[1]+radius1) ]
            while (not ( in_circle(rand, center1, radius1) and out_circle(rand, center2, radius2) ) ) or collide(rand, points):
                rand = [ random.uniform(center1[0]-radius1, center1[0]+radius1), random.uniform(center1[1]-radius1, center1[1]+radius1) ]
            points.append((rand,index))
        if i[0] == 'right':
            rand = [ random.uniform(center2[0]-radius2, center2[0]+radius2), random.uniform(center2[1]-radius2, center2[1]+radius2) ]
            while (not ( in_circle(rand, center2, radius2) and out_circle(rand, center1, radius1) ) ) or collide(rand, points):
                rand = [ random.uniform(center2[0]-radius2, center2[0]+radius2), random.uniform(center2[1]-radius2, center2[1]+radius2) ]
            points.append((rand, index))
        index += 1
    return points

radius1 = 10
shift1 = -6
center1 = (shift1, 0)
x1 = [(-radius1+shift1)+i*0.001 for i in range(2*1000*radius1 + 1)]
y1_upper = [sqrt(radius1**2 - (i-shift1)**2) for i in x1]
y1_lower = [-y for y in y1_upper]

radius2 = 10
shift2 = 6
center2 = (shift2, 0)
x2 = [(-radius2+shift2)+i*0.001 for i in range(2*1000*radius2 + 1)]
y2_upper = [sqrt(radius2**2 - (i-shift2)**2) for i in x2]
y2_lower = [-y for y in y2_upper]


fig,ax = plt.subplots()
ax.plot(x1, y1_upper, color = 'k')
ax.plot(x1, y1_lower, color = 'k')
ax.plot(x2, y2_upper, color = 'k')
ax.plot(x2, y2_lower, color = 'k')
ax.set_axis_bgcolor('white')
points = set_point(tweets_dic['category'], center1, radius1, center2, radius2)
indexes = [i[1] for i in points]
rts = [tweets_dic['stats'][i][0] for i in indexes]
maxrt = max(rts)
ns = {'left':0, 'middle':0, 'right':0}
for i in points:
    index = i[1]
    col = tweets_dic['category'][index][1]
    cat = tweets_dic['category'][index][0]
    ns[cat]+=1
    ax.plot(*i[0], marker = 'o', ms = msize, \
            color = [col[0], col[1], col[2], 0.2 + min(0.8, tweets_dic['stats'][index][0]/maxrt)], \
            markeredgecolor = 'black', lw = 4)
ax.text(shift1-radius1-2, 0, highlight1[0]+'\n'+str(ns['left'])+' tweets', ha = 'center', fontproperties = helv_15, color = 'red')
ax.text(shift2+radius2+2, 0, highlight2[0]+'\n'+str(ns['right'])+' tweets', ha = 'center', fontproperties = helv_15, color = 'blue')
ax.tick_params(colors = [0,0,0,0])
plt.axis('equal')
ax.set_title('Twitter Venn Diagram', fontproperties = helv_24)
fig.show()
