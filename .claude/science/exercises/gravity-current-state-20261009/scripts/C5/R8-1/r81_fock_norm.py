"""R8-1, script 1: the quartic prefactor (referee defect 2), decided by spectra.

The R7-1 runner (and BT) uses W(P; k1', k1) as the PRODUCT-BASIS (ordered-pair) kernel:
first-quantized H = diag(H0(k1)) + W(k1', k1) on ordered pairs (k1, P - k1), projected on the
odd (fermionic) subspace.  Question: which second-quantized prefactor reproduces that operator,
  (1/2) sum_{P,k1',k1} W a+_{k1'} a+_{P-k1'} a_{P-k1} a_{k1}   or   (1/4) sum (...) ?
Exact CAR enumeration on a small momentum set; compare full 2-particle spectra at fixed P.
Also: the same test for a generic exchange-symmetric two-body kernel that does NOT conserve P
(the boost's two-body part K_W = (1/2){W, X_P} is of that kind).
"""
import numpy as np, itertools
rng = np.random.default_rng(7)

def annihilate(state, mode):
    if not (state >> mode) & 1: return state, 0
    return state ^ (1 << mode), (-1) ** bin(state & ((1 << mode) - 1)).count('1')
def create(state, mode):
    if (state >> mode) & 1: return state, 0
    return state | (1 << mode), (-1) ** bin(state & ((1 << mode) - 1)).count('1')

def fock_2body(V, nm, pref):
    """matrix of pref * sum V[(a',b'),(a,b)] a+_{a'} a+_{b'} a_b a_a on the 2-particle sector."""
    basis = [(1 << a) | (1 << b) for a, b in itertools.combinations(range(nm), 2)]
    ix = {s: i for i, s in enumerate(basis)}
    Mx = np.zeros((len(basis), len(basis)), dtype=complex)
    for j, ket in enumerate(basis):
        for a in range(nm):
            for b in range(nm):
                s1, z1 = annihilate(ket, a); s2, z2 = annihilate(s1, b) if z1 else (0, 0)
                if z1*z2 == 0: continue
                for ap in range(nm):
                    for bp in range(nm):
                        v = V[ap*nm + bp, a*nm + b]
                        if v == 0: continue
                        s3, z3 = create(s2, bp); s4, z4 = create(s3, ap) if z3 else (0, 0)
                        if z3*z4 == 0: continue
                        Mx[ix[s4], j] += pref*v*z1*z2*z3*z4
    return Mx, basis

def first_quantized_antisym(V, nm):
    """V on the product space restricted to the antisymmetric subspace (orthonormal basis)."""
    basis = list(itertools.combinations(range(nm), 2))
    Bm = np.zeros((nm*nm, len(basis)))
    for i, (a, b) in enumerate(basis):
        Bm[a*nm + b, i] = 1/np.sqrt(2); Bm[b*nm + a, i] = -1/np.sqrt(2)
    return Bm.T @ V @ Bm

out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line); out.append(line)

nm = 7                                   # momenta k = 2 pi n / 7, n = 0..6 ; P = 0 sector: (n, -n)
# (A) product-basis W(P=0; k1', k1), odd under k1 -> -k1 on each side (as the BT W is)
g = np.array([0.0, 1.0, 2.0, 3.0, -3.0, -2.0, -1.0])     # odd: g[-n] = -g[n]
H0 = np.array([0.3, 1.1, 1.7, 2.2, 2.2, 1.7, 1.1])
V = np.zeros((nm*nm, nm*nm))
for a in range(nm):
    for ap in range(nm):
        V[ap*nm + (-ap) % nm, a*nm + (-a) % nm] = 0.37*g[ap]*g[a]   # conserves P = 0
H1 = np.zeros((nm*nm, nm*nm))
for a in range(nm):
    for b in range(nm):
        H1[a*nm + b, a*nm + b] = H0[a] + H0[b]
# first-quantized, runner style: ordered pairs (k1, -k1), odd projection
Wrun = 0.37*np.outer(g, g); Hrun = np.diag(H0 + H0[(-np.arange(nm)) % nm]) + Wrun
X = np.eye(nm)[(-np.arange(nm)) % nm]; Po = 0.5*(np.eye(nm) - X)
ev_run = np.linalg.eigvalsh(Po @ Hrun @ Po); ev_run = np.sort(ev_run[np.abs(ev_run) > 1e-12])
pr('(A) runner-style first-quantized odd spectrum at P=0:', np.round(ev_run, 12))
for pref in [0.5, 0.25]:
    Vf, basis = fock_2body(V, nm, pref)
    Hf = np.diag([H0[[i for i in range(nm) if (s >> i) & 1]].sum() for s in basis]) + Vf
    # restrict to the P = 0 pairs
    sel = [i for i, s in enumerate(basis) if (sum(i2 for i2 in range(nm) if (s >> i2) & 1) % nm) == 0]
    evf = np.sort(np.linalg.eigvalsh(Hf[np.ix_(sel, sel)].real))
    pr('(A) Fock prefactor %.2f, P=0 spectrum:' % pref, np.round(evf, 12),
       '| max diff to runner = %.1e' % np.max(np.abs(evf - ev_run)))
# matrix-element form of the referee's check: <pair k'| . |pair k> vs W(k', k)
Vf2, basis = fock_2body(V, nm, 0.5)
ix = {s: i for i, s in enumerate(basis)}
for kp, k in [(1, 1), (2, 1), (1, 2)]:
    bra = (1 << kp) | (1 << ((-kp) % nm)); ket = (1 << k) | (1 << ((-k) % nm))
    sgn = (1 if kp < (-kp) % nm else -1)*(1 if k < (-k) % nm else -1)
    A = first_quantized_antisym(V, nm)
    bi = list(itertools.combinations(range(nm), 2)).index(tuple(sorted((kp, (-kp) % nm))))
    ki = list(itertools.combinations(range(nm), 2)).index(tuple(sorted((k, (-k) % nm))))
    pr('(A) k\'=%d k=%d : Fock(1/2) <pair|.|pair> = %+.4f ; first-quantized <A\'|W|A> = %+.4f ; W(k\',k) = %+.4f'
       % (kp, k, sgn*Vf2[ix[bra], ix[ket]].real, sgn*A[bi, ki], 0.37*g[kp]*g[k]))
# (B) generic exchange-symmetric two-body kernel (no P conservation), e.g. a boost-type K_W
Kr = rng.normal(size=(nm*nm, nm*nm)) + 1j*rng.normal(size=(nm*nm, nm*nm))
Kr = 0.5*(Kr + Kr.conj().T)
Xc = np.zeros((nm*nm, nm*nm))
for a in range(nm):
    for b in range(nm): Xc[b*nm + a, a*nm + b] = 1
Kr = 0.5*(Kr + Xc @ Kr @ Xc)                                   # commutes with exchange
A = first_quantized_antisym(Kr, nm)
for pref in [0.5, 0.25]:
    F, basis = fock_2body(Kr, nm, pref)
    sg = []                                                    # phase between Fock pair a+_a a+_b|0> (a<b) and (|ab>-|ba>)/sqrt2
    pr('(B) generic exchange-symmetric kernel, Fock prefactor %.2f : max |Fock - first-quantized antisym| = %.2e'
       % (pref, np.max(np.abs(F - A))))
with open(__file__.replace('.py', '.out'), 'w') as fh:
    fh.write('\n'.join(out) + '\n')
