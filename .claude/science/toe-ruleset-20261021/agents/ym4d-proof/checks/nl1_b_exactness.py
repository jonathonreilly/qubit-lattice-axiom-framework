#!/usr/bin/env python3
"""check nl1-b - the two divisibility facts used in Lemma NL-11's proof. Criteria: checks/nl1_b_criteria.md.
Reuses the polynomial helpers of checks/nl1_division.py by import; that file is unaltered."""
import importlib.util, random, sys, os
spec = importlib.util.spec_from_file_location("nl1", os.path.join(os.path.dirname(os.path.abspath(__file__)), "nl1_division.py"))
# nl1_division.py runs its own check at import; suppress its stdout so nl2's output is clean.
import io, contextlib
nl1 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(nl1)
padd, pscale, pmul_nu, E, T, D = nl1.padd, nl1.pscale, nl1.pmul_nu, nl1.E, nl1.T, nl1.D

def rnd_poly(rng):
    p = {}
    for _ in range(4):
        k = tuple(rng.randint(0, 2) for _ in range(D)); c = rng.randint(-4, 4)
        if c: p[k] = p.get(k, 0) + c
    return {k: v for k, v in p.items() if v}

rng = random.Random(1028202624)
bad_A = bad_B = 0; nonzero_C = 0
for _ in range(200):
    g = rnd_poly(rng)
    for a in range(D):
        q, r = T(padd(g, pscale(E(g, a), -1)), a)
        if r: bad_A += 1
        _, r2 = T(g, a)
        if r2: nonzero_C += 1
    for a in range(D):
        Ta_nu_a = T(pmul_nu(g, a), a)[0]
        if padd(Ta_nu_a, pscale(g, -1)): bad_B += 1
        for b in range(D):
            if b == a: continue
            lhs = T(pmul_nu(g, b), a)[0]
            rhs = pmul_nu(T(g, a)[0], b)
            if padd(lhs, pscale(rhs, -1)): bad_B += 1
print("nl1b-A: nonzero remainders dividing (g - E_a g) by (z_a-1):", bad_A, "/ 800  -> ", "PASS" if bad_A == 0 else "FAIL")
print("nl1b-B: failures of T_a(nu_a g)=g and T_a(nu_b g)=nu_b T_a g:", bad_B, "/", 200*(D + D*(D-1)), " -> ", "PASS" if bad_B == 0 else "FAIL")
print("nl1b-C: nonzero remainders dividing g itself (control):", nonzero_C, "/ 800  -> ", "PASS" if nonzero_C >= 150 else "FAIL (nl1b-A vacuous)")
