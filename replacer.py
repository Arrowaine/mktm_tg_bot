import random
import Config_repos
import best_mat_ever_py

def replacer_mat(text):
    #text = 'Да вот вообще воспринимать трудно'
    #print(text)
    replacer_word1 = 'мат'                  
    #replaced_word2 = random.choice(best_mat_ever_py.f_ck_list)
    splitted_text= text.split()
    #print(splitted_text)
    for i in range(0,len(splitted_text)):
        if replacer_word1 in splitted_text[i].casefold():
            splitted_text[i] = random.choice(best_mat_ever_py.f_ck_list)
    #print(splitted_text)
    final_text = ' '.join(splitted_text)
    #print(final_text)
    return final_text

def replacer_her(text):
    #text = 'Да вот вообще воспринимать трудно'
    #print(text)
    replacer_word1 = 'хер'                  
    #replaced_word2 = random.choice(best_mat_ever_py.f_ck_list)
    splitted_text= text.split()
    #print(splitted_text)
    for i in range(0,len(splitted_text)):
        if replacer_word1 in splitted_text[i].casefold():
            splitted_text[i] = random.choice(best_mat_ever_py.f_ck_list)
    #print(splitted_text)
    final_text = ' '.join(splitted_text)
    #print(final_text)
    return final_text

def replacer_skush(text):
    #text = 'Да вот вообще воспринимать трудно'
    #print(text)
    replacer_word1 = 'скуш'                  
    #replaced_word2 = random.choice(best_mat_ever_py.f_ck_list)
    splitted_text= text.split()
    #print(splitted_text)
    for i in range(0,len(splitted_text)):
        if replacer_word1 in splitted_text[i].casefold():
            splitted_text[i] = random.choice(best_mat_ever_py.f_ck_list)
    #print(splitted_text)
    final_text = ' '.join(splitted_text)
    #print(final_text)
    return final_text
