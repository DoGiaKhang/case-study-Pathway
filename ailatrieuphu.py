import random
questions = [
    "What is the capital city of Australia?",
    "Who painted the Mona Lisa?",
    "What is the chemical symbol for water?",
    'Which planet is known as the "Red Planet"?',
    "What is the tallest mountain in the world?",
    'Who wrote the novel "1984"?',
    "What is the chemical symbol for gold?",
    "Which continent is the largest by land area?",
    "Who discovered penicillin?",
    "What is the chemical formula for glucose?"
]

options = [
    ['A: Melbourne', 'B: Perth', 'C: Brisbane', 'D: Canberra'],
    ['A: Vincent van Gogh', 'B: Pablo Picasso', 'C: Michelangelo', 'D: Leonardo da Vinci'],
    ['A: Wa', 'B: O', 'C: H2', 'D: H2O'],
    ['A: Venus', 'B: Jupiter', 'C: Saturn', 'D: Mars'],
    ['A: K2', 'B: Mount Kilimanjaro', 'C: Mount McKinley', 'D: Mount Everest'],
    ['A: George Eliot', 'B: Ernest Hemingway', 'C: F. Scott Fitzgerald', 'D: George Orwell'],
    ['A: Ag', 'B: Au', 'C: Fe', 'D: Au'],
    ['A: Europe', 'B: Africa', 'C: North America', 'D: Asia'],
    ['A: Ellen Osturn,', 'B: Louis Pasteur', 'C: Marie Curie', 'D: Alexander Fleming'],
    ['A: G', 'B: C6O12', 'C: H2O', 'D: C6H12O6']
]

correct_answers = ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D']
y_kien_khan_gia = ['A','B', 'D','C','A','C','D','D']
money_score = 0
wrong = 0
corr = 0
print('luat cua tro choi ai la ty phu: \n 1. Neu muon hoi y kien cua khan gia, hay ghi "hoi y kien khan gia" vao o dap an ')
for i in range(1,len(questions)+1):
    print( "\nso tien thuong cua ban hien tai la", money_score)
    if i < 5:
        print("Question:", questions[i-1], "So tien thuong cua cau hoi nay la", money_score + 100000 * i)
    else:
        print("Question:", questions[i-1], "So tien thuong cua cau hoi nay la", money_score + 100000 * i)
    for option in options[i-1]:
        print(option)
    answer = input("Answer: ").upper()
    if answer == correct_answers[i-1]:
        corr +=1
        if i < 5:
            print("Dung! So tien thuong cua ban da duoc cong", money_score + 100000 * i)
            money_score += 100000 * i
        else:
            print("Dung! So tien thuong cua ban da duoc cong", money_score + 1000000 * i )
            money_score += 1000000 * i
    # elif answer == "HOI Y KIEN KHAN GIA":
    #     ran = random.randint(0,7)
    #     ykien = y_kien_khan_gia[ran]
    #     print("Toi nghi dap an cua cau hoi nay la", ykien)
    #     answer = input("Vay dap an cua ban la gi? ")
        
    else:
        wrong += 1
        if i < 5:
            print("Sai! So tien thuong cua ban da bi tru", 1000 * i)
            money_score -= 1000 * i
        elif i < 8:
            print("Sai! So tien thuong cua ban da bi tru", 1000000 * i)
            money_score -= 1000000 * i
        else:
            print("Sai! So tien thuong cua ban da bi tru", 100000 * i)
            money_score -= 100000 * i
        if money_score < 0:
            money_score = 0
print("so tien thuong ban duoc sau", corr, "cau hoi dung va", wrong,"cau hoi sai la:",money_score)
