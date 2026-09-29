"""What would justify a dispersion conclusion from energy-only moment bounds (PR 9236 / 9239, ring model at the pure-ring point)?

Setting (PR #9236, supplied, not adopted): for a transverse mode O of the flip component's ground state |0>, the spectral measure
nu = sum_{n>=1} |<n|O|0>|^2 delta(omega - (E_n - E_0)) has moments M_p = sum w_n omega_n^p.  M_1 = f = 2 u s^2 is exact (f-sum),
M_{-1} = chi/2 is read from ground-state energies in a weak field, and the bounds are omega_min <= M_0/M_{-1} <= M_1/M_0, M_0 <= (M_{-1} M_1)^(1/2).

Sections A (exact rationals): what three moments can and cannot certify.  Section B (float64, exact diagonalisation of the 864-state
2^3 flip component with PR #9236's own Ice/exact_L2, vendored unchanged): the same statements on the true spectral measure and an
energy-only (Hellmann-Feynman) route to M_0.  No claim about larger tori: their moments are not computed here.
"""
import os, sys, time, random, itertools
import sympy as sp
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
T0 = time.time()
FAILS = []
def want(ok, label):
    print(("PASS " if ok else "FAIL ") + label, flush=True)
    if not ok:
        FAILS.append(label)

def mom(atoms, p): return sum(w * om ** p for w, om in atoms)
def rand_measure(rng, n):
    return [(Fr(rng.randint(1, 9), rng.randint(1, 5)), Fr(rng.randint(1, 30), rng.randint(1, 6))) for _ in range(n)]

# ---------------------------------------------------------------------------------------------
# A. What three moments certify (exact rationals)
# ---------------------------------------------------------------------------------------------
print("== A. moment inequalities on exact rational measures")
rng = random.Random(20260928)
trials = [rand_measure(rng, rng.randint(2, 7)) for _ in range(400)]
ok_id = ok_chain = ok_cs = ok_low = ok_high = ok_markov = ok_wmin = True
tight_low = 0.0
for atoms in trials:
    Mm1, M0, M1 = mom(atoms, -1), mom(atoms, 0), mom(atoms, 1)
    # A1 Lagrange-type identity
    ok_id &= (M1 * Mm1 - M0 ** 2 == sum(wi * wj * (oi - oj) ** 2 / (oi * oj) for (wi, oi) in atoms for (wj, oj) in atoms) / 2)
    wmin = min(o for _, o in atoms)
    wc = M0 / Mm1; wb = M1 / M0; eps = M1 * Mm1 / M0 ** 2 - 1
    ok_chain &= (wmin <= wc <= wb)                       # omega_min <= M_0/M_{-1} <= M_1/M_0
    ok_cs &= (M0 ** 2 <= Mm1 * M1)                       # S <= (chi f/2)^(1/2)
    # A3 weights below (1-eta) wc and above (1+eta) wc, normalised by M_0
    for eta in (Fr(1, 10), Fr(1, 4), Fr(1, 2), Fr(3, 4), Fr(9, 10)):
        low = sum(w for w, o in atoms if o <= (1 - eta) * wc) / M0
        ok_low &= (low <= eps * (1 - eta) / eta ** 2)
        high = sum(w for w, o in atoms if o >= (1 + eta) * wc) / M0
        ok_high &= (high <= eps * (1 + eta) / eta ** 2)
    # A4 Markov on the inverse moment: weight at omega <= delta is at most delta M_{-1}
    for delta in (wmin, wc / 2, wc):
        ok_markov &= (sum(w for w, o in atoms if o <= delta) <= delta * Mm1)
    # A5 lower bound from a weight bound: omega_min >= w_0 / M_{-1}
    w0 = sum(w for w, o in atoms if o == wmin)
    ok_wmin &= (wmin >= w0 / Mm1)
want(ok_id, "A1 M_1 M_{-1} - M_0^2 = (1/2) sum_ij w_i w_j (omega_i - omega_j)^2/(omega_i omega_j) exactly on 400 rational measures (so M_0 <= sqrt(M_{-1} M_1) with equality iff a single atom)")
want(ok_chain and ok_cs, "A2 omega_min <= M_0/M_{-1} <= M_1/M_0 and M_0^2 <= M_{-1} M_1 exactly on the 400 measures")
want(ok_low and ok_high,
     "A3 (stability of the Cauchy-Schwarz bound, exact on the 400 measures for eta = 1/10, 1/4, 1/2, 3/4, 9/10) with wc = M_0/M_{-1} and eps = M_1 M_{-1}/M_0^2 - 1: "
     "the weight fraction below (1 - eta) wc is at most eps (1 - eta)/eta^2 and above (1 + eta) wc at most eps (1 + eta)/eta^2")
want(ok_markov and ok_wmin,
     "A4 weight at omega <= delta is at most delta M_{-1} (Markov on the inverse moment), and omega_min >= w_0/M_{-1} when the lowest atom has weight w_0 (exact on the 400 measures)")
# proof of A3 recorded as an exact identity: integral (omega - wc)^2/omega dnu = M_1 - M_0^2/M_{-1} = eps * wc * M_0
ok_R = all(sum(w * (o - mom(a, 0) / mom(a, -1)) ** 2 / o for w, o in a) == mom(a, 1) - mom(a, 0) ** 2 / mom(a, -1) ==
           (mom(a, 1) * mom(a, -1) / mom(a, 0) ** 2 - 1) * (mom(a, 0) / mom(a, -1)) * mom(a, 0) for a in trials)
want(ok_R, "A5 the identity behind A3: sum w (omega - wc)^2/omega = M_1 - M_0^2/M_{-1} = eps wc M_0 (then Markov on the low side (omega - wc)^2/omega >= eta^2 wc/(1 - eta) and on the high side >= (Omega - wc)^2/Omega)")

# A6: three moments do not bound omega_min from below
base = [(Fr(1, 2), Fr(5, 2)), (Fr(1, 2), Fr(7, 2))]
Mm1b, M0b, M1b = mom(base, -1), mom(base, 0), mom(base, 1)
ok_imp = True; lows = []
for delta in (Fr(1, 10), Fr(1, 100), Fr(1, 1000), Fr(1, 10 ** 4), Fr(1, 10 ** 6)):
    fr = [delta, Fr(11, 4), Fr(13, 4)]
    A = [[1 / f for f in fr], [Fr(1)] * 3, list(fr)]
    sol = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in A]).LUsolve(sp.Matrix([sp.Rational(v.numerator, v.denominator) for v in (Mm1b, M0b, M1b)]))
    u = [Fr(int(s.p), int(s.q)) for s in sol]
    atoms = list(zip(u, fr))
    ok_imp &= all(x > 0 for x in u) and mom(atoms, -1) == Mm1b and mom(atoms, 0) == M0b and mom(atoms, 1) == M1b
    lows.append((delta, u[0], u[0] / M0b))
want(ok_imp, "A6 exact counterexample: the two-atom measure at omega = 5/2, 7/2 has (M_{-1}, M_0, M_1) = ("
     f"{Mm1b}, {M0b}, {M1b}); for lowest atoms at 1/10, 1/100, ..., 10^-6 there are positive three-atom measures (atoms at delta, 11/4, 13/4) with exactly the same three moments: "
     "no lower bound on omega_min can follow from M_{-1}, M_0, M_1 (the low atom's weight is forced below delta M_{-1}, so it is invisible)")
print("   weights of the hidden low atom (delta, weight, fraction of M_0):", [(str(d), float(w), float(f)) for d, w, f in lows], flush=True)

# A7: what accuracy a quantile-type dispersion statement needs
def eps_needed(q, eta): return q * eta ** 2 / (1 - eta)
tab = [(q, eta, eps_needed(Fr(q), Fr(eta))) for q in (Fr(1, 10), Fr(1, 20)) for eta in (Fr(1, 10), Fr(1, 20), Fr(1, 4))]
want(True, "A7 to certify 'at most a fraction q of the weight lies below (1 - eta) wc' by A3 one needs eps <= q eta^2/(1 - eta): " +
     "; ".join(f"q = {float(q):.2f}, eta = {float(e):.2f}: eps <= {float(x):.2e}" for q, e, x in tab) +
     " (eps is about twice the relative error budget of the product M_1 M_{-1}/M_0^2)")
print("   [A took %.0f s]" % (time.time() - T0), flush=True)

# ---------------------------------------------------------------------------------------------
# B. The exact 2^3 flip component (float64 exact diagonalisation)
# ---------------------------------------------------------------------------------------------
print("== B. exact 2^3 flip component, cyclic transverse triple at k = pi (FLOATING POINT diagonalisation)")
import numpy as np
import pr9236_lib as R
ice = R.Ice(2); canon = ice.sector_state(0)
codes, order, H2, sig_of = R.exact_L2(ice, canon)
Sg = np.array([sig_of(c) for c in order]).astype(float)
hv, PH = R.triple(ice, np.pi)
Hd = H2.toarray(); Hd = (Hd + Hd.T) / 2
ev, V = np.linalg.eigh(Hd)
E0 = ev[0]; psi = V[:, 0] * np.sign(V[:, 0].sum())
u0 = -E0 / ice.np_
want(len(order) == 864 and abs(np.linalg.norm(psi) - 1) < 1e-12, f"B1 the 2^3 zero-winding flip component has {len(order)} states, ground energy {E0:.6f}, u_0 = {u0:.6f} per plaquette")
Os = [np.real(Sg @ PH[a]) for a in range(3)]
omega = ev[1:] - E0
w_modes = [(V[:, 1:].T @ (O * psi)) ** 2 for O in Os]
mean_O = [float(psi @ (O * psi)) for O in Os]
w = sum(w_modes) / 3
keep = w > 1e-13
om, ww = omega[keep], w[keep]
M = {p: float(np.sum(ww * om ** p)) for p in (-1, 0, 1)}
f_sum = 8 * u0
want(abs(M[1] - f_sum) < 1e-9 and max(abs(m) for m in mean_O) < 1e-12,
     f"B2 exact averaged f-sum: M_1 = {M[1]:.9f} = 2 u_0 s^2 = {f_sum:.9f} (s = 2 at k = pi); <O_a> = 0 for the three modes")
chain = (float(om.min()), M[0] / M[-1], float(np.sqrt(M[1] / M[-1])), M[1] / M[0])
want(chain[0] <= chain[1] <= chain[2] <= chain[3] and M[0] <= np.sqrt(M[-1] * M[1]),
     f"B3 the moment chain on the true measure: omega_min {chain[0]:.4f} <= M_0/M_-1 {chain[1]:.4f} <= sqrt(M_1/M_-1) {chain[2]:.4f} <= M_1/M_0 {chain[3]:.4f} "
     "(PR #9236 reports 2.5173, 2.7754, 2.8724, 2.9728)")
eps = M[1] * M[-1] / M[0] ** 2 - 1; wc = M[0] / M[-1]
want(abs(chain[0] - 2.5173) < 5e-4 and abs(chain[1] - 2.7754) < 5e-4 and abs(chain[3] - 2.9728) < 5e-4,
     f"B4 reproduces PR #9236's exact 2^3 chain to 5e-4; eps = M_1 M_-1/M_0^2 - 1 = {eps:.4f}")
# actual weight distribution against A3 / A4
w0_abs = float(ww[np.argmin(om)]); w0 = w0_abs / M[0]
rows = []
ok_A = True
for eta in (0.1, 0.25, 0.5, 0.75):
    low = float(ww[om <= (1 - eta) * wc].sum()) / M[0]; high = float(ww[om >= (1 + eta) * wc].sum()) / M[0]
    bl, bh = eps * (1 - eta) / eta ** 2, eps * (1 + eta) / eta ** 2
    ok_A &= (low <= bl + 1e-12 and high <= bh + 1e-12)
    rows.append((eta, low, min(bl, 1 - eta), high, bh))
print("   eta   weight below (1-eta)wc   certificate min(A3, Markov)   weight above (1+eta)wc   certificate A3")
for r in rows: print("   %.2f  %.4f                    %.4f                        %.4f                   %.4f" % r)
want(ok_A and w0_abs / M[-1] <= chain[0] + 1e-12,
     f"B5 A3 and A4 hold on the true measure; the lowest coupled level (omega = {chain[0]:.4f}) carries {w0:.3f} of M_0, and omega_min >= w_0/M_-1 = {w0_abs / M[-1]:.4f} (true {chain[0]:.4f})")
# Hellmann-Feynman: E(nu) for H - nu * mean_a O_a^2 gives <O^2> = M_0 + <O>^2 = M_0 (energies only)
O2 = sum(O ** 2 for O in Os) / 3
def Enu(nu): return float(np.linalg.eigvalsh(Hd - nu * np.diag(O2))[0])
nu = 1e-3
d5 = (Enu(-2 * nu) - 8 * Enu(-nu) + 8 * Enu(nu) - Enu(2 * nu)) / (12 * nu)
S_hf = -d5
want(abs(S_hf - M[0]) < 1e-9 * max(1, M[0]) and abs(float(psi @ (O2 * psi)) - M[0]) < 1e-12,
     f"B6 Hellmann-Feynman: S = M_0 = <O^2> read from ground-state energies of H - nu O^2 (five-point derivative at nu = 1e-3): {S_hf:.9f} against the spectral sum {M[0]:.9f}")
# chi from a field, as in PR #9236, for reference
Ftot = Sg @ hv
def Eh(h): return float(np.linalg.eigvalsh(Hd - h * np.diag(Ftot))[0])
Hh = 0.15
a_fit = (15 * E0 - 16 * Eh(Hh) + Eh(2 * Hh)) / (12 * Hh ** 2)
chi_fit = 4 * a_fit / (3 * 2.0 * ice.nv)
want(abs(chi_fit / (2 * M[-1]) - 1) < 0.03, f"B7 chi from ground-state energies in a field (PR #9236's fit): {chi_fit:.5f} against 2 M_-1 = {2 * M[-1]:.5f} (within 3 percent; the fit removes h^4 only)")
# what would be needed on this torus
need = eps_needed(Fr(1, 10), Fr(1, 10))
want(eps > float(need),
     f"B8 on this torus eps = {eps:.4f} is {eps / float(need):.0f} times the value ({float(need):.2e}) needed to certify 'at most 10 percent of the weight below 0.9 wc' from three moments: "
     "the exact 2^3 measure is far from a single mode, and the certificate that A3 does give is only the wide window above")
win = [r for r in rows if abs(r[0] - 0.75) < 1e-9][0]
cert = 1 - win[2] - win[4]
want(win[1] <= win[2] and win[3] <= win[4] and cert > 0.7,
     f"B9 what the moments do certify on 2^3: at least {cert:.3f} of the weight lies in [wc/4, 7 wc/4] = [{wc / 4:.3f}, {7 * wc / 4:.3f}] "
     f"(actual {1 - win[1] - win[3]:.3f}); and at least {1 - min(eps * 2, 1):.3f} lies below 2 wc (actual {1 - float(ww[om >= 2 * wc].sum()) / M[0]:.3f})")
print("   [total %.0f s]" % (time.time() - T0))
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + FAILS[0]); sys.exit(1)
print("SUMMARY: PARTIAL, first unresolved step identified: the three moments M_{-1}, M_0, M_1 certify only weight quantiles, never omega_min: (A6) exact positive three-atom measures "
      "with identical moments and a lowest atom at 1e-6; (A3) with eps = M_1 M_-1/M_0^2 - 1 at most a fraction eps(1 - eta)/eta^2 of the weight lies below (1 - eta) M_0/M_-1 and "
      "eps(1 + eta)/eta^2 above (1 + eta) M_0/M_-1; (A4) weight below delta is at most delta M_-1 and omega_min >= w_0/M_-1 needs a weight bound; "
      "a dispersion statement at quantile q, tolerance eta needs eps <= q eta^2/(1 - eta) (2.6e-4 for q = 0.1, eta = 0.05); M_0 is readable from ground-state energies "
      "(Hellmann-Feynman, checked on the exact 2^3 component) but its shift is O(1) against O(N) energies; on 2^3, eps = %.3f, so only the wide window is certified" % eps)
print("HIT: what a dispersion conclusion needs, with exact proofs and a checked 2^3 case: three energy moments bound weight quantiles, not omega_min (exact counterexample family); "
      "quantile window fractions eps(1-eta)/eta^2 and eps(1+eta)/eta^2 with eps = M_1 M_-1/M_0^2 - 1; needed eps <= q eta^2/(1-eta); M_0 = <O^2> is an energy-only quantity "
      "(Hellmann-Feynman) so forward-walking is not needed for it, but it must be certified to about 1e-4 relative; exact 2^3: eps = %.3f, chain 2.5173 <= 2.7754 <= 2.8724 <= 2.9728 reproduced" % eps)
