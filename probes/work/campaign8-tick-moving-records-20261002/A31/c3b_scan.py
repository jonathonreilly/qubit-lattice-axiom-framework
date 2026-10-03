"""A31 c3b: robustness scan for c3. For each lattice and law, the largest TV over all choices of
(excitation site a, record site r) for the swap-step experiments, and over all site pairs for the
two-site X-basis readout. Same laws and conventions as c3_readability.py."""
import signal, numpy as np
signal.alarm(55)
import re
src = open('c3_readability.py').read()
src = "\n".join(l for l in src.splitlines() if not l.startswith("experiments("))
exec(src)
import itertools
_hcache = {}
_hraw = hamiltonian
def hamiltonian(lat, eta, law, basis):
    key = (id(lat), np.asarray(eta).tobytes(), law, len(basis), basis[0], basis[-1])
    if key not in _hcache: _hcache[key] = _hraw(lat, eta, law, basis)
    return _hcache[key]
_ecache = {}
def evolve(H, psi, t):
    key = (H.tobytes(), t)
    if key not in _ecache: _ecache[key] = np.linalg.eigh(H)
    w, V = _ecache[key]; return V @ (np.exp(-1j * w * t) * (V.conj().T @ psi))
def scan(name, lat, eta):
    eta2 = lat.pullback(eta)
    for law in ('XXZ', 'SHEIS'):
        m3 = m3s = m3b = m4 = 0.0; m1 = m2 = 0.0
        for a in range(lat.N):
            S1 = {1 << a: 1.0}
            m1 = max(m1, tv(run(lat,eta,law,1,S1), run(lat,eta2,law,1,S1)))
            for r in range(lat.N):
                if r == a: continue
                m3 = max(m3, tv(run(lat,eta,law,1,S1,rec={r:0},sw='blind'), run(lat,eta2,law,1,S1,rec={r:0},sw='blind')))
                if law == 'XXZ':
                    m3s = max(m3s, tv(run(lat,eta,law,1,S1,rec={r:0},sw='signed'), run(lat,eta2,law,1,S1,rec={r:0},sw='signed')))
                S2 = {(1 << a) | (1 << r): 1.0}
                m2 = max(m2, tv(run(lat,eta,law,2,S2), run(lat,eta2,law,2,S2)))
                m3b = max(m3b, tv(run(lat,eta,law,2,S2,rec={r:1},sw='blind'), run(lat,eta2,law,2,S2,rec={r:1},sw='blind')))
            for s, t in itertools.combinations(range(lat.N), 2):
                m4 = max(m4, tv(run(lat,eta,law,1,S1,readout='X',xpair=(s,t)), run(lat,eta2,law,1,S1,readout='X',xpair=(s,t))))
        extra = f"; E3s signed SW {m3s:.1e}" if law == 'XXZ' else ""
        print(f"  {name} {law:5s}: max TV  E1 {m1:.1e}; E2 {m2:.1e}; E3 blind SW, record 0 {m3:.1e}{extra}; "
              f"E3b blind SW, record 1 {m3b:.1e}; E4 two-site X readout {m4:.1e}")
scan("(A) 3x3 patch, C4  ", latA, etaA)
scan("(B1) 4x2 torus KS   ", latB, np.array(ks))
scan("(B2) 4x2 torus dimer", latB, np.array(dim))
