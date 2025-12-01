import csv
from collections import defaultdict

AUTHOR_PREFIX = "NikitaKhripunkov"
SUMMARY_CSV = f"{AUTHOR_PREFIX}RunsSummary.csv"

def main():
    runs_by_image = defaultdict(list)

    with open(SUMMARY_CSV, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            image_idx = int(row["image_index"])
            runs_by_image[image_idx].append(row)

    print("Image\tAvg final fitness\tAvg generations\tAvg time [s]")
    for image_idx in sorted(runs_by_image.keys()):
        rows = runs_by_image[image_idx]
        n = len(rows)
        avg_fit = sum(float(r["final_best_fitness"]) for r in rows) / n
        avg_gen = sum(float(r["final_generation"]) for r in rows) / n
        avg_time = sum(float(r["elapsed_seconds"]) for r in rows) / n

        print(
            f"input{image_idx}\t"
            f"{avg_fit:.3f}\t\t"
            f"{avg_gen:.1f}\t\t"
            f"{avg_time:.1f}"
        )

if __name__ == "__main__":
    main()
