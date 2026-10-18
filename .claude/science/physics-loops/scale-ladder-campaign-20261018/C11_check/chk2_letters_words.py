"""C11 check, parts (b)-(d): step-3 sign, letter values, additivity on random words (analytic derivatives,
labels tracked by subspace overlap, speeds by direct diagonalisation, signs by Berry flux)."""
import time
from c11lib import *

NP = NF = 0
def rep(ok, msg):
    global NP, NF
    NP += bool(ok); NF += (not ok); print(("[PASS] " if ok else "[FAIL] ") + msg, flush=True)
rng = np.random.default_rng(424242)
r23 = np.sqrt(2) / 3

# ---------------------------------------------------------------- (b) step 3: V^dag tau^(b) V = +tau^(a) for unitary intertwiners
print("== (b) step-3 sign: conjugating the frame by intertwiners")
worst = 0; nneg = 0; cases = 0
for t in range(60):
    # random intertwiners: random even/odd products of covariant constant letters and letters evaluated at k*
    w = []
    for _ in range(int(rng.integers(1, 5))):
        r = rng.random()
        w.append(L_AS(int(rng.integers(-2, 3))) if r < 0.4 else L_onsite(rng) if r < 0.7 else L_gen(rng)[0])
    for k0 in KP.values():
        V = word_eval(w, k0)
        for a in (+1, -1):
            B = V @ DOUB[a]; b = label_of(B)
            assert b is not None
            X = DOUB[b].conj().T @ B          # 2x2 unitary D_a -> D_b
            C = [X.conj().T @ TAU[b][i] @ X for i in range(3)]
            c = sum(np.trace(TAU[a][i] @ C[i]) for i in range(3)) / 6
            worst = max(worst, max(np.abs(C[i] - TAU[a][i]).max() for i in range(3))); nneg += c.real < 0; cases += 1
rep(worst < 1e-9 and nneg == 0, f"V^dag tau^(b) V = +tau^(a) exactly on {cases} intertwiners (A1 and A2, both k*); never -tau (worst {worst:.1e})")
print("   reason: V^dag tau V is again a Hermitian T1 triple on D_a, hence c tau^(a) with c real, c^2 = 1; conjugation preserves "
      "tau_x tau_y = i tau_z, which -tau violates, so c = +1. The eps relation is what fixes the sign.")

# ---------------------------------------------------------------- (c) letter values
print("== (c) letter values (analytic derivatives)")
named = [L_S(1), L_S(2), L_S(-1), L_S(-2), L_RL, L_RT,
         L_expX("E+", RLX, np.pi / 4), L_expX("E-", RLX, -np.pi / 4)]
named += [L_expX(f"exp(i{m}pi/6 R_L)", RLX, m * np.pi / 6) for m in (1, 2, 3, 4, 5)] + [L_expX("exp(1.234i R_L)", RLX, 1.234)]
named += [L_expX("exp(i0.9 Rt)", RTX, 0.9)]
named += [L_onsite(rng) for _ in range(3)] + [L_AS(p) for p in (-2, -1, 0, 1, 2)]
gens = [L_gen(rng)[0] for _ in range(6)] + [L_gen(rng, a2=True)[0] for _ in range(2)]
named += gens
rep(all(covariant(L, rng) for L in named), f"all {len(named)} letters covariant with declared chi (24 rotations, 2 random k)")
# derivative sanity: analytic vs finite difference for generic letters
fdw = 0
for L in gens + [named[6]]:
    k = rng.uniform(-3, 3, 3); d = L.df(k)
    for i in range(3):
        e = np.zeros(3); e[i] = 1e-6; fd = (L.f(k + e) - L.f(k - e)) / 2e-6; fdw = max(fdw, np.abs(fd - d[i]).max())
rep(fdw < 1e-6, f"analytic (Daleckii-Krein) derivatives of exp(iH) letters agree with finite differences ({fdw:.1e})")
VT = {}; worst = 0; maps = True; imag = 0
print("   %-18s %10s %10s %10s %10s" % ("letter", "D+,+k*", "D-,+k*", "D+,-k*", "D-,-k*"))
for L in named:
    row = []
    for kn, k0 in KP.items():
        U = L.f(k0)
        for b in (+1, -1):
            lab = label_of(U @ DOUB[b]); maps &= lab == L.chi * b
            if L.chi == 1:
                X = DOUB[b].conj().T @ U @ DOUB[b]; maps &= np.allclose(X, X[0, 0] * np.eye(2), atol=1e-10)
            v, res = letter_v(L, k0, b); worst = max(worst, res); imag = max(imag, abs(v.imag)); row.append(v.real)
            VT[(L.name, id(L), kn, b)] = v.real
    L.vrow = row
    print("   %-18s" % L.name + "".join("%11.6f" % x for x in row))
rep(maps, "A1 letters are scalars on D+ and D-, A2 letters swap D+ <-> D- (label by subspace overlap)")
rep(worst < 1e-9 and imag < 1e-9, f"P U^dag dU P = i v tau^(b) with v real for every letter (fit residual {worst:.1e}, |Im v| {imag:.1e})")
vS = named[0].vrow
rep(np.allclose(vS, [-r23, r23, -r23, r23], atol=1e-10),
    "v_S = -+sqrt2/3 on D+-: |v_S| = sqrt2/3, opposite on D+ and D-, same at +-k*. (Overall sign opposite to C11's table "
    "because this build uses X(k)=sum X_a e^{-ik.a}; a global convention)")
rep(all(np.allclose(named[i].vrow, p * np.array(vS), atol=1e-10) for i, p in ((1, 2), (2, -1), (3, -2))), "v_{S^p} = p v_S")
zero = [L for L in named if L.name in ("R_L", "Rt", "E+", "E-", "onsite") or "R_L" in L.name or "Rt" in L.name]
rep(all(np.allclose(L.vrow, 0, atol=1e-10) for L in zero), f"v = 0 for R_L, Rt, E+-, exp(i theta R_L) (6 angles incl. 4pi/6, 1.234), exp(0.9i Rt), on-site ({len(zero)} letters)")
rep(all(np.allclose(L.vrow, p * np.array(vS), atol=1e-10) for L, p in zip([L for L in named if L.name.startswith('A0S^')], (-2, -1, 0, 1, 2))), "A0 S^a: v^(b) = a v_S^(b) (input label b)")
g = [L.vrow for L in gens]
nonanti = sum(abs(r[0] + r[1]) > 1e-3 for r in g); nonk = sum(abs(r[0] - r[2]) > 1e-3 for r in g)
rep(nonanti == len(g) and nonk == len(g) and max(abs(x) for r in g for x in r) > 1e-2,
    f"generic exp(iH) letters: v real and letter-dependent; v(D+)+v(D-) != 0 in {nonanti}/{len(g)}, v(+k*) != v(-k*) in {nonk}/{len(g)}")

# ---------------------------------------------------------------- (d) random words
print("== (d) random words")
def pool():
    r = rng.random()
    if r < 0.15: return L_S(int(rng.choice([1, 2, -1, -2])))
    if r < 0.24: return L_RL
    if r < 0.31: return L_RT
    if r < 0.40: return L_onsite(rng)
    if r < 0.47: return L_expX("E+", RLX, np.pi / 4) if rng.random() < .5 else L_expX("E-", RLX, -np.pi / 4)
    if r < 0.52: return L_expX("expRL", RLX, rng.uniform(-3, 3))
    if r < 0.74: return L_gen(rng)[0]
    if r < 0.90: return L_AS(int(rng.integers(-2, 3)))
    return L_gen(rng, a2=True)[0]
def rand_word(mingen):
    while True:
        w = [pool() for _ in range(int(rng.integers(2, 7)))]
        if sum(L.chi == -1 for L in w) % 2 == 0 and sum('exp(iH)' in L.name for L in w) >= mingen: return w
t0 = time.time()
nlev = 0; nskip = 0; wsp = 0; wtilt = 0; wterm = 0; wlab = 0; wsum = 0; berry = []; nfd = 0; wfd = 0
for t in range(200):
    w = rand_word(1 if t % 2 == 0 else 0)
    for kn, k0 in KP.items():
        W = word_eval(w, k0); ev = np.linalg.eigvals(W)
        for a in (+1, -1):
            X = DOUB[a].conj().T @ W @ DOUB[a]
            assert np.allclose(W @ DOUB[a], DOUB[a] @ X, atol=1e-10) and np.allclose(X, X[0, 0] * np.eye(2), atol=1e-10)
            w0 = X[0, 0]; gaps = np.sort(np.abs(ev - w0))
            if gaps[2] < 1e-3: nskip += 1; continue
            terms, lab_out = path_terms(w, k0, a)
            # labels: tracked label vs C11 formula b_j = a prod_{l>j} chi_l
            bb = a; labs_formula = []
            for L in reversed(w): labs_formula.append(bb); bb *= L.chi
            labs_formula = labs_formula[::-1]
            wlab += sum(tl[0] != lf for tl, lf in zip(terms, labs_formula)) + (lab_out != a)
            pred = 0.0
            for (lab, L, T, B), _ in zip(terms, labs_formula):
                v, _ = letter_v(L, k0, lab); pred += v.real
                wterm = max(wterm, max(np.abs(T[i] - 1j * v.real * TAU[a][i]).max() for i in range(3)))   # termwise step 3
            # whole-word M by summing tracked terms equals D^dag W^dag dW D (finite difference of whole word, no product rule)
            if nfd < 120:
                Md = []
                for i in range(3):
                    e = np.zeros(3); e[i] = 1e-6
                    dW = (word_eval(w, k0 + e) - word_eval(w, k0 - e)) / 2e-6; Md.append(DOUB[a].conj().T @ W.conj().T @ dW @ DOUB[a])
                wfd = max(wfd, max(np.abs(Md[i] - 1j * pred * TAU[a][i]).max() for i in range(3))); nfd += 1
            for _ in range(3):
                q = rng.normal(size=3); q /= np.linalg.norm(q)
                s, tl = direct_speed(w, k0, w0, q); s2, tl2 = direct_speed(w, k0, w0, -q); tl = (tl - tl2) / 2; wsp = max(wsp, abs(s - abs(pred))); wtilt = max(wtilt, abs(tl))
            if len(berry) < 60 and abs(pred) > 0.03 and gaps[2] > 2e-2:
                r = min(1e-3, 0.05 * gaps[2] / max(abs(pred), 1e-9))
                (ch,), gmin = sphere_chern(lambda k: word_eval(w, k), k0, w0, [(1,)], r, nth=14, nph=28)
                berry.append((a, kn, pred, ch, gmin))
            nlev += 1
print(f"   {nlev} isolated (gap>1e-3) D+- levels, {nskip} skipped as near-degenerate; {time.time()-t0:.0f}s")
rep(nlev > 300 and wlab == 0, f"tracked doublet labels (subspace overlap) agree with b_j = a prod_(l>j) chi_l on every letter of every level")
rep(wterm < 1e-9, f"termwise: B_j^dag U_j^dag dU_j B_j = i v_j^(b_j) tau^(a) for every letter of every level (worst {wterm:.1e}) - step 3 holds with +tau")
rep(wfd < 1e-6, f"whole-word finite-difference P W^dag dW P = i (sum v) tau^(a) on {nfd} levels (worst {wfd:.1e})")
rep(wsp < 1e-6 and wtilt < 1e-6, f"direct diagonalisation (3 random directions/level): half-splitting = |sum v| (worst {wsp:.1e}), tilt {wtilt:.1e}")
cs = [round(c) for (_, _, _, c, _) in berry]; kap = {int(np.sign(p)) * c for (_, _, p, c, _) in berry for c in [round(c)]}
okint = all(abs(c - round(c)) < 1e-6 and abs(round(c)) == 1 for (_, _, _, c, _) in berry)
print(f"   Berry: {len(berry)} levels (D+ {sum(b[0]==1 for b in berry)}, D- {sum(b[0]==-1 for b in berry)}); sign(sum v)*Chern(upper band) values: {kap}")
rep(len(berry) >= 40 and okint and len(kap) == 1,
    f"Berry flux (FHS, sphere about k0): Chern(upper band) = kappa sign(sum v) with ONE global kappa = {kap} for D+ and D- at +-k* "
    f"-> chirality = sign(sum v) in the tau frames is convention-consistent across doublets")
print(f"TOTAL PASS={NP} FAIL={NF}")
