"""A28 c1b: in every CUT-rule branch of c1, (i) each recorded site's qubit equals its record
content (records cut to agree: the A16 C2/C4 / A21 condition); (ii) every formation occurred at
a site with a recorded neighbour in that branch's PRE-tick pattern (gating); (iii) count how
often the gating record moved away in the same tick (new record left with no recorded neighbour)."""
import signal
import numpy as np
signal.alarm(55)
import c1_nosignal as c1

worst = 0.0; gate_viol = 0; nform = 0; orphan = 0; nbranch = 0
for seed in range(3):
    rng = np.random.default_rng(1000 + seed)
    model = c1.Model(rng)
    ra = rng.normal(size=2) + 1j * rng.normal(size=2); ra /= np.linalg.norm(ra)
    chi = rng.normal(size=(2,) * 4) + 1j * rng.normal(size=(2,) * 4); chi /= np.linalg.norm(chi)
    psi0 = np.einsum('i,jklm,n->ijklmn', ra, chi, np.array([1, 0], dtype=complex))
    br = [((), psi0, {0: ra}, 1.0)]
    for t in range(3):
        nxt = []
        for b in br:
            pre = b[2]
            for hist, ph, recs, w in c1.tick([b], model, 'cut'):
                nrm = np.vdot(ph, ph).real
                nxt.append((hist, ph, recs, w))
                if nrm < 1e-14:
                    continue
                nbranch += 1
                for s, r in recs.items():
                    ph2 = c1.apply(np.eye(2) - np.outer(r, r.conj()), [s], ph)
                    worst = max(worst, np.sqrt(np.vdot(ph2, ph2).real / nrm))
                for o in hist[-2]:
                    if o[1] == 'form':
                        nform += 1
                        if not any(i in pre for i in c1.NBR[o[0]]):
                            gate_viol += 1
                        if not any(i in recs and i != o[0] for i in c1.NBR[o[0]]):
                            orphan += 1
        br = nxt
print(f'branches {nbranch}; worst |(1-P_content)psi|/|psi| on recorded sites = {worst:.2e}')
print(f'formations {nform}; formed with no PRE-tick recorded neighbour: {gate_viol}')
print(f'formed records left with no recorded neighbour after the same tick (gating record moved away): {orphan}')
