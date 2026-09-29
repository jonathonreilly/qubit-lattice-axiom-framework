#!/usr/bin/env python3
"""J:provenance:PR9313 -- every number in the theorem statements of the spin-model-to-comparator note, located in the runner's cached stdout, the runner source, or an exact derivation
re-executed here.

Statement text = the front-matter claim_scope + the "Result" section (the note has no theorem headings).  Every numeric token (integers, decimals, a/b, 1.1 x 10^-13 forms, number words)
must fall inside one item:
  CACHE       printed by the PR's cached runner output (logs/runner-cache/composite_site_network_spin_model_to_comparator_operator_identities_and_sign_conventions_2026_09_26.txt at the PR head)  -> sourced
  RUNNER      a constant of the runner source at the PR head                                                                                                                                 -> sourced
  DERIVED     an exact derivation re-executed here (sympy / exact Fractions)                                                                                                                  -> sourced
  DEFINITION  a constant of a declared object                                                                                                                                                 -> not a claim
  (else)      HIT: no runner line, no cache line, no derivation.
Tokens covered by no item are printed as UNCOVERED and counted as HIT. Self-contained; reads the PR head via git.
"""
import itertools
import re
import subprocess
import sys
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np
import sympy as sp
from functools import reduce as freduce

ROOT = Path(__file__).resolve().parents[3]
PR = 9313
BRANCH = "claude/composite-network-spin-model-to-comparator-operator-identities-20260926"
STEM = "composite_site_network_spin_model_to_comparator_operator_identities_and_sign_conventions_2026_09_26"
NOTE = "docs/COMPOSITE_SITE_NETWORK_THE_POSITIVE_J_SPIN_MODEL_EQUALS_THE_QUADRATIC_COMPARATOR_WITH_THE_OPPOSITE_BOND_SIGN_AND_ITS_PROJECTED_SECTOR_ENERGIES_DO_NOT_DEPEND_ON_THE_SIGN_CONVENTION_BOUNDED_THEOREM_NOTE_2026-09-26.md"
RUNNER = f"scripts/{STEM}.py"
CACHE = f"logs/runner-cache/{STEM}.txt"


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def head():
    git("fetch", "origin", BRANCH, "--quiet")
    r = git("rev-parse", f"origin/{BRANCH}")
    if r.returncode != 0:
        raise SystemExit("cannot resolve the PR branch: " + r.stderr.strip())
    return r.stdout.strip()


HEAD = head()


def show(path):
    r = git("show", f"{HEAD}:{path}")
    if r.returncode != 0:
        raise SystemExit(f"cannot read {path} at {HEAD}: {r.stderr.strip()}")
    return r.stdout


SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺", "0123456789-+")
SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")


def norm(t):
    t = re.sub(r"([⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+)", lambda m: "^" + m.group(1).translate(SUP), t)
    t = re.sub(r"([₀₁₂₃₄₅₆₇₈₉]+)", lambda m: "_" + m.group(1).translate(SUB), t)
    for a, b in (("−", "-"), ("×", "x"), ("κ", "kappa"), ("π", "pi"), ("√", "sqrt"), ("≥", ">="), ("≤", "<="), ("·", "*"), ("²", "^2"), ("∈", " in "), ("→", "->"), ("`", ""),
                 ("σ", "sigma"), ("τ", "tau"), ("ε", "eps"), ("ν", "nu"), ("ᵃ", "^a"), ("ˡ", "^l"), ("ᵐ", "^m"), ("ᵇ", "^b"), ("ᶜ", "^c"), ("ˣ", "^x"), ("ʸ", "^y"), ("ᶻ", "^z")):
        t = t.replace(a, b)
    return t


def statement_pieces(note):
    fm = note.split("\n---\n", 1)[0]
    cs = re.search(r'^claim_scope:\s*"(.*)"\s*$', fm, flags=re.M).group(1)
    secs = {s.split("\n", 1)[0].strip(): s for s in re.split(r"^#+ ", note, flags=re.M)[1:]}
    res = next(v for k, v in secs.items() if k.startswith("Result"))
    return [(n, re.sub(r"\s+", " ", norm(t))) for n, t in (("claim_scope", cs), ("Result", res.split("\n", 1)[1]))]


NUM = re.compile(r"(?<![A-Za-z_\^\d./])(\d+e-\d+|\d+/\d+|[+-]?\d+\.\d+|\d+)(?![\d])")
WORDS = re.compile(r"\b(zero|one|two|three|four|five|six|seven|eight|nine|ten|half|first|second|single|pair)\b", re.I)


def tokens(text):
    return [(m.start(), m.end(), m.group(1)) for m in NUM.finditer(text)] + [(m.start(), m.end(), m.group(1)) for m in WORDS.finditer(text)]


def pfaffian(M):
    n = M.shape[0]
    if n == 0:
        return sp.Integer(1)
    total = 0
    for j in range(1, n):
        keep = [k for k in range(n) if k not in (0, j)]
        total += (-1) ** (j + 1) * M[0, j] * pfaffian(M.extract(keep, keep))
    return sp.expand(total)


def own_bond_norms():
    """Build the three-site constrained Clifford space independently (Jordan-Wigner on 9 qubits) and return, for the flavour-x bond with J = 1, the largest matrix entry and the operator norm of
    P (H_spin - comparator(+2J u)) P, where comparator(+) = sum_a (i/2)(+1)(2 u_01) c_0^a c_1^a."""
    X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1]).astype(complex); I2 = np.eye(2)
    g = []
    for k in range(9):
        for Pm in (X, Y):
            g.append(freduce(np.kron, [Z] * k + [Pm] + [I2] * (9 - k - 1)))
    bx = lambda s, l: g[6 * s + "xyz".index(l)]; cx = lambda s, a: g[6 * s + 3 + "xyz".index(a)]
    D = lambda s: -1j * bx(s, "x") @ bx(s, "y") @ bx(s, "z") @ cx(s, "x") @ cx(s, "y") @ cx(s, "z")
    P = freduce(lambda A, B: A @ B, [(np.eye(512) + D(s)) / 2 for s in range(3)])
    sig = lambda s, a: -1j * cx(s, "yzx"["xyz".index(a)]) @ cx(s, "zxy"["xyz".index(a)])
    tau = lambda s, l: -1j * bx(s, "yzx"["xyz".index(l)]) @ bx(s, "zxy"["xyz".index(l)])
    Hs = tau(0, "x") @ tau(1, "x") @ sum(sig(0, a) @ sig(1, a) for a in "xyz")
    u01 = 1j * bx(0, "x") @ bx(1, "x")
    comp_plus = sum(0.5j * 2 * u01 @ cx(0, a) @ cx(1, a) for a in "xyz")
    Dm = P @ (Hs - comp_plus) @ P
    return float(np.abs(Dm).max()), float(np.abs(np.linalg.eigvalsh((Dm + Dm.conj().T) / 2)).max()), float(np.abs(Dm - Dm.conj().T).max()), int(round(np.trace(P).real))


def main():
    note = show(NOTE); runner = show(RUNNER)
    raw = show(CACHE)
    lines = raw.split("----- stdout -----\n", 1)[1].splitlines()
    pieces = statement_pieces(note)
    covered = {n: set() for n, _ in pieces}
    print(f"PR #{PR} head {HEAD[:10]}; cache {len(lines)} stdout lines; statement pieces: {', '.join(n for n, _ in pieces)}")
    out = {"CACHE": 0, "RUNNER": 0, "DERIVED": 0, "DEFINITION": 0, "HIT": 0}
    hits = []

    def cover(pat):
        c = 0
        for name, text in pieces:
            for m in re.finditer(pat, text, flags=re.I):
                covered[name].update(range(m.start(), m.end())); c += 1
        return c

    def item(iid, pat, kind, ok, source):
        if cover(pat) == 0:
            print(f"[UNUSED] {iid}: pattern not found in the statement text")
            return
        if ok:
            out[kind] += 1
            print(f"[{kind}] {iid} | {source}")
        else:
            out["HIT"] += 1
            hits.append(f"HIT: {iid} | {source}")

    def cline(needle):
        for i, l in enumerate(lines):
            if needle in l:
                return i + 1
        return None

    L1, L2, L3, L4 = (next(l for l in lines if l.startswith(k)) for k in ("[PASS] on the constrained space", "[PASS] each positive-J", "[PASS] each odd path", "[PASS] for random bond sectors"))
    item("constraint D_i = 1 and rank", r"D = -i b\^x b\^y b\^z c\^x c\^y c\^z = 1, dimension four|D_i = 1|\bfour\b(?= \)| Majorana)|dimension four|constraints D_i = 1|-\(i/2\)|\(i/2\)|sigma\^a = -\(i/2\)", "CACHE",
         "D_i = 1 (rank 4 per site)" in L1 and "rank 64" in L1, f"cache line {cline('[PASS] on the constrained space')}: 'D_i = 1 (rank 4 per site)', 'three sites: rank 64'")
    item("rank 64 of 512", r"three sites \(rank 64 of 512\)|\b64 of 512\b|rank 64|\b512\b|\bthree\b sites|constrained space of three sites", "CACHE", "rank 64" in L1 and "majoranas(9)" in runner and 2 ** 9 == 512 and 4 ** 3 == 64,
         f"cache line {cline('[PASS] on the constrained space')} prints rank 64; the runner builds majoranas(9) = 18 Majoranas = 3 sites x 6 on 9 qubits, dimension 2^9 = 512 (runner source; 4^3 = 64 constrained)")
    item("two sites (bond)", r"constrained Clifford spaces of two and three sites|\btwo and three sites\b|\btwo\b(?= and three)", "RUNNER", "SPN[0]" in runner and "SPN[1]" in runner and "s0, t0 = SPN[0]; s1, t1 = SPN[1]" in runner,
         "runner check 2 builds the bond from SPN[0] and SPN[1] (two sites of the three-site space); check 3 uses SPN[0..2] (three sites); the cache prints only 'three sites: rank 64' (docstring: 'two sites' for the bond)")
    item("hopping -2J, sign -", r"hopping -2J u_ij|hopping -2 kappa u u|\(-2J u|\(-2kappa u|-2J|-2kappa|-2 kappa|\b2 kappa\b|\b2J\b|\+2J|the opposite", "CACHE",
         "hopping -2J u_ij" in L2 and all(f"{x}: residual 4.0e+00 (+), 0.0e+00 (-)" in L2 for x in "xyz") and "sign {-1}" in L3, f"cache lines {cline('[PASS] each positive-J')}-{cline('[PASS] each odd path')}: residual 4.0e+00 for + and 0.0e+00 for - on x, y, z; odd path 'sign {{-1}}' with all six (colour pair, sublattice) cases")
    ent, opn, herm, rk = own_bond_norms()
    item("norm 4", r"has norm 4|norm 4|\b4\b(?= So)", "CACHE", False,
         f"the cache (line {cline('[PASS] each positive-J')}) prints residual 4.0e+00 (+), which in the runner is res = max |entry| of P A P (largest matrix entry); recomputed here with an independent Jordan-Wigner construction (rank {rk}): "
         f"largest entry {ent:.3f} = 4, but the OPERATOR norm of P (H_spin - comparator(+2J u)) P (Hermitian to {herm:.0e}) is {opn:.3f}; the note's 'the difference with the other sign has norm 4' holds for the entrywise sup norm, not the operator norm")
    # derivations
    okdet = all(sp.diag(*([-1] * (n // 2) + [1] * (n // 2))).det() == (-1) ** (n // 2) for n in (2, 4, 6, 8, 10))
    A = sp.Matrix(6, 6, lambda i, j: 0)
    okpf = True
    for n in (2, 4, 6, 8):
        rng = sp.symbols(f"a0:{n * n}")
        M = sp.zeros(n, n)
        for i in range(n):
            for j in range(i + 1, n):
                M[i, j] = rng[i * n + j]; M[j, i] = -rng[i * n + j]
        okpf &= sp.expand(pfaffian(-M) - (-1) ** (n // 2) * pfaffian(M)) == 0
    item("(-1)^(N/2): det S and Pf(-A)", r"\(-1\)\^\(N/2\)|\(-1\)\^\{N/2\}|det S = \(-1\)\^\{N/2\}|ground parity by|Pf\(A\)|Pf\(-A\)|\b1\b(?= sends|\))", "DERIVED", okdet and okpf,
         "det of the sublattice flip S (N/2 entries -1) is (-1)^(N/2) for N = 2..10, and Pf(-A) = (-1)^(N/2) Pf(A) for symbolic antisymmetric A with N = 2, 4, 6, 8 (sympy)")
    a, b, c = sp.symbols("a b c", positive=True, integer=True)
    okN = sp.simplify((2 * a) * (2 * b) * (4 * c) / 2 - 8 * a * b * c) == 0 and all(sp.Rational(n, 2) % 2 == 0 for n in (8, 16, 32, 64, 128))
    item("N = Lx Ly Lz/2 = 8abc, N/2 even", r"N = Lx Ly Lz / 2|Lx, Ly even|multiple of four|N = 8abc|N/2 is even|Lz a multiple|N = 8abc\b|\b2\b(?= with Lx| Lx)|\b8\b(?=abc)|\b2\b(?= Lx)|Lx Ly Lz / 2 with", "DERIVED", okN,
         "Lx = 2a, Ly = 2b, Lz = 4c give N = Lx Ly Lz/2 = 8abc (sympy), so N/2 = 4abc is even")
    item("32-, 64-, 128-site tori", r"32-, 64- and 128-site tori|\b32\b|\b64\b(?!\s+of)|\b128\b|random sectors of the|random bond sectors", "CACHE", all(f"{n} sites (N/2 = {n // 2})" in L4 for n in (32, 64, 128)) and "(4, 4, 4), (8, 4, 4), (8, 8, 4)" in runner,
         f"cache line {cline('[PASS] for random bond sectors')}: '32 sites (N/2 = 16), 64 sites (N/2 = 32), 128 sites (N/2 = 64)'; runner tori (4,4,4), (8,4,4), (8,8,4)")
    item("kappa = 0.3", r"at kappa = 0\.3|kappa = 0\.3|\b0\.3\b", "CACHE", "at kappa = 0.3" in L4 and "sod * 0.3" in runner, f"cache line {cline('[PASS] for random bond sectors')}: 'at kappa = 0.3'; runner: odd coupling sod * 0.3")
    m = re.search(r"max spread over conventions ([0-9.e+-]+)", L4)
    item("1.1 x 10^-13", r"1\.1 x 10\^-13|\b1\.1\b|\b10\b(?=\^-13)|\b13\b", "CACHE", m is not None and f"{float(m.group(1)):.1e}" == "1.1e-13", f"cache line {cline('[PASS] for random bond sectors')}: 'max spread over conventions {m.group(1) if m else None}'")
    item("four conventions", r"\bfour\b sign conventions|the four sign conventions|\bfour conventions\b|\bfour\b", "RUNNER", "for sbd in (1.0, -1.0) for sod in (1.0, -1.0)" in runner, "runner: es = [... for sbd in (1.0, -1.0) for sod in (1.0, -1.0)]: bond +-, odd +- = four conventions")
    item("six Majoranas", r"six-Majorana representation|\bsix\b", "RUNNER", "g[6 * s]" in runner and "g[6 * s + 5]" in runner, "runner site(g, s): the six Majoranas g[6s .. 6s+5] of site s (b^x, b^y, b^z, c^x, c^y, c^z)")
    item("word counts", r"\bone\b|\btwo\b|\bthree\b|\bzero\b|\bpair\b|\bsingle\b", "DEFINITION", True, "wording ('one sign', 'two outer sites', 'colour pair', 'single-particle levels', 'pair excitations', ...)")
    unc = []
    ntok = 0
    for name, text in pieces:
        for a_, b_, v in tokens(text):
            ntok += 1
            if not any(p in covered[name] for p in range(a_, b_)):
                unc.append((name, v, text[max(0, a_ - 40):b_ + 30]))
    for name, v, ctx in unc:
        print(f"[UNCOVERED] {name} | {v} | ...{ctx}...")
    for h in hits:
        print(h)
    print(f"[COVERAGE] {ntok} numeric tokens in the statement text; uncovered {len(unc)}")
    print(f"SUMMARY: {sum(v for kk, v in out.items() if kk != 'HIT')} items over claim_scope + Result ({ntok} numeric tokens, {len(unc)} uncovered): cache {out['CACHE']}, runner {out['RUNNER']}, derived {out['DERIVED']}, definitions {out['DEFINITION']}; unsourced {out['HIT']}")
    if hits:
        print("HIT: " + "; ".join(h[5:] for h in hits))
    if unc:
        print("HIT: uncovered tokens " + "; ".join(f"{v} in {n}" for n, v, _ in unc))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
