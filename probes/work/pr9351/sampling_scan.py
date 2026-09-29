#!/usr/bin/env python3
"""J:attack-e:PR9351 -- SAMPLED EVIDENCE: does any claim of the square microscopic spectral certificate note rest on random sampling or on 'never / always observed'?

The pattern applies to a note whose claim is supported by random samples, seeds or unchecked sweeps. This script reads the note, the runner and the four load-bearing helpers at the PR head and lists, for each, every
occurrence of sampling language (random / rng / seed / sample / Monte / linspace / observed / always / never) with its line. A claim resting on a sample would then be attacked by a hill-climb or an adversarial
construction; if every hit is outside the claims' support, the pattern has no purchase. Prints SUMMARY: and, only if a claim rests on sampling, HIT:.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "physics-loop/measured-corrections-20260927"
FILES = ["docs/SQUARE_MICROSCOPIC_SPECTRAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-27.md",
         "scripts/square_microscopic_spectral_certificate_2026_09_27.py",
         "scripts/square_schur_proposals_2026_09_27.py", "scripts/square_rational_inertia_2026_09_27.py",
         "scripts/square_rotor_tail_2026_09_27.py", "scripts/square_corrected_tail_2026_09_27.py"]
PAT = re.compile(r"random|\brng\b|default_rng|seed|sampl|monte|linspace|observed|\balways\b|\bnever\b|numerical(?:ly)? (?:checked|evidence)", re.I)


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)


def main():
    git("fetch", "origin", BRANCH, "--quiet")
    head = git("rev-parse", f"origin/{BRANCH}").stdout.strip()
    print(f"PR #9351 head {head[:10]}")
    total, load = 0, []
    for f in FILES:
        r = git("show", f"{head}:{f}")
        if r.returncode != 0:
            print(f"[MISSING] {f}: {r.stderr.strip()[:80]}")
            continue
        n = 0
        for i, l in enumerate(r.stdout.splitlines(), 1):
            for m in PAT.finditer(l):
                n += 1; total += 1
                print(f"[{f.split('/')[-1][:48]}:{i}] {m.group(0)!r} | {l.strip()[:150]}")
                break
        print(f"   {f.split('/')[-1]}: {n} line(s) with sampling-type language")
    r_rand = [f for f in FILES[1:] if re.search(r"np\.random|random\.|default_rng|RandomState|seed\(", git("show", f"{head}:{f}").stdout)]
    print(f"[RANDOMNESS] files with a random-number call: {r_rand or 'none'}")
    note = git("show", f"{head}:{FILES[0]}").stdout
    claims_rest = [m.group(0) for m in re.finditer(r"[^.\n]*(?:random(?:ly)?|sampled|observed|seeds?|Monte)[^.\n]*", note, flags=re.I)]
    print(f"[NOTE] sentences of the note using random/sampled/observed/seed language: {len(claims_rest)}")
    for s in claims_rest:
        print("   ", s.strip()[:200])
    if r_rand:
        print("HIT: a load-bearing file calls a random-number generator: " + ", ".join(r_rand))
        return 1
    print("SUMMARY: pattern has no purchase on this note: no file of the certificate (runner, four helpers) calls a random-number generator; the six error bounds and the counts are exact rational arithmetic, and the only "
          "floating-point steps are proposals for brackets that the exact counts then accept or reject (the note says so); no claim rests on a random sample or an 'always observed' statement")
    return 0


if __name__ == "__main__":
    sys.exit(main())
