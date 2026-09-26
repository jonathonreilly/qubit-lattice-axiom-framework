#!/usr/bin/env python3
"""Independent check of the evolving-sea source identities.

Does not import the author's script. The adiabatic amplitude formula is the
author's assumption A1; everything else is an exact identity.
"""
import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f" :: {detail}" if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


lam, I0, l0, mu = sp.symbols("lambda I ell0 mu", positive=True)
ell = sp.exp(lam)
y = sp.symbols("y", positive=True)


def pressure(m):
    return sp.simplify(-sp.diff(m, lam) / (3 * ell**3))


m_sea = -I0 / ell
m_ct = I0 / ell
m_const = I0 / l0
check(
    "K1 equations of state",
    sp.simplify(pressure(m_sea) - (m_sea / ell**3) / 3) == 0
    and sp.simplify(pressure(m_ct) - (m_ct / ell**3) / 3) == 0
    and pressure(m_const) == 0
    and sp.simplify(m_sea + m_const - (I0 / l0 - I0 / ell)) == 0,
    "m=-I/l has p=rho/3; the counterterm +I/l does too; a constant I/l0 has p=0 and leaves I/l0-I/l",
)
em = sp.sqrt(mu**2 + y * sp.exp(-2 * lam))
ratio = sp.simplify(pressure(-em) / (-em / ell**3) - y * sp.exp(-2 * lam) / (3 * em**2))
check(
    "K2 massive ratio",
    ratio == 0,
    "p/rho = (s^2/l^2) / (3(mu^2 + s^2/l^2))",
)

# 4x4 block H = (sigma.s / l) tau_z + mu tau_x
s1, s2, s3 = sp.symbols("s1 s2 s3", real=True)
l1, l2 = sp.symbols("l1 l2", positive=True)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
A = s1 * sx + s2 * sy + s3 * sz
sabs = sp.sqrt(s1**2 + s2**2 + s3**2)


def block(length, mass):
    top = sp.eye(2) * mass
    return sp.Matrix(sp.BlockMatrix([[A / length, top], [top, -A / length]]))


comm = (block(l1, mu) * block(l2, mu) - block(l2, mu) * block(l1, mu)).applyfunc(sp.expand)
fro = sp.simplify(sp.expand((comm.H * comm).trace()))
target = sp.simplify(16 * mu**2 * (s1**2 + s2**2 + s3**2) * (l1 - l2) ** 2 / (l1**2 * l2**2))
same = sp.simplify(target - 16 * mu**2 * (s1**2 + s2**2 + s3**2) * (1 / l1 - 1 / l2) ** 2)
massless = sp.simplify(block(l1, 0) - block(1, 0) / l1)
check(
    "C1 commutator",
    sp.simplify(fro - target) == 0 and same == 0 and massless == sp.zeros(4),
    "||[H_l1,H_l2]||^2 = 16 mu^2 |s|^2 (1/l1-1/l2)^2, and mu=0 gives H_l = H_1/l",
)
ev = sorted(sp.simplify(v) for v in A.eigenvals())
check(
    "C1b sigma.s",
    ev == [-sabs, sabs],
    "sigma.s has eigenvalues ±|s|, independent of l",
)
H0 = block(ell, 0)
spec = H0.eigenvals()
neg_mult = pos_mult = 0
for val, mult in spec.items():
    if sp.simplify(val + sabs * sp.exp(-lam)) == 0:
        neg_mult += mult
    elif sp.simplify(val - sabs * sp.exp(-lam)) == 0:
        pos_mult += mult
check(
    "C1c massless sea",
    neg_mult == 2 and pos_mult == 2,
    "half filling of one block has energy -2|s|/l, hence -|s|/l per site",
)

# two-level sector h = (r/l) tau_z + mu tau_x
r = sp.symbols("r", real=True, nonzero=True)
alpha = r * sp.exp(-lam)
E = sp.sqrt(alpha**2 + mu**2)
h = sp.Matrix([[alpha, mu], [mu, -alpha]])
vm = sp.Matrix([mu, -(alpha + E)])
vp = sp.Matrix([mu, E - alpha])
nm = sp.simplify(sp.sqrt((vm.T * vm)[0]))
np_ = sp.simplify(sp.sqrt((vp.T * vp)[0]))
vm, vp = vm / nm, vp / np_
dh = sp.diff(h, lam)
elem2 = sp.simplify(sp.Abs((vp.T * dh * vm)[0]) ** 2)
want = sp.simplify(r**2 * sp.exp(-2 * lam) * mu**2 / E**2)
# differentiate the eigenvalue equation: <+|d_lambda -> = <+|d h|-> / (E_- - E_+)
berry = sp.simplify((vp.T * sp.diff(vm, lam))[0])
def entries_zero(mat):
    return all(sp.simplify(entry) == 0 for entry in sp.simplify(mat))


check(
    "A1 matrix element",
    entries_zero(h * vm + E * vm)
    and entries_zero(h * vp - E * vp)
    and sp.simplify(elem2 - want) == 0
    and sp.simplify(berry**2 - elem2 / (2 * E) ** 2) == 0,
    "|<+|d_lambda h|->|^2 = mu^2 r^2/(l^2 E^2), and |<+|d_lambda ->| = that over 2E",
)

lamdot = sp.symbols("lamdot", real=True)
# assumed adiabatic formula: c_+ = i lamdot <+|d_lambda -> / (2E)
c2 = sp.simplify((lamdot * berry / (2 * E)) ** 2)
excess = sp.simplify(2 * E * c2)
m_sector = sp.simplify(2 * elem2 / (2 * E) ** 3)
check(
    "M1 dressing algebra",
    sp.simplify(excess - m_sector * lamdot**2 / 2) == 0
    and sp.simplify(m_sector - mu**2 * r**2 * sp.exp(-2 * lam) / (4 * E**5)) == 0,
    "under c = i lamdot <+|d_lambda ->/(2E), the excess is (1/2) m lamdot^2 with m = mu^2 r^2/(4 l^2 E^5)",
)
S2 = sp.symbols("S2", positive=True)
Eb = sp.sqrt(mu**2 + S2)
per_site = sp.Rational(1, 2) * 2 * (mu**2 * S2 / (4 * Eb**5))
quoted = mu**2 * S2 / (16 * Eb**5)
check(
    "M2 per site",
    sp.simplify(per_site - mu**2 * S2 / (4 * Eb**5)) == 0
    and sp.simplify(per_site - 4 * quoted) == 0,
    "two sectors and half a block per site give m_lambda = <mu^2 |s|^2/(4 E^5)> at l=1, which is 4 times mu^2|s|^2/(16 E^5)",
)

t = sp.symbols("t")
L = sp.Function("lam")(t)
mf, ef, cf, Vf = (sp.Function(name) for name in ("m", "e", "c", "V"))
Ld = sp.diff(L, t)
Lag = sp.Rational(1, 2) * (mf(L) + cf(L)) * Ld**2 - ef(L) - Vf(L)
EL = sp.diff(sp.diff(Lag, Ld), t) - sp.diff(Lag, L)
energy = Ld * sp.diff(Lag, Ld) - Lag
check(
    "N1 Noether",
    sp.simplify(sp.diff(energy, t) - Ld * EL) == 0
    and sp.simplify(energy - (ef(L) + Vf(L) + sp.Rational(1, 2) * (mf(L) + cf(L)) * Ld**2)) == 0,
    "d/dt of e+V+(1/2)(m+c) lamdot^2 equals lamdot times the Euler-Lagrange expression",
)

def fully_blocked(length):
    full = (1,) * length
    for x in range(length):
        for a, b in ((x, (x + 1) % length), ((x + 1) % length, x)):
            if full[a] == 0 and full[b] == 1:
                return False
    return True


check(
    "H1 hard core",
    all(fully_blocked(n) for n in range(1, 8)),
    "on a fully occupied ring every hop targets an occupied site, so the hopping annihilates the state",
)

print(f"TOTAL FAIL={len(FAIL)}", flush=True)
if FAIL:
    print("SUMMARY: fails at " + ", ".join(FAIL), flush=True)
else:
    print(
        "SUMMARY: PARTIAL on a uniformly stretched lattice with dm/dlam = -3 p l^3. "
        "Massless: H_l = H_1/l, half-filled block energy -2|s|/l, p=rho/3 for m=-I/l, "
        "and the subtraction that cancels it at every length is +I/l. A time-constant I/l0 leaves I/l0-I/l. "
        "Massive: ||[H_l1,H_l2]||^2 = 16 mu^2 |s|^2 (1/l1-1/l2)^2, and the ground state of a sector "
        "has a nonzero first time derivative of the excited amplitude whenever mu|s| lamdot != 0. "
        "The leading adiabatic dressing (1/2) m lamdot^2 with m = mu^2 r^2/(4 l^2 E^5) per sector "
        "uses the assumed formula c = i lamdot <+|d_lambda ->/(2E). "
        "Fully occupied hard-core hopping is blocked. Irreversible pair creation was not treated.",
        flush=True,
    )
    print(
        "HIT: confirmed - without the staggered mass the free sea keeps its occupations for every history "
        "and its energy is -|s|/l per site with p=rho/3; cancelling that at every length takes the counterterm +I/l, "
        "while a subtraction frozen at one length leaves I/l0-I/l. "
        "With the staggered mass the blocks at two lengths fail to commute by 16 mu^2 |s|^2 (1/l1-1/l2)^2, "
        "and a sea started in the instantaneous ground state is excited at order tau wherever mu|s| lamdot != 0. "
        "Granting the first adiabatic correction, the excess energy is (1/2) m_lambda lamdot^2 per site "
        "with m_lambda = <mu^2 |s|^2/(4 l^2 E^5)>, and that term plus the member conserves its Noether energy.",
        flush=True,
    )
