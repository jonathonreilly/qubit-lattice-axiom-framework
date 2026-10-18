#!/usr/bin/env python3
"""B24_check part 3b: confirm an odd-level C2-pair-not-T class (claim 5 scoping).  Word S2.L101.S2.H13 (a recorded survivor),
own Lambda_0; list the fixing rotations of q = (0, pi/8, pi/4) mod Lambda_0, the spectrum at k* + q and along its class,
and the operator-level status of the tastes (does a unitary V with V W(k) V^-1 = W(k+t) exist? tested via commutant rank)."""
import sys, os, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util
spec = importlib.util.spec_from_file_location('c3', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chk3_witnesses.py'))
src = open(spec.origin).read().split("def load(f)")[0]          # reuse only the definitions (builder, Lambda_0, typing)
exec(compile(src, 'chk3_defs', 'exec'))
w = word(('S2', 'p', 'S2', 'o'), ('L101', 'H13'))
L0 = lambda0(w); print("Lambda_0:", lname(L0), len(L0))
names = {i: ('C2' if tr[i] == -1 else {3: 'E', 0: 'C3', 1: 'C4'}[tr[i]]) + str(ROT[i].tolist()) for i in range(24)}
for rep in [(0, 2, 4), (0, 4, 2), (2, 0, 4), (0, 0, 4), (0, 4, 4)]:
    q = np.array(rep); k = KST + np.pi / 16 * q
    t_, fix = ptype(L0, k)
    print(f"q={rep} (pi/16): type {t_}; fixers: {[names[i] for i in fix]}; level mults {mults(ph(w, k))}")
    # spectrum invariance along class: k + t for a few t in L0
    ts = sorted(L0)[1:6]
    print("   same spectrum along class:", all(same_spec(ph(w, k), ph(w, k + np.pi / 4 * np.array(t))) for t in ts))
# operator-level tastes: for t in L0 test existence of V with W(k+t) V = V W(k) at two k simultaneously (null space of linear map)
def op_taste(t, ks=KT[:2]):
    rows = []
    for k in ks:
        A = W(w, k + np.pi / 4 * np.array(t)); B = W(w, k)
        rows.append(np.kron(A, np.eye(12)) - np.kron(np.eye(12), B.T))
    M = np.vstack(rows); s = np.linalg.svd(M, compute_uv=False); return int(np.sum(s < 1e-8))
gens = [(2, 0, 0), (0, 2, 0), (0, 0, 2), (1, 1, 1)]
print("operator-level intertwiner dimension for Lambda_0 generators (k-independent V would need >0 here):", {g: op_taste(g) for g in gens})
# omega-twisted intertwiners  W(k+t) V = omega V W(k), and antiunitary-type  W(k+t) V = V W(k)^T, W(-k...) not tried
def op_taste_om(t, om, transpose=False, ks=KT[:2]):
    rows = []
    for k in ks:
        A = W(w, k + np.pi / 4 * np.array(t)); B = W(w, k); B = B.T if transpose else B
        rows.append(np.kron(A, np.eye(12)) - om * np.kron(np.eye(12), B.T))
    s = np.linalg.svd(np.vstack(rows), compute_uv=False); return int(np.sum(s < 1e-8))
for om in (1, -1, 1j, -1j):
    print(f"t=(1,1,1)pi/4: intertwiner dim omega={om}: {op_taste_om((1,1,1), om)};  with W(k)^T: {op_taste_om((1,1,1), om, True)}")
# is the spectrum at generic k invariant under E -> E + pi (global)?
print("spectrum E -> E+pi invariant at random k:", [same_spec(ph(w, k), ph(w, k) + np.pi) for k in KT])
print("spectrum E -> -E invariant at random k:", [same_spec(ph(w, k), -ph(w, k)) for k in KT])
