"""Exact Gaussian-integer engine for n records of block 54's walk on Z^d (distinguishable tensor space).
H' = 2H, D' = 4 D_a (so every coefficient is a Gaussian integer).  [H,[H,D]] = (1/16)[H',[H',D']]."""
from itertools import product

SIG = {
    0: {(0, 1): (1, 0), (1, 0): (1, 0)},          # sigma_x : entry (c', c)
    1: {(0, 1): (0, -1), (1, 0): (0, 1)},         # sigma_y
    2: {(0, 0): (1, 0), (1, 1): (-1, 0)},         # sigma_z
}


def gmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def gadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def vadd(v, k, a):
    cur = v.get(k)
    if cur is None:
        if a != (0, 0):
            v[k] = a
    else:
        n = (cur[0] + a[0], cur[1] + a[1])
        if n == (0, 0):
            del v[k]
        else:
            v[k] = n


def vscale(v, a):
    out = {}
    for k, x in v.items():
        y = gmul(x, a)
        if y != (0, 0):
            out[k] = y
    return out


def vsum(*vs):
    out = {}
    for v in vs:
        for k, x in v.items():
            vadd(out, k, x)
    return out


class Walk:
    """records: tuple of (pos tuple, coin).  excl = set of record-index pairs forbidden to coincide in position."""

    def __init__(self, dim, nrec, excl_pairs):
        self.dim, self.nrec = dim, nrec
        self.excl = [tuple(p) for p in excl_pairs]

    def allowed(self, st):
        for (i, j) in self.excl:
            if st[i][0] == st[j][0]:
                return False
        return True

    def proj(self, v):
        return {k: a for k, a in v.items() if self.allowed(k)}

    def hop_amp(self, a, sg):
        # coefficient of |x + sg e_a><x| in H' = 2H :  sg * i * sigma_a
        return (0, sg)

    def apply(self, v, which, comp=0):
        """which = 'H' (H' = 2 sum_records h) or 'D' (D'_comp = 4 D_comp = sum_records (x_t+x_s)_comp * 2h hop)"""
        out = {}
        for st, a in v.items():
            for r in range(self.nrec):
                x, c = st[r]
                for ax in range(self.dim):
                    for sg in (1, -1):
                        y = list(x)
                        y[ax] += sg
                        y = tuple(y)
                        for (c2, c1), val in SIG[ax].items():
                            if c1 != c:
                                continue
                            amp = gmul((0, sg), val)
                            if which == 'D':
                                w = x[comp] + y[comp]
                                amp = (amp[0] * w, amp[1] * w)
                                if w == 0:
                                    continue
                            nst = st[:r] + ((y, c2),) + st[r + 1:]
                            vadd(out, nst, gmul(a, amp))
        return out

    def Hc(self, v):
        return self.proj(self.apply(self.proj(v), 'H'))

    def Dc(self, v, comp=0):
        return self.proj(self.apply(self.proj(v), 'D', comp))

    # nested commutators of the scaled operators
    def comm_HD(self, v, comp=0):          # [H',D'] v
        return vsum(self.Hc(self.Dc(v, comp)), vscale(self.Dc(self.Hc(v), comp), (-1, 0)))

    def J8(self, v, comp=0):               # J = (i/8) J8,  J8 = [H',D']
        return self.comm_HD(v, comp)

    def O16(self, v, comp=0):              # [H, J] = (i/16) O16 with O16 = [H',[H',D']] = [H', J8]
        return vsum(self.Hc(self.J8(v, comp)), vscale(self.J8(self.Hc(v), comp), (-1, 0)))


def nz(v):
    return len(v) > 0
