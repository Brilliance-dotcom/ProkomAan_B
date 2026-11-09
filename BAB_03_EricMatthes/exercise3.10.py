Wordle_answer = ["slide", "Motor", "Grist", "Pzazz", "Geeky"]
#1
print(Wordle_answer)
#2
print(Wordle_answer[1])
#3
print("Who would have thought that today's wordle answer is " , Wordle_answer[3], "like i've never heard that word before")
#4
Wordle_answer[0] = "Holey"
print(Wordle_answer)
#5
Wordle_answer.insert(1, "Yahoo")
Wordle_answer.append("thrice")
print(Wordle_answer)
#6
del Wordle_answer[2]
print(Wordle_answer)
#7
wrong_wordle = Wordle_answer.pop(5)
print("it seems i make a mistake" , wrong_wordle , "is not a wordle answer because it has 6 letters, so i have to remove it from the list")
print(Wordle_answer)
#8
Wordle_answer.remove("Geeky")
print(Wordle_answer)
#9
Wordle_answer = sorted(Wordle_answer)
print(Wordle_answer)
#10
Wordle_answer = sorted(Wordle_answer, reverse=True)
print(Wordle_answer)
#11
Wordle_answer.reverse()
print(Wordle_answer)
#12
Wordle_answer.reverse()
print(Wordle_answer)
#13
Wordle_answer.sort()
print(Wordle_answer)
#14
Wordle_answer.sort(reverse=True)
print(Wordle_answer)
#15
print("there are" , len(Wordle_answer), "Wordle answers in the list")