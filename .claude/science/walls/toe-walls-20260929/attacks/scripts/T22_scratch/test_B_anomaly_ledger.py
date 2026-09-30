"""T22 test B: anomaly and node-count ledger for mirror-removal routes (exact rationals).

A left-handed Weyl multiplet is (c, w, Y): colour type c in {'3','3b','1'}, SU(2) dim w in {1,2}, hypercharge Y.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement as cwr

DIM3 = {'3':3, '3b':3, '1':1}
A3 = {'3':1, '3b':-1, '1':0}
T3 = {'3':F(1,2), '3b':F(1,2), '1':F(0)}
T2 = {1:F(0), 2:F(1,2)}

def traces(content):
    r = dict(SU3cubed=F(0), SU3sqY=F(0), SU2sqY=F(0), Ycubed=F(0), gravY=F(0), doublets=0, nu=0)
    for (c, w, Y) in content:
        r['SU3cubed'] += A3[c]*w
        r['SU3sqY']   += T3[c]*w*Y
        r['SU2sqY']   += T2[w]*DIM3[c]*Y
        r['Ycubed']   += DIM3[c]*w*Y**3
        r['gravY']    += DIM3[c]*w*Y
        r['doublets'] += DIM3[c] if w == 2 else 0
        r['nu']       += DIM3[c]*w
    return r

QL = ('3', 2, F(1,3)); LL = ('1', 2, F(-1))
UC = ('3b', 1, F(-4,3)); DC = ('3b', 1, F(2,3)); EC = ('1', 1, F(2)); NC = ('1', 1, F(0))

cases = {
 "(i)  native 8-state L surface Q_L + L_L": [QL, LL],
 "(ii) + u^c, d^c, e^c  (P-COMP without nu_R, 15)": [QL, LL, UC, DC, EC],
 "(iii)+ nu^c            (16)": [QL, LL, UC, DC, EC, NC],
}
print("== Anomaly traces (left-handed Weyl content)")
for name, cont in cases.items():
    t = traces(cont)
    gauge_ok = all(t[k] == 0 for k in ['SU3cubed','SU3sqY','SU2sqY','Ycubed','gravY']) and t['doublets'] % 2 == 0
    print(f"{name}\n    SU3^3={t['SU3cubed']}  SU3^2Y={t['SU3sqY']}  SU2^2Y={t['SU2sqY']}  Y^3={t['Ycubed']}  grav^2Y={t['gravY']}"
          f"  #doublets={t['doublets']}  nu={t['nu']}  nu mod 16={t['nu'] % 16}  gauge-anomaly-free={gauge_ok}")

# Brute-force minimal SU(2)-singlet completions of (i)
grid = [F(n,3) for n in range(-12, 13)]
col_types = [('3b', 1, y) for y in grid] + [('3', 1, y) for y in grid]
sing_types = [('1', 1, y) for y in grid]
base = traces([QL, LL])

sols = []
for m in range(0, 4):                       # coloured multiplets
    for cc in cwr(col_types, m):
        t = traces(list(cc))
        if base['SU3cubed'] + t['SU3cubed'] != 0: continue
        if base['SU3sqY'] + t['SU3sqY'] != 0: continue
        for s in range(0, 4):               # colourless singlets
            for ss in cwr(sing_types, s):
                tt = traces(list(cc) + list(ss))
                if base['gravY'] + tt['gravY'] != 0: continue
                if base['Ycubed'] + tt['Ycubed'] != 0: continue
                if base['SU2sqY'] + tt['SU2sqY'] != 0: continue
                n_states = tt['nu']
                sols.append((n_states, cc, ss))
sols.sort(key=lambda x: (x[0], str(x[1]), str(x[2])))
nmin = sols[0][0]
print("\n== Minimal SU(2)-singlet completions of (i), grid Y in n/3, |Y|<=4, <=3 coloured + <=3 colourless multiplets")
print("   minimal number of added states:", nmin)
def fmt(sol):
    n, cc, ss = sol
    return f"{n} states: " + ", ".join(f"({c},{w},{y})" for c,w,y in list(cc)+list(ss))
mins = [s for s in sols if s[0] == nmin]
print("   number of distinct minimal solutions:", len(mins))
for s in mins[:12]: print("   ", fmt(s))
sm = set([UC, DC, EC])
print("   SM completion {u^c,d^c,e^c} among minimal solutions:", any(set(list(s[1])+list(s[2])) == sm for s in mins))
by_n = {}
for s in sols: by_n.setdefault(s[0], 0); by_n[s[0]] += 1
print("   solution counts by added-state count (<=10):", {k:v for k,v in sorted(by_n.items()) if k <= 10})

# Node-count comparison
print("\n== Lattice node count needed for a symmetric-mirror route (nu chiral + nu mirror)")
for nu in (8, 15, 16):
    print(f"   nu = {nu:2d}: nodes needed = {2*nu}")
print("   nodes supplied: flowing walker 8 (4R+4L); ordered tick U_- 16 (8R+8L); tails tick U_g 8 (all R, 4 at quasi-energy 0 + 4 at pi)")
print("   copies of the flowing walker for nu=16: ", 32/8, "; copies of the ordered tick: ", 32/16)
# gap between the native surface and the walker: the 8-state surface has Tr Y^3 != 0 as a pure left-handed set;
# a vector-like 4R+4L walker can carry it only as 4 L + 4 conj(R) or as a Dirac set, i.e. with Y^3 anomaly cancelled by construction.
