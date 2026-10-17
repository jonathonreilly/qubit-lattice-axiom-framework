"""Dressed creators S' = E S E^R (E local near q, E^R = U E U^dag): lambda' vs lambda; and R-defect endpoints."""
import random
from pair import *

rng = random.Random(7)
C2s = [i for i, M in enumerate(Ms) if classify(M) in ('C2axis', 'C2edge')]
tot = agree = notin = 0
rdef = []
for gi in C2s:
    M = Ms[gi]
    cand = [((x, y, z), ct) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2) for ct in CTYPES]
    cand = [q for q in cand if rot_uc(M, q) != q and max(abs(t) for t in q[0]) >= 1]
    for q in rng.sample(cand, 4):
        Rq = rot_uc(M, q)
        S = string(rand_path(q, Rq, 1, rng, detour=False))
        lam = G.member_sign(pmul(pdag(S), Uc[gi].conj(S)))
        sq = lat.sidx[lat.wrap(q[0])]
        qubits = [i for i in range(C.nq) if C.site_of[i] == sq]
        for t in range(6):
            x = z = 0
            for i in rng.sample(qubits, 3):
                r = rng.randrange(3)
                if r in (0, 2): x |= 1 << i
                if r in (1, 2): z |= 1 << i
            E = (x, z, 0)
            ER = Uc[gi].conj(E)
            if not commute(E, ER):
                continue
            Sp = pmul(pmul(E, S), ER)
            lp = G.member_sign(pmul(pdag(Sp), Uc[gi].conj(Sp)))
            tot += 1
            if lp is None: notin += 1
            elif lp == lam: agree += 1
        # R-defect endpoints: E = X on a link half at q (flips B_q and R_l): endpoints become R-defects
        cq = cid(q)
        e = next(e for e in C.order[cq] if C.ekind[e] == 'link')
        E = (1 << C.Q[(e, cq)], 0, 0)
        ER = Uc[gi].conj(E)
        Sp = pmul(pmul(E, S), ER)
        lp = G.member_sign(pmul(pdag(Sp), Uc[gi].conj(Sp)))
        rdef.append((classify(M), lam, lp))
print('random local dressings: tested', tot, 'lambda unchanged', agree, 'S^dag S^R not in group', notin)
print('R-defect-endpoint creators (type, lambda clean, lambda dressed):', sorted(set(rdef)))
