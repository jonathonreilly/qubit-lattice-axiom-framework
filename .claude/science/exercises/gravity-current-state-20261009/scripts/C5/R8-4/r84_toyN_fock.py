"""R8-4 script B2: two-loop toy N on the explicit Fock Hamiltonian (d = 1, small L).
Species X,Y,A,B (outer quartet, coupling go) and Y,U,C,D (inner quartet, coupling gi).  Terms (each + h.c.):
  outer forward  X -> Y A B ;  outer vacuum 0 -> X Y A B  (vertex depends on rest(X) = (Y,A,B) only)
  inner forward  Y -> U C D ;  inner vacuum 0 -> Y U C D  (vertex depends on rest(Y) = (U,C,D) only)
The mixed O(go^2 gi^2) coefficient of E4(X_p) - E4(vac) is computed (i) by brute-force RS4 on the Fock space
and (ii) from the Goldstone linked closed form
  mixed = sum_{outer fwd} |o|^2 N(E_p - W_o, Y) + sum_{outer vac, X at p} (-|o_v|^2) N(-(E_p + W_o), Y)
  N(al, Y) = sum_{inner fwd} |i|^2 / (al^2 (al - c)) + sum_{inner vac, Y in it} (-|i_v|^2)(al - b)/(al^2 b^2),
  c = W_in - E_Y,  b = E_Y + W_in."""
import numpy as np, itertools, time, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import r84_fock as RF
from r84_fock import Ham, Lat, rs, Psi, legc, totc, P
STAT = ['F']
def hfac(Ex, W): return RF.hfac(Ex, W) if STAT[0] == 'F' else 1.0
def zs(): return -1.0 if STAT[0] == 'F' else 1.0
OUT = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); OUT.append(s)

def build_N(lat, go, gi):
    H = Ham(); H.E = lat.Em; N = lat.N
    terms = dict(of=[], ov=[], if_=[], iv=[])
    def quartet(Xs, rest, g, kf, kv):
        for mx in lat.modes_of[Xs]:
            for m1 in lat.modes_of[rest[0]]:
                for m2 in lat.modes_of[rest[1]]:
                    q3 = tuple(np.array(lat.q[mx]) - lat.q[m1] - lat.q[m2]); m3 = lat.find(rest[2], q3)
                    if m3 is None: continue
                    ms = (m1, m2, m3); W = sum(lat.Em[x] for x in ms); Ex = lat.Em[mx]
                    base = Psi(lat, ms)*np.prod([legc(lat, x) for x in ms])*totc(lat, mx)
                    a_f = base*np.sqrt(hfac(Ex, W))/np.sqrt(2*Ex*np.prod([2*lat.Em[x] for x in ms]))/N
                    if a_f != 0:
                        terms[kf].append((mx, ms, a_f))
                        if g: H.add(ms, (mx,), g*a_f)
                    # vacuum: X at -q_x ... i.e. create X' with q = -(q1+q2+q3)
                    qx = tuple(-(np.array(lat.q[m1]) + lat.q[m2] + lat.q[m3])); mxv = lat.find(Xs, qx)
                    if mxv is None: continue
                    a_v = Psi(lat, ms)*np.prod([legc(lat, x) for x in ms + (mxv,)])*totc(lat, mxv)/np.sqrt(np.prod([2*lat.Em[x] for x in ms + (mxv,)]))/N
                    if a_v != 0 and mx == lat.modes_of[Xs][0]:
                        pass
    # vacuum terms enumerated separately (one per rest configuration)
    def vac(Xs, rest, g, kv):
        for m1 in lat.modes_of[rest[0]]:
            for m2 in lat.modes_of[rest[1]]:
                for m3 in lat.modes_of[rest[2]]:
                    ms = (m1, m2, m3)
                    qx = tuple(-(np.array(lat.q[m1]) + lat.q[m2] + lat.q[m3])); mxv = lat.find(Xs, qx)
                    if mxv is None: continue
                    a_v = Psi(lat, ms)*np.prod([legc(lat, x) for x in ms + (mxv,)])*totc(lat, mxv)/np.sqrt(np.prod([2*lat.Em[x] for x in ms + (mxv,)]))/N
                    if a_v != 0:
                        terms[kv].append((mxv, ms, a_v))
                        if g: H.add((mxv,) + ms, (), g*a_v)
    quartet('X', ['Y', 'A', 'B'], go, 'of', 'ov'); vac('X', ['Y', 'A', 'B'], go, 'ov')
    quartet('Y', ['U', 'C', 'D'], gi, 'if_', 'iv'); vac('Y', ['U', 'C', 'D'], gi, 'iv')
    return H, terms

def closed_mixed(lat, T, mx):
    Ep = lat.Em[mx]
    def Nf(al, my):
        Ey = lat.Em[my]; s = 0.0
        for (y, ms, a) in T['if_']:
            if y == my:
                c = sum(lat.Em[x] for x in ms) - Ey; s += a*a/(al*al*(al - c))
        for (y, ms, a) in T['iv']:
            if y == my:
                b = Ey + sum(lat.Em[x] for x in ms); s += zs()*a*a*(al - b)/(al*al*b*b)
        return s
    tot = 0.0; one = 0.0
    for (x, ms, a) in T['of']:
        if x == mx:
            Wo = sum(lat.Em[y] for y in ms); al = Ep - Wo; tot += a*a*Nf(al, ms[0]); one += a*a/al
    for (x, ms, a) in T['ov']:
        if x == mx:
            Wo = sum(lat.Em[y] for y in ms); al = -(Ep + Wo); tot += zs()*a*a*Nf(al, ms[0]); one += zs()*a*a/al
    return tot, one

if __name__ == '__main__':
    t0 = time.time()
    if len(sys.argv) > 1 and sys.argv[1] == 'B':
        STAT[0] = 'B'; RF.BOSE[0] = True
    pr(f'# statistics: {STAT[0]}')
    pr('# R8-4 B2: toy N mixed O(go^2 gi^2) coefficient: brute-force RS4 on the Fock space vs Goldstone closed form')
    mass = dict(X=0.30, Y=0.33, A=0.37, B=0.41, U=0.29, C=0.35, D=0.43)
    pr(f'# params {P}  masses {mass}')
    for (L, tw) in [(5, dict(X=0, Y=0, A=0, B=0, U=0, C=0, D=0)), (6, dict(X=1, Y=1, A=0, B=0, U=1, C=0, D=0)), (7, dict(X=0, Y=0, A=0, B=0, U=0, C=0, D=0))]:
        sp = ['X', 'Y', 'A', 'B', 'U', 'C', 'D']
        lat = Lat(L, 1, sp, tw, mass)
        res = {}
        for (go, gi) in [(1, 1), (1, 0), (0, 1)]:
            H, T = build_N(lat, go, gi)
            Ev = rs(H, ())
            for mx in lat.modes_of['X'][:3]:
                Ex = rs(H, (mx,))
                res[(go, gi, mx)] = (Ex[0] - Ev[0], Ex[2] - Ev[2], Ex[1] - Ev[1])
        H, T = build_N(lat, 1, 1)
        pr(f'## L={L} twists={tw}: |of|={len(T["of"])} |ov|={len(T["ov"])} |if|={len(T["if_"])} |iv|={len(T["iv"])}  t={time.time()-t0:.1f}s')
        for mx in lat.modes_of['X'][:3]:
            b = res[(1, 1, mx)][1] - res[(1, 0, mx)][1] - res[(0, 1, mx)][1]
            cm, one = closed_mixed(lat, T, mx)
            pr(f'   X k={lat.k[mx][0]:+.4f}: E2(1,0)={res[(1,0,mx)][0]:+.12e} (closed 1-loop {one:+.12e});  E3={res[(1,1,mx)][2]:+.1e};'
               f'  mixed RS4(H) = {b:+.15e}   closed = {cm:+.15e}   diff {b-cm:+.1e};  E4(0,1)={res[(0,1,mx)][1]:+.1e}')
    open(__file__.replace('.py', f'_{STAT[0]}.out'), 'w').write('\n'.join(OUT) + '\n')
