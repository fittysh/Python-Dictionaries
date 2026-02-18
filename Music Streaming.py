# How to create a dictionary
# How to add elements to a dictionary
# How to update elements in a dictionary
# How to use a dict comprehension to create a dictionary from two lists

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song:playcount for [song, playcount] in zip(songs, playcounts)}
plays ["Purple Haze"] = 1
print(plays)
plays ["Respect"] = 94
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)
