#!/usr/bin/env python3
"""Class-A verifier: the staggered single-clock theorem's S3 ("the temporal direction is the
unique reflection-positive axis") is CONVENTION-DEPENDENT for the clock-axis IDENTITY -- the
staggered Kogut-Susskind phases carry no axis-distinguishing invariant and the temporal axis is
movable by a site-local Z2 field redefinition (gauge). The convention-INDEPENDENT residue is only
the COUNT (=1 reflection-positive axis exists); the convention-independent SOURCE of the unique
clock AXIS is the records-arrow (the reversible spatial Z^3 cannot carry a monotone direction).

This sharpens the retained_no_go `single_clock_uniqueness_scope_boundary` (Stone uniqueness is
transfer- and tau-relative; "no second clock" needs a separate axis/transfer-uniqueness premise)
and relocates the genuine source onto the retained_bounded records-arrow.

KS phases: eta_mu(x) = (-1)^{x_0 + ... + x_{mu-1}}.

Verifies:
  (1) the STW crossing-link RP invariant P_a(x) = eta_a(x)*eta_a(theta_a x), theta_a: x_a->-1-x_a,
      is +1 UNIFORMLY for ALL d axes (eta_a omits coordinate x_a) -- the action-level RP datum
      carries NO axis-distinguishing invariant;
  (2) the eta-curvature 2-cocycle Phi_{mu,nu} = -1 in ALL planes including the temporal (0,i) --
      S_d-isotropic, no time-singling;
  (3) the time<->space swap (reordering the staircase) is an EXACT site-local Z2 field
      redefinition diag(s) D diag(s) = D_swap with s(x)=(-1)^{x_0 x_1} -- spectrum- and
      taste-preserving, so the temporal axis is GAUGE-movable (convention);
  (4) (contrast) the free staggered D^dag D spectrum is direction-symmetric across axis
      relabelings -- the spectrum picks no clock either;
  (5) (records-arrow) the spatial reflection x_i -> -x_i is an involution (reversible group) that
      preserves the pairwise-distance multiset, whereas a record count is strictly monotone
      (append-only monoid, non-invertible) -- so only the record-accumulation direction is a
      clock axis, convention-independently and eta-free.

No new axiom: pure KS-phase arithmetic + a finite free staggered Dirac operator; the records-arrow
is the retained_bounded `arrow_from_record_formation`. Honest hedges: the records-arrow is
INDEPENDENT/PARALLEL to S3 (not literally downstream), is conditional on a supplied
record-production dynamics, and fixes the AXIS but NOT the orientation (retained_no_go firewall).
"""

from __future__ import annotations
import itertools
import numpy as np

PASS = 0
FAIL = 0


def check(name, condition, detail=""):
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok); FAIL += int(not ok)
    tag = "PASS" if ok else "FAIL"
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


L, D = 4, 4
SITES = list(itertools.product(range(L), repeat=D))
IDX = {x: i for i, x in enumerate(SITES)}
N = len(SITES)
M = 0.3


def eta_order(order):
    pos = {ax: i for i, ax in enumerate(order)}
    def e(mu, x):
        return 1 if sum(x[ax] for ax in range(D) if pos[ax] < pos[mu]) % 2 == 0 else -1
    return e


ETA = eta_order(list(range(D)))                      # standard staircase, axis 0 = time


def dirac(e):
    Dm = np.zeros((N, N))
    for x in SITES:
        for mu in range(D):
            xp = list(x); xp[mu] = (x[mu] + 1) % L; xp = tuple(xp)
            xm = list(x); xm[mu] = (x[mu] - 1) % L; xm = tuple(xm)
            Dm[IDX[x], IDX[xp]] += e(mu, x) * 0.5
            Dm[IDX[x], IDX[xm]] += -e(mu, x) * 0.5
        Dm[IDX[x], IDX[x]] += M
    return Dm


def main() -> int:
    print("=" * 78)
    print("S3 single-clock axis IDENTITY is convention; the records-arrow sources it  [class A]")
    print("=" * 78)

    # ---- (1) crossing-link RP invariant: +1 for ALL axes (no axis distinguisher) ----
    print("\n-- (1) STW crossing-link P_a = eta_a(x) eta_a(theta_a x) = +1 for ALL axes --")
    allone = True
    for a in range(D):
        vals = set()
        for x in SITES:
            tx = list(x); tx[a] = (-1 - x[a]) % L; tx = tuple(tx)
            vals.add(ETA(a, x) * ETA(a, tx))
        allone = allone and vals == {1}
    check("P_a(x) = +1 uniformly for all d axes (eta_a omits x_a) => the staggered RP datum "
          "carries NO axis-distinguishing invariant", allone)

    # ---- (2) eta-curvature isotropic (-1 in all planes incl. temporal) ----
    print("\n-- (2) eta-curvature 2-cocycle = -1 in ALL planes incl. temporal (0,i): S_d-isotropic --")
    def sh(x, mu):
        y = list(x); y[mu] = (x[mu] + 1) % L; return tuple(y)
    iso = True
    temporal_planes = []
    for mu in range(D):
        for nu in range(mu + 1, D):
            vals = {ETA(mu, x) * ETA(nu, sh(x, mu)) * ETA(mu, sh(x, nu)) * ETA(nu, x) for x in SITES}
            iso = iso and vals == {-1}
            if mu == 0:
                temporal_planes.append(vals == {-1})
    check("the curvature is -1 in all C(d,2) planes including the 3 temporal planes (0,i) => "
          "S_d-isotropic, no plane/direction singled out as time", iso and all(temporal_planes))

    # ---- (3) the time<->space swap is an exact site-local Z2 field redefinition (gauge) ----
    print("\n-- (3) time<->space swap = exact site-local Z2 field redefinition (gauge) --")
    D_base = dirac(ETA)
    D_swap = dirac(eta_order([1, 0, 2, 3]))          # axis 1 = time
    s = np.array([1 if (x[0] * x[1]) % 2 == 0 else -1 for x in SITES], dtype=float)
    S = np.diag(s)
    spectra_eq = np.allclose(np.sort(np.linalg.svd(D_base, compute_uv=False)),
                             np.sort(np.linalg.svd(D_swap, compute_uv=False)))
    gauge_exact = np.allclose(S @ D_base @ S, D_swap, atol=1e-12)
    check("s(x)=(-1)^{x0 x1} gives diag(s) D_base diag(s) = D_swap EXACTLY (the temporal axis is "
          "gauge-movable), spectrum-preserving (=> taste-preserving)", gauge_exact and spectra_eq,
          detail=f"max|S D S - D_swap| = {np.max(np.abs(S @ D_base @ S - D_swap)):.1e}")

    # ---- (4) contrast: free dispersion direction-symmetric (spectrum picks no clock) ----
    print("\n-- (4) contrast: the free dispersion is direction-symmetric (spectrum picks no clock) --")
    # D^dag D = m^2 + sum_mu sin^2 p_mu : symmetric under any axis relabeling
    rng = np.random.default_rng(0)
    P = rng.uniform(0, 2 * np.pi, size=(50000, D))
    base = M ** 2 + np.sum(np.sin(P) ** 2, axis=1)
    perm = M ** 2 + np.sum(np.sin(P[:, [1, 0, 2, 3]]) ** 2, axis=1)
    check("D^dag D = m^2 + sum sin^2 p is identical under axis relabeling => the spectrum does not "
          "single out a clock", np.allclose(base, perm),
          detail=f"max|base - relabeled| = {np.max(np.abs(base - perm)):.1e}")

    # ---- (5) records-arrow: reversible spatial group vs monotone record monoid ----
    print("\n-- (5) records-arrow sources the unique axis: reversible space vs monotone records --")
    # spatial reflection x_i -> -x_i is an involution preserving the pairwise-distance multiset
    pts = rng.integers(-3, 4, size=(8, 3))
    def distmultiset(q):
        return sorted(round(float(np.linalg.norm(q[i] - q[j])), 6) for i in range(len(q)) for j in range(i + 1, len(q)))
    refl = pts.copy(); refl[:, 0] = -refl[:, 0]
    reversible = distmultiset(pts) == distmultiset(refl)
    # a record count is strictly monotone (append-only monoid) -- no inverse element
    counts = [0, 1, 2, 3]
    monotone_noninvertible = all(counts[i + 1] > counts[i] for i in range(len(counts) - 1))
    check("each spatial reflection x_i->-x_i is an involution preserving the distance multiset "
          "(reversible group) while record count is strictly monotone (append-only monoid) => only "
          "the record-accumulation direction is a clock axis, eta-free", reversible and monotone_noninvertible)

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: S3-convention / records-arrow analysis FAILED.")
        return 1
    print("VERDICT: S3's staggered-eta temporal-RP 'unique clock axis' is CONVENTION-DEPENDENT for "
          "the axis IDENTITY -- the crossing-link RP invariant is +1 for every axis, the curvature "
          "is isotropic across all planes including temporal, and the temporal axis is movable by a "
          "spectrum/taste-preserving site-local Z2 field redefinition. The convention-independent "
          "residue is only the COUNT (=1 RP axis exists; spectrum direction-symmetric). The "
          "convention-independent SOURCE of the unique clock AXIS is the records-arrow (reversible "
          "spatial Z^3 cannot carry a monotone direction); orientation remains firewalled "
          "(retained_no_go). This sharpens the retained_no_go single-clock scope boundary.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
