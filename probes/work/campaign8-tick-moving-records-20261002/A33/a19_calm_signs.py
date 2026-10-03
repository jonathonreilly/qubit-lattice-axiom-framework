"""A33 a19: exact-sign version of the site-centred calm parent test.
usage: python3 a19_calm_signs.py r2 i1,i2,...
For each sign choice s = (s_V, s_C, s_E, s_F) (the vacuum has g_role = s_role; each choice is
covariant because every shape is exactly invariant under its site group), the 8 operators
-s_{role(o)} g_o(0), o in {0,1}^3, commute; the projector prod_o (1 - s g_o)/2 is nonzero iff no
product of a subset of them equals -1 (exact Pauli algebra, A20's P class). If nonzero it is a
translation-invariant, covariant, frustration-free law term of the generators' range annihilating all
8 translates (EXACT). Reports the sign choices that admit it.
"""
import signal, sys, time, pickle, itertools
signal.alarm(55)
from p2a_core import Space, shapes_of, role_of, shape_at
from p2lib import pauli_exact, P

r2 = int(sys.argv[1]); idx = [int(t) for t in sys.argv[2].split(",")]
S = Space(r2)
D = pickle.load(open(f"p2a_sols_r{r2}.pkl", "rb"))
for n in idx:
    sol, ti = D["sols"][n]
    sh = shapes_of(S, sol)
    ops = []
    for o in itertools.product((0, 1), repeat=3):
        role, axis = role_of(o)
        sg, p = shape_at(sh[role], role, axis, (0, 0, 0))
        ops.append((role, pauli_exact(p, sg)))
    ok_signs = []
    for sv in itertools.product((1, -1), repeat=4):
        s = dict(zip("VCEF", sv))
        neg = [P(0 if -s[r] == 1 else 2, {}) * op for r, op in ops]
        bad = False
        for mask in range(1, 256):
            prod = P()
            for i in range(8):
                if (mask >> i) & 1:
                    prod = prod * neg[i]
            if not prod.s:          # proportional to identity
                if prod.k % 4 != 0:  # equals -1 (or +-i): the all-violated projector vanishes
                    bad = True
                    break
        if not bad:
            ok_signs.append(sv)
    print(f"#{n} ti={int(ti)} sol={sol}: sign choices (sV,sC,sE,sF) admitting the site-centred commuting parent: "
          f"{len(ok_signs)}/16 {ok_signs[:4]}{'...' if len(ok_signs) > 4 else ''}")
