Guest = ["Malcolm X", "Tolkein", "Brennan lee mulligan"]
print("Hello " + Guest[0] + ", I would like to invite you to dinner.") 
print("Hello " + Guest[1] + ", I would like to invite you to dinner.")
print("Hello " + Guest[2] + ", I would like to invite you to dinner.")

print("\nUnfortunately, " + Guest[0] + " can't make it to dinner.")
Guest[0] = "Richard Garfield"
print("Hello " + Guest[0] + ", I would like to invite you to dinner.") 
print("Hello " + Guest[1] + ", I would like to invite you to dinner.")
print("Hello " + Guest[2] + ", I would like to invite you to dinner.")

print("\nfortunately, i've found a bigger table for us, so if it okay with you guys, i would like to invite 3 more people to dinner")
Guest.insert(0, "Andrea Hirata")
Guest.insert(2, "Agatha Christie")
Guest.append("J.K. Rowling")
print("Hello " + Guest[0] + ", I would like to invite you to dinner.") 
print("Hello " + Guest[1] + ", I would like to invite you to dinner.")
print("Hello " + Guest[2] + ", I would like to invite you to dinner.")
print("Hello " + Guest[3] + ", I would like to invite you to dinner.") 
print("Hello " + Guest[4] + ", I would like to invite you to dinner.")
print("Hello " + Guest[5] + ", I would like to invite you to dinner.")

print("\nUnfortunately, i'm really sorry  this time but for this dinner i can only invite 2 people, so i have to uninvite some of you")
uninvited_guest1 = Guest.pop(5)
print("i'm so sorry to inform you " , uninvited_guest1 , "that i can't invite you to dinner this time, but i hope we can meet again soon")
uninvited_guest2 = Guest.pop(1)
print("i'm so sorry to inform you " , uninvited_guest2 , "that i can't invite you to dinner this time, but i hope we can meet again soon")
uninvited_guest3 = Guest.pop(0)
print("i'm so sorry to inform you " , uninvited_guest3 , "that i can't invite you to dinner this time, but i hope we can meet again soon")
uninvited_guest4 = Guest.pop(0)
print("i'm so sorry to inform you " , uninvited_guest4 , "that i can't invite you to dinner this time, but i hope we can meet again soon")

print("Hello " + Guest[0] + ", I would like to inform you that you are still invited to dinner.") 
print("Hello " + Guest[1] + ", I would like to inform you that you are still invited to dinner.")

#Using Len()
print("The number of people that are still invited to dinner is ",len(Guest), "people")
