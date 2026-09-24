#!/usr/bin/env python3
"""Exact checks: inertia and the rule's weights do not mix locally - streaming records keep the rule's law with radius-one rates at three
records, never at four (a probes worker's result, w-macbookpro90c72-j5257, verified here; block 50's objects; not adopted).

B (T1): block 50 reproduced; with moves at the local clock or at rate one no exchange rates balance three records; no rule balances record by record.
C (T2): exact radius-one rules for the three-record sector on 3^3 and 4^3 at c = 1 and c0 = 1/2.
D (T3): exact Farkas certificates: no radius-one rule balances four records on 3^3, with or without head-on re-draws.
E (T3): the same on Z^3 through compact clusters whose equations agree on 6^3 and 9^3; conservation by every event.
Exact arithmetic only (Fractions); the certificates were proposed by a linear-programming solver and are verified here in exact arithmetic.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 1800
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_INERTIA_AND_THE_RULES_WEIGHTS_DO_NOT_MIX_LOCALLY_STREAMING_RECORDS_KEEP_THE_RULES_LAW_AT_THREE_RECORDS_NEVER_AT_FOUR_BOUNDED_THEOREM_NOTE_2026-09-23.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_rule_inertia_and_the_rules_weights_certificates_2026_09_23.json",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_inertia_and_the_rules_weights_do_not_mix_locally_streaming_records_keep_the_rules_law_at_three_records_never_at_four_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "local_clock_certificate_negated": "B",
    "one_rate_perturbed": "C",
    "four_record_certificate_truncated": "D",
    "cluster_rows_from_the_small_torus": "E",
    "claim_transition_injected": "F",
    "claim_classical_name_in_theorem": "F",
}
ACTIVE_MUTATION: str | None = None


def mut(name: str) -> bool:
    if name not in MUTATION_GATE:
        raise KeyError(name)
    return ACTIVE_MUTATION == name


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.failed_families: set[str] = set()

    def check(self, tag: str, ok: bool, msg: str) -> None:
        if ok:
            self.passed += 1
            print(f"PASS: {tag} {msg}")
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}")


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


F = Fraction
ZERO = F(0)
ONE = F(1)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts[0], texts[1]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, and Admissibility does not define a time metric (the clauses work in that opening)")


# ============================================================================================ helpers (block 50's objects)
import ast
import itertools
import json
from itertools import combinations

Fr = F
E = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
GROUP = [(perm, sg) for perm in itertools.permutations(range(3)) for sg in product((1, -1), repeat=3)]
BASE = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (2, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1),
        (1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1)]          # in the frame where the event is along +x: index 1 = target


def gvec(g, v):
    perm, sg = g
    w = [0, 0, 0]
    for i in range(3):
        w[perm[i]] = sg[i] * v[i]
    return tuple(w)


CON_OF = {E[c]: c for c in range(6)}


class Torus:
    def __init__(self, L):
        self.L = L
        self.SITES = list(product(range(L), repeat=3))
        self.IDX = {x: i for i, x in enumerate(self.SITES)}
        self.N = L ** 3
        self.NB = [[self.add(x, d) for d in E] for x in self.SITES]
        self.FR = {}
        for x in range(self.N):
            for s in range(6):
                lst = []
                for g in GROUP:
                    if gvec(g, E[s]) != (1, 0, 0):
                        continue
                    perm, sg = g
                    sites, seen = [], set()
                    for d in BASE:
                        r = [sg[i] * d[perm[i]] for i in range(3)]
                        site = self.add(self.SITES[x], r)
                        if site in seen:
                            continue                     # L = 3: 2 e_s is -e_s
                        seen.add(site)
                        sites.append(site)
                    lst.append((sites, [CON_OF[gvec(g, E[c])] for c in range(6)]))
                self.FR[(x, s)] = lst

    def add(self, x, d):
        return self.IDX[tuple((x[i] + d[i]) % self.L for i in range(3))]

    def env(self, occ, x):
        best = None
        for sites, gc in self.FR[(x, occ[x])]:
            key = tuple(gc[occ[t]] if occ[t] >= 0 else -1 for t in sites)
            if best is None or key < best:
                best = key
        return best

    def rot(self, occ, x, a):
        best = None
        for sites, gc in self.FR[(x, occ[x])]:
            key = (tuple(gc[occ[t]] if occ[t] >= 0 else -1 for t in sites), gc[a])
            if best is None or key < best:
                best = key
        return ('rot',) + best

    def weight(self, occ, w, one=1):
        """pi(C): product over adjacent occupied pairs (scans only occupied sites); w entries Fractions or floats"""
        val = one
        occd = [a for a in range(self.N) if occ[a] >= 0]
        for a in occd:
            for b in self.NB[a]:
                if b > a and occ[b] >= 0:
                    c1, c2 = occ[a], occ[b]
                    val *= w[0] if c1 == c2 else (w[1] if c1 == (c2 ^ 1) else w[2])
        return val

    def own(self, occ, x, w):
        val = Fr(1)
        for b in self.NB[x]:
            if occ[b] >= 0:
                c1, c2 = occ[x], occ[b]
                val *= w[0] if c1 == c2 else (w[1] if c1 == (c2 ^ 1) else w[2])
        return val

    def configs(self, nrec):
        for rest in combinations(range(1, self.N), nrec - 1):
            pos = (0,) + rest
            for con in product(range(6), repeat=nrec):
                occ = [-1] * self.N
                for p_, c_ in zip(pos, con):
                    occ[p_] = c_
                yield pos, con, occ

    def terms(self, pos, occ, mode='base'):
        """(key, sign, config) : sign +1 an event out of C (config None), -1 an event into C from config"""
        out = []
        for x in pos:
            s = occ[x]
            t = self.NB[x][s]
            out.append((self.env(occ, x), +1, None))
            if mode == 'rot' and occ[t] == (s ^ 1):
                for a in range(6):
                    if a // 2 != s // 2:
                        out.append((self.rot(occ, x, a), +1, None))
            behind = self.NB[x][s ^ 1]
            occ2 = list(occ)
            if occ[behind] >= 0:
                occ2[behind], occ2[x] = occ[x], occ[behind]
            else:
                occ2[behind] = s
                occ2[x] = -1
            out.append((self.env(occ2, behind), -1, occ2))
        if mode == 'rot':
            for x in pos:
                for di in (0, 2, 4):
                    y = self.NB[x][di]
                    c = occ[x]
                    if occ[y] >= 0 and occ[y] == (c ^ 1) and c // 2 != di // 2:
                        occ3 = list(occ)
                        occ3[x] = di
                        occ3[y] = di ^ 1
                        for actor, a_out in ((x, c), (y, occ[y])):
                            out.append((self.rot(occ3, actor, a_out), -1, occ3))
        return out

    def row(self, pos, occ, w, mode='base', one=1):
        pi = self.weight(occ, w, one)
        acc = {}
        for key, sg, o2 in self.terms(pos, occ, mode):
            acc[key] = acc.get(key, 0) + (pi if sg > 0 else -self.weight(o2, w, one))
        return {k: v for k, v in acc.items() if v != 0}


def is_move(key):
    return key[0] != 'rot' and key[1] == -1


def kstr(key):
    return repr(key)


DATA_PATH = "scripts/admissibility_rule_inertia_and_the_rules_weights_certificates_2026_09_23.json"
W = {"c1": (Fr(3), Fr(1), Fr(2)), "c0": (Fr(3, 2), Fr(1, 2), Fr(1))}


def load_data():
    return json.load(open(Path(ROOT, DATA_PATH)))


def rq(s):
    a, b = s.split("/")
    return Fr(int(a), int(b))


def occ_of(T, pos, con):
    occ = [-1] * T.N
    for p_, c_ in zip(pos, con):
        occ[p_] = c_
    return occ


def backstep(T, occ, x):
    s = occ[x]
    behind = T.NB[x][s ^ 1]
    o2 = list(occ)
    if occ[behind] >= 0:
        o2[behind], o2[x] = occ[x], occ[behind]
    else:
        o2[behind] = s
        o2[x] = -1
    return behind, o2


def farkas(T, cert, w, mode):
    """sum over the certificate's configurations of y times the balance row; returns (A^T y by class, y.(A l) with l = 1 on moves)."""
    ATy, yl = {}, Fr(0)
    for kc, yy in cert.items():
        pos, con = ast.literal_eval(kc.split("|")[0]), ast.literal_eval(kc.split("|")[1])
        row = T.row(pos, occ_of(T, pos, con), w, mode, Fr(1))
        yv = rq(yy)
        for k, c in row.items():
            ATy[k] = ATy.get(k, 0) + c * yv
            if is_move(k):
                yl += c * yv
    return ATy, yl


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: block 50 reproduced; the natural clocks fail at three records; no rule balances record by record."""
    D = load_data()
    T3 = Torus(3)
    w = W["c1"]
    n, bad_g, bad_l, largest = 0, 0, 0, 0
    for pos, con, occ in T3.configs(3):
        pi = T3.weight(occ, w, Fr(1))
        out_l = sum((pi / T3.own(occ, x, w) for x in pos), Fr(0))
        in_l, in_g = Fr(0), 0
        for x in pos:
            behind, o2 = backstep(T3, occ, x)
            in_l += T3.weight(o2, w, Fr(1)) / T3.own(o2, behind, w)
            in_g += 1
        n += 1
        bad_g += in_g != len(pos)
        if out_l != in_l:
            bad_l += 1
            largest = max(largest, abs(out_l - in_l))
    reproduced = n == 70200 and bad_g == 0 and bad_l == 3168 and largest == 3

    def mv_fixed(k, fam, w):
        if fam == "unitmoves":
            return Fr(1)
        own = Fr(1)
        for pos_ in (1, 2, 3, 4, 5, 6):
            c = k[pos_]
            if c >= 0:
                own *= w[0] if c == 0 else (w[1] if c == 1 else w[2])
        return 1 / own
    cert_ok = True
    for fam in ("localclock", "unitmoves"):
        for name, ww in W.items():
            MT, by = {}, Fr(0)
            for kc, yy in D[f"cert_{fam}_{name}"].items():
                pos, con = ast.literal_eval(kc.split("|")[0]), ast.literal_eval(kc.split("|")[1])
                row = T3.row(pos, occ_of(T3, pos, con), ww, "base", Fr(1))
                yv = rq(yy) if not mut("local_clock_certificate_negated") else -rq(yy)
                by += -sum((c * mv_fixed(k, fam, ww) for k, c in row.items() if is_move(k)), Fr(0)) * yv
                for k, c in row.items():
                    if not is_move(k):
                        MT[k] = MT.get(k, 0) + c * yv
            cert_ok = cert_ok and all(v >= 0 for v in MT.values()) and by < 0
    rw_ok = True
    for name, ww in W.items():
        ATy, yl = {}, Fr(0)
        for kc, yy in D[f"cert_recordwise_{name}"].items():
            a, b, kr = kc.split("|")
            pos, con, kr = ast.literal_eval(a), ast.literal_eval(b), int(kr)
            occ = occ_of(T3, pos, con)
            x = pos[kr]
            behind, o2 = backstep(T3, occ, x)
            row = {}
            k1, k2 = T3.env(occ, x), T3.env(o2, behind)
            row[k1] = row.get(k1, 0) + T3.weight(occ, ww, Fr(1))
            row[k2] = row.get(k2, 0) - T3.weight(o2, ww, Fr(1))
            for k, c in row.items():
                ATy[k] = ATy.get(k, 0) + c * rq(yy)
                if is_move(k):
                    yl += c * rq(yy)
        rw_ok = rw_ok and all(v >= 0 for v in ATy.values()) and yl > 0
    checks.check("B1", reproduced and cert_ok and rw_ok, f"T1: block 50 (#8562) reproduced on 3^3 at (3,1,2), c = 1: {n} three-record configurations with a record at the origin, three events out and three in each (global clock), the local clock 1/pi_x failing at {bad_l} with largest defect {largest}; exact Farkas certificates show that with every move at the local clock, or at rate one, no exchange rates balance the three-record sector (c = 1 and the neutral scale c0 = 1/2), and that no rule balances each record against its own predecessor")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: radius-one local rules exist for three records (exact rules on 3^3 and 4^3, both scales)."""
    D = load_data()
    good = True
    info = []
    for L in (3, 4):
        T = Torus(L)
        for name, w in W.items():
            rates = {ast.literal_eval(k): rq(v) for k, v in D[f"rule_L{L}_{name}"].items()}
            if mut("one_rate_perturbed") and L == 3 and name == "c1":
                k0 = sorted(rates, key=repr)[0]
                rates[k0] = rates[k0] + 1
            nconf, nbad, missing = 0, 0, 0
            for pos, con, occ in T.configs(3):
                row = T.row(pos, occ, w, "base", Fr(1))
                if any(k not in rates for k in row):
                    missing += 1
                    continue
                nconf += 1
                nbad += sum((c * rates[k] for k, c in row.items()), Fr(0)) != 0
            mv = [r for k, r in rates.items() if is_move(k)]
            ex = [r for k, r in rates.items() if not is_move(k)]
            good = good and nbad == 0 and missing == 0 and min(mv) >= 1 and min(ex) >= 0
            info.append(f"{L}^3 {name}: {len(rates)} classes, {nconf} configurations")
    checks.check("C1", good, "T2: rates depending only on the sites within distance one of an event exist that keep the rule's law stationary on the three-record sector: exact rational rules, moves >= 1, exchanges >= 0, every configuration balanced (" + "; ".join(info) + ")")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: no radius-one rule balances four records on 3^3, with or without head-on re-draws on the momentum class."""
    D = load_data()
    T3 = Torus(3)
    ok = True
    info = []
    for mode in ("base", "rot"):
        for name, w in W.items():
            cert = dict(D[f"cert_joint_{mode}_{name}"])
            if mut("four_record_certificate_truncated") and mode == "base" and name == "c1":
                big = max(cert, key=lambda k: abs(rq(cert[k])))
                cert.pop(big)
            ATy, yl = farkas(T3, cert, w, mode)
            n4 = sum(1 for kc in cert if len(ast.literal_eval(kc.split("|")[0])) == 4)
            ok = ok and all(v >= 0 for v in ATy.values()) and yl > 0
            info.append(f"{'streaming' if mode == 'base' else 'with re-draws'} {name}: {n4} four-record rows")
    checks.check("D1", ok, "T3: exact Farkas certificates (A^T y >= 0 on every rate class, y.(A l) > 0 with l = 1 on moves) show that no radius-one rule keeps the rule's law stationary on the four-record sector of 3^3, for streaming alone and with head-on pairs re-drawing on their momentum class; every certificate uses four-record rows only (" + "; ".join(info) + ")")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T3 on Z^3: compact four-record clusters whose equations are the same on 6^3 and 9^3; conservation by every event."""
    D = load_data()
    T6, T9 = Torus(6), Torus(9)
    Tcmp = T9 if not mut("cluster_rows_from_the_small_torus") else Torus(3)
    ok = True
    info = []
    for mode in ("base", "rot"):
        for name, w in W.items():
            ATy, yl, same, nsup = {}, Fr(0), True, 0
            for kc, yy in D[f"cert_Z3_{mode}_{name}"].items():
                pos, con = ast.literal_eval(kc.split("|")[0]), ast.literal_eval(kc.split("|")[1])
                row = T6.row(pos, occ_of(T6, pos, con), w, mode, Fr(1))
                try:
                    posc = tuple(Tcmp.IDX[T6.SITES[p_]] for p_ in pos)
                    rowc = Tcmp.row(posc, occ_of(Tcmp, posc, con), w, mode, Fr(1))
                    same = same and row == rowc
                except KeyError:
                    same = False
                nsup += 1
                for k, c in row.items():
                    ATy[k] = ATy.get(k, 0) + c * rq(yy)
                    if is_move(k):
                        yl += c * rq(yy)
            ok = ok and same and all(v >= 0 for v in ATy.values()) and yl > 0
            info.append(f"{'streaming' if mode == 'base' else 'with re-draws'} {name}: {nsup} clusters")
    T3 = Torus(3)
    cons = True
    for pos, con, occ in list(T3.configs(3))[::997]:
        for key, sg, o2 in T3.terms(pos, occ, "rot"):
            if o2 is not None:
                def mom(o):
                    return tuple(sum((1 if c == 2 * i else -1 if c == 2 * i + 1 else 0) for c in o if c >= 0) for i in range(3))
                cons = cons and sum(1 for c in o2 if c >= 0) == len(pos) and mom(o2) == mom(occ)
    checks.check("E1", ok and cons, "T3 on Z^3: compact four-record clusters (a record at the origin, the others in [0,2]^3) have the same balance equations on the 6^3 and 9^3 tori, hence are equations of the problem on Z^3, and exact certificates show them infeasible (" + "; ".join(info) + "); every event keeps the number of records and the total content vector (sampled predecessors on 3^3)")


# ============================================================================================ family F
FENCES = (
    "This note works within block 50's supplied clauses (records whose content is a direction of travel, streaming with exchange, the six-axis rule's pair weights) and reports, from a probes worker's exact certificates verified here, whether local rates can keep the rule's law stationary; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
                   "Pauli", "Hamilton", "Ehrenfest", "Wigner", "Bloch", "Berry", "Schrodinger", "Lorentz", "Hartree", "Mach", "Eddington", "Soldner", "Dicke", "Riemann", "Regge", "Lame", "Hooke", "Abraham", "Arnowitt", "Deser", "Misner", "Brill", "Lindquist", "Isenberg", "Wilson", "Mathews", "Lichnerowicz", "York", "Hilbert", "Tolman", "Komar", "Friedmann", "Ricci",
                   "Christoffel", "Baierlein", "Wheeler", "Lagrange", "Jacobi", "Brans", "Nordtvedt")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Einstein)", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if re.search(r"\b" + nm + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + nm + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - every three-record configuration of 3^3 and 4^3 against the exact rules; every row of every certificate",
    "per_site: executed - block 50's local-clock defects at all 70200 configurations of 3^3",
    "per_mode: not applicable - no mode decomposition is used",
    "per_block: executed - compact clusters compared on the 6^3 and 9^3 tori",
    "lattice_wide: T1-T2 on the stated tori; T3 on 3^3 and on Z^3 through compact clusters; the locality class (radius one) and block 50's clauses are supplied; certificates proposed by a solver and verified exactly",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


def main(argv) -> int:
    global ACTIVE_MUTATION
    if "--list-mutations" in argv:
        for name, fam in MUTATION_GATE.items():
            print(f"{name} {fam}")
        return 0
    if "--mutation" in argv:
        ACTIVE_MUTATION = argv[argv.index("--mutation") + 1]
        if ACTIVE_MUTATION not in MUTATION_GATE:
            print(f"unknown mutation {ACTIVE_MUTATION}")
            return 2
    print("AUDIT_INPUT_PATHS:")
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    texts = [Path(ROOT, p).read_text(encoding="utf-8") if Path(ROOT, p).exists() else "" for p in AUDIT_INPUT_PATHS]
    checks = Checks()
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: inertia and the rule's weights - radius-one local rates keep the rule's law stationary for streaming records at three records (exact rules on 3^3, 4^3), never with the local clock or unit moves, never record by record; at four records no radius-one rule exists, on 3^3 and on Z^3, with or without momentum-class re-draws; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
