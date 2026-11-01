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