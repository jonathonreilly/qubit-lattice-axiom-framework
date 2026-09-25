#!/usr/bin/env python3
"""The tight-sibling lemma, exhaustively on small cones (README section 8; blocks 32-33, PR #8177), run 1 of 2.

Two-level majority automaton in level time (probes/lib/family.py): a site is 1 if at least two of its three predecessors are 1, else 1 iff
marked.  Rooted value v(z) = min over the counted family's trees containing z and lying at levels <= level(z) of E - 3(|S| - 1) - |A| (c = 1)
(probes/lib/rooted.py by integer programming).  Since a site's kind depends only on its predecessors, v(z) depends only on the configuration
at levels <= level(z); here it is computed EXACTLY by probes/lib/family.brute_min on that restriction (Fractions), and cross-checked
against rooted.py's integer program on a random subset.  Lemma (open): a processed 1-site all of whose 1-predecessors are processed and tight
(v = 0) has v <= 0.  Exhaustive enumeration of every mark configuration with at most 6 marks on the depth-3 cone below a root, and with at
most 5 marks on the depth-4 cone; configurations are reduced by the cone's axis-permutation symmetry (orbit sizes weighted back).
"""
import itertools, os, sys, time
from fractions import Fraction as Fr
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "lib"))
import family as fam

def out(s): print(s, flush=True)

ROOT = (4, 4, 4)
def restricted(eta, z):
    lz = fam.level(z)
    return {w: v for w, v in eta.items() if fam.level(w) <= lz}

VCACHE = {}
def v_of(eta, z):
    """exact rooted value; cached on the (translated) set of 1-sites at levels <= level(z)"""
    r = restricted(eta, z)
    key = frozenset((w[0] - z[0], w[1] - z[1], w[2] - z[2]) for w, v in r.items() if v == 1)
    if key not in VCACHE:
        VCACHE[key] = fam.brute_min(r, z, 1)
    return VCACHE[key]

def canon(marks):
    best = None
    for perm in itertools.permutations(range(3)):
        t = tuple(sorted(tuple(m[perm[i]] for i in range(3)) for m in marks))
        if best is None or t < best: best = t
    return best

def exhaust(depth, kmax):
    sites = fam.cone(ROOT, depth)
    seen = {}
    for k in range(0, kmax + 1):
        for marks in itertools.combinations(sites, k):
            c = canon(marks)
            seen[c] = seen.get(c, 0) + 1
    stats = dict(configs=0, orbits=len(seen), processed=0, all_proc_tight=0, all_tight_incl_seeds=0, maxv=None, maxv_incl=None, witness=None, pos=[], vdist={})
    for c, mult in seen.items():
        stats["configs"] += mult
        zeta = {m: 1 for m in c}
        eta = fam.run_automaton(sites, zeta)
        ones, npred, kind = fam.kinds(eta)
        proc = [z for z in ones if kind[z] == "proc"]
        stats["processed"] += mult * len(proc)
        for z in proc:
            vz = v_of(eta, z)
            stats["vdist"][vz] = stats["vdist"].get(vz, 0) + mult
            ps = npred[z]
            vs = [(kind[u], v_of(eta, u) if kind[u] != "seed" else Fr(0)) for u in ps]
            if all(kk == "proc" and vv == 0 for kk, vv in vs):
                stats["all_proc_tight"] += mult
                if stats["maxv"] is None or vz > stats["maxv"]:
                    stats["maxv"] = vz
                if vz > 0:
                    stats["pos"].append((c, z, vz))
            if all(vv == 0 for kk, vv in vs):
                stats["all_tight_incl_seeds"] += mult
                if stats["maxv_incl"] is None or vz > stats["maxv_incl"]:
                    stats["maxv_incl"] = vz; stats["witness"] = (c, z)
                if vz > 0 and all(kk == "proc" for kk, vv in vs) is False:
                    stats.setdefault("pos_incl", []).append((c, z, vz))
    return stats

# ------------------------------------------------------------------ cross-check brute_min against rooted.py's integer program
import random
try:
    import rooted as rt
    rnd = random.Random(33); sites = fam.cone(ROOT, 3); agree = 0; tried = 0
    for _ in range(150):
        marks = rnd.sample(sites, rnd.randint(3, 7))
        eta = fam.run_automaton(sites, {m: 1 for m in marks})
        ones, npred, kind = fam.kinds(eta)
        for z in [w for w in ones if kind[w] == "proc"][:2]:
            vb = v_of(eta, z); vm, _ = rt.rooted(restricted(eta, z), z, 1.0)
            tried += 1; agree += (vm is not None and abs(float(vb) - vm) < 1e-6)
    out("N cross-check: exact brute-force rooted value against rooted.py's integer program on %d processed sites of random depth-3 configurations "
        "(3-7 marks): %d agree" % (tried, agree))
except Exception as ex:
    out("N cross-check against rooted.py skipped: %s" % ex)

t0 = time.time()
for depth, kmax in ((3, 6), (4, 5)):
    st = exhaust(depth, kmax)
    vd = ", ".join("%s: %d" % (k, v) for k, v in sorted(st["vdist"].items()))
    out("X depth %d cone (%d sites), every configuration with at most %d marks: %d configurations (%d symmetry orbits); %d processed 1-sites "
        "(with multiplicity); v over processed sites: {%s}; sites all of whose 1-predecessors are processed and tight: %d, largest v among them %s; "
        "allowing tight seeds among the 1-predecessors: %d, largest v %s (%.0f s)"
        % (depth, len(fam.cone(ROOT, depth)), kmax, st["configs"], st["orbits"], st["processed"], vd, st["all_proc_tight"], st["maxv"],
           st["all_tight_incl_seeds"], st["maxv_incl"], time.time() - t0))
    tightp = sum(n for vv, n in st["vdist"].items() if vv == 0)
    out("X depth %d: processed sites with v = 0 (tight): %d; largest v over all processed sites %s: the lemma's hypothesis (every 1-predecessor "
        "processed and tight) %s on this cone" % (depth, tightp, max(st["vdist"]), "never occurs" if st["all_proc_tight"] == 0 else "occurs %d times" % st["all_proc_tight"]))
    for c, z, vz in st["pos"][:5]:
        out("HIT: depth %d, marks %s: processed site %s has all 1-predecessors processed and tight but v = %s" % (depth, list(c), z, vz))
    if depth == 3: st3 = st
    else: st4 = st
out("")
out("SUMMARY: tight-sibling lemma, exhaustive: depth 3 with <= 6 marks (%d configurations) and depth 4 with <= 5 marks (%d): %d and %d processed "
    "sites have all 1-predecessors processed and tight (no processed site is tight at all on these cones: v <= -1), largest v among them %s and %s; "
    "with tight seeds allowed as predecessors: largest v %s and %s; no counterexample" % (st3["configs"], st4["configs"], st3["all_proc_tight"], st4["all_proc_tight"], st3["maxv"], st4["maxv"],
                                           st3["maxv_incl"], st4["maxv_incl"]))
