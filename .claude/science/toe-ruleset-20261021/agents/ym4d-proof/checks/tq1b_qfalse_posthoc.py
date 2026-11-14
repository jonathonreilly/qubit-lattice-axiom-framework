"""POST-HOC probe (run AFTER tq1; labelled post-hoc in TENTQ.md).
Criteria tq1_criteria.md are untouched; this probe has no PASS/FAIL of its own.
It exhibits TENTQ Proposition QFALSE's configuration explicitly and prints the ratio
max_X|<chi5_X D>| / (n ||D||_inf) for d = 4 at k = 1, 2, to show it grows like n^2.
j_0 := sign(d chi5_{X0}) (own sup 1), D := d* j_0.
"""
from fractions import Fraction as F
from itertools import product

L, d = 3, 4


def sigma5(a, n):
    t = F(a, n)
    if t >= 1:
        return F(0)
    return 1 - (10 * t ** 3 - 15 * t ** 4 + 6 * t ** 5)


for k in (1, 2):
    n = L ** k
    cX = (0,) * d                      # work in absolute coords, box = |w|_inf < n
    R = n                              # chi5 support radius
    chi = {}
    for w in product(range(-R, R + 1), repeat=d):
        v = F(1)
        for nu in range(d):
            v *= sigma5(abs(w[nu]), n)
            if v == 0:
                break
        if v:
            chi[w] = v
    # j_0 = sign(d chi5) on links with at least one endpoint in the support
    j = {}
    for w in product(range(-R - 1, R + 1), repeat=d):
        for mu in range(d):
            w2 = list(w); w2[mu] += 1
            dv = chi.get(tuple(w2), F(0)) - chi.get(w, F(0))
            if dv > 0:
                j[(w, mu)] = 1
            elif dv < 0:
                j[(w, mu)] = -1
    QX = sum(chi[w] * 0 for w in chi)  # placeholder
    # Q_X by the summation-by-parts form (exact) and by the box sum of D (exact): both
    Q_sbp = sum(dvv for dvv in
                (abs(chi.get(tuple([w[i] + (1 if i == mu else 0) for i in range(d)]), F(0)) - chi.get(w, F(0)))
                 for (w, mu) in j))
    D = {}
    for z in product(range(-R - 1, R + 2), repeat=d):
        tot = 0
        for mu in range(d):
            zm = list(z); zm[mu] -= 1
            tot += j.get((tuple(zm), mu), 0) - j.get((z, mu), 0)
        if tot:
            D[z] = tot
    Q_box = sum(chi.get(z, F(0)) * v for z, v in D.items())
    Dsup = max(abs(v) for v in D.values())
    ratio = Q_box / (n * Dsup)
    print(f"k={k}, n={n}: ||d chi5_X||_1 = {Q_sbp} (= 2d n^3 = {2*d*n**3}: {Q_sbp == 2*d*n**3})")
    print(f"         Q_X (box sum of chi5*D) = {Q_box};  equals ||d chi5||_1: {Q_box == Q_sbp}")
    print(f"         ||D||_inf = {Dsup} (<= 2d = {2*d}: {Dsup <= 2*d});  "
          f"Q_X/(n||D||_inf) = {ratio} = {float(ratio):.1f}   [n^2 = {n**2}]")
