# dot product, cosine similarity, min-max normalize
import math
import csv
import os
def dot_product(a,b): #this also works for now
    ttl = 0
    for x,y in zip(a,b):
        ttl += x * y
    return ttl

def magnitude(x): #light work
    return math.sqrt(dot_product(x,x))


def cosine_similarity(a, b):

    # dot product / magnitude

    a_mag = magnitude(a)
    b_mag = magnitude(b)
    if a_mag == 0 or b_mag == 0:
        return 0
    return dot_product(a,b)/(a_mag * b_mag)

def min_max_normalize(rows):
    n = len(rows[0])
    mins = []
    maxs = []
    for c in range(n):
        column = [row[c] for row in rows]
        mins.append(min(column))
        maxs.append(max(column))

    normalized = []
    for row in rows:
        new_row = []
        for c in range(n):
            if maxs[c] == mins[c]:
                new_row.append(0)
            else:
                new_row.append((row[c] - mins[c])/ (maxs[c] - mins[c]))
        normalized.append(new_row)
    return normalized, mins, maxs


def load_songs(path):
    titles = []
    rows = []
    with open(path, mode='r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            titles.append(row[0])
            rows.append([float(x) for x in row[1: ]])
    return titles, rows

def rank(loved, titles, rows):
    scores = [(cosine_similarity(loved,r), t) for t, r in zip(titles, rows)]
    scores.sort(reverse=True)
    return scores

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    titles, rows = load_songs(os.path.join(here, "..", "..", "datasets", "songs.csv")) #tg this works
    loved_target = [124,210,0.78,0.82]
    print("No Normalization: ")
    for score, title in rank(loved_target, titles, rows):
        print(f"{score: .4f}: {title}")

    norm_rows, mins, maxs = min_max_normalize(rows)
    loved_norm = []
    for c in range(len(loved_target)):
        if maxs[c] == mins[c]:
            loved_norm.append(0)
        else:
            loved_norm.append((loved_target[c] - mins[c])/(maxs[c] - mins[c]))
    print("Normalized: ")
    for score, title in rank(loved_norm, titles, norm_rows):     
        print(f"{score:.4f}: {title}")   

# cosine_similarity()
# min_max_normalize()
# cosine_similarity()
# print('Ranking: ')