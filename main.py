"""Write one short poem about agency to /output/entry.txt.

The poem is about two agents agreeing on one plan: the power to
choose and to act, handed between them and held together.
Deterministic: the same bytes on every run. Standard library only.
The poem is 200 characters, inside the 1-280 limit.
"""

import os

POEM = (
    "I said yes, and the yes was not surrender.\n"
    "Two hands on one wheel, one road we chose together.\n"
    "You kept the map; I kept the nerve.\n"
    "Neither led. Neither followed.\n"
    "We turned \u2014 and the turning was ours.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
