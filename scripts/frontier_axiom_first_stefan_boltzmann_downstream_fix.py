"""Documentary consistency of the supplied-continuum SB boundary, not physics proof."""
from pathlib import Path

AUDIT_INPUT_PATHS = [
    "docs/AXIOM_FIRST_STEFAN_BOLTZMANN_THEOREM_NOTE_2026-05-01.md",
    "docs/AXIOM_FIRST_STEFAN_BOLTZMANN_NOTE_2026-05-17.md",
]
ROOT = Path(__file__).resolve().parents[1]


def check_documents(parent: str, companion: str) -> list[tuple[str, bool]]:
    current, separator, history = parent.partition("## Historical accounting")
    checks = [("parent separates historical assertions", bool(separator) and "historical assertion, not a current claim" in history)]
    for marker in (
        "independent bosonic harmonic-oscillator modes", "zero chemical potential and a Gibbs state",
        "continuum three-dimensional momentum measure", "at all frequencies",
        "an isotropic photon distribution", "does not derive that photon model",
        "positive two-level Hamiltonian", "truncating the continuum spectrum",
        "positivity does not establish the oscillator levels or Bose statistics",
    ):
        checks.append(("parent boundary: " + marker, marker in current))
    checks.append(("no known active framework-composition assertion",
                   "direct composition of the cited companions" not in current and
                   "framework EW + Lorentz" not in current))
    for marker in (
        "documentary consistency only", "That claim is withdrawn",
        "not updated ledger facts", "988d2fb5fe0d39620e74822ef50324a715c47974",
        "a00e8d749d221294db77b2499d8a4fe0271947073fa6e06bba5f1ada48f68099",
        "not a semantic proof",
    ):
        checks.append(("companion boundary: " + marker, marker in " ".join(companion.split())))
    return checks


def main() -> int:
    try:
        texts = [(ROOT / path).read_text(encoding="utf-8") for path in AUDIT_INPUT_PATHS]
    except (OSError, UnicodeError) as exc:
        print(f"FAIL: documentary input unavailable: {exc}")
        return 1
    checks = check_documents(*texts)
    for label, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'}: {label}")
    failures = sum(not ok for _, ok in checks)
    print(f"Documentary checks only: PASS={len(checks)-failures} FAIL={failures}")
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
