"""(a)+(b): classification of translation-invariant phased permutations covariant under the dressed O action."""
import sys, itertools, time
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from mymodel import *
P = F = 0
def check(n, ok, d=""):
    global P, F; P += bool(ok); F += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {n}  {d}", flush=True)
t0 = time.time()
check("flux constraints determine the translation-invariant gauge class: rank 22 = 36 - 14 (15 (lam,tau) gauge params - global sign)",
      LOOP_RANK == 22)
check("own model: H_on, H_link, Lambda, S commute with all 24 dressed rotations; PSG lift unique up to global sign (kernel dim 1 for all 48)",
      all(bl_eq(conjG(g, X), X) for g in PROPER for X in (HON, HLINK, LAMX, S1)) and all(g['kdim'] == 1 for g in PSG))
idx = {tuple(g['M'].ravel()): n for n, g in enumerate(PROPER)}
# 1. composition: G_g G_h = +- G_gh exactly (lam_gh = lam_h + R_h^T lam_g, tau_gh(c) = tau_h(c) + tau_g(R_h c) + const)
okc = True; okrep = True
rng = np.random.default_rng(0)
X = {a: rng.normal(size=(12, 12)) + 1j * rng.normal(size=(12, 12)) for a in itertools.product((-1, 0, 1), repeat=3)}
for g in PROPER:
    for h in PROPER:
        gh = PROPER[idx[tuple((g['M'] @ h['M']).ravel())]]
        lam = (h['lam'] + h['M'].T @ g['lam']) % 2
        tau = np.array([(h['tau'][c] + g['tau'][CI[rc(h['M'], CORN[c])]]) % 2 for c in range(12)])
        dt = (tau - gh['tau']) % 2
        okc &= np.array_equal(lam, gh['lam'] % 2) and len(set(dt)) == 1
        okrep &= bl_eq(conjG(g, conjG(h, X)), conjG(gh, X))
check("dressed lifts compose exactly up to a GLOBAL sign: G_g G_h = +-G_gh (no staggered (-1)^{mu.v} defect)", okc)
check("hence Ad(G_g) is a genuine linear representation of O on translation-invariant operators (checked on random range-1 X)", okrep)
# characters of O: abelianisation Z2 -> only A1, A2
chis = {'A1': lambda g: 1, 'A2': lambda g: g['chi']}
okhom = all(PROPER[idx[tuple((g['M'] @ h['M']).ravel())]]['chi'] == g['chi'] * h['chi'] for g in PROPER for h in PROPER)
check("A2 (axis-permutation sign) is a homomorphism of O; with Ad(G) a true rep, chi in G X G^-1 = chi X must be A1 or A2", okhom)

# 2. stabiliser of corner c@0 in O, and C2' fixed targets
for c0 in range(12):
    st = [g for g in PROPER if rc(g['M'], CORN[c0]) == CORN[c0]]
    if c0 == 0: print(f"  stabiliser of {sorted(CORN[c0])}: {[g['M'].tolist() for g in st]}")
stab_ok = all(len([g for g in PROPER if rc(g['M'], CORN[c]) == CORN[c]]) == 2 for c in range(12))
check("stabiliser of every corner@0 in O is order 2 = {1, C2' about f_c} (dressing only adds signs; translations act freely)", stab_ok)
# stabiliser in O_h for the record
print("  O_h stabiliser order of a corner:", len([g for g in PSG if rc(g['M'], CORN[0]) == CORN[0]]))

# 3. exhaustive enumeration over (target corner, displacement) for source c_xy, range <= R, both characters
def enumerate_letters(R):
    found = []; nocand = 0
    for a in itertools.product(range(-R, R + 1), repeat=3):
        for i in range(12):
            nocand += 1
            # target_of: equivariant extension of (c_xy -> i @ a): for c = R_g c_xy, target = R_g i @ R_g a (if well defined)
            tmap = {}; bad = False
            for g in PROPER:
                c = CI[rc(g['M'], CORN[c_xy])]; t = (CI[rc(g['M'], CORN[i])], rd(g['M'], a))
                if c in tmap and tmap[c] != t: bad = True; break
                tmap[c] = t
            if bad: continue                         # not fixed by C2' -> no phased permutation (two entries per column)
            for nm, ch in chis.items():
                Xl = orbit_solve(lambda c: tmap[c], ch, c0=c_xy)
                if Xl is not None: found.append((a, i, nm, Xl))
    return found, nocand
for R in (1, 2, 3, 4):
    found, nc = enumerate_letters(R)
    kinds = sorted(((round(np.dot(a, FACE[c_xy]) / 2), 'same' if i == c_xy else ('anti' if i == ANTI[c_xy] else str(i)), nm) for a, i, nm, _ in found))
    expect = sorted([(t, 'same', 'A1') for t in range(-R, R + 1)] + [(t, 'anti', 'A2') for t in range(-R, R + 1)])
    ok = kinds == expect
    # identify: same -> z S^t ; anti -> z A0 S^t
    okid = True
    for a, i, nm, Xl in found:
        t = int(round(np.dot(a, FACE[c_xy]) / 2)); ref = Spow(t) if i == c_xy else mul({Z0: A0m}, Spow(t))
        k = rng.uniform(-np.pi, np.pi, 3); M1, M2 = bloch(Xl, k), bloch(ref, k)
        z = np.vdot(M2.ravel(), M1.ravel()) / 12
        okid &= abs(abs(z) - 1) < 1e-12 and np.allclose(M1, z * M2)
        okid &= all(np.allclose(np.abs(B[np.abs(B) > 1e-9]), 1) for B in Xl.values())
        okid &= all(bl_eq(conjG(g, Xl), Xl, chis[nm](g)) for g in PROPER)
    check(f"range <= {R}: {nc} (displacement, target) candidates x {{A1,A2}} -> exactly {len(found)} letters = S^t (A1) and A0 S^t (A2), |t| <= {R}",
          ok and okid, f"{kinds if not ok else ''}")
# 4. the stabiliser sign rule: rho(h) = (-1)^{lam_h.a + tau_h(i) + tau_h(c)} for C2' h, for every corner (not just c_xy)
okrule = True
for c in range(12):
    h = [g for g in PROPER if rc(g['M'], CORN[c]) == CORN[c] and not np.array_equal(g['M'], np.eye(3))][0]
    lf = int(np.dot(h['lam'], FACE[c])) % 2; tsum = (h['tau'][c] + h['tau'][ANTI[c]]) % 2
    okrule &= (lf == 0) and (tsum == 1) and h['chi'] == -1
check("for every corner: lam_{C2'}.f_c even (so S^t is A1 for ALL t) and tau_{C2'}(c)+tau_{C2'}(-c) odd with A2(C2') = -1 (so A0 S^t is A2 for all t)",
      okrule)
# 5. other characters / non-1-d: on each C2'-fixed 12-dim support space, decompose Ad(G) and confirm only one 1-d component
okdec = True
for t in (-1, 0, 1, 2):
    for tgt in ('same', 'anti'):
        # basis E_c: entry (target(c) <- c) with displacement t f_c
        def T(c): return (c if tgt == 'same' else ANTI[c], tuple(int(x) for x in t * FACE[c]))
        Ms = []
        for g in PROPER:
            Mg = np.zeros((12, 12))
            for c in range(12):
                i, a = T(c); Rc = CI[rc(g['M'], CORN[c])]
                Mg[Rc, c] = (-1.0) ** (int(np.dot(g['lam'], a)) + g['tau'][c] + g['tau'][i])
            Ms.append(Mg)
        rA1 = np.linalg.matrix_rank(sum(Ms) / 24); rA2 = np.linalg.matrix_rank(sum(g['chi'] * M for g, M in zip(PROPER, Ms)) / 24)
        okdec &= (rA1, rA2) == ((1, 0) if tgt == 'same' else (0, 1))
check("support spaces (12-dim, induced from the C2' sign): A1/A2 multiplicities are (1,0) for c->c and (0,1) for c->-c (Frobenius)", okdec)
check("A0 under improper elements: G A0 G^-1 = A2(perm part) A0 (B26 'A2 x inv'); A0 is not O_h-symmetric",
      all(bl_eq(conjG(g, A0), A0, chiA2(g['M'])) for g in PSG if g['chi'] is None))
print(f"\nTOTAL: PASS={P} FAIL={F}   [{time.time() - t0:.1f}s]")
