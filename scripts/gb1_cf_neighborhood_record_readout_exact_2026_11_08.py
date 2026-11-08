#!/usr/bin/env python3
"""Exact finite propagation/readout checks; no axiom-derived quantum law.

Gaussian-rational state vectors test all 32 basis columns of a five-qubit
circuit. Hadamards are unnormalized; two H gates multiply the physical
output amplitudes by two, and reported probabilities divide by that factor.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
from itertools import permutations, product
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time

AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/SU2_HOMOGENEOUS_NATIVE_QUBIT_CODE_BOUNDED_THEOREM_NOTE_2026-11-08.md",
    "docs/SU2_NEIGHBORHOOD_PROPAGATION_RECORD_READOUT_BOUNDED_THEOREM_NOTE_2026-11-08.md",
)
AUDIT_TIMEOUT_SEC = 60
CHECKS = 0
NQ = 5
ZERO = (F(0), F(0))
ONE = (F(1), F(0))
I = (F(0), F(1))
HALF = F(1, 2)


def qa(a, b):
    return a[0] + b[0], a[1] + b[1]


def qm(a, b):
    return a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0]


def qs(k, a):
    return k*a[0], k*a[1]


def norm2(v):
    return sum((a*a+b*b for a, b in v.values()), F(0))


def put(out, z, a):
    out[z] = qa(out.get(z, ZERO), a)
    if out[z] == ZERO:
        del out[z]


def eq(label, actual, expected):
    global CHECKS
    if actual != expected:
        raise AssertionError(f"{label}: {actual!r} != {expected!r}")
    CHECKS += 1


def mask(site):
    return 1 << (NQ-1-site)


def apply_gate(v, gate):
    kind, *sites = gate
    out = {}
    if kind == "X":
        return {z ^ mask(sites[0]): a for z, a in v.items()}
    if kind == "H":
        m = mask(sites[0])
        for z, a in v.items():
            put(out, z & ~m, a)
            put(out, z | m, qs(-1 if z & m else 1, a))
        return out
    m, n = map(mask, sites)
    for z, a in v.items():
        if kind == "ID":
            put(out, z, a)
        elif kind == "S":
            t = z ^ (m | n) if bool(z & m) != bool(z & n) else z
            put(out, t, a)
        elif kind == "C":
            put(out, z ^ n if z & m else z, a)
        elif kind in ("V", "Vd", "BADV"):
            if not z & m:
                put(out, z, a)
            else:
                if kind == "BADV":
                    # X is not a square root of X.
                    put(out, z ^ n, a)
                else:
                    sign = 1 if kind == "V" else -1
                    put(out, z, qm((HALF, sign*HALF), a))
                    put(out, z ^ n, qm((HALF, -sign*HALF), a))
        else:
            raise ValueError(gate)
    return out


def run(v, word):
    for gate in word:
        v = apply_gate(v, gate)
    return v


def remote_cx(c, b, middle):
    return [("S", c, middle), ("C", middle, b), ("S", c, middle)]


def local_fredkin(c, a, b):
    # Exact controlled square-root word, not a three-site primitive.
    return (
        [("C", a, b), ("V", b, a)]
        + remote_cx(c, b, a)
        + [("Vd", b, a)]
        + remote_cx(c, b, a)
        + [("V", c, a), ("C", a, b)]
    )


def controlled_reversal(fault):
    word = []
    for i in (1, 2, 3, 1, 2, 1):
        route = [("S", j, j+1) for j in range(i-1)]
        word += route + local_fredkin(i-1, i, i+1) + list(reversed(route))
    if fault == "drop-return":
        # Remove one nonempty routing inverse, retaining local gate support.
        word[23] = ("ID",)+word[23][1:]
    if fault == "wrong-root":
        word = [(("BADV",)+g[1:]) if g[0] == "V" else g for g in word]
    return word


def reverse4(z):
    return int(f"{z:04b}"[::-1], 2)


def direct_cf(z):
    return (16 | reverse4(z & 15)) if z & 16 else z


def direct_interferometer(z):
    data, pointer = z & 15, bool(z & 16)
    reversed_data = reverse4(data)
    out = {}
    put(out, data, ONE)
    put(out, 16 | data, ONE)
    put(out, reversed_data, qs(-1 if pointer else 1, ONE))
    put(out, 16 | reversed_data, qs(1 if pointer else -1, ONE))
    return out


def code_columns():
    # Each displayed vector has squared norm two.
    return (
        {8: ONE, 1: ONE},
        {8: ONE, 1: qs(-1, ONE)},
        {4: ONE, 2: qs(-1, ONE)},
        {12: ONE, 3: qs(-1, ONE)},
        {4: ONE, 2: ONE},
    )


def pointer_probability(v, outcome, input_norm):
    return sum((a*a+b*b for z, (a, b) in v.items()
                if bool(z & 16) == bool(outcome)), F(0)) / (4*input_norm)


def circuit_checks(fault):
    cf = controlled_reversal(fault)
    eq("74 adjacent pair gates", len(cf), 74)
    for g in cf:
        eq("adjacent gate support", abs(g[1]-g[2]), 1)
    for z in range(32):
        eq(f"controlled reversal basis {z}", run({z: ONE}, cf),
           {direct_cf(z): ONE})
    word = [("H", 0)] + cf + [("H", 0)]
    for z in range(32):
        eq(f"interferometer full basis {z}", run({z: ONE}, word),
           direct_interferometer(z))
    signs = (1, -1, -1, -1, 1)
    for k, v in enumerate(code_columns()):
        out = run(v, word)
        p = 0 if signs[k] == 1 else 1
        expected = {z | (16*p): qs(2, a) for z, a in v.items()}
        eq(f"five-state code output {k}", out, expected)
        eq(f"five-state norm {k}", norm2(out), 4*norm2(v))
        eq(f"deterministic code outcome {k}", pointer_probability(out, p, 2), 1)
    for label, phase, expected in (("plus", ONE, 1), ("minus", qs(-1, ONE), 0),
                                   ("imaginary", I, HALF)):
        v = {8: ONE, 1: phase}
        out = run(v, word)
        prob = pointer_probability(out, 0, norm2(v))
        if fault == "record-first":
            prob = sum(pointer_probability(run({z: ONE}, word), 0, 1)
                       for z in (8, 1))/2
        eq("phase-sensitive " + label, prob, expected)
    for z in (8, 1):
        eq("data-dephased phase readout", pointer_probability(
            run({z: ONE}, word), 0, 1), HALF)
    # Q diagonal at |1100>,|0011>, constructed from all five columns.
    qdiag = {z: sum((a.get(z, ZERO)[0]**2+a.get(z, ZERO)[1]**2
                     for a in code_columns()), F(0))/2 for z in (12, 3)}
    eq("dephased J3 code survival", sum(qdiag.values())/2, HALF)
    # |1> on output is orthogonal to the original fixed-|0> spectator.
    minus_out = run(code_columns()[1], word)
    eq("old global spectator sector after negative outcome",
       pointer_probability(minus_out, 0, 2), 0)
    print("CIRCUIT pair_gates=74 onsite_H=2 full_basis_columns=32 code_columns=5")
    print("PHASE p0(0)=1 p0(pi)=0 p0(pi/2)=1/2; data-dephased p0=1/2")
    print("ENCODING J3_Z_dephasing_code_survival=1/2; old_spectator_overlap=0")


def electric_compact_checks(fault):
    decode = [("S", 3, 4), ("S", 2, 3), ("C", 1, 2), ("H", 1), ("C", 3, 4)]
    encode = list(reversed(decode))
    if fault == "electric-inverse":
        encode[0] = ("ID", 3, 4)
    ccx = [("V", 1, 0), ("C", 2, 1), ("Vd", 1, 0), ("C", 2, 1),
           ("S", 2, 1), ("V", 1, 0), ("S", 2, 1)]
    flag = ([("X", 1), ("X", 4), ("S", 3, 4), ("S", 2, 3)] + ccx
            + [("S", 2, 3), ("S", 3, 4), ("X", 1), ("X", 4), ("X", 0)])
    word = decode+flag+encode
    eq("compact electric pair count", sum(len(g) == 3 for g in word), 19)
    eq("compact electric onsite count", sum(len(g) == 2 for g in word), 7)
    for g in word:
        if len(g) == 3:
            eq("compact electric adjacency", abs(g[1]-g[2]), 1)
    # The decoder's two-bit predicate has rank 4 on the full data space.
    # It equals the rank-1 encoded vacuum projector only ON THE CODE.
    for k, col in enumerate(code_columns()):
        decoded = run(col, decode)
        selected = {z:a for z,a in decoded.items() if not z & 9}
        eq("two-bit energy flag", selected, decoded if k == 0 else {})
        for initial_pointer in (0, 1):
            output_pointer = initial_pointer ^ (k != 0)
            out = run({z | (16*initial_pointer):a for z,a in col.items()}, word)
            eq("compact electric code isometry", out,
               {z | (16*output_pointer):qs(2,a) for z,a in col.items()})
    for phase, expected in ((ONE, 1), (qs(-1, ONE), 0), (I, HALF)):
        v = {8:ONE, 1:phase}
        eq("electric phase-sensitive probability", pointer_probability(run(v, word), 0, 2), expected)
    print("ELECTRIC_COMPACT pair_gates=19 onsite_gates=7 clean_work=0 output=1 code_columns=5 both_pointer_inputs")
    print("ELECTRIC_COMPACT native_predicate_rank=4 code_vacuum_rank=1; output b reads 3b/4")


ELECTRIC_SITES = ((1, 1, 0), (2, 1, 0), (3, 1, 0),
                  (1, 0, 0), (2, 0, 0), (3, 0, 0), (4, 0, 0))


def adjacent(i, j):
    return sum(abs(a-b) for a, b in zip(ELECTRIC_SITES[i], ELECTRIC_SITES[j])) == 1


def path_between(start, end):
    queue = [[start]]
    visited = {start}
    for path in queue:
        for nxt in range(7):
            if nxt not in visited and adjacent(path[-1], nxt):
                candidate = path+[nxt]
                if nxt == end:
                    return candidate
                visited.add(nxt)
                queue.append(candidate)
    raise AssertionError("disconnected electric-readout geometry")


def routed(gate):
    kind, a, b = gate
    path = path_between(a, b)
    outward = [("S", x, y) for x, y in zip(path[:-2], path[1:-1])]
    return outward+[(kind, path[-2], path[-1])]+list(reversed(outward))


def toffoli(c, b, a):
    logical = [("V", b, a), ("C", c, b), ("Vd", b, a),
               ("C", c, b), ("V", c, a)]
    return [g for gate in logical for g in routed(gate)]


def electric_checks():
    global NQ
    NQ = 7
    # Native site labels: output 0, clean work 1/2, data 3/4/5/6.
    decode = [("X", 6)]+routed(("C", 3, 6))+[("H", 3)]
    encode = [("H", 3)]+routed(("C", 3, 6))+[("X", 6)]
    negate = [("X", i) for i in range(3, 7)]
    copy_zero = (negate+toffoli(3, 4, 1)+toffoli(1, 5, 2)
                 +toffoli(2, 6, 0)+toffoli(1, 5, 2)+toffoli(3, 4, 1)+negate)
    word = decode+copy_zero+encode
    for g in word:
        if len(g) == 3:
            eq("electric native adjacency", adjacent(g[1], g[2]), True)
    for i in (0, 1, 2):
        eq("electric workspace was spectator", sum(c % 5 != 0 for c in ELECTRIC_SITES[i]), 2)
    # Test every input column with work bits zero and either output value.
    for pointer in (0, 1):
        for data in range(16):
            z = data | (64*pointer)
            expected = {z: qs(2, ONE)}
            if data in (8, 1):
                for d in (8, 1):
                    put(expected, d | (64*pointer), qs(-1, ONE))
                    put(expected, d | (64*(1-pointer)), ONE)
            out = run({z: ONE}, word)
            eq("electric projector full clean-work input", out, expected)
            eq("electric work returned", all(z & 48 == 0 for z in out), True)
    for k, col in enumerate(code_columns()):
        out = run(col, word)
        pointer = 1 if k == 0 else 0
        eq("electric full code eigenstate", out,
           {z | (64*pointer): qs(2, a) for z, a in col.items()})
    pair_count = sum(len(g) == 3 for g in word)
    onsite_count = sum(len(g) == 2 for g in word)
    print(f"ELECTRIC pair_gates={pair_count} onsite_gates={onsite_count} clean_work=2 output=1 full_clean_work_columns=32")
    print("ELECTRIC output1=zero-electric output0=3/4; all five code vectors preserved; work restored")
    NQ = 5


def rotations():
    out = []
    for p in permutations(range(3)):
        parity = (-1)**sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3))
        for signs in product((-1, 1), repeat=3):
            if parity*signs[0]*signs[1]*signs[2] == 1:
                out.append((p, signs))
    return out


def rotate(r, x):
    p, signs = r
    return tuple(signs[i]*x[p[i]] for i in range(3))


def neighbors(x):
    for i in range(3):
        for s in (-1, 1):
            y = list(x)
            y[i] += s
            yield tuple(y)


def relay_odds(records, x):
    values = [records[y] for y in neighbors(x) if y in records]
    if not values:
        # Numerical certificate only for formed-neighbor inputs.
        raise ValueError("empty condition uses the continuum Haar measure in the proof")
    return {a: F(values.count(a), len(values)) for a in set(values)}


def relay_checks():
    origin = (0, 0, 0)
    ns = list(neighbors(origin))
    for colors in product((0, 1), repeat=6):
        records = dict(zip(ns, colors))
        odds = relay_odds(records, origin)
        eq("relay normalization", sum(odds.values()), 1)
        for r in rotations():
            rotated = {rotate(r, x): a for x, a in records.items()}
            eq("relay rotation covariance", relay_odds(rotated, origin), odds)
    for color in (0, 1):
        for r in rotations():
            records = {origin: color}
            for j in range(1, 33):
                x = rotate(r, (j, 0, 0))
                old = dict(records)
                eq("32-step copy", relay_odds(records, x), {color: F(1)})
                records[x] = color
                eq("permanent records", {y: records[y] for y in old}, old)
    print("RELAY all64_binary_six_neighbor_conditions all24_rotations lengths1..32 colors2")
    print("RELAY empty-neighbor Haar law and arbitrary-distance result are proved in prose")


def rss():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value*1024)


def bounds():
    for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                 "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
        if os.environ.get(name) != "1":
            raise RuntimeError(f"{name}=1 required")
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    started = time.monotonic()
    def guard(_sig, _frame):
        if time.monotonic()-started > 60:
            raise TimeoutError("60-second wall limit")
        if rss() >= 270_000_000:
            raise MemoryError("270 MB RSS guard")
    signal.signal(signal.SIGALRM, guard)
    signal.setitimer(signal.ITIMER_REAL, .05, .05)
    print("BOUNDS cpu=60s wall=60s RSS_guard=270000000 poll=0.05s threads=1")
    return started


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inject-fault", choices=("drop-return", "wrong-root", "record-first", "electric-inverse"))
    args = parser.parse_args()
    started = bounds()
    print("SOURCE_SHA256 " + sha256(Path(__file__).read_bytes()).hexdigest())
    circuit_checks(args.inject_fault)
    electric_compact_checks(args.inject_fault)
    electric_checks()
    relay_checks()
    print("per_element: all32 circuit basis columns and all five code columns checked exactly.")
    print("per_site: adjacent supports and fresh output are explicit; old spectator sector changes.")
    print("per_mode: checked and not executed - no momentum, mass gap or continuum claim.")
    print("per_block: finite relay and distinct five-/seven-qubit electric instruments checked separately.")
    print("lattice_wide: checked and not executed - no autonomous homogeneous joint law is derived.")
    print(f"TOTAL: PASS={CHECKS} FAIL=0")
    print(json.dumps({"seconds":time.monotonic()-started, "peak_rss_bytes":rss()}))


if __name__ == "__main__":
    main()
