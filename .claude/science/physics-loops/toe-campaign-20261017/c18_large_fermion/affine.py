"""Affine action of the site rotations on crystal momentum, from the PSG:
M(R) M(T_a) M(R)^-1 = eps(R,a) M(T_{Ra}) => R maps momentum k to R k + pi * s_R (mod 2pi)."""
import sys, itertools, numpy as np
sys.argv=['x','4']
import corner_psg as C
from sg import comp, inv, tm, rotm
nV=len(C.VERTS)
def rel_sign(ops):
    perm,sign=comp(ops); assert (perm==np.arange(nV)).all(); v=set(sign.tolist()); assert len(v)==1
    return 1 if v.pop() else 0
E3=[(1,0,0),(0,1,0),(0,0,1)]
for Fb in itertools.product((0,1),repeat=4):
    F=dict(zip(('square','triangle','plaquette','tube'),Fb)); u=C.solve_u(F)
    T={a: C.psg_sign(tm(a),u) for a in E3}
    def Tm(v):  # translation by integer vector v (product of unit ones)
        ops=[]
        for a,n in zip(E3,v):
            g=T[a] if n>0 else inv(*T[a])
            ops += [g]*abs(n)
        return ops
    shifts=[]; ok=True
    for R in C.ROTS:
        MR=C.psg_sign(rotm(R),u)
        s=np.zeros(3,int)
        # R T_a R^-1 = eps * T_{Ra}: eps = sign of  R T_a R^-1 T_{Ra}^-1
        for i,a in enumerate(E3):
            Ra=tuple(int(x) for x in R@np.array(a))
            ops=[MR, T[a], inv(*MR)] + [inv(*g) for g in reversed(Tm(Ra))][::-1]
            # careful ordering: product R T_a R^-1 (T_Ra)^-1 ; comp applies right-to-left
            eps=rel_sign([MR, T[a], inv(*MR)] + [ (inv(*g)) for g in Tm(Ra)][::-1])
            # T_{Ra} eigenvalue of R psi: e^{i k.a} eps  => component along Ra gets +pi*eps
            s += eps*np.abs(np.array(Ra))
        shifts.append(s%2)
    # fixed momenta: R k + pi s_R = k mod 2pi, search k in (pi/2) Z^3
    fixed=[]
    for k in itertools.product(range(4),repeat=3):  # units of pi/2
        kk=np.array(k)
        if all(((R@kk + 2*s - kk) % 4 == 0).all() for R,s in zip(C.ROTS,shifts)): fixed.append(tuple(kk))
    # orbit sizes of the affine action on (pi/2)Z^3/4
    orbs=set()
    for k in itertools.product(range(4),repeat=3):
        o=frozenset(tuple(((R@np.array(k)+2*s)%4)) for R,s in zip(C.ROTS,shifts)); orbs.add(o)
    print({k:('pi' if v else '0') for k,v in F.items()}, 'O-fixed momenta (units pi/2):', fixed, ' orbit sizes:', sorted(len(o) for o in orbs))
