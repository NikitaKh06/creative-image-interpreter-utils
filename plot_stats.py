import os
import re
import csv
import glob
import matplotlib.pyplot as plt

AUTHOR_PREFIX = "NikitaKhripunkov"
stats_pattern = re.compile(rf"{AUTHOR_PREFIX}Stats(\d+)_(\d+)\.csv")
MAX_GEN_TO_SHOW = 40000


def load_stats(csv_path):
    generations = []
    best = []
    avg = []

    with open(csv_path, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            generations.append(int(row["generation"]))
            best.append(float(row["best_fitness"]))
            avg.append(float(row["avg_fitness"]))

    return generations, best, avg


def main():
    stats_files = sorted(glob.glob(f"{AUTHOR_PREFIX}Stats*_*.csv"))
    if not stats_files:
        print("No stats CSV files found. Run assignment2.py first")
        return

    for path in stats_files:
        name = os.path.basename(path)
        m = stats_pattern.match(name)
        if not m:
            print("Skip file (pattern mismatch):", name)
            continue

        image_idx = int(m.group(1))
        run_idx = int(m.group(2))

        generations, best, avg = load_stats(path)

        if MAX_GEN_TO_SHOW is not None:
            filtered_gen = []
            filtered_best = []
            filtered_avg = []
            for g, b, a in zip(generations, best, avg):
                if g <= MAX_GEN_TO_SHOW:
                    filtered_gen.append(g)
                    filtered_best.append(b)
                    filtered_avg.append(a)
            generations, best, avg = filtered_gen, filtered_best, filtered_avg

        plt.figure()
        plt.plot(generations, best, label="best fitness")
        plt.plot(generations, avg, label="avg fitness")
        plt.xlabel("Generation")
        plt.ylabel("Fitness")
        plt.title(f"Image {image_idx}, run {run_idx}")
        plt.legend()
        plt.grid(True, alpha=0.3)

        out_name = f"{AUTHOR_PREFIX}Plot{image_idx}_{run_idx}.png"
        plt.savefig(out_name, dpi=150, bbox_inches="tight")
        plt.close()

        print("Saved plot:", out_name)

    print("All plots generated")

if __name__ == "__main__":
    main()
