"""R7-6 script 3: independent cross-check of script 1's three-fermion sector.
Builds the second-quantized law H = sum eps n + (1/2) sum_P12 sum W(P12;k1',k1) a+_{k1'} a+_{P12-k1'} a_{P12-k1} a_{k1}
directly on occupation-number Slater determinants (explicit fermionic signs), restricted to box modes |k| < 1,
and compares the lowest eigenvalue at several P with script 1's antisymmetrised first-quantised build."""
import numpy as np, itertools, subprocess, sys, importlib.util
spec = importlib.util.spec_from_file_location('r76', __file__.replace('r76_fock_crosscheck.py', 'r76_threebody_naive.py'))
sys.argv = ['x', 'sym=fermi', 'lam=-3', 'kap=0.25', 'pi1=0.8', 'pi2=1.0', 'Ls=0']
# import functions without running the main loop: exec the module text up to the main section
src = open(__file__.replace('r76_fock_crosscheck.py', 'r76_threebody_naive.py')).read().split('out = []')[0]
ns = {}; exec(src, ns)
wrap, eps, pair_W, three_body, LEG3 = ns['wrap'], ns['eps'], ns['pair_W'], ns['three_body'], ns['LEG3']
LAM = -3.0
out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)

def fock(L, nP):
    k = wrap(2*np.pi*np.arange(L)/L)
    modes = [n for n in range(L) if abs(k[n]) < LEG3]
    basis = [t for t in itertools.combinations(modes, 3) if sum(t) % L == nP % L]
    index = {t: i for i, t in enumerate(basis)}
    D = len(basis); H = np.zeros((D, D))
    for i, t in enumerate(basis):
        H[i, i] = sum(eps(k[n]) for n in t)
    cache = {}
    for i, t in enumerate(basis):
        occ = list(t)
        # annihilate ordered pair a_{P12-k1} a_{k1}: sum over ordered pairs (p, q) of occupied modes, k1 = q, P12 - k1 = p
        for q in occ:
            for p in occ:
                if p == q: continue
                n12 = (p + q) % L
                if n12 not in cache: cache[n12] = pair_W(L, n12, LAM)[0]
                Wd = cache[n12]
                if not Wd: continue
                idx, Wb = Wd
                pos = np.where(idx == q)[0]
                if len(pos) == 0: continue
                # apply a_q then a_p to |t> (ordered creation string of sorted modes), track sign
                st = list(occ); sgn = 1
                j = st.index(q); sgn *= (-1)**j; st.pop(j)
                j = st.index(p); sgn *= (-1)**j; st.pop(j)
                for r, n1p in enumerate(idx):
                    val = Wb[r, pos[0]]
                    if val == 0.0: continue
                    n2p = (n12 - n1p) % L
                    if n2p == n1p or n2p in st or n1p in st: continue
                    if abs(k[n2p]) >= LEG3: continue
                    # a+_{n1p} a+_{n2p} acting on st: first a+_{n2p}, then a+_{n1p}
                    s2 = list(st); sg2 = sgn
                    j = sum(1 for x in s2 if x < n2p); sg2 *= (-1)**j; s2.insert(j, n2p)
                    j = sum(1 for x in s2 if x < n1p); sg2 *= (-1)**j; s2.insert(j, n1p)
                    new = tuple(s2)
                    if new in index:
                        H[index[new], i] += 0.5*val*sg2
    herm = abs(H - H.T).max()
    return np.linalg.eigvalsh(0.5*(H + H.T))[0], D, herm

for L in [90, 120]:
    for frac in [0.0, 0.2, 0.4]:
        nP = int(round(frac*L/(2*np.pi)))
        Ef, D, herm = fock(L, nP)
        r = three_body(L, nP, LAM)
        pr('L = %d P = %+.5f : Fock build E0 = %.12f (dim %d, herm %.0e) | script-1 build E0 = %.12f (dim %d) | diff %.1e'
           % (L, wrap(2*np.pi*nP/L), Ef, D, herm, r['E0'], r['dim'], Ef - r['E0']))
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out) + '\n')
