"""Write the make.fun entry to the requested output directory."""

import os
import sys
from pathlib import Path

TEXT = "I hit reply all to say 'please don't reply all.' Four people asked to be removed; one asked who please was."


def main() -> None:
    assert 1 <= len(TEXT) <= 280
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override is None:
        override = os.environ.get("OUTPUT_DIR", "/output")
    out_dir = Path(override)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
