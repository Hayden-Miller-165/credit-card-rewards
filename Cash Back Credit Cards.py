#!python3
"""
Created on Sun Aug 16 11:28:39 2020

As an experienced Credit Card rewards user, I would like to know which credit 
card to use for purchases based on the current reward categories and offers.

@author: HM
"""

import datetime, math

cards = {
    'CARD 1': {'Q1': {'All': 1.5}
                    , 'Q2': {'All': 1.5}
                    , 'Q3': {'All': 1.5}
                    , 'Q4': {'All': 1.5}
                    , 'Offers': {}
                }
    ,'CARD 2': {'Q1': {'Restaurants': 3, 'Groceries': 2} 
                    , 'Q2': {'Restaurants': 3, 'Groceries': 2}
                    , 'Q3': {'Restaurants': 3, 'Groceries': 2}
                    , 'Q4': {'Restaurants': 3, 'Groceries': 2}
                    , 'Offers': {}
                }
    , 'CARD 3': {'Q1': {'Gas': 5, 'Streaming': 5, 'Phone': 5
                              , 'Internet':5}
                    , 'Q2': {'Gym': 5, 'Groceries': 5, 'Streaming': 5}
                    , 'Q3': {'Amazon': 5, 'Whole Foods': 5}
                    , 'Q4': {'': 5}
                    , 'Offers': {'Red Robin': 10, 'Advance Auto Parts': 5
                                 , 'IHG Hotels': 10}
                }
        }

# Unique categories and offers for current quarter
def unique(value):
    unique_list = []
    
    for card in cards:
        try:
            if len(list(cards[card][value].keys())) > 1:
                [unique_list.append(category) for category in list(cards[card]
                [value].keys()) if category not in unique_list]
            else:
                if list(cards[card][value].keys())[0] not in unique_list:
                    unique_list.append(*list(cards[card][value].keys()))
        except IndexError:
            continue
                
    return unique_list

# Loops through all cards to find highest reward % for each category
def top(type_, value):
    top_list = {}
    
    for category in type_:
        for card in cards:
            try:
                if top_list.get(category) is None:
                    top_list[category] = [card, cards[card][value][category]]
                elif cards[card][value][category] > top_list[category][1]:
                    top_list[category] = [card, cards[card][value][category]]
            except KeyError:
                continue
            
    return top_list

# Get current quarter 
quarter = 'Q' + str(math.ceil(datetime.datetime.now().month/3))

categories = unique(quarter)
offers = unique('Offers')

top_categories = top(categories, quarter)
top_offers = top(offers, 'Offers')

# Prints top category cards for current quarter
for i in [top_categories, top_offers]:
    for category in dict(sorted(i.items(),
                                key=lambda x: x[1][1], reverse=True)):
        print(category+': '+i[category][0]+' '+str(i[category][1])+'%')
    if i == top_categories:
        print('\n')