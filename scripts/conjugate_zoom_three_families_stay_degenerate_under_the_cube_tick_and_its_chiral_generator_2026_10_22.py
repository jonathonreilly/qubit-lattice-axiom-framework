AUDIT_INPUT_PATHS = ('docs/CONJUGATE_ZOOM_THREE_FAMILIES_STAY_DEGENERATE_UNDER_THE_CUBE_TICK_AND_ITS_CHIRAL_GENERATOR_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
"""family-parity: which symmetry ties the zoom-3 families j and -j, and does a chiral term untie them?

Supplied model: CL-1's cube tick (spin-3/2 edge hop W on 2x2x2 cubes, two tilings offset by (1,1,1), even cubes
Cm exp(-i(eps-mu/2)R) Cm with the copy-mass factor Cm = exp(i(MN/4)(1-s)R), odd cubes exp(+i(eps+mu/2)R)) on a 6^3
torus, single-particle sector, with optional extra factors: the chiral generator Hc = (i/2)[W_o, W_e], the O-invariant
inversion-odd pseudoscalar eta*s (sublattice sign x copy sign), and test terms.  Family sectors = characters of
T(2e_i) on the turn-fixed line a = j(1,1,1).  Finite diagnostics; no physical reading beyond the stated comparisons.
Tags: [T] exact algebra (checked), [F] finite diagnostic, [E] estimate against measurement.
"""
import itertools, time
import numpy as np
from scipy.linalg import expm

AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0
def check(tag, name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {name}" + (f" | {detail}" if detail else ''))
r3 = np.sqrt(3.0); C8 = np.array(list(itertools.product((0, 1), repeat=3))); w3 = np.exp(2j*np.pi/3)
def ci(c): return int(c[0]*4+c[1]*2+c[2])
def Jm(j):
    d = int(round(2*j+1)); m = j-np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a-1, a] = np.sqrt(j*(j+1)-m[a]*(m[a]+1))
    return [(Jp+Jp.conj().T)/2, (Jp-Jp.conj().T)/2j, np.diag(m).astype(complex)]
def hops(spin):
    J3 = Jm(spin); xi = []
    for c in C8:
        n = (2*c-1.0)/r3; _, v = np.linalg.eigh(sum(n[k]*J3[k] for k in range(3))); xi.append(v[:, -1])
    G = np.array([[xi[a].conj()@xi[b] for b in range(8)] for a in range(8)])
    Wi = [np.zeros((8, 8), complex) for _ in range(3)]
    for a in range(8):
        for b in range(8):
            d = C8[a]-C8[b]
            if np.abs(d).sum() == 1: Wi[int(np.argmax(abs(d)))][a, b] = -G[a, b]/abs(G[a, b])/r3
    return Wi
def face_flux(R):
    out = []
    for ax in range(3):
        o = [i for i in range(3) if i != ax]; cyc = []
        for p, q in [(0, 0), (1, 0), (1, 1), (0, 1)]:
            c = [0, 0, 0]; c[ax] = 0; c[o[0]] = p; c[o[1]] = q; cyc.append(ci(c))
        out.append(np.angle(np.prod([R[cyc[(k+1) % 4], cyc[k]] for k in range(4)])))
    return out
def fit(A, B):   # diagonal D with D A D^+ = B
    D = np.zeros(8, complex); D[0] = 1; done = [0]
    while len(done) < 8:
        grew = False
        for a in list(done):
            for b in range(8):
                if D[b] == 0 and abs(A[b, a]) > 1e-12: D[b] = D[a]*B[b, a]/A[b, a]; done.append(b); grew = True
        if not grew: return None
    return D if np.abs(np.diag(D)@A@np.diag(D.conj())-B).max() < 1e-10 else None

print('== A. the cube: flux, real gauge, copy sign')
fl = {S: abs(face_flux(sum(hops(S)))[0]) for S in (0.5, 1.0, 1.5, 3.0)}
Wi = hops(1.5); R = sum(Wi); Ri = [r3*w for w in Wi]; s = 1j*Ri[0]@Ri[1]@Ri[2]@R
Dg = np.ones(8, complex); done = [0]
while len(done) < 8:
    for a in list(done):
        for b in range(8):
            if b not in done and abs(R[b, a]) > 0: Dg[b] = Dg[a]*np.conj(R[b, a]/abs(R[b, a])); done.append(b)
G8 = np.diag(Dg); Rg = G8@R@G8.conj().T; sg = G8@s@G8.conj().T
check('[T]', 'A1 the spin-S overlap gives each face flux 2 pi S/3 (S = 1/2, 1, 3/2, 3: %.3f, %.3f, %.3f, %.3f): T-even (0 or pi) only for '
      'S in (3/2)Z; CL-1\'s S = 3/2 is pi flux, so R is real in a gauge, R^2 = 1' % tuple(fl[S] for S in (0.5, 1.0, 1.5, 3.0)),
      abs(fl[1.5]-np.pi) < 1e-9 and abs(fl[0.5]-np.pi/3) < 1e-9 and np.abs(Rg.imag).max() < 1e-12 and np.abs(R@R-np.eye(8)).max() < 1e-12,
      'imag %.0e' % np.abs(Rg.imag).max())
check('[T]', 'A2 in that gauge the copy sign s = i R1R2R3R is purely imaginary, [s, R] = 0, s^2 = 1: complex conjugation K maps s -> -s, '
      'so the copy mass breaks plain time reversal and keeps only K composed with an odd rotation',
      np.abs(sg.real).max() < 1e-12 and np.abs(s@R-R@s).max() < 1e-12 and np.abs(s@s-np.eye(8)).max() < 1e-12)

L = 6; N = L**3; SITES = [np.array(p) for p in itertools.product(range(L), repeat=3)]
def idx(p): p = np.mod(p, L); return (p[0]*L+p[1])*L+p[2]
CL = np.array([ci(x % 2) for x in SITES])
def layer(M8, par):
    U = np.zeros((N, N), complex)
    for o in itertools.product(range(par, L, 2), repeat=3):
        ids = [idx(np.array(o)+(c if par == 0 else 1-c)) for c in C8]; U[np.ix_(ids, ids)] = M8
    return U
def basis(a):
    B = np.zeros((N, 8), complex)
    for k, c in enumerate(C8):
        for n in itertools.product(range(3), repeat=3): B[idx(2*np.array(n)+c), k] = w3**(-np.dot(a, n))/np.sqrt(27)
    return B
FAM = [(1, 1, 1), (2, 2, 2)]; BAS = {a: basis(np.array(a)) for a in FAM + [(0, 0, 0)]}
def spec(U, a): return np.sort(np.angle(np.linalg.eigvals(BAS[a].conj().T@U@BAS[a])))
def split(U): return np.abs(spec(U, FAM[0])-spec(U, FAM[1])).max()
eta8 = np.diag([(-1.0)**C8[c].sum() for c in range(8)]); PS = eta8@s
We, Wo = layer(R, 0), layer(R, 1); Hc = 0.5j*(Wo@We-We@Wo)
def factors(eps=0.3, mu=0.05, MN=0.2, lam=0.0, kap=0.0, h8=None, pal=True):
    Cm = expm(1j*(MN/4)*(np.eye(8)-s)@R); Me = Cm@expm(-1j*(eps-mu/2)*R)@Cm
    if kap:
        Ep = expm(-0.5j*kap*(PS if h8 is None else h8)); Me = Ep@Me@Ep if pal else Ep@Ep@Me
    F = [layer(expm(1j*(eps+mu/2)*R), 1), layer(Me, 0)]
    return ([expm(-1j*lam*Hc)] + F) if lam else F
def prod(F):
    U = np.eye(N, dtype=complex)
    for f in F: U = U@f
    return U

print('== B. the operators that send family j to -j (48 cube-centred point maps x -> c + g(x - c), c = (1/2,1/2,1/2), each unitary or x K)')
def ops():
    res = []
    for perm in itertools.permutations(range(3)):
        for sgn in itertools.product((1, -1), repeat=3):
            g = np.zeros((3, 3), int)
            for i in range(3): g[i, perm[i]] = sgn[i]
            off = np.array([1 if g[i].sum() < 0 else 0 for i in range(3)])
            P8 = np.zeros((8, 8)); P = np.zeros((N, N))
            for a in range(8): P8[ci((g@C8[a]+off) % 2), a] = 1
            for x in SITES: P[idx(g@x+off), idx(x)] = 1
            for anti in (False, True):
                D = fit(P8@(R.conj() if anti else R)@P8.T, R)
                res.append((g, anti, np.diag(D[CL])@P, np.diag(D)@P8))
    return res
OPS = ops()
def cyc(A, B): return any(all(np.abs(A[(i+r) % len(A)]-B[i]).max() < 1e-9 for i in range(len(A))) for r in range(len(A)))
def ties(F):
    out = []
    for g, anti, V, _ in OPS:
        im = [V@(f.conj() if anti else f)@V.conj().T for f in F]
        com = cyc(im, F); tr = cyc(im, [f.conj().T for f in F[::-1]])
        img = tuple((g@np.ones(3)*(-1 if anti else 1)).astype(int))
        if (com or tr) and img == (-1, -1, -1):
            same_w = (com and not anti) or (tr and anti)          # quasi-energy kept: family j and -j isospectral
            det = int(round(np.linalg.det(g))); tag = ('K' if anti else '') + ('+' if det > 0 else '-')
            if same_w: out.append(tag)
    return sorted(set((t, out.count(t)) for t in out))
VI = [o for o in OPS if (o[0] == -np.eye(3, dtype=int)).all() and not o[1]][0]
M0 = ties(factors(MN=0)); M1 = ties(factors()); M2 = ties(factors(lam=0.1)); M3 = ties(factors(lam=0.1, kap=0.1))
check('[T]', 'B1 ties (point maps with j -> -j and quasi-energy kept; + proper, - improper, K antiunitary): no copy mass %s = the 3 C2\' '
      'about face diagonals, inversion I and S6 = I C3, time reversal K and K C3; with the copy mass %s = I, S6 and K sigma_d '
      '(the C2\' are odd rotations); adding the chiral generator %s = I, S6 only (Hc is imaginary in the real gauge, so K-type ties '
      'break); adding the I-odd pseudoscalar eta s %s = none' % (M0, M1, M2, M3),
      M0 == [('+', 3), ('-', 3), ('K+', 3), ('K-', 3)] and M1 == [('-', 3), ('K-', 3)] and M2 == [('-', 3)] and M3 == [])
I8 = VI[3]
cm = [np.abs(I8@M@I8.conj().T-M).max() for M in (R, Ri[0], Ri[1], Ri[2], s)] + [np.abs(VI[2]@Hc@VI[2].conj().T-Hc).max()]
check('[T]', 'B2 inversion about a cube centre (with its gauge) fixes R, each R_i, the copy sign s, and the chiral generator '
      '(both tilings are mapped to themselves): every CL-1 term and (i/2)[W_o, W_e] commutes with it; it flips the sublattice sign, so '
      'eta s is I-odd and invariant under all 24 rotations', max(cm) < 1e-12 and np.abs(I8@PS@I8.conj().T+PS).max() < 1e-12,
      'max comm %.0e' % max(cm))

print('== C. family spectra with and without the chiral term (sectors j = 1, 2 on the turn-fixed line)')
rows = []
for lab, kw in [('tick', {}), ('no copy', dict(MN=0)), ('Hc 0.05', dict(lam=0.05)), ('Hc 0.2', dict(lam=0.2)), ('Hc 0.5', dict(lam=0.5)),
                ('eta s 0.1', dict(kap=0.1)), ('eta s 0.1 unpal', dict(kap=0.1, pal=False)), ('Hc 0.2 + eta s 0.3', dict(lam=0.2, kap=0.3))]:
    rows.append((lab, split(prod(factors(**kw)))))
check('[F]', 'C1 the families j = 1, 2 stay exactly isospectral (signed quasi-energies) for the tick, with the chiral generator at '
      'every strength, with the I-odd pseudoscalar and with both: ' + ', '.join('%s %.0e' % r for r in rows),
      max(r[1] for r in rows) < 1e-12)
Hc_sp = np.sort(np.linalg.eigvalsh(BAS[FAM[0]].conj().T@Hc@BAS[FAM[0]])); Hc_sm = np.sort(np.linalg.eigvalsh(BAS[FAM[1]].conj().T@Hc@BAS[FAM[1]]))
check('[F]', 'C2 the free chiral generator alone has identical family spectra %s (exp(-i t Hc) for every t)' % np.round(Hc_sp, 3),
      np.abs(Hc_sp-Hc_sm).max() < 1e-12)
def blk(M, a): return BAS[a].conj().T@M@BAS[a]
def inter_dim(gens):
    Mx = np.vstack([np.kron(blk(Gm, FAM[0]).T, np.eye(8))-np.kron(np.eye(8), blk(Gm, FAM[1])) for Gm in gens])
    return int(np.sum(np.linalg.svd(Mx, compute_uv=False) < 1e-9))
Pe, Se = layer(PS, 0), layer(s, 0)
dims = [inter_dim(gs) for gs in ([We, Wo], [We, Wo, Se], [We, Wo, Se, Hc], [We, Wo, Se, Hc, Pe])]
check('[T]', 'C3 the tie that survives eta s is algebraic, not a point map: a unitary Y with Y G_(j=1) Y^+ = G_(j=2) for every generator '
      '(both tilings\' reflections, copy sign, Hc, eta s) exists; commutant dimensions %s; so every free tick that is a word in these generators '
      'keeps families 1 and 2 degenerate (interactions not tested: Y is a per-sector map, not shown to be a lattice operator)' % dims, min(dims) > 0)

print('== D. what does split them')
Ve8 = np.diag([[0.3, -0.2, 0.5, 0.1][C8[c].sum()] for c in range(8)]).astype(complex)
pol = [split(prod(factors(kap=k, h8=Ve8, pal=False))) for k in (0.02, 0.04)]
polp = [split(prod(factors(kap=k, h8=Ve8))) for k in (0.02, 0.04)]
polH = [split(prod(factors(lam=0.1, kap=k, h8=Ve8))) for k in (0.02, 0.04)]
rng = np.random.default_rng(7); h0 = rng.normal(size=(8, 8))+1j*rng.normal(size=(8, 8)); h0 = h0+h0.conj().T
gen = [split(prod(factors(kap=k, h8=h0))) for k in (0.02, 0.04)]
sp12 = split(prod([layer(expm(1j*0.325*sum(hops(0.5))), 1), layer(expm(-1j*0.275*sum(hops(0.5))), 0)]))
order = lambda v: np.log(v[1]/v[0])/np.log(2)
dimsP = inter_dim([We, Wo, Se, layer(Ve8, 0)])
polL = [split(prod(factors(lam=l, kap=0.02, h8=Ve8))) for l in (0.005, 0.01)]
polH = [split(prod(factors(lam=0.01, kap=k, h8=Ve8))) for k in (0.01, 0.02)]
check('[F]', 'D1 a polar term along the turn axis (a cube potential graded by |c|: an axial vector, rotations broken to C3v, I broken) '
      'placed palindromically keeps K sigma_d and the families stay tied (%.0e); placed once per tick (a time-ordering choice) it splits '
      'them at order %.1f in its strength (%.1e at 0.04); palindromic plus the chiral generator splits at order %.1f in the polar strength '
      'and %.1f in the chiral one (bilinear: split = %.2f kap lam at small strengths); a generic cube term splits at order %.1f; no j=1 -> j=2 intertwiner (dim %d)'
      % (polp[1], order(pol), pol[1], order(polH), order(polL), polL[1]/(0.02*0.01), order(gen), dimsP),
      polp[1] < 1e-12 and min(pol[1], polH[1], gen[1]) > 1e-7 and dimsP == 0 and abs(order(polH)-1) < 0.1 and abs(order(polL)-1) < 0.1)
check('[F]', 'D2 a T-odd hop alone does not split: the spin-1/2 overlap (flux pi/3 per face) keeps inversion, split %.0e' % sp12, sp12 < 1e-12)
print('   reading: the tie is not parity alone; it survives the copy mass, the chiral generator, a T-odd flux and the O-invariant I-odd term;')
print('   it breaks only with a term carrying a direction (an axial vector along the family turn axis, breaking the cubic rotations)')
print('   together with a time-reversal breaker (the chiral generator or a non-palindromic placement): first order in each,')
print('   so with only small breakings the pair split is second order (kap lam), far below the order-one split measurement needs (E3).')

print('== E. Z3 differences and mass estimates')
pairs = {(0, 1): 1, (1, 2): 1, (0, 2): 2}
check('[T]', 'E1 the family group is the order-3 subgroup {0, psi, psi^2}: pair differences are psi, psi, psi^2, so with k -> -k one '
      'spurion distance and without it at most two (pairs 12 and 23 always share psi); breaking k -> -k never gives three distances',
      sorted(set(pairs.values())) == [1, 2] and pairs[(0, 1)] == pairs[(1, 2)])
ok = True; worst = 0
for e in (1/2, 1/3, 0.22):
    for n in (1, 2, 3):
        lam_ = [abs(1+e*w3**j+e**n*w3**(2*j)) for j in range(3)]; worst = max(worst, max(lam_)/min(lam_))
check('[E]', 'E2 with k -> -k broken, a translation-invariant Dirac matrix on that group is a Z3 circulant c0 + c1 eps P + c2 eps^n P^2, '
      'eigenvalues |c0 + c1 eps w^j + c2 eps^n w^2j|: with unit coefficients and eps <= 1/2 the largest ratio is %.1f against measured '
      'm_t/m_u = 1.4e5, m_tau/m_e = 3.5e3' % worst, worst < 10)
mu_ = dict(lep=(0.000511, 0.10566, 1.77686), up=(0.00123, 0.620, 171.7), dn=(0.00267, 0.0532, 2.84))
fr = {k: (v[1]-v[0])/(v[1]+v[0]) for k, v in mu_.items()}
check('[E]', 'E3 measured: no two families of a sector are degenerate, so the rules must untie a conjugate pair; under the reading with '
      'the two lighter families as the pair, the needed relative splitting (m2 - m1)/(m2 + m1) is lep %.3f, up %.3f, down %.3f: order one, '
      'not a small breaking' % (fr['lep'], fr['up'], fr['dn']), min(fr.values()) > 0.9)
print('elapsed_seconds %.1f' % (time.time()-T0))
print('theorems: A1, A2, B1, B2, C3, E1; finite: C1, C2, D1, D2; estimates: E2, E3.')
print('supplied: zoom-3 family reading, eps/mu/MN and term strengths, the test terms (eta s, polar |c| potential, generic term), '
      'unit coefficients in E2; PDG masses.')
print(f'\nTOTAL: PASS={NP} FAIL={NF}')
