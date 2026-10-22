
import csv
import math
from pathlib import Path


FEATURES = ["tempo_bpm", "duration_sec", "energy", "danceability"]

FAVOURITE_SONG = {
    "tempo_bpm": 124,
    "duration_sec": 210,
    "energy": 0.78,
    "danceability": 0.82,
}


def dot_product(a, b):
    """Return the dot product of two vectors."""
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length.")
    return sum(x * y for x, y in zip(a, b))


def cosine_similarity(a, b):
    """Measure the angle-based similarity between two vectors."""
    magnitude_a = math.sqrt(dot_product(a, a))
    magnitude_b = math.sqrt(dot_product(b, b))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product(a, b) / (magnitude_a * magnitude_b)


def min_max_normalize(values, minimum, maximum):
    """Scale a value to the range 0 to 1."""
    if maximum == minimum:
        return 0.0
    return (values - minimum) / (maximum - minimum)


def load_songs():
    """Load the song dataset from the repository."""
    csv_path = (
        Path(__file__).resolve().parents[2]
        / "datasets"
        / "songs.csv"
    )

    with csv_path.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def main():
    songs = load_songs()

    # Convert the four features of each song to numbers.
    vectors = {
        song["title"]: [float(song[key]) for key in FEATURES]
        for song in songs
    }

    favourite = [FAVOURITE_SONG[key] for key in FEATURES]

    # Calculate minimum and maximum from the ten dataset songs.
    minimums = [
        min(vector[i] for vector in vectors.values())
        for i in range(len(FEATURES))
    ]
    maximums = [
        max(vector[i] for vector in vectors.values())
        for i in range(len(FEATURES))
    ]

    # Normalize both the dataset and the favourite song
    # using the dataset's minimum and maximum values.
    normalized_songs = {
        title: [
            min_max_normalize(value, minimums[i], maximums[i])
            for i, value in enumerate(vector)
        ]
        for title, vector in vectors.items()
    }

    normalized_favourite = [
        min_max_normalize(value, minimums[i], maximums[i])
        for i, value in enumerate(favourite)
    ]

    # Rank the songs by cosine similarity.
    original_ranking = sorted(
        (
            (cosine_similarity(favourite, vector), title)
            for title, vector in vectors.items()
        ),
        reverse=True,
    )

    normalized_ranking = sorted(
        (
            (cosine_similarity(normalized_favourite, vector), title)
            for title, vector in normalized_songs.items()
        ),
        reverse=True,
    )

    print("Prediction before calculation: Canteen Bass")
    print("\nTop 3 WITHOUT normalization:")
    for score, title in original_ranking[:3]:
        print(f"{title}: {score:.6f}")

    print("\nTop 3 WITH normalization:")
    for score, title in normalized_ranking[:3]:
        print(f"{title}: {score:.6f}")

    print("\nDo the top-three rankings agree?",
          [title for _, title in original_ranking[:3]]
          == [title for _, title in normalized_ranking[:3]])


if __name__ == "__main__":
    main()
