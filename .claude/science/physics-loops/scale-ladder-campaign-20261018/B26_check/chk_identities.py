"""(c)+(d): conjugation identities, even-A reduction on random words, D+/D- swap, L1 with effective n_S."""
import sys, itertools, time
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from mymodel import *
P = F = 0
def check(n, ok, d=""):
    global P, F; P += bool(ok); F += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {n}  {d}", flush=True)
t0 = time.time(); rng = np.random.default_rng(11)
KS = rng.uniform(-np.pi, np.pi, (10, 3))
A0i = A0m.conj().T
def eqk(f, g, ks=KS): return max(np.abs(f(k) - g(k)).max() for k in ks)
RLk = lambda k: bloch(RL, k); RTk = lambda k: bloch(RTX, k)
Si = lambda k: Sk(k, -1); S = lambda k: Sk(k, 1)
kst = np.array([1, -1, 1]) * np.pi / 2

check("A0 is a real signed permutation c -> -c with A0^2 = -1 (in its real normalisation; (iA0)^2 = +1)",
      np.allclose(A0m.imag, 0) and all(abs(A0m[ANTI[c], c]) == 1 for c in range(12)) and np.allclose(A0m @ A0m, -np.eye(12)))
check("A0 S A0^-1 = S^-1 (and A0 S^2 A0^-1 = S^-2)", eqk(lambda k: A0m @ S(k) @ A0i, Si) < 1e-13 and eqk(lambda k: A0m @ Sk(k, 2) @ A0i, lambda k: Sk(k, -2)) < 1e-13)
d1 = eqk(lambda k: A0m @ RLk(k) @ A0i, lambda k: -S(k) @ RLk(k) @ Si(k))
d2 = eqk(lambda k: A0m @ RLk(k) @ A0i, lambda k: -Si(k) @ RLk(k) @ S(k))
d3 = eqk(lambda k: A0m @ RLk(k) @ A0i, lambda k: S(k) @ RLk(k) @ Si(k))
check("A0 R_L A0^-1 = -S R_L S^-1  (and NOT -S^-1 R_L S, NOT +S R_L S^-1)", d1 < 1e-13 and d2 > 0.1 and d3 > 0.1, f"res {d1:.1e}, alt {d2:.2f}, {d3:.2f}")
# Rt identities (not listed in FINDINGS)
dA = eqk(lambda k: A0m @ RTk(k) @ A0i, RLk)
dB = eqk(lambda k: Si(k) @ RTk(k) @ S(k), lambda k: -RLk(k))
dC = eqk(lambda k: RTk(k) @ RTk(k), lambda k: np.eye(12))
dD = eqk(RTk, lambda k: RTk(k).conj().T)
dE = min(eqk(RTk, RLk), eqk(RTk, lambda k: -RLk(k)))
dF = eqk(RTk, lambda k: -S(k) @ S(k) @ RLk(k) @ Si(k) @ Si(k))
dG = eqk(lambda k: S(k) @ RTk(k) @ Si(k), lambda k: -Sk(k, 2) @ RLk(k) @ Sk(k, -2))
check("Rt identities: A0 Rt A0^-1 = +R_L ; S^-1 Rt S = -R_L ; Rt^2 = 1 ; Rt Hermitian ; Rt != +-R_L ; Rt != -S^2 R_L S^-2",
      dA < 1e-13 and dB < 1e-13 and dC < 1e-13 and dD < 1e-13 and dE > 0.1 and dF > 0.1, f"{dA:.0e} {dB:.0e} {dC:.0e} {dD:.0e} {dE:.2f} {dF:.2f}")
# Rt as a hopping operator: corner {a,b} hops along -a/-b (reversed link), i.e. R_L with displacement reversed
okhop = all(np.allclose(np.abs(RTX.get(neg(a), 0)), np.abs(RL.get(a, 0))) for a in RL)
check("Rt hop pattern = R_L with every link displacement reversed (|Rt_{-a}| = |RL_a|), so Rt(k) is not R_L(k)", okhop)
check("A0 H_on A0^-1 = H_on ; A0 Lambda A0^-1 = -Lambda",
      np.allclose(A0m @ HON0 @ A0i, HON0) and np.allclose(A0m @ LAM @ A0i, -LAM))
# palettes: A0 (palette) A0^-1 = phase * palette element
def find_in(M, pal):
    for n, B in pal.items():
        z = np.vdot(B.ravel(), M.ravel()) / 12
        if abs(abs(z) - 1) < 1e-10 and np.allclose(M, z * B): return n, z
    return None, None
okpal = True; lmap = {}
for n, B in PC.items():
    m, z = find_in(A0m @ B @ A0i, PC); okpal &= m is not None; lmap[n] = (m, np.round(z, 6))
check("A0 maps the 80-element Clifford palette PC onto itself up to a global phase (H_ab fixed; L_abc -> phase * L reversed)",
      okpal, f"e.g. L130 -> {lmap['L130']}, L332 -> {lmap['L332']}, H20 -> {lmap['H20']}")
pi6 = {("H",a,b): PH[0] + np.exp(1j*np.pi*a/6) * PH[1] + np.exp(1j*np.pi*b/6) * PH[2] for a in range(12) for b in range(12)}
pi6.update({("L",a,b,c): PL[0] + np.exp(1j*np.pi*a/6) * PL[1] + np.exp(1j*np.pi*b/6) * PL[2] + np.exp(1j*np.pi*c/6) * PL[3]
            for a in range(12) for b in range(12) for c in range(12)})
okp6 = all(find_in(A0m @ pi6[n] @ A0i, pi6)[0] is not None for n in pi6)
check("A0 maps the pi/6 palette onto itself up to phase (all 144 H + 1728 L elements; keys as tuples)", okp6)
okalg = True
for B in ONB:
    Bt = A0m @ B @ A0i
    okalg &= all(np.allclose(g['U'] @ Bt @ g['U'].T, Bt) for g in PROPER)
check("A0 conjugation maps the 6-dim symmetric on-site algebra into itself; A0 itself is not in it",
      okalg and not all(np.allclose(g['U'] @ A0m @ g['U'].T, A0m) for g in PROPER))

# ---------------- even-A reduction on random words
def letter(tok, k):
    if tok[0] == 'S': return Sk(k, tok[1])
    if tok[0] == 'R': return RLk(k)
    if tok[0] == 'Rt': return RTk(k)
    if tok[0] == 'A': return A0m @ Sk(k, tok[1])
    return tok[1]                                   # ('U', matrix) on-site
def word(w, k):
    M = np.eye(12, dtype=complex)
    for t in w: M = M @ letter(t, k)
    return M
def reduce_word(w):
    """even-A word -> (sign, old-palette word in S^p, R_L, on-site) using A0 X A0 = -X~ and Rt = -S R_L S^-1."""
    out = []; par = 0; sign = 1
    for t in w:
        if t[0] == 'A':
            if par == 1: sign *= -1                  # closing A0 of a pair: A0 w A0 = A0 w A0^-1 A0^2 = -(w~)
            par ^= 1; t = ('S', t[1])
        if par:                                      # dual letter
            if t[0] == 'S': out.append(('S', -t[1]))
            elif t[0] == 'R': sign *= -1; out += [('S', 1), ('R',), ('S', -1)]   # R~ = Rt = -S R S^-1
            elif t[0] == 'Rt': out.append(('R',))                                # Rt~ = R_L
            else: out.append(('U', A0m @ t[1] @ A0i))
        else:
            if t[0] == 'Rt': sign *= -1; out += [('S', 1), ('R',), ('S', -1)]
            else: out.append(t)
    assert par == 0
    return sign, out
def neff(w):
    n = 0; par = 0
    for t in w:
        if t[0] == 'A': par ^= 1; n += (-1) ** par * t[1]
        elif t[0] == 'S': n += (-1) ** par * t[1]
    return n
def rand_word(rng, nA):
    L = rng.integers(3, 9); toks = []
    for _ in range(L):
        r = rng.integers(0, 4)
        if r == 0: toks.append(('S', int(rng.choice([-2, -1, 1, 2]))))
        elif r == 1: toks.append(('R',) if rng.random() < .5 else ('Rt',))
        else: toks.append(('U', rand_onsite_unitary(rng) if rng.random() < .5 else PC[list(PC)[rng.integers(80)]]))
    for _ in range(nA): toks.insert(int(rng.integers(0, len(toks) + 1)), ('A', int(rng.integers(-2, 3))))
    return toks
okred = True; maxd = 0
for trial in range(300):
    w = rand_word(rng, 2 * int(rng.integers(1, 3)))
    s, wo = reduce_word(w)
    for k in rng.uniform(-np.pi, np.pi, (3, 3)):
        d = np.abs(word(w, k) - s * word(wo, k)).max(); maxd = max(maxd, d)
    okred &= all(t[0] in ('S', 'R', 'U') for t in wo)
check("300 random even-A words (2 or 4 A_a letters, S^p, R_L, Rt, random symmetric on-site / PC letters) equal +-(old-palette word)",
      okred and maxd < 1e-12, f"max dev {maxd:.1e}")
# literal formula A_a X A_b Y = - S^-a X~ S^b Y with X = R_L U S (one example family)
okf = True
for a, b in itertools.product(range(-2, 3), repeat=2):
    U = rand_onsite_unitary(rng); Ut = A0m @ U @ A0i
    for k in KS[:3]:
        lhs = A0m @ Sk(k, a) @ RLk(k) @ U @ S(k) @ A0m @ Sk(k, b)
        rhs = -Sk(k, -a) @ RTk(k) @ Ut @ Si(k) @ Sk(k, b)
        okf &= np.allclose(lhs, rhs)
check("formula A_a X A_b = -S^-a X~ S^b (X = R_L U S, all a,b in -2..2)", okf)
# n_S conservation: det-free check -- the reduced word has total S power = n_eff
okn = True
for trial in range(100):
    w = rand_word(rng, 2); s, wo = reduce_word(w)
    okn &= sum(t[1] for t in wo if t[0] == 'S') == neff(w)
check("reduced word's total S power equals n_eff = sum (-1)^{#A0 to the left} p (100 words)", okn)

# ---------------- (d) D+/D- swap and L1 with n_eff
okswap = True
for a in range(-2, 3):
    for k0 in (kst, -kst):
        A = A0m @ Sk(k0, a)
        okswap &= np.linalg.norm(DP.conj().T @ A @ DP) < 1e-12 and np.linalg.norm(DM.conj().T @ A @ DM) < 1e-12
        okswap &= abs(np.linalg.norm(DM.conj().T @ A @ DP) ** 2 - 2) < 1e-12 and abs(np.linalg.norm(DP.conj().T @ A @ DM) ** 2 - 2) < 1e-12
check("A_a (a=-2..2) maps D+ onto D- and D- onto D+ at +k* and -k* (P_D+ A P_D+ = 0, ||P_D- A P_D+||^2 = 2)", okswap)
# S, R_L, Rt on D+/D- at +-k*: scalars and compressed derivative norms
for nm, X in (('S', S1), ('R_L', RL), ('Rt', RTX)):
    for k0, kn in ((kst, '+k*'), (-kst, '-k*')):
        for D, dn in ((DP, 'D+'), (DM, 'D-')):
            M = bloch(X, k0); c = D.conj().T @ M @ D; G = bloch_grad(X, k0)
            print(f"   {nm:3s} {kn} {dn}: value {np.round(np.linalg.eigvals(c), 6)}  leak {np.linalg.norm(M @ D - D @ c):.0e}  ||P d_j X P|| = {[round(np.linalg.norm(D.conj().T @ g @ D, 2), 6) for g in G]}")
# on-site algebra on D+-: scalar?
oks = all(np.allclose(DP.conj().T @ B @ DP, (np.trace(DP.conj().T @ B @ DP) / 2) * np.eye(2)) and np.linalg.norm(B @ DP - DP @ (DP.conj().T @ B @ DP)) < 1e-10 for B in ONB)
check("every symmetric on-site operator acts on D+ (and D-) as a scalar (D+-: multiplicity-1 irreps)", oks and
      all(np.allclose(DM.conj().T @ B @ DM, (np.trace(DM.conj().T @ B @ DM) / 2) * np.eye(2)) for B in ONB))
def dpt_speed(w, k0, Q, E):
    h = 1e-6; G = []
    for j in range(3):
        dk = np.zeros(3); dk[j] = h; G.append((word(w, k0 + dk) - word(w, k0 - dk)) / (2 * h))
    hj = [-1j * np.exp(-1j * E) * Q.conj().T @ g @ Q for g in G]; hj = [(x + x.conj().T) / 2 for x in hj]
    dirs = rng.normal(size=(30, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
    sp = np.array([np.linalg.eigvalsh(sum(d[j] * hj[j] for j in range(3))) for d in dirs])
    tilt = max(abs(np.trace(x).real) / len(Q[0]) for x in hj)
    return np.abs(sp).min(), np.abs(sp).max(), tilt
nd = 0; maxdev = 0; okL1 = True; nzero = 0; sign_matters = 0
for trial in range(400):
    w = rand_word(rng, 2 * int(rng.integers(0, 3)))
    W0 = word(w, kst); ne = neff(w); nraw = sum(t[1] for t in w if t[0] in ('S', 'A'))
    for D in (DP, DM):
        c = D.conj().T @ W0 @ D
        if np.linalg.norm(W0 @ D - D @ c) > 1e-9 or not np.allclose(c, c[0, 0] * np.eye(2)): okL1 = False; continue
        E = np.angle(c[0, 0]); ev = np.angle(np.linalg.eigvals(W0))
        if np.sum(np.abs(wrap(ev - E)) < 1e-7) != 2: continue          # accidental extra degeneracy: skip
        smin, smax, tilt = dpt_speed(w, kst, D, E); v = abs(ne) * np.sqrt(2) / 3
        nd += 1; maxdev = max(maxdev, abs(smin - v), abs(smax - v), tilt)
        if ne == 0: nzero += 1
        if abs(ne) != abs(nraw): sign_matters += 1
check("L1 with n_eff: on 400 random words with 0/2/4 A-letters, D+ and D- are invariant with scalar W(k*) (exact 2-fold unless accidental); "
      "every exact 2-fold D+- level is an untilted isotropic cone at |n_eff| sqrt2/3",
      okL1 and maxdev < 1e-6, f"{nd} doublets, max dev {maxdev:.1e} (finite diff h=1e-6), {sign_matters} with |n_eff| != |n_raw|, {nzero} with n_eff=0")
print(f"\nTOTAL: PASS={P} FAIL={F}   [{time.time() - t0:.1f}s]")
