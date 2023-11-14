guests=["jozef","bennet","jyothir"]
name= guests[0].title()
print(name + ", please come to dinner.")
name= guests[1].title()
print(name + ", please come to dinner.")
name= guests[2].title()
print(name + ", please come to dinner.")
#bennetcan't make it to dinner
name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")
#bennetcan't make it to dinner invite najvan instead
del(guests[1])
guests.insert(1,"najvan")
#print invitation again
name= guests[0].title()
print(name + ", please come to dinner.")
name= guests[1].title()
print(name + ", please come to dinner.")
name= guests[2].title()
print(name + ", please come to dinner.")
