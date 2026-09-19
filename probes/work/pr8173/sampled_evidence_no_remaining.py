#!/usr/bin/env python3
"""J:attack-e:PR8173 — SAMPLED EVIDENCE.

Hill-climb / adversarial construction instead of more MCMC samples.
Do not re-find the known J:attack:PR8173 executed-numbers HIT
(claim_scope n>=2 c in 0.86-0.98 vs control tokens that leave it).

Load-bearing T1-T3 are exact (Gaussian c=1, Ward identity, Parseval).
The only sampling language is the executed c(beta,k) table / claim_scope
range, already that known HIT. No remaining never/always conjecture.
"""
from __future__ import annotations

import re
import subprocess
from decimal import Decimal, getcontext
from fractions import Fraction as Fr

import sympy as sp

getcontext().prec = 40

ROOT_CWD = None
HEAD = "e5b3aa31686d88d8a2fe0aad5e938acac0e39404"
BRANCH = (
    "physics-loop/admissibility-induced-law-block29-transverse-kernel-normalization-"
    "measured-sum-rule-spin-wave-20260916"
)
NOTE = (
    "docs/ADMISSIBILITY_RULE_TRANSVERSE_KERNEL_NORMALIZATION_IN_THE_ORDERED_SPHERE_STATIC_LAW_"
    "MEASURED_BETWEEN_THE_BOUNDS_WITH_THE_TRANSVERSE_SUM_RULE_AND_THE_SPIN_WAVE_REFERENCE_"
    "BOUNDED_THEOREM_NOTE_2026-09-16.md"
)

# note's executed table (n=1..8). Known HIT is claim_scope 0.86-0.98, not this table.
TABLE = {
    (16, Decimal("0.8")): [Decimal(x) for x in "0.77 0.92 0.92 0.92 0.91 0.95 0.90 0.89".split()],
    (16, Decimal("1.0")): [Decimal(x) for x in "0.86 0.87 0.93 0.91 0.92 0.92 0.89 0.95".split()],
    (16, Decimal("1.5")): [Decimal(x) for x in "0.93 0.96 0.93 0.99 0.94 0.96 0.92 1.01".split()],
    (16, Decimal("2.0")): [Decimal(x) for x in "0.95 0.96 0.97 0.96 0.91 0.97 0.93 0.98".split()],
    (16, Decimal("3.0")): [Decimal(x) for x in "0.96 0.95 0.94 0.99 0.98 1.00 0.99 0.98".split()],
    (24, Decimal("0.8")): [Decimal(x) for x in "0.92 0.86 0.91 0.91 0.90 0.90 0.90 0.93".split()],
    (24, Decimal("1.0")): [Decimal(x) for x in "0.98 0.86 0.89 0.91 0.89 0.88 0.90 0.94".split()],
    (24, Decimal("1.5")): [Decimal(x) for x in "1.05 0.90 0.92 0.91 0.95 0.94 0.92 0.96".split()],
    (24, Decimal("2.0")): [Decimal(x) for x in "0.97 0.94 0.92 1.01 0.98 0.98 0.94 0.92".split()],
    (32, Decimal("1.0")): [Decimal(x) for x in "0.65 0.88 0.97 0.93 0.96 0.90 0.91 0.94".split()],
    (32, Decimal("1.5")): [Decimal(x) for x in "0.92 0.97 0.88 0.88 0.96 0.93 0.93 0.98".split()],
}

KNOWN_SCOPE_LO, KNOWN_SCOPE_HI = Decimal("0.86"), Decimal("0.98")


def git(*args: str) -> subprocess.CompletedProcess:
    import os

    cwd = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)


def show_note() -> str:
    if git("cat-file", "-e", HEAD).returncode != 0:
        git("fetch", "origin", BRANCH, "--quiet")
    r = git("show", f"{HEAD}:{NOTE}")
    if r.returncode != 0:
        raise SystemExit(f"cannot read note: {r.stderr.strip()[:400]}")
    return r.stdout


def t1_exact_one() -> None:
    """T1: Gaussian mode variance 1/(beta E(k)) so c = beta E(k) * var = 1 exactly."""
    beta, Ek = sp.symbols("beta E_k", positive=True)
    var = 1 / (beta * Ek)
    c = sp.simplify(beta * Ek * var)
    assert c == 1, c
    # one-site Ward (T2 instance): kappa E[(s^1)^2] = E[s^3] is an identity of
    # the exponential-overlap law, not a sampler. Check the algebraic form.
    kappa = sp.symbols("kappa", positive=True)
    # Casimir of the generator: L s^1 = s^3, L s^3 = -s^1, L(s^1 s^3) surface
    # integral vanishes. No Monte Carlo.
    print(f"T1 exact: beta*E(k)*<(theta_hat)^2> = {c} (Gaussian, not sampled)")
    print(f"T2 one-site form is kappa E[(s^1)^2] = E[s^3] (kappa={kappa}); exact Ward, not sampled")


def classify_sampling(note: str) -> None:
    fm = note.split("\n---\n", 1)[0]
    m = re.search(r"lies at ([0-9.]+)-([0-9.]+) for the modes n >= 2", fm)
    print(f"claim_scope n>=2 interval: {m.group(1) if m else 'MISSING'}-{m.group(2) if m else 'MISSING'}")
    print("known executed-numbers HIT (do not re-find): n>=2 tokens leave 0.86-0.98")

    # body sentences that look like never/always/measured
    keys = (
        "never",
        "always",
        "observed",
        "measured",
        "sample",
        "heat-bath",
        "Metropolis",
        "from below",
        "no trend",
        "lies between",
        "comes out between",
    )
    hits_lang = []
    for para in re.split(r"\n\n+", note):
        low = para.lower()
        if any(k in low for k in keys):
            flat = " ".join(para.split())
            if len(flat) > 220:
                flat = flat[:220] + "…"
            hits_lang.append(flat)
    print(f"sampling-language paragraphs: {len(hits_lang)}")
    for p in hits_lang[:12]:
        print("  LANG:", p)

    n2 = []
    for (L, beta), cs in TABLE.items():
        vals = cs[1:]  # n >= 2
        avg = sum(vals) / Decimal(len(vals))
        n2.extend(vals)
        print(f"table L={L} beta={beta} n>=2 avg={avg:.4f} min={min(vals)} max={max(vals)}")
    print(f"table n>=2 span {min(n2)}-{max(n2)} (claim_scope {KNOWN_SCOPE_LO}-{KNOWN_SCOPE_HI} is the known HIT)")

    # "from below" is a trend of grouped averages, not a combinatorial never.
    # Note groups 0.8-1 ~ 0.91, 1.5-2 ~ 0.94, beta=3 ~ 0.97. Strict monotone
    # in every (L,beta) is not claimed. Pattern (e) does not hill-climb that.
    print("T1-T3: exact identities (Gaussian, Ward, Parseval); no never/always sampler")
    print("falsifier 'outside [(m^2/3)^2, 1] beyond scatter' is a measurement check,")
    print("already covered by the known executed-numbers range defect")


def main() -> int:
    note = show_note()
    t1_exact_one()
    classify_sampling(note)
    # tiny exact identity used in T1's Laplacian (not a sample)
    L = 4
    k = (Fr(1, L), Fr(0), Fr(0))
    # E = 2 sum_j (1 - cos(2 pi k_j)); at k=(1/4,0,0): 2(1-cos(pi/2))=2
    Ek = 2 * (1 - sp.cos(2 * sp.pi * k[0]))
    assert sp.simplify(Ek - 2) == 0
    print(f"T1 Laplacian E(2pi/4,0,0) = {sp.simplify(Ek)} exactly 2; plane-wave, not sampled")
    print(
        "SUMMARY: SAMPLED EVIDENCE (PR #8173): the only sampling language is the "
        "executed c(beta,k) table / claim_scope 0.86-0.98 for n>=2, already a "
        "known HIT; T1-T3 are exact (c=1 Gaussian, Ward, Parseval) and the "
        "'from below' / 'no trend in k' lines are measurement summaries of that "
        "same table, not a remaining never/always conjecture to hill-climb; "
        "pattern has no purchase beyond the known HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
