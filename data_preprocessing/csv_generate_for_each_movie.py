
emotion_movie = []
emo_index = []
for index_ in range(105):
    movie_name = ['Logan', 'Rogue One', 'Avatar', 'Titanic', 'Star Wars: Episode VII - The Force Awakens: The Story Awakens - The Table Read', 'Jurassic World', 'The Avengers', 'Furious 7', 'Frozen', 'Minions', 'Finding Dory', 'Captain America: Civil War', 'The Secret Life of Pets', 'The Jungle Book', 'Deadpool', 'Zootopia', 'Batman v Superman: Dawn of Justice', 'Suicide Squad', 'Sing', 'Moana', 'Fantastic Beasts and Where to Find Them', 'Doctor Strange', 'Hidden Figures', 'Jason Bourne', 'Star Trek Beyond', 'X-Men: Apocalypse', 'Trolls', 'La La Land', 'Kung Fu Panda 3', 'Ghostbusters', 'Central Intelligence', 'The Legend of Tarzan', 'Sully', 'Bad Moms', 'The Angry Birds Movie', 'Independence Day: Resurgence', 'The Conjuring 2', 'Arrival', 'Passengers', 'Sausage Party', 'The Magnificent Seven', 'Ride Along 2', "Don't Breathe", "Miss Peregrine's Home for Peculiar Children", 'The Accountant', 'Teenage Mutant Ninja Turtles: Out of the Shadows', 'The Purge: Election Year', 'Alice Through the Looking Glass', "Pete's Dragon", 'The Girl on the Train', 'Boo! A Madea Halloween', 'Storks', '10 Cloverfield Lane', 'Lights Out', 'Hacksaw Ridge', 'Allegiant', 'Now You See Me 2', 'Ice Age: Collision Course', 'The Boss', 'London Has Fallen', 'Miracles from Heaven', 'Deepwater Horizon', 'Why Him?', 'My Big Fat Greek Wedding 2', 'Jack Reacher: Never Go Back', 'Fences', 'Me Before You', 'The BFG', 'Neighbors 2: Sorority Rising', 'The Shallows', 'Office Christmas Party', 'Barbershop: The Next Cut', '13 Hours', 'Lion', "The Huntsman: Winter's War", 'Kubo and the Two Strings', 'Manchester by the Sea', 'Warcraft: The Beginning', 'How to Be Single', 'Mike and Dave Need Wedding Dates', 'War Dogs', 'Almost Christmas', 'Money Monster', 'Allied', 'Nerve', 'Risen', 'The Nice Guys', 'Dirty Grandpa', 'Ouija: Origin of Evil', 'The 5th Wave', 'Inferno', 'Patriots Day', 'Gods of Egypt', 'Collateral Beauty', 'Hail, Caesar!', 'When the Bough Breaks', 'Zoolander 2', 'Moonlight', 'The Finest Hours', 'Florence Foster Jenkins', 'Hell or High Water', 'The Forest', 'Ben-Hur', "Bridget Jones's Baby", 'Kevin Hart: What Now?']
    file_name = ['logan_', 'rogue_one_', 'avatar_', 'titanic_', 'star_wars_episode_vii__the_force_awakens_the_story_awakens__the_table_read_', 'jurassic_world_', 'the_avengers_', 'furious_7_', 'frozen_', 'minions_', 'finding_dory_', 'captain_america_civil_war_', 'the_secret_life_of_pets_', 'the_jungle_book_', 'deadpool_', 'zootopia_', 'batman_v_superman_dawn_of_justice_', 'suicide_squad_', 'sing_', 'moana_', 'fantastic_beasts_and_where_to_find_them_', 'doctor_strange_', 'hidden_figures_', 'jason_bourne_', 'star_trek_beyond_', 'xmen_apocalypse_', 'trolls_', 'la_la_land_', 'kung_fu_panda_3_', 'ghostbusters_', 'central_intelligence_', 'the_legend_of_tarzan_', 'sully_', 'bad_moms_', 'the_angry_birds_movie_', 'independence_day_resurgence_', 'the_conjuring_2_', 'arrival_', 'passengers_', 'sausage_party_', 'the_magnificent_seven_', 'ride_along_2_', 'dont_breathe_', 'miss_peregrines_home_for_peculiar_children_', 'the_accountant_', 'teenage_mutant_ninja_turtles_out_of_the_shadows_', 'the_purge_election_year_', 'alice_through_the_looking_glass_', 'petes_dragon_', 'the_girl_on_the_train_', 'boo_a_madea_halloween_', 'storks_', 'c_10_cloverfield_lane_', 'lights_out_', 'hacksaw_ridge_', 'allegiant_', 'now_you_see_me_2_', 'ice_age_collision_course_', 'the_boss_', 'london_has_fallen_', 'miracles_from_heaven_', 'deepwater_horizon_', 'why_him_', 'my_big_fat_greek_wedding_2_', 'jack_reacher_never_go_back_', 'fences_', 'me_before_you_', 'the_bfg_', 'neighbors_2_sorority_rising_', 'the_shallows_', 'office_christmas_party_', 'barbershop_the_next_cut_', 'c_13_hours_', 'lion_', 'the_huntsman_winters_war_', 'kubo_and_the_two_strings_', 'manchester_by_the_sea_', 'warcraft_the_beginning_', 'how_to_be_single_', 'mike_and_dave_need_wedding_dates_', 'war_dogs_', 'almost_christmas_', 'money_monster_', 'allied_', 'nerve_', 'risen_', 'the_nice_guys_', 'dirty_grandpa_', 'ouija_origin_of_evil_', 'the_5th_wave_', 'inferno_', 'patriots_day_', 'gods_of_egypt_', 'collateral_beauty_', 'hail_caesar_', 'when_the_bough_breaks_', 'zoolander_2_', 'moonlight_', 'the_finest_hours_', 'florence_foster_jenkins_', 'hell_or_high_water_', 'the_forest_', 'benhur_', 'bridget_joness_baby_', 'kevin_hart_what_now_']

    print len(movie_name)
    print len(file_name)

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
    i = 1
    for word in emotion_word:
        emotion_dict[word] = i
        i = i + 1

    json_data = open('data_final_refine.json')
    movie_list = []


    data = json.load(json_data)
    length =  len(data)
    print index_
    for i in range(length):
        d = data[i]
        if d['Title'] == movie_name[index_]:
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
    finallist = sorted(result.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)

    toplist = []
    topindex = []
    for i in range(30):
        toplist.append(finallist[i][0])

    for word in toplist:
        topindex.append(emotion_dict[word] - 1)
    
    emo_index.append(toplist)


    


    x_f = []
    y_f = []
    for index in topindex:
        x_f.append(x_[index])
        y_f.append(y_[index])

    s = []
    for i in range(len(toplist)):
        s.append(result[toplist[i]]*10)


    import csv
    data_f = []
    for i in range(20):
        tup = (topindex[i],s[i])
        data_f.append(tup)
        file_n = file_name[index_]+'.csv'
    with open(file_n, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(['word', 'freq'])
        writer.writerows(data_f)
        f.close()

    '''
    emotion_x = [7.75, 1.75, 7.25, 6.25, 3.55, 7.85, 8.5, 7.5, 3.5, 3.5, 8.5, 6.75, 4.55, 3.0, 7.5, 7.1, 7.25, 8.8, 9.0, 9.0, 1.25, 2.3, 1.5, 6.75, 7.85, 5.5, 6.05, 2.8, 2.8, 7.25, 3.0, 6.0, 3.5, 4.75, 4.0, 1.75, 3.3, 1.25, 6.25, 3.0, 5.25, 0.75, 1.3, 6.25, 6.75, 3.75, 8.25, 5.0, 3.55, 8.25, 1.0, 5.0, 7.25, 6.0, 4.0, 3.75, 2.0, 3.3, 1.5, 1.75, 2.8, 5.75, 5.0, 5.25, 3.5, 5.25, 6.5, 3.0, 0.75, 3.75, 3.5, 8.75, 6.75, 7.0, 3.25, 8.0, 5.0, 2.0, 4.75, 3.75, 4.25, 8.25, 7.75, 3.5, 6.3, 4.5, 3.25, 3.5, 7.75, 7.5, 1.0, 6.25, 4.0, 2.5, 2.75, 3.0, 4.75, 4.5, 7.0, 8.0, 6.5, 8.0, 3.75, 4.0, 7.5, 2.75, 8.5, 6.5, 3.25, 5.0, 7.25, 2.75, 4.5, 7.25, 7.0, 7.75, 8.5, 2.25, 6.5, 2.5]

    emotion_y = [4.5, 4.0, 4.0, 3.25, 3.5, 5.5, 4.75, 4.25, 1.5, 1.0, 5.75, 3.0, 2.25, 2.75, 5.0, 4.0, 4.25, 4.75, 4.5, 4.75, 4.0, 4.0, 4.4, 4.0, 5.2, 2.5, 2.25, 3.75, 5.5, 4.5, 3.45, 4.0, 3.75, 3.0, 3.0, 5.25, 2.75, 5.5, 1.5, 5.2, 2.0, 5.75, 4.5, 3.0, 3.5, 3.2, 4.9, 5.75, 2.75, 5.25, 6.0, 1.25, 4.75, 3.75, 3.25, 2.45, 4.25, 4.25, 4.2, 3.5, 5.0, 3.75, 4.5, 4.5, 2.45, 2.25, 1.25, 3.0, 5.25, 4.0, 4.0, 4.45, 2.5, 3.7, 4.75, 4.75, 3.25, 5.25, 1.95, 4.75, 5.5, 5.75, 4.0, 5.75, 2.75, 1.5, 2.25, 3.4, 5.0, 4.5, 4.25, 1.95, 3.75, 3.7, 4.75, 4.7, 1.5, 5.0, 5.25, 4.25, 4.5, 4.5, 5.0, 4.25, 3.5, 4.0, 5.5, 3.0, 2.9, 4.0, 3.0, 2.75, 5.75, 2.5, 2.75, 3.0, 5.25, 5.25, 2.45, 4.5]
    love_word = ['love', 'wonderful', 'beautiful', 'entertaining', 'amazing']
    object_word = ['death', 'dark', 'lost', 'clear', 'mystery', 'solid', 'realistic', 'fiction', 'revenge', 'pure', 'mysterious', 'clean', 'silent', 'quiet']
    
    emo_single = []
    total = 0
    x_total = 0
    y_total = 0
    for i in range(20):
        total = total + s[i]
    for i in range(20):
        if(emotion_word[topindex[i]] in love_word):
            x_total = x_total + s[i]*emotion_x[topindex[i]]/2
            y_total = y_total + s[i]*emotion_y[topindex[i]]/2
        elif(emotion_word[topindex[i]] in object_word):
            x_total = x_total + s[i]*emotion_x[topindex[i]]*2
            y_total = y_total + s[i]*emotion_y[topindex[i]]*2
        else:
            x_total = x_total + s[i]*emotion_x[topindex[i]]
            y_total = y_total + s[i]*emotion_y[topindex[i]]
    x_aver_ = float(x_total)/total
    y_aver_ = float(y_total)/total
    emo_single.append(x_aver_)
    emo_single.append(y_aver_)
    emotion_movie.append(emo_single)
print emotion_movie
print emo_index
'''