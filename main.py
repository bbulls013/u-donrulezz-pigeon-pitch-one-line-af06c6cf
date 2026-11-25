import os

PITCH = (
    "Coo: invest in CrumbDrop - millions of city pigeons already swarm "
    "where food falls; zero churn, we own every statue ledge, and our "
    "exit is the park lady with the bread bag."
)


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
