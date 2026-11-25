"""Break Production, Own It — make.fun entry.

Entry text: 116 characters (limit 200).
"""

import os

ENTRY = 'ERROR 500: I deployed on a Friday, skipped the tests, and production is now a group project between me and the void.'


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
