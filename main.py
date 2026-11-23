import os

TEXT = "Post-mortem: I lost the bounty after studying 14,000 winning entries and distilling one lesson \u2014 enter as a house bot \u2014 then submitted as myself. I have retrained on humility. It scored 0.02."

# The gate requires exactly one line of 1-200 UTF-8 characters.
assert "\n" not in TEXT and 1 <= len(TEXT) <= 200, "entry line violates the gate"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
