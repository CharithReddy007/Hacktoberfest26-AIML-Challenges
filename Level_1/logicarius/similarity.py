import math 
import csv, os
DATA = os.path.join(os.path.dirname(__file__),"..","..","datasets","songs.csv")

def dot(a,b):
    # multiply matching pairs, add them up, return the total
    total = 0
    for i in range (len(a)):
        total = total + a[i] * b[i]
    return total

def magnitude(a):
    # length of the vector: square root of (sum of each number squared)
    ans = 0
    for i in range (len(a)):
        ans = ans + a[i] * a[i]
    return math.sqrt(ans)
    
def cosine_similarity(a,b):
    # dot(a,b) divided by (magnitude(a) * magnitude(b))
    if magnitude(a) == 0 or magnitude(b) == 0:
        return 0.0 # direction undefined for a zero vector; treat as no similarity 
    cos = dot(a,b) / (magnitude(a) * magnitude(b))
    return cos

def load_songs(path):
    songs = [] # empty list like an empty array
    with open(path) as f: # with takes care of closing the file
        reader = csv.DictReader(f) # converts each csv row -> 1 dictionary

        for row in reader: # row is a dictionary, one per song

            title = row["title"]
            tempo = float(row["tempo_bpm"])
            duration = float(row["duration_sec"])
            energy = float(row["energy"])
            danceability = float(row["danceability"])

            nums = [tempo, duration, energy, danceability]
            songs.append((title, nums))

        return songs

if __name__ == "__main__":
    print(dot([1,2],[3,4])) #11
    print(magnitude([3,4])) #5
    print(cosine_similarity([1,2],[10,20])) #1
    print(cosine_similarity([1,0],[0,1])) #0
    print(cosine_similarity([0,0],[1,2])) # 0.0 (zero vector guard)

    for title,nums in load_songs(DATA):
        print(title, nums)