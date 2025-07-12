def calculate_love_score(name1, name2):
    True_counter = 0
    Love_counter = 0
    combine_name = (name1+name2).lower()
    for Letter in combine_name:
       if Letter in 'true':
           True_counter+=1;
    print(True_counter)
    for Letter in combine_name:
       if Letter in 'love':
           Love_counter+=1;
    print(Love_counter)

    love_score = str(True_counter)+str(Love_counter);
    print(love_score)

calculate_love_score('Kanye West', 'Kim Kardashian')
    
    