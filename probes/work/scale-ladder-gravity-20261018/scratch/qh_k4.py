import sys, numpy as np
sys.path.insert(0, '/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/scripts')
import scale_ladder_gravity_regge_metric_universality_common_cone_2026_10_18 as R
Qe, Mh = R.regge(np.eye(4)); HC = R.HC
def Qh(k): return Mh(-k).T @ Qe(k) @ Mh(k)
vec = lambda h: np.array([h[x, y] for (x, y) in HC])
for name, n in {'axis': (1,0,0), 'face': (1,1,0), 'body': (1,1,1)}.items():
    n = np.array(n, float); n /= np.linalg.norm(n); law = -(1+(n**4).sum())/12
    a = np.cross(n, [0.3, 0.5, 0.7]); a /= np.linalg.norm(a); b = np.cross(n, a)
    e1, e2 = np.array([*a, 0]), np.array([*b, 0])
    Et = np.array([vec(np.outer(e1, e1)-np.outer(e2, e2)), vec(np.outer(e1, e2)+np.outer(e2, e1))]).T
    al = []
    for k in (0.02, 0.01):
        p = np.array([*(k*n), 1j*k]); al.append(np.sort(np.linalg.eigvals(Et.T @ Qh(p) @ Et).real)/(-0.5*k**4))
    r = (4*al[1]-al[0])/3
    # on-lattice-shell test for Q_h: nullity at Hodge shell
    ks = 0.8*n; p = np.array([*ks, R.lattice_kt(ks)]); s = R.sv(Qh(p))
    print(f"{name}: Q_h TT k^4 first-order {r[0]:+.5f} {r[1]:+.5f} (full-form law {law:+.5f}); Q_h on Hodge shell sv4..6 " + " ".join(f"{x:.1e}" for x in s[3:6]))
