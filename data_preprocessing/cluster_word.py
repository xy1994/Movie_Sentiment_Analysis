import json
result = {}
emotion_word = []
emotion_dict = {}
i = 0

with open('emo_dict.txt') as emoword:
    for line in emoword:
        if i < 120:
            word = line[:-1]
            word = filter(str.isalpha, word)
            word = word.lower()
            emotion_word.append(word)
            i = i + 1
        
x_1 = [9,1,8,7,4,8,10,8,3,3,7,6,4,3,8,9,7,10,9,8,2,4,2,7,9,5,6,3,4,8,2,7,4,5,5,1,2,0,7,4,6,0,1,6,8,3,8,5,4,10,0,5,7,6,3,2,3,4,3,2,3,7,4,6,2,7,6,4,1,5,4,8,8,7,4,8,4,3,5,4,5,8,7,5,6,5,4,4,10,9,1,7,3,3,2,4,5,4,8,9,3,8,4,5,8,3,9,5,3,5,10,2,6,7,6,8,10,0,6,1]
y_1 = [6,5,6,3,4,6,4,7,2,0,6,2,1,2,6,7,5,6,3,2,0,1,0,2,7,3,2,4,6,7,1,4,3,4,2,5,1,7,0,6,1,6,3,5,6,5,5,7,2,6,7,1,5,2,2,0,2,6,3,1,6,7,4,6,2,1,0,1,5,3,4,3,4,5,6,6,5,5,3,4,4,6,5,7,2,0,0,3,7,5,2,2,5,2,5,4,0,5,6,5,6,6,5,4,5,5,7,2,1,6,5,2,7,1,2,5,6,5,1,5]

x_2 = [8,2,7,6,4,9,8,8,4,2,10,8,4,2,8,7,7,8,9,9,1,1,0,7,9,6,7,3,1,7,4,6,2,4,3,0,4,0,7,1,5,0,1,6,6,4,9,5,3,8,1,5,8,5,4,5,1,2,0,1,2,5,5,5,4,5,7,3,0,2,2,9,7,8,3,9,5,0,6,2,5,9,8,4,7,4,3,2,8,8,0,6,4,2,2,2,4,3,8,9,8,8,3,3,7,3,8,8,2,5,6,3,3,7,8,8,8,3,7,3]
y_2 = [5,5,3,3,3,6,6,4,1,1,6,4,2,2,5,1,3,4,6,6,6,6,7,6,7,2,1,3,6,5,5,5,4,2,3,6,3,6,1,6,1,6,6,2,1,3,6,6,2,6,6,0,6,5,5,4,6,2,6,5,5,1,4,6,5,2,1,3,6,5,5,6,1,6,5,6,3,6,1,5,6,6,2,6,2,1,2,5,5,5,6,1,1,5,5,5,1,5,5,5,4,4,6,5,3,5,5,5,2,2,2,3,6,1,2,3,5,6,4,5]

x_3 = [9,2,8,7,3,9,9,7,2,5,10,7,4,3,7,6,8,9,9,10,1,2,1,6,8,6,5,3,2,7,2,6,3,5,4,2,3,1,6,2,5,1,2,6,7,4,9,4,3,8,1,5,7,7,4,3,1,3,1,2,2,6,5,5,3,4,7,2,1,4,4,10,7,7,3,8,4,2,6,2,2,9,9,2,6,5,3,3,7,6,1,7,4,3,3,2,5,5,7,8,8,8,3,3,7,3,10,5,3,4,7,4,4,8,8,7,9,3,7,2]
y_3 = [4,5,3,3,5,6,5,2,2,2,7,3,2,3,5,4,5,6,6,7,7,6,7,5,6,2,3,5,6,3,5,3,4,3,4,6,4,6,1,6,1,6,5,2,5,3,7,7,3,6,7,1,4,5,2,3,6,5,6,4,5,5,6,3,2,2,1,5,6,4,4,7,2,1,5,4,2,7,1,7,7,7,6,6,3,1,4,5,5,5,6,2,5,6,5,7,1,6,6,4,5,5,5,4,3,3,7,2,4,4,1,2,7,5,3,1,7,6,2,4]

x_4 = [5 ,2,6, 5, 4, 7, 7, 7, 5, 4, 7, 6, 7, 4, 7, 6, 7, 8, 9, 9, 1, 3, 3, 7, 7, 5, 7, 3, 5, 7, 4, 5, 5, 5, 4, 4, 5, 4, 5, 5, 5, 2, 2, 7, 6, 4, 7, 6, 5, 7, 2, 5, 7, 6 ,5 ,5, 3, 5, 2, 2, 5, 5, 6, 5, 5, 5, 6, 3, 1, 4, 4, 8, 5, 6, 3, 7, 7, 3, 2, 7, 5, 7, 7, 3, 7, 4, 3, 5, 6, 7, 2, 5, 5, 2, 4, 4, 5, 6, 5, 6, 7, 8, 5, 5, 8, 2, 7, 8, 5, 6, 6, 2, 5, 7, 6, 8, 7, 3, 6, 4]

y_4 = [3, 1, 4, 4, 2, 4, 4, 4, 1, 1, 4, 3, 4, 4, 4, 4, 4, 3, 3, 4, 3, 3, 3, 3, 2, 3, 3, 3, 4, 3, 4, 4, 4, 3, 3, 4, 3, 3, 4, 4, 5, 5, 4, 3, 2, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 4, 3, 4, 3, 4, 4, 2, 4, 3, 2, 4, 3, 3, 4, 4, 3, 3 ,3 ,4, 3, 3, 3, 3, 4, 3, 5, 4, 3, 4, 4, 4, 3, 4, 3, 3, 3, 4, 4, 3, 4, 4, 4, 4, 4, 3, 3, 3, 4, 4, 3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 4, 3, 3, 4, 4, 4 ]


xy = []

x_ = []
y_ = []


for i in range(120):
    x_aver = float(x_1[i] + x_2[i] + x_3[i] +x_4[i])/4.0 
    y_aver = float(y_1[i] + y_2[i] + y_3[i] +y_4[i])/4.0 
    x_.append(x_aver)
    y_.append(y_aver)

for i in range(120):
    list_xy = []
    list_xy.append(x_[i])
    list_xy.append(y_[i])
    xy.append(list_xy)

duplicate = []
for i in range(120):
    for j in range(120):
        if x_[i] == x_[j] and y_[i] == y_[j] and i!=j:
            list_dup = []
            list_dup.append(i)
            list_dup.append(j)
            duplicate.append(list_dup)
#print duplicate
#print xy[17]
#print xy[71]
#print emotion_word[17]
#print emotion_word[71]
i = 1
for word in emotion_word:
    emotion_dict[word] = i
    i = i + 1
'''
import matplotlib.pyplot as plt
#f1 = plt.figure(1)  
plt.scatter(x_,y_)
'''
'''
for label, x, y in zip(emotion_word[30:50], x_[30:50],y_[30:50]):
    plt.annotate(
        label,
        xy=(x, y), xytext=(-5, 5),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.1', fc='yellow', alpha=0.5),
        arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))

plt.show()
'''

json_data = open('data_final_refine.json')
movie_list = []


data = json.load(json_data)
length =  len(data)

for i in range(length):
    d = data[i]
    if d['Title'] not in movie_list:
        movie_list.append(str(d['Title']))
#print movie_list

for i in range(length):
    d = data[i]
    if d['Title'] == 'Florence Foster Jenkins':
        text = d['ReviewText']
        text = str(text)
        #text = filter(str.isalpha, text)
        text = text.split()
        #text = filter(str.isalpha, text)
        for word in text:
            word = filter(str.isalpha, word)
            word = word.lower()
            if word in emotion_word:
                if word not in result:
                    result[word] = 0
                result[word] += 1
'''
movie_name = []
for i in range(length):
    d = data[i]
    text = d['Title']
    text = str(text)
    text = text.split()
    text_refined = ''
    for word in text:
        word = filter(str.isalnum, word)
        word = word.lower()
        text_refined = text_refined + word + '_'
    if text_refined not in movie_name:
        movie_name.append(text_refined)
print len(movie_name)
'''
finallist = sorted(result.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)

toplist = []
topindex = []
for i in range(30):
    toplist.append(finallist[i][0])

for word in toplist:
    topindex.append(emotion_dict[word] - 1)

x_f = []
y_f = []
for index in topindex:
    x_f.append(x_[index])
    y_f.append(y_[index])

s = []
for i in range(len(toplist)):
    s.append(result[toplist[i]]*10) 

'''
import matplotlib.pyplot as plt
#f1 = plt.figure(1)  

plt.scatter(x_f,y_f,s=s)

print topindex
print s

for label, x, y in zip(toplist, x_f,y_f):
    plt.annotate(
        label,
        xy=(x, y), xytext=(-5, 5),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.1', fc='yellow', alpha=0.5),
        arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))

plt.show()
'''
from sklearn.cluster import KMeans
import numpy as np
X = np.array(xy)
kmeans = KMeans(n_clusters=6, random_state=0).fit(X)
y_pred =kmeans.fit_predict(X)
c_1 = []
c_2 = []
c_3 = []
c_4 = []
c_5 = []
c_6 = []
for i in range(120):
    if (y_pred[i] == 0):
        c_1.append(i)
    elif(y_pred[i] == 1):
        c_2.append(i)
    elif(y_pred[i] == 2):
        c_3.append(i)
    elif(y_pred[i] == 3):
        c_4.append(i)
    elif(y_pred[i] == 4):
        c_5.append(i)
    else:
        c_6.append(i)

w_1 = []
w_2 = []
w_3 = []
w_4 = []
w_5 = []
w_6 = []
w_1_ = []
w_2_ = []
w_3_ = []
w_4_ = []
w_5_ = []
w_6_ = []
for index in c_1:
    w_1.append(emotion_word[index])
    w_1_.append(index)
for index in c_2:
    w_2.append(emotion_word[index])
    w_2_.append(index)
for index in c_3:
    w_3.append(emotion_word[index])
    w_3_.append(index)
for index in c_4:
    w_4.append(emotion_word[index])
    w_4_.append(index)
for index in c_5:
    w_5.append(emotion_word[index])
    w_5_.append(index)
for index in c_6:
    w_6.append(emotion_word[index])
    w_6_.append(index)

print w_1
print w_2
print w_3
print w_4
print w_5
print w_6

print w_1_
print w_2_
print w_3_
print w_4_
print w_5_
print w_6_
movie_name = ['logan_', 'rogue_one_', 'avatar_', 'titanic_', 'star_wars_episode_vii__the_force_awakens_the_story_awakens__the_table_read_', 'jurassic_world_', 'the_avengers_', 'furious_7_', 'frozen_', 'minions_', 'finding_dory_', 'captain_america_civil_war_', 'the_secret_life_of_pets_', 'the_jungle_book_', 'deadpool_', 'zootopia_', 'batman_v_superman_dawn_of_justice_', 'suicide_squad_', 'sing_', 'moana_', 'fantastic_beasts_and_where_to_find_them_', 'doctor_strange_', 'hidden_figures_', 'jason_bourne_', 'star_trek_beyond_', 'xmen_apocalypse_', 'trolls_', 'la_la_land_', 'kung_fu_panda_3_', 'ghostbusters_', 'central_intelligence_', 'the_legend_of_tarzan_', 'sully_', 'bad_moms_', 'the_angry_birds_movie_', 'independence_day_resurgence_', 'the_conjuring_2_', 'arrival_', 'passengers_', 'sausage_party_', 'the_magnificent_seven_', 'ride_along_2_', 'dont_breathe_', 'miss_peregrines_home_for_peculiar_children_', 'the_accountant_', 'teenage_mutant_ninja_turtles_out_of_the_shadows_', 'the_purge_election_year_', 'alice_through_the_looking_glass_', 'petes_dragon_', 'the_girl_on_the_train_', 'boo_a_madea_halloween_', 'storks_', '10_cloverfield_lane_', 'lights_out_', 'hacksaw_ridge_', 'allegiant_', 'now_you_see_me_2_', 'ice_age_collision_course_', 'the_boss_', 'london_has_fallen_', 'miracles_from_heaven_', 'deepwater_horizon_', 'why_him_', 'my_big_fat_greek_wedding_2_', 'jack_reacher_never_go_back_', 'fences_', 'me_before_you_', 'the_bfg_', 'neighbors_2_sorority_rising_', 'the_shallows_', 'office_christmas_party_', 'barbershop_the_next_cut_', '13_hours_', 'lion_', 'the_huntsman_winters_war_', 'kubo_and_the_two_strings_', 'manchester_by_the_sea_', 'warcraft_the_beginning_', 'how_to_be_single_', 'mike_and_dave_need_wedding_dates_', 'war_dogs_', 'almost_christmas_', 'money_monster_', 'allied_', 'nerve_', 'risen_', 'the_nice_guys_', 'dirty_grandpa_', 'ouija_origin_of_evil_', 'the_5th_wave_', 'inferno_', 'patriots_day_', 'gods_of_egypt_', 'collateral_beauty_', 'hail_caesar_', 'when_the_bough_breaks_', 'zoolander_2_', 'moonlight_', 'the_finest_hours_', 'florence_foster_jenkins_', 'hell_or_high_water_', 'the_forest_', 'benhur_', 'bridget_joness_baby_', 'kevin_hart_what_now_']
'''
import csv
data = []
for i in range(20):
    tup = (topindex[i],s[i])
    data.append(tup)
with open('florence_foster_jenkins_.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(['word', 'freq'])
    writer.writerows(data)
    f.close()
'''
'''
x_x = []
y_y = []
for index in topindex:
    x_x.append(x_[index])
    y_y.append(y_[index])
plt.scatter(x_x,y_y)
'''
emotion_movie = [[5.0713630406290955, 3.385812581913499], [5.70849582172702, 3.3704387186629527], [4.854433139534883, 3.455123546511628], [4.441789087093389, 3.1282528856243443], [5.440025094102886, 3.434598494353827], [5.3447008547008545, 3.8047008547008545], [6.206002202643171, 3.577285242290749], [5.081598513011152, 3.8201363073110284], [4.800389321468298, 3.266963292547275], [4.72888180764774, 3.5918018539976826], [5.982837837837838, 3.4230405405405406], [5.6947066326530615, 3.6362244897959184], [5.74226393629124, 3.5532138794084185], [5.443071895424836, 3.438071895424837], [5.9454566420664205, 3.670179889298893], [5.99574074074074, 3.5389506172839504], [3.729354990583804, 3.7694209039548023], [3.692679195804196, 3.8814466783216783], [5.747777101096224, 3.492783191230207], [5.488457008244994, 3.1845111896348643], [6.339648602878916, 3.6611981371718882], [5.260781383432963, 3.281063193851409], [5.853981937602628, 3.449425287356322], [4.855842607313195, 3.6254372019077903], [5.734928385416667, 3.608268229166667], [4.712986651835372, 3.71412680756396], [5.990245995423341, 3.7479977116704806], [4.707121922626026, 3.3610492379835875], [6.2810625, 3.49296875], [3.7270250723240115, 4.1259884281581485], [5.418421052631579, 3.810387811634349], [4.637104622871046, 3.576794403892944], [5.884082892416226, 3.6597442680776013], [4.3623569794050345, 4.03220823798627], [4.116775777414075, 4.113031914893617], [3.1990266963292546, 4.1092602892102335], [4.099560889929743, 4.195052693208431], [5.622727272727273, 3.4405894886363635], [5.10683615819209, 3.320056497175141], [4.695878746594006, 3.838658038147139], [6.0646909827760895, 3.924772036474164], [4.315617848970252, 3.9437643020594964], [4.5975979772439945, 3.647914032869785], [4.3952959830866805, 3.584963002114165], [5.663298722044728, 3.3301517571884984], [4.452110552763819, 3.7622361809045226], [4.246012064343163, 3.9344839142091153], [4.403164225941422, 3.781511506276151], [5.566182572614108, 3.5803941908713695], [4.785969738651994, 3.7305020632737276], [3.938556338028169, 4.188292253521126], [5.681324701195219, 3.653585657370518], [5.542236662106703, 4.145964432284542], [4.156753006475486, 4.0653098982423685], [5.54375, 3.7233770718232044], [3.2125879043600563, 3.9333684950773558], [4.9776585820895525, 3.625], [3.91625, 3.8754375], [3.916191904047976, 3.945352323838081], [3.7729811574697174, 3.9131897711978465], [4.71824942791762, 3.418192219679634], [6.062460815047022, 3.773746081504702], [4.959839816933639, 3.9032608695652176], [5.509410339256866, 3.831946688206785], [4.0307092198581564, 3.8690425531914894], [4.3207118353344764, 3.600257289879931], [4.83351282051282, 3.427], [5.204332615715823, 3.586248654467169], [4.82997542997543, 3.8431818181818183], [4.904868913857678, 3.694756554307116], [4.59054054054054, 4.151412776412776], [4.972859922178988, 3.7157587548638134], [5.405332302936631, 3.543083462132921], [5.7060344827586205, 3.4721902937420177], [4.472672672672672, 3.3464714714714714], [5.067148309705561, 3.118157033805889], [4.152804709141274, 3.7516274238227147], [4.805817422434368, 3.6772076372315037], [5.023066298342542, 3.7123388581952117], [5.107562154696133, 4.0291091160220995], [5.576515151515151, 3.385966810966811], [5.817372881355932, 3.7885593220338984], [4.556388564760794, 3.962777129521587], [5.148427152317881, 3.170157284768212], [5.377488558352403, 3.709525171624714], [5.7063646788990825, 3.1642201834862385], [6.040529841656516, 3.8528623629719854], [4.098842155009452, 3.856001890359168], [3.2853070175438597, 4.104229323308271], [3.3847877358490566, 3.7615271226415095], [4.3732092696629215, 3.89561095505618], [4.977431421446384, 3.536658354114713], [3.597736520854527, 3.841556459816887], [4.805093099671413, 3.271960569550931], [4.919981862152358, 3.6294135429262395], [3.2338323353293412, 4.091916167664671], [3.161019210245464, 4.303601921024547], [4.307252440725244, 3.5482914923291493], [5.483866279069767, 3.4391472868217052], [5.2092, 3.69372], [6.051825127334465, 3.535271646859083], [2.9715528781793843, 4.322289156626506], [4.394512195121951, 3.7408536585365852], [5.710342920353982, 3.781637168141593], [5.056048387096774, 3.8568548387096775]]
movie_pred = kmeans.fit_predict(emotion_movie)
print movie_pred
c_1_m = []
c_2_m = []
c_3_m = []
c_4_m = []
c_5_m = []
c_6_m = []
for i in range(105):
    if (movie_pred[i] == 0):
        c_1_m.append(i)
    elif(movie_pred[i] == 1):
        c_2_m.append(i)
    elif(movie_pred[i] == 2):
        c_3_m.append(i)
    elif(movie_pred[i] == 3):
        c_4_m.append(i)
    elif(movie_pred[i] == 4):
        c_5_m.append(i)
    else:
        c_6_m.append(i)

w_1_m = []
w_2_m = []
w_3_m = []
w_4_m = []
w_5_m = []
w_6_m = []
w_1_m_ = []
w_2_m_ = []
w_3_m_ = []
w_4_m_ = []
w_5_m_ = []
w_6_m_ = []
for index in c_1_m:
    w_1_m.append(movie_name[index])
    w_1_m_.append(index)
for index in c_2_m:
    w_2_m.append(movie_name[index])
    w_2_m_.append(index)
for index in c_3_m:
    w_3_m.append(movie_name[index])
    w_3_m_.append(index)
for index in c_4_m:
    w_4_m.append(movie_name[index])
    w_4_m_.append(index)
for index in c_5_m:
    w_5_m.append(movie_name[index])
    w_5_m_.append(index)
for index in c_6_m:
    w_6_m.append(movie_name[index])
    w_6_m_.append(index)

print w_1_m_
print w_2_m_
print w_3_m_
print w_4_m_
print w_5_m_
print w_6_m_