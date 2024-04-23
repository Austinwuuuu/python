#建立判定用串列
card_amount=[1,3,4,4,5,6,8,9]           #每個牌陣所需的牌數
button_answer = ['1','2']                   #判定輸入的答案是否在限制範圍內
language_answer = ['1','2']                 
spread_answer = ['1','2','3','4','5','6','7','8']       
range22=[]                              #建立數列判斷玩家選擇的數字是否在卡牌張數範圍內
range78=[]                              
for i in range(1,23):                   
    range22.append(i)
for i in range(1,79):
    range78.append(i)
up_down_word=['','（逆）']                 #跑出逆位
En_up_down_word=['','(reversed)']

#Choose the language

button = 1
while button == 1:
    print("Please choose your language. \n請選擇語言")
    language = input("Enter 1 for English.\n欲選擇繁體中文請輸入2\n")       #選擇中英文版
    if language in language_answer:
       button = 0
       language=int(language)                                               #將變數轉成int格式以利程式後續判斷
    else:
        pass

#請使用者選擇牌陣
if language == 1:
    print("Welcome to the Tarot Card System")
    print("Find an answer to your questiones here!")
    print("Choose a suitable spread")
    print()
    print("Spread 1:")
    print('Sinle card divination method: Use one card to get daily reading or an answer to something')
    print('1')
    print('① Represents an outcome.')
    print()
    print('Spread 2:')
    print('Spread of time:Analyzes the past, present and future of a situation')
    print('1 2 3')
    print('① Represents the situation or condition of the past.')
    print('② Represents the present situation or condition.')
    print('③ Represents future trends.')
    print()
    print('Spread 3:')
    print('Diamond Divination Method: Similar to the spread of time，the difference is to analyze present card, two cards are needed，this method gives a detailed analysis')
    print('   4')
    print('3     2')
    print('   1')
    print('① Represents the situation or condition of the past.')
    print('② 、③ Represents the present situation or condition.')
    print('④ Represents future trends.')
    print()
    print('Spread 4:')
    print('Element divination method: Use the basic characteristics of fire, wind, water and earth, to help you to solve a problem and to give you suggestions ')
    print('2  3')
    print('4  1')
    print('① Fire Element,fire symbolizes movement.This card suggests movement to solve the problem.')
    print('② Wind Element,wind symbolizes language and communication.This card suggests communication to solve the problem.')
    print('③ Water Element,water symbolizes emotions.This card tells you what your emotional state should be to solve the problem.')
    print('④ Earth Element,earth symbolizes money and tangible resources. This card suggests using your wealth and other tangible resources to solve the problem. ')
    print()
    print('Spread 5:')
    print('The Spread of Choice:Analyze the choice ，it can provide help to make decisions')
    print('4       5')
    print('  2   3')
    print('    1')
    print('① Symbolizes you and the current status of your problem.')
    print('② If you choose choice A, it is about your near future.')
    print('③ If you choose choice B, it is about your near future.')
    print('④ If you choose choice A, it is about your distant future.')
    print('⑤ If you choose choice B, it is about your distant future.')
    print()
    print('Spread 6:')
    print('This spread is about friendship: understand how your friend feels.')
    print('Can reflect the blindspots of your thoughts.')
    print('1 3 5')
    print('2 4 6')
    print('① Represents your thoughts toward your friend.')
    print('② Represents your friends thoughts toward you.')
    print('③ Represents your thoughts toward your friendship.')
    print('④ Represents your friends thoughts toward your friendship.')
    print('⑤ Represents your expectations for your friendship.')
    print('⑥ Represents your friends expectations for your friendship.')
    print()
    print('Spread 7:')
    print('Spread of seven days:Prediction for seven days about your fortune,love and finance and so on.')
    print('            8')
    print('1 2 3 4 5 6 7')
    print('① Today\'s situation.')
    print('② Tomorrow\'s situation.')
    print('③ The third day\'s situation.')
    print('④ The fourth day\'s situation.')
    print('⑤ The fifth day\'s situation.')
    print('⑥ The sixth day\'s situation.')
    print('⑦ The seventh day\'s situation.')
    print('⑧ Situation of all seven days.')
    print()
    print('Spread 8:')
    print('This spread is about your previous life and current life. Know your previous life and know yourself and your life\'s mission.\nWe suggest using all cards. ')
    print('  9')
    print('8   7')
    print('  6')
    print('  5')
    print('  4')
    print('  3')
    print('  2')
    print('  1')
    print('① Who you were in the previous life. ')
    print('② What you learnt in the previous life.')
    print('③ What were your failures in your previous life.')
    print('④ Who you are in this life.')
    print('⑤ What is the most simple thing for you in this life.')
    print('⑥ What is the most difficult thing for you in this life.')
    print('⑦ Your most frequently recurring problem.')
    print('⑧ What is the best way to solve the problem.')
    print('⑨ What do you need to learn in this life.\n\n')

    button = 1
    while button == 1:
        spread = input("Please choose a spread. For example, to choose spread number one, choose 1.\n")
        if spread in spread_answer:
            button = 0
            spread= int(spread)                                     #將變數轉成int格式以利程式後續判斷           
        else:
            pass
    
if language == 2:
    print("歡迎來到塔羅抽卡系統")
    print("困擾你許久的問題或許可在這裡得到解答")
    print("選擇適合的牌陣")
    print()
    print('編號1:')
    print('單張占卜法:用一張塔羅牌簡易得出今日運勢或某件事情的結果')
    print('1')
    print('① 代表得出的結果。')
    print()
    print('編號2:')
    print('時間之流牌陣:分析任何情況的過去、現在和未來')
    print('1 2 3')
    print('① 代表過去的情況與狀況。')
    print('② 代表現在的狀態與處境。')
    print('③ 代表未來的走向與趨勢。')
    print()
    print('編號3:')
    print('鑽石占卜法:基本上與時間之流牌陣相同，不同處為分析現在狀態的排卡增為兩張，可做更準確的分析')
    print('   4')
    print('3     2')
    print('   1')
    print('① 過去所發生的事情及狀況。')
    print('② 、③ 皆是事物的現況與局面。')
    print('④ 為未來有可能出現的狀況。')
    print()
    print('編號4:')
    print('要素展開法:利用火、風、水、土元素的基本特性，從各個面向幫助找到解決困難的方向，以及能採取的行動')
    print('2  3')
    print('4  1')
    print('① 代表火元素，火象徵行動。這張牌主要是提供給你行動上的建議。')
    print('② 代表風元素，風象徵言語、溝通。這張牌主要是提供你言語上應該採取的對策。')
    print('③ 代表水元素，水象徵情緒、感情。這張牌是建議你在感情層面上，應該採取何種態度。')
    print('④ 代表土元素，土象徵實際物質、金錢。這張牌是告訴你物質方面應該如何處理，才能徹底解決問題。')
    print()
    print('編號5:')
    print('二擇一占卜法:分析選項的可能結果，能提供使用者決策上的幫助')
    print('4       5')
    print('  2   3')
    print('    1')
    print('① 代表求問者本身，象徵目前求問者的狀況、問題的現況。')
    print('② 選擇『選項一』的現況或近未來。')
    print('③ 選擇『選項二』的現況或近未來。')
    print('④ 當求問者選擇了『選項一』以後，未來的發展。')
    print('⑤ 當求問者選擇了『選項二』以後，未來的發展。')
    print()
    print('編號6:')
    print('友誼發展牌陣:讓自己明白他人心意的占卜牌陣，')
    print('能反映自己內心想法的盲點，也能明瞭他人心思')
    print('1 3 5')
    print('2 4 6')
    print('① 代表你對對方的看法。')
    print('② 代表對方對你的看法。')
    print('③ 代表你認為目前雙方關係。')
    print('④ 代表對方認為目前雙方關係。')
    print('⑤ 代表你期望未來雙方關係的發展。')
    print('⑥ 代表對方期望未來雙方關係的發展。')
    print()
    print('編號7:')
    print('七日牌陣:預測未來一週的運勢、愛情、人際關係、財務狀況、工作運勢等')
    print('            8')
    print('1 2 3 4 5 6 7')
    print('① 今天的狀況。')
    print('② 明天的狀況。')
    print('③ 後天的狀況。')
    print('④ 第四天的狀況。')
    print('⑤ 第五天的狀況。')
    print('⑥ 第六天的狀況。')
    print('⑦ 第七天的狀況。')
    print('⑧ 一整週的總體狀況。')
    print()
    print('編號8:')
    print('前世今生占卜法:探索並知曉你的前世，你的際遇與個性，還有這一生的課題(建議使用整副牌)')
    print('  9')
    print('8   7')
    print('  6')
    print('  5')
    print('  4')
    print('  3')
    print('  2')
    print('  1')
    print('① 前世自己是誰，包含個性、感情傾向。')
    print('② 前世所學到的事，特別是情感上的事。')
    print('③ 前世所學當中曾失敗的事。')
    print('④ 今生自己是誰，包含個性、感情傾向。')
    print('⑤ 今生對自己是簡單的事。')
    print('⑥ 今生對自己是困難的事。')
    print('⑦ 經常出現的問題。')
    print('⑧ 解決問題的最佳方法。')
    print('⑨ 今生的學習目標，特別是情感方面。')

    button = 1
    while button == 1:
        spread = input("請選擇一個牌陣，例如:欲使用編號1的牌陣，請輸入1\n")
        if spread in spread_answer:
            button = 0
            spread = int(spread)                                     #將變數轉成int格式以利程式後續判斷   
        else:
            pass
        
#讓使用者決定參數

if language == 1:
    
    button = 1
    while button == 1:
        Major_or_all = input("Use Major Arcana or all cards. \nSelect 1 for Major Arcana or 2 for all cards.\n")
        if Major_or_all in button_answer:
            button = 0
            Major_or_all=int(Major_or_all)
        else:
            pass

    button = 1
    while button == 1:
        up_down= input("Please choose 1 for original shape and reversed or 2 for original shape. \n")
        if up_down in button_answer:
            button = 0
            up_down=int(up_down)
        else:
            pass

    button = 1
    while button == 1:
        auto = input("If you want to choose on your own, please select 1. If you want a computer generated selection, choose 2.\n")
        if auto in button_answer:
            button = 0
            auto=int(auto)
        else:
            pass
    
if language == 2:
    
    button = 1
    while button == 1:
        Major_or_all = input("要使用大牌占卜還是整副塔羅牌占卜?\n如果要選擇大牌，請輸入1；如果要使用整副塔羅牌，請輸入2\n")
        if Major_or_all in button_answer:
            button = 0
            Major_or_all=int(Major_or_all)
        else:
            pass

    button = 1
    while button == 1:
        up_down= input("是否要開啟正逆位，或只用正位占卜\n如果要開啟請輸入1；不開啟，請輸入2\n")
        if up_down in button_answer:
            button = 0
            up_down=int(up_down)
        else:
            pass

    button = 1
    while button == 1:
        auto = input("是否要自己選牌\n如果要，請輸入1；電腦選牌，請輸入2\n")
        if auto in button_answer:
            button = 0
            auto=int(auto)
        else:
            pass

#洗牌
Major_Arcana = ["愚者","魔術師","女教皇","女帝","皇帝","教皇","戀人","戰車","力量","隱者","命運之輪","正義","吊人","死神","節制","惡魔","高塔","星星","月亮","太陽","審判","世界"]
Minor_Arcana = ["錢幣Ｉ","錢幣ＩＩ","錢幣ＩＩＩ","錢幣ＩＶ","錢幣Ｖ","錢幣ＶＩ","錢幣ＶＩＩ","錢幣ＶＩＩＩ","錢幣ＩＸ","錢幣Ｘ","錢幣侍者","錢幣騎士","錢幣皇后","錢幣國王","寶劍Ｉ","寶劍ＩＩ","寶劍ＩＩＩ","寶劍ＩＶ","寶劍Ｖ","寶劍ＶＩ","寶劍ＶＩＩ","寶劍ＶＩＩＩ","寶劍ＩＸ","寶劍Ｘ","寶劍侍者","寶劍騎士","寶劍皇后","寶劍國王","聖杯Ｉ","聖杯ＩＩ","聖杯ＩＩ","聖杯ＩＶ","聖杯Ｖ","聖杯ＶＩ","聖杯ＶＩＩ","聖杯ＶＩＩＩ","聖杯ＩＸ","聖杯Ｘ","聖杯侍者","聖杯騎士","聖杯皇后","聖杯國王","權杖Ｉ","權杖ＩＩ","權杖ＩＩＩ","權杖ＩＶ","權杖Ｖ","權杖ＶＩ","權杖ＶＩＩ","權杖ＶＩＩＩ","權杖ＩＸ","權杖Ｘ","權杖侍者","權杖騎士","權杖皇后","權杖國王"]
All_card = Major_Arcana + Minor_Arcana

En_major_arcana=[
                'The Fool','The Magician','The High Priestess', 'The Empress','The Emperor','The Hierophant',
                'The Lovers','The Chariot', 'Strength', 'The Hermit', 'The Wheel of Fortune', 'Justice',
                'The Hanged Man', 'Death','Temperance', 'The Devil','The Blasted Tower', 'The Star', 'The Moon','The Sun',
                'Judgement','The World']
En_full_deck=[
              'The Fool','The Magician','The High Priestess', 'The Empress','The Emperor','The Hierophant',
              'The Lovers','The Chariot', 'Strength', 'The Hermit', 'The Wheel of Fortune', 'Justice', 'The Hanged Man',
              'Death','Temperance', 'The Devil','The Blasted Tower', 'The Star', 'The Moon','The Sun', 'Judgement','The World',
              'King of Wands', 'Queen of Wands', 'Knight of Wands', 'Page of Wands', 'Ace of Wands', 'Two of Wands', 'Three of Wands'
              , 'Four of Wands','Five of Wands','Six of Wands','Seven of Wands', 'Eight of Wands', 'Nine of Wands', 'Ten of Wands',
              'King of Cups','Queen of Cups', 'Knight of Cups', 'Page of Cups', 'Ace of Cups', 'Two of Cups', 'Three of Cups',
              'Four of Cups', 'Five of Cups', 'Six of Cups', 'Seven of Cups', 'Eight of Cups','Nine of Cups', 'Ten of Cups', 'King of Swords',
              'Queen of Swords', 'Knight of Swords','Page of Swords','Ace of Swords','Two of Swords', 'Three of Swords','Four of Swords',
              'Five of Swords','Six of Swords','Seven of Swords', 'Eight of Swords','Nine of Swords','Ten of Swords', 'King of Pentacles',
              'Queen of Pentacles','Knight of Pentacles','Page of Pentacles', 'Ace of Pentacles', 'Two of Pentacles','Three of Pentacles',
              'Four of Pentacles', 'Five of Pentacles','Six of Pentacles', 'Seven of Pentacles', 'Eight of Pentacles', 'Nine of Pentacles',
              'Ten of Pentacles']

import random   #引進隨機數模組
card = []       #建立抽排串列
En_card = []
#建立數字形式已抽選過的牌陣串列
if language == 1:
    if auto == 1:
        if Major_or_all == 1:
            random.shuffle(En_major_arcana)
            print(f"Please choose non-duplicate numbers between 1~22. Please choose {card_amount[spread-1]} cards.")
            for i in range(card_amount[spread-1]):
                button = 1
                while button == 1:
                    card_variable = eval(input(f'Please choose card number {i+1}.\n'))
                    if card_variable in range22:
                        if card_variable not in En_card:
                            button = 0
                        else:
                            print('You have already chosen this card. ')
                    else:
                        print('Your selection is out of the range. ')
                    
                En_card.append(card_variable)
                print(f'Your selection: \n{En_card}')
                
        if Major_or_all == 2:
            random.shuffle(En_full_deck)
            print(f"Please choose non-duplicate numbers between 1~78. Please choose {card_amount[spread-1]} cards.")
            for i in range(card_amount[spread-1]):
                button = 1
                while button == 1:
                    card_variable = eval(input(f'Please choose card number {i+1}.\n'))
                    if card_variable in range78:
                        if card_variable not in En_card:
                            button = 0
                        else:
                            print('You have already chosen this card. ')
                    else:
                        print('Your selection is out of the range. ')
                    
                En_card.append(card_variable)
                print(f'Your selection: \n{En_card}')

            
    if auto == 2:
        if Major_or_all == 1:
            random.shuffle(Major_Arcana)
            button = 1
            while button == 1:
                card_variable = random.randint(1,22)
                if card_variable not in En_card:
                    En_card.append(card_variable)
                else:
                    pass
                if len(En_card) == card_amount[spread-1]:
                    button = 0
                else:
                    pass
            
        if Major_or_all == 2:
            random.shuffle(All_card)
            button = 1
            while button == 1:
                card_variable = random.randint(1,78)
                if card_variable not in En_card:
                    En_card.append(card_variable)
                else:
                    pass
                if len(En_card) == card_amount[spread-1]:
                    button = 0
                else:
                    pass

        

if language == 2:
    if auto == 1:                               #玩家選擇手動輸入
        if Major_or_all == 1:                   #只要大牌
            random.shuffle(Major_Arcana)          #洗牌
            print(f"請在1~22中選擇不重複的{card_amount[spread-1]}個數字\n")
            for i in range(card_amount[spread-1]):
                button = 1
                while button == 1:
                    card_variable = eval(input(f'請輸入第{i+1}張牌\n'))
                    if card_variable in range22:
                        if card_variable not in card:
                            button = 0
                        else:
                            print('這張牌你已選過')
                    else:
                        print('選擇的牌不在範圍內')
                    
                card.append(card_variable)
                print(f'你選的牌\n{card}')
                
        if Major_or_all == 2:                   #選整副牌
            random.shuffle(All_card)
            print(f"請在1~78中選擇不重複的{card_amount[spread-1]}個數字\n")
            for i in range(card_amount[spread-1]):
                button = 1
                while button == 1:
                    card_variable = eval(input(f'請輸入第{i+1}張牌\n'))
                    if card_variable in range78:
                        if card_variable not in card:
                            button = 0
                        else:
                            print('這張牌你已選過')
                    else:
                        print('選擇的牌不在範圍內')
                    
                card.append(card_variable)
                print(f'你選的牌\n{card}')

            
    if auto == 2:                              #選擇電腦自動選牌
        if Major_or_all == 1:
            random.shuffle(Major_Arcana)
            button = 1
            while button == 1:
                card_variable = random.randint(1,22)
                if card_variable not in card:
                    card.append(card_variable)
                else:
                    pass
                if len(card) == card_amount[spread-1]:
                    button = 0
                else:
                    pass
            
        if Major_or_all == 2:
            random.shuffle(All_card)
            button = 1
            while button == 1:
                card_variable = random.randint(1,78)
                if card_variable not in card:
                    card.append(card_variable)
                else:
                    pass
                if len(card) == card_amount[spread-1]:
                    button = 0
                else:
                    pass
    




#導入卡牌資料
                
if language == 1:
    if up_down == 2:        #只有正位
        if Major_or_all == 1:        
            for i in range(len(En_card)):
                En_card[i-1] = En_major_arcana[En_card[i-1]-1]

        if Major_or_all == 2:
            for i in range(len(En_card)):
                En_card[i-1] = En_full_deck[En_card[i-1]-1]

    if up_down == 1:        #開啟正逆位
        if Major_or_all == 1:
            for i in range(len(En_card)):
                En_card[i-1] = En_major_arcana[En_card[i-1]-1]
                En_card[i-1] = En_card[i-1] + En_up_down_word[random.randint(0,1)]
            
        if Major_or_all == 2:
            for i in range(len(En_card)):
                En_card[i-1] = En_full_deck[En_card[i-1]-1]
                En_card[i-1] = En_card[i-1] + En_up_down_word[random.randint(0,1)]

    #建立儲存字串長度數值的串列
    lenth = []                                              #此串列儲存牌陣中每張牌的長度
    for i in range(len(En_card)):
        lenth.append(len(En_card[i]))

    if (spread == 1):
        print(En_card[0])
        print("Sinle card divination method: Use one card to get daily reading or an answer to something\n1st represents an outcome.\n")
    elif(spread == 2):
        print(f"%{lenth[0]}s"f"%{lenth[1]+2}s"f"%{lenth[2]+2}s" % (f"{En_card[0]}",f"{En_card[1]}",f"{En_card[2]}"))    #賦予每張塔羅牌的欄位長度依照牌的字數為基準，使牌陣的顯示不至於太長
        print("Spread of time:Analyzes the past, present and future of a situation\n123\n1st represents the situation or condition of the past.\n2nd represents the present situation or condition.\n3rd represents future trends.\n")
    elif(spread == 3):
        if lenth[3] > lenth[0]:                             #賦予每張塔羅牌的欄位長度以該直行中字數最多的牌為基準
            lenth[3] = lenth[3]
        else:
            lenth[3] = lenth[0]
        print(f"%{lenth[2]}s"f"%{lenth[3]+1}s"f"%{lenth[1]+1}s" % ("",f"{En_card[3]}",""))
        print(f"%{lenth[2]}s"f"%{lenth[3]+1}s"f"%{lenth[1]+1}s" % (f"{En_card[2]}","",f"{En_card[1]}"))
        print(f"%{lenth[2]}s"f"%{lenth[3]+1}s"f"%{lenth[1]+1}s" % ("",f"{En_card[0]}",""))
        print("Diamond Divination Method: Similar to the spread of time，the difference is to analyze present card, two cards are needed，this method gives a detailed analysis\n 4\n3 2\n 1\n1st represents the situation or condition of the past.\n2nd&3rd represents the present situation or condition.\n4thRepresents future trends\n.")
    elif(spread == 4):
        if lenth[1] > lenth[3]:
            lenth[3] = lenth[1]
        else:
            lenth[3] = lenth[3]
        if lenth[0] > lenth[2]:
            lenth[2] = lenth[0]
        else:
            lenth[2] = lenth[2]
        print(f"%{lenth[3]}s""%20s"f"%{lenth[2]+1}s" % (f"{En_card[1]}","",f"{En_card[2]}"))
        print(f"%{lenth[3]}s""%20s"f"%{lenth[2]+1}s" % (f"{En_card[3]}","",f"{En_card[0]}"))
        print("Element divination method: Use the basic characteristics of fire, wind, water and earth, to help you to solve a problem and to give you suggestions\n2 3\n4 1\n1st represent fire element,fire symbolizes movement.This card suggests movement to solve the problem.\n2nd represents wind element,wind symbolizes language and communication.This card suggests communication to solve the problem.\n3rd represents water element,water symbolizes emotions.This card tells you what your emotional state should be to solve the problem.\n4th represents earth element,earth symbolizes money and tangible resources. This card suggests using your wealth and other tangible resources to solve the problem.\n")
    elif(spread == 5):
        print(f"%{lenth[3]}s"f"%{lenth[1]+1}s"f"%{lenth[0]+1}s"f"%{lenth[4]+1}s"f"%{lenth[2]+1}s" % (f"{En_card[3]}","","","",f"{En_card[4]}"))
        print(f"%{lenth[3]}s"f"%{lenth[1]+1}s"f"%{lenth[0]+1}s"f"%{lenth[4]+1}s" % ("",f"{En_card[1]}","",f"{En_card[2]}"))
        print(f"%{lenth[3]}s"f"%{lenth[1]+1}s"f"%{lenth[0]+1}s" % ("","",f"{En_card[0]}"))
        print("The Spread of Choice:Analyze the choice ，it can provide help to make decisions\n4   5\n 2 3\n  1\n1st symbolizes you and the current status of your problem.\nIf you choose choice A,the 2nd is about your near future.\nIf you choose choice B, the 3rd is about your near future.\nIf you choose choice A, the 4th is about your distant future.\nIf you choose choice B, the 5th is about your distant future.\n")
    elif(spread == 6):
        if lenth[1] > lenth[0]:
            lenth[0] = lenth[1]
        else:
            lenth[0] = lenth[0]
        if lenth[2] > lenth[3]:
            lenth[3] = lenth[2]
        else:
            lenth[3] = lenth[3]
        if lenth[4] > lenth[5]:
            lenth[5] = lenth[4]
        else:
            lenth[5] = lenth[5]
        print(f"%{lenth[0]}s""%20s"f"%{lenth[3]+1}s""%20s"f"%{lenth[5]+1}s" % (f"{En_card[0]}","",f"{En_card[2]}","",f"{En_card[4]}"))
        print(f"%{lenth[0]}s""%20s"f"%{lenth[3]+1}s""%20s"f"%{lenth[5]+1}s" % (f"{En_card[1]}","",f"{En_card[3]}","",f"{En_card[5]}"))
        print("This spread is about friendship: understand how your friend feels.\n1 3 5\n2 4 6\n1st represents your thoughts toward your friend.\n2nd represents your friends thoughts toward you.\n3rd represents your thoughts toward your friendship.\n4th represents your friends thoughts toward your friendship.\n5th represents your expectations for your friendship.\n6th represents your friends expectations for your friendship.\n")
    elif(spread == 7):
        if lenth[7] > lenth[6]:
            lenth[6] = lenth[7]
        else:
            lenth[6] = lenth[6]        
        print(f"%{lenth[0]}s"f"%{lenth[1]+2}s"f"%{lenth[2]+2}s"f"%{lenth[3]+2}s"f"%{lenth[4]+2}s"f"%{lenth[5]+2}s"f"%{lenth[6]+2}s" % ("","","","","","",f"{En_card[7]}"))
        print(f"%{lenth[0]}s"f"%{lenth[1]+2}s"f"%{lenth[2]+2}s"f"%{lenth[3]+2}s"f"%{lenth[4]+2}s"f"%{lenth[5]+2}s"f"%{lenth[6]+2}s" % (f"{En_card[0]}",f"{En_card[1]}",f"{En_card[2]}",f"{En_card[3]}",f"{En_card[4]}",f"{En_card[5]}",f"{En_card[6]}"))
        print("Spread of seven days:Prediction for seven days about your fortune,love and finance and so on.\n            8\n1 2 3 4 5 6 7\n1st represents today's situation.\n2nd represents tomorrow's situatio.\n3rd represents the third day's situation.\n4th represents the fourth day's situation.\n5th represents the fifth day's situation.\n6th represents the sixth day's situation.\n7th represents the seventh day's situation.\n8th represents the situation of seven days.\n")
    elif(spread == 8):
        lenth[0] = max(lenth[0],lenth[1],lenth[2],lenth[3],lenth[4],lenth[5],lenth[8])#賦予每張塔羅牌的欄位長度以該直行中字數最多的牌為基準
        print(f"%{lenth[7]}s"f"%{lenth[0]+1}s" % ("",f"{En_card[8]}"))
        print(f"%{lenth[7]}s"f"%{lenth[0]+1}s"f"%{lenth[6]+1}s" % (f"{En_card[7]}","",f"{En_card[6]}"))
        print(f"%{lenth[7]}s"f"%{lenth[0]+1}s" % ("",f"{En_card[5]}"))
        print(f"%{lenth[7]}s"f"%{lenth[0]+1}s" % ("",f"{En_card[4]}"))
        print(f"%{lenth[7]}s"f"%{lenth[0]+1}s" % ("",f"{En_card[3]}"))
        print(f"%{lenth[7]}s"f"%{lenth[0]+1}s" % ("",f"{En_card[2]}"))
        print(f"%{lenth[7]}s"f"%{lenth[0]+1}s" % ("",f"{En_card[1]}"))
        print(f"%{lenth[7]}s"f"%{lenth[0]+1}s" % ("",f"{En_card[0]}"))
        print("This spread is about your previous life and current life. Know your previous life and know yourself and your life's mission.\nWe suggest using all cards.\n 9\n8 7\n 6\n 5\n 4\n 3\n 2\n 1\1st represents who you were in the previous life.\n2nd represents what you learnt in the previous life.\n3rd represents What were your failures in your previous life.\n4th represents who you are in this life.\n5th represents what is the most simple thing for you in this life.\n6th represents what is the most difficult thing for you in this life.\n7th represents your most frequently recurring problem.\n8th represents what is the best way to solve the problem.\n9th represents what do you need to learn in this life.\n")


if language == 2:
    if up_down == 2:        #只有正位
        if Major_or_all == 1:
            for i in range(len(card)):
                card[i-1] = Major_Arcana[card[i-1]-1]

        if Major_or_all == 2:
            for i in range(len(card)):
                card[i-1] = All_card[card[i-1]-1]

    if up_down == 1:        #開啟正逆位
        if Major_or_all == 1:
            for i in range(len(card)):
                card[i-1] = Major_Arcana[card[i-1]-1]
                card[i-1] = card[i-1] + up_down_word[random.randint(0,1)]
            
        if Major_or_all == 2:
            for i in range(len(card)):
                card[i-1] = All_card[card[i-1]-1]
                card[i-1] = card[i-1] + up_down_word[random.randint(0,1)]

    if (spread == 1):
        print(card[0])
        print("單張占卜法:用一張塔羅牌簡易得出今日運勢或某件事情的結果\n第一張代表得出的結果\n")
    elif(spread == 2):
        print("{0:　>9s}{1:　>9s}{2:　>9s}".format(f"{card[0]}",f"{card[1]}",f"{card[2]}"))    #賦予每張塔羅牌9~10格的空間，靠右對齊，多出的部分用全形空格填滿
        print("時間之流牌陣:分析任何情況的過去、現在和未來\n123\n第一張代表過去的情況與狀況\n第二張代表現在的狀態與處境\n第三張代表未來的走向與趨勢\n")
    elif(spread == 3):
        print("{0:　>9s}{1:　>9s}{2:　>9s}".format("",f"{card[3]}",""))
        print("{0:　>9s}{1:　>9s}{2:　>9s}".format(f"{card[2]}","",f"{card[1]}"))
        print("{0:　>9s}{1:　>9s}{2:　>9s}".format("",f"{card[1]}",""))
        print("鑽石占卜法:基本上與時間之流牌陣相同，不同處為分析現在狀態的排卡增為兩張，可做更準確的分析\n 4\n3 2\n 1\n第一張過去所發生的事情及狀況\n第二、三皆是事物的現況與局面\n")
    elif(spread == 4):
        print("{0:　>9s}{1:　>3s}{2:　>9s}".format(f"{card[1]}","",f"{card[2]}"))
        print("{0:　>9s}{1:　>3s}{2:　>9s}".format(f"{card[3]}","",f"{card[0]}"))
        print("要素展開法:利用火、風、水、土元素的基本特性，從各個面向幫助找到解決困難的方向，以及能採取的行動\n2 3\n4 1\n第一張代表火元素，火象徵行動。這張牌主要是提供給你行動上的建議\n第二張代表風元素，氣象徵言語、溝通。這張牌主要是提供你言語上應該採取的對策\n第三張代表水元素，水象徵情緒、感情。這張牌是建議你在感情層面上，應該採取何種態度\n第四張代表土元素，土象徵實際物質、金錢。這張牌是告訴你物質方面應該如何處理，才能徹底解決問題\n")
    elif(spread == 5):
        print("{0:　>9s}{1:　>9s}{2:　>9s}{3:　>9s}{{4:　>9s}{".format(f"{card[3]}","","","",f"{card[4]}"))
        print("{0:　>9s}{1:　>9s}{2:　>9s}{3:　>9s}{".format("",f"{card[1]}","",f"{card[2]}"))
        print("{0:　>9s}{1:　>9s}{2:　>9s}".format("","",f"{card[0]}"))
        print("二擇一占卜法:分析選項的可能結果，能提供使用者決策上的幫助\n4   5\n 2 3\n  1\n第一張代表求問者本身，象徵目前求問者的狀況、問題的現況\n第二張選擇『選項一』的現況或近未來\n第三張選擇『選項二』的現況或近未來\n第四張當求問者選擇了『選項一』以後，未來的發展\n第五張當求問者選擇了『選項二』以後，未來的發展\n")
    elif(spread == 6):
        print("{0:　>9s}{1:　>10s}{2:　>10s}".format(f"{card[0]}",f"{card[2]}",f"{card[4]}"))
        print("{0:　>9s}{1:　>10s}{2:　>10s}".format(f"{card[1]}",f"{card[3]}",f"{card[5]}"))
        print("友誼發展牌陣:讓自己明白他人心意的占卜牌陣，能反映自己內心想法的盲點，也能明瞭他人心思\n1 3 5\n2 4 6\n第一張代表你對對方的看法\n第二張代表對方對你的看法\n第三張代表你認為目前雙方關係\n第四張代表對方認為目前雙方關係\n第五張代表你期望未來雙方關係的發展\n第六張代表對方期望未來雙方關係的發展\n")
    elif(spread == 7):
        print("{0:　>9s}{1:　>9s}{2:　>9s}{3:　>9s}{4:　>9s}{5:　>9s}{6:　>9s}".format("","","","","","",f"{card[7]}"))
        print("{0:　>9s}{1:　>9s}{2:　>9s}{3:　>9s}{4:　>9s}{5:　>9s}{6:　>9s}".format(f"{card[0]}",f"{card[1]}",f"{card[2]}",f"{card[3]}",f"{card[4]}",f"{card[5]}",f"{card[6]}"))
        print("七日牌陣:預測未來一週的運勢、愛情、人際關係、財務狀況、工作運勢等\n            8\n1 2 3 4 5 6 7\n第一張代表今天的狀況\n第二張代表明天的狀況\n第三張代表後天的狀況\n第四張代表第四天的狀況\n第五張代表第五天的狀況\n第六張代表第六天的狀況\n第七張代表第七天的狀況\n第八張代表一整週的總體狀況\n")
    elif(spread == 8):
        print("{0:　>9s}{1:　>9s}".format("",f"{card[8]}"))
        print("{0:　>9s}{1:　>9s}{2:　>9s}".format(f"{card[7]}","",f"{card[6]}"))
        print("{0:　>9s}{1:　>9s}".format("",f"{card[5]}"))
        print("{0:　>9s}{1:　>9s}".format("",f"{card[4]}"))
        print("{0:　>9s}{1:　>9s}".format("",f"{card[3]}"))
        print("{0:　>9s}{1:　>9s}".format("",f"{card[2]}"))
        print("{0:　>9s}{1:　>9s}".format("",f"{card[1]}"))
        print("{0:　>9s}{1:　>9s}".format("",f"{card[0]}"))
        print("前世今生占卜法:探索並知曉你的前世，你的際遇與個性，還有這一生的課題(建議使用整副牌)\n 9\n8 7\n 6\n 5\n 4\n 3\n 2\n 1\n第一張代表前世自己是誰，包含個性、感情傾向\n第二張代表前世所學到的事，特別是情感上的事\n第三張代表前世所學當中曾失敗的事\n第四張代表今生自己是誰，包含個性、感情傾向\n第五張代表今生對自己是簡單的事\n第六張代表今生對自己是困難的事\n第七張代表經常出現的問題\n第八張代表解決問題的最佳方法\n第九張代表今生的學習目標，特別是情感方面\n")
