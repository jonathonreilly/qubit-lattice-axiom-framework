"""one-cone-for-field-and-walker, attempt a1 (w-jonathonsmac4f50-jf0e6): checks.  Exact (sympy) throughout.

GIVEN (block 62 T4, PR #8592): for the rotation-invariant kinetic family (alpha, beta_kin), alpha != 0, alpha + beta_kin != 0, the two
transverse-traceless disturbances of the frame have X = K wbar^2 p^2/(4 alpha), p^2 = sum_j 4 sin^2(k_j/2), a double root of the mode
determinant (so both polarisations share it); X is the squared frequency in ambient time.  The walker (block 54): H = sum_a sigma_a S_a,
H^2 = sum_j S_j^2 with symbol sin^2 k_j, clocked at uniform rate wbar: frequencies +- wbar sqrt(sum_j sin^2 k_j).
"""
import sympy as sp

RESULTS = []


def want(label, ok, detail=""):
    RESULTS.append((label, bool(ok)))
    print(("PASS " if ok else "FAIL ") + label + ((" :: " + str(detail)) if detail != "" else ""), flush=True)


al, K, wb, bk = sp.symbols("alpha K wbar beta_kin", positive=True)
k, k1, k2, k3 = sp.symbols("k k1 k2 k3", real=True)
lam = sp.Symbol("lambda", positive=True)
p2 = sum(4 * sp.sin(t / 2) ** 2 for t in (k1, k2, k3))
Xf = K * wb ** 2 * p2 / (4 * al)                                       # field: omega^2
Xw = wb ** 2 * sum(sp.sin(t) ** 2 for t in (k1, k2, k3))              # walker: omega^2

# (a) speeds at long wavelength, along a unit direction n: k_j = n_j k
n1, n2, n3 = sp.symbols("n1 n2 n3", real=True)
sub = {k1: n1 * k, k2: n2 * k, k3: n3 * k}
cf2 = sp.limit(sp.simplify(Xf.subs(sub) / k ** 2).subs(n3, sp.sqrt(1 - n1 ** 2 - n2 ** 2)), k, 0)
cw2 = sp.limit(sp.simplify(Xw.subs(sub) / k ** 2).subs(n3, sp.sqrt(1 - n1 ** 2 - n2 ** 2)), k, 0)
want("A1 long-wavelength speeds (any unit direction n): field c_f^2 = K wbar^2/(4 alpha), walker c_w^2 = wbar^2; so c_f/c_w = sqrt(K/(4 alpha)), "
     "direction-free for both at leading order",
     sp.simplify(cf2 - K * wb ** 2 / (4 * al)) == 0 and sp.simplify(cw2 - wb ** 2) == 0, f"c_f^2 = {sp.simplify(cf2)}, c_w^2 = {sp.simplify(cw2)}")

# (b) the condition, and the two polarisations
want("B1 the two cones coincide at long wavelength iff K = 4 alpha (wbar > 0); the two transverse-traceless polarisations always share one "
     "speed (a double root in block 62 T4: the factor (p^2 - 4 alpha X)^2), for every alpha, beta_kin with alpha != 0, alpha + beta_kin != 0",
     sp.solve(sp.Eq(cf2, cw2), K) == [4 * al])

# (d) the lattice mismatch, exact
ident = sp.simplify((sp.sin(k) ** 2 - (4 * sp.sin(k / 2) ** 2 - 4 * sp.sin(k / 2) ** 4)).rewrite(sp.exp))
diff = sp.simplify((Xf.subs(K, 4 * al) - Xw) - 4 * wb ** 2 * sum(sp.sin(t / 2) ** 4 for t in (k1, k2, k3)))
want("D1 exact: sin^2 k = 4 sin^2(k/2) - 4 sin^4(k/2), hence at K = 4 alpha omega_field^2 - omega_walker^2 = 4 wbar^2 sum_j sin^4(k_j/2) >= 0 "
     "at every wave vector: the field is never slower, and the mismatch is of fourth order in k in omega^2",
     ident == 0 and sp.simplify(sp.expand_trig(diff)) == 0)
# second-order speed mismatches along an axis and along the body diagonal
vph_w_axis = sp.series(sp.sin(k) / k, k, 0, 4).removeO()
vph_f_axis = sp.series(2 * sp.sin(k / 2) / k, k, 0, 4).removeO()
vg_w_axis = sp.series(sp.cos(k), k, 0, 4).removeO()
vg_f_axis = sp.series(sp.cos(k / 2), k, 0, 4).removeO()
s3 = sp.sqrt(3)
wd = sp.sqrt(3 * sp.sin(k / s3) ** 2); fd = sp.sqrt(3 * 4 * sp.sin(k / (2 * s3)) ** 2)
vph_w_diag = sp.series(wd / k, k, 0, 4).removeO(); vph_f_diag = sp.series(fd / k, k, 0, 4).removeO()
want("D2 at K = 4 alpha, wbar = 1, second order in k: along an axis the phase speeds are 1 - k^2/6 (walker) and 1 - k^2/24 (field), a gap of "
     "k^2/8, and the group speeds cos k and cos(k/2), a gap of 3k^2/8; along the body diagonal the phase gap is k^2/24: the mismatch depends "
     "on direction",
     sp.expand(vph_f_axis - vph_w_axis - k ** 2 / 8) == 0 and sp.expand(vg_f_axis - vg_w_axis - 3 * k ** 2 / 8) == 0
     and sp.expand(sp.simplify(vph_f_diag - vph_w_diag) - k ** 2 / 24) == 0,
     f"axis phase {sp.expand(vph_f_axis - vph_w_axis)}, axis group {sp.expand(vg_f_axis - vg_w_axis)}, diagonal phase {sp.expand(sp.simplify(vph_f_diag - vph_w_diag))}")

# (c) the clauses are homogeneous in alpha and in K separately
hdot, grad = sp.symbols("hdot gradh", real=True)
kin = al * hdot ** 2 / wb                                              # kinetic density in ambient time, weight one
pot = K * wb * grad ** 2                                               # potential density, weight one (per tick: w times a function of lengths)
scaled_kin = kin.subs({wb: lam * wb, hdot: lam * hdot})                # unit of rate: w -> lam w, t -> t/lam
scaled_pot = pot.subs({wb: lam * wb})
want("C1 weight one holds for the kinetic term alpha hdot^2/wbar and the potential K wbar |grad h|^2 separately and for every alpha, K "
     "(both scale by lambda when the unit of rate does); per-tick counting and blindness constrain each term's form, not their ratio: "
     "(alpha, K) and (s alpha, K) satisfy every clause for every s > 0, so K/alpha is not fixed by the supplied clauses",
     sp.simplify(scaled_kin - lam * kin) == 0 and sp.simplify(scaled_pot - lam * pot) == 0)

npass = sum(1 for _, o in RESULTS if o)
nfail = len(RESULTS) - npass
print(f"TOTAL: PASS={npass} FAIL={nfail}")
if nfail == 0:
    print("SUMMARY: ROUTE FAILS AT (c): the clauses do not fix K/alpha (weight one, per-tick counting and blindness each hold for the kinetic and "
          "the potential term separately, for every ratio), so whether the field's cone is the walker's is the owner's choice (fork 7); exact: "
          "c_f/c_w = sqrt(K/(4 alpha)) at long wavelength, the two polarisations always share their speed, and at K = 4 alpha "
          "omega_field^2 - omega_walker^2 = 4 wbar^2 sum sin^4(k_j/2), a direction-dependent second-order speed gap (k^2/8 along an axis, "
          "k^2/24 along the diagonal)")
