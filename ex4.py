nameSet = {"Joe", "Ed", "Fred"}
otherSet = {"Jack", "Ed"}
# adding an item
nameSet.add("Jane")
print(nameSet)
# and (&) operator, print common items
print(nameSet & otherSet)
# union (|) operator, all items (no duplicates though)
print(nameSet | otherSet)
# difference (-) operator, show items left over when you subtract from set
print(nameSet - otherSet)
