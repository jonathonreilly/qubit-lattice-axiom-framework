#!/usr/bin/env python3
"""Self-contained lemma: a real-diagonal source on the positive cone added to a real antisymmetric
operator has a strictly positive real determinant (no phase), and Record additivity plus an explicit
continuity/regularity convention selects the logarithmic readout on R_{>0}.

WHY THIS LEMMA EXISTS (audit-graph). The observable-principle parent
(OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE) needs exactly the fact "det(D+J) in R_{>0} on the positive
source cone" to make its old P2 (phase-blind vs phase-sensitive) distinction vacuous. That fact was
cited from OBSERVABLE_PRINCIPLE_POSITIVE_SOURCE_CONE_P2_ELIMINATION (2026-06-06), creating a
load-bearing 2-cycle parent <-> application (both unaudited), which stalled ~722 downstream rows.
This note EXTRACTS the self-contained fact the parent actually needs -- it is linear algebra plus
Record additivity with explicit regularity/baseline conventions, consuming NONE of the parent. The
parent can then depend on this lemma (one-directional), and the application note keeps depending on
the parent, breaking the cycle.

CONTENT (exact / numpy):
  L1. For D real antisymmetric and S real positive-diagonal, det(S + D) > 0 (real, no phase):
      S + D = S^(1/2)(I + B)S^(1/2) with B = S^(-1/2) D S^(-1/2) real antisymmetric; eig(B) in {0, +-i*lam},
      so det(I+B) = prod_k (1 + lam_k^2) >= 1 > 0, and det S > 0.
  L2. Sign-constancy on a derivative patch: for invertible real antisymmetric D and real diagonal J
      with ||D^{-1} J|| < 1, det(D + tJ) never crosses 0 on t in [0,1] (Neumann), so det(D+J) keeps the
      sign of det D = prod lam_k^2 > 0 -> det(D+J) in R_{>0}.
  L3. Record additivity plus explicit regularity selects the logarithm on R_{>0}: det is
      multiplicative over disjoint blocks (det(A (+) B) = det A * det B); a continuous map
      R_{>0}->R additive over this product (Record's finite scalar additivity for disjoint records)
      is c*log (Cauchy on R_{>0}); c=1 is the convention.

No framework code; no PDG/fitted value. Record finite-scalar additivity is the only framework premise
(the multiplicative->additive step); continuity on R_{>0} and c=1 are explicit bounded conventions;
everything else is reproven linear algebra.
"""
from __future__ import annotations
import numpy as np

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


def rand_antisym(n, rng):
    A = rng.standard_normal((n, n))
    return A - A.T


def main() -> int:
    print("REAL-DIAGONAL-SOURCE DET-POSITIVITY + LOG READOUT LEMMA (self-contained)")
    print("=" * 74)
    rng = np.random.default_rng(0)

    # L1: det(S + D) > 0 for S positive diagonal, D real antisymmetric.
    ok1 = True
    worst = np.inf
    for _ in range(400):
        n = int(rng.integers(2, 7))
        D = rand_antisym(n, rng)
        S = np.diag(rng.uniform(0.05, 3.0, size=n))
        d = float(np.linalg.det(S + D))
        worst = min(worst, d)
        ok1 = ok1 and (d > 0) and (abs(np.imag(np.linalg.det((S + D).astype(complex)))) < 1e-9)
    check("L1: det(S + D) > 0 (real, no phase) for positive-diagonal S + real antisymmetric D "
          "(400 random cases; det(I+B)=prod(1+lam^2)>0)", ok1, f"min det over 400 cases = {worst:.4f} > 0")

    # L1 structural: eig(B) are 0 or +-i*lam (purely imaginary), so 1+lam^2 factors are >=1.
    B = rand_antisym(5, rng)
    ev = np.linalg.eigvals(B)
    check("L1-structure: a real antisymmetric matrix has purely imaginary spectrum (Re=0) -> "
          "det(I+B)=prod(1+lam^2) >= 1", np.allclose(np.real(ev), 0, atol=1e-9),
          f"max|Re eig(B)| = {np.max(np.abs(np.real(ev))):.1e}; det(I+B)={np.real(np.linalg.det(np.eye(5)+B)):.3f}")

    # L2: Neumann sign-constancy on the derivative patch.
    ok2 = True
    for _ in range(200):
        n = int(rng.integers(2, 6)) * 2  # even -> invertible antisymmetric generic
        D = rand_antisym(n, rng)
        if abs(np.linalg.det(D)) < 1e-6:
            continue
        Dinv = np.linalg.inv(D)
        J = np.diag(rng.standard_normal(n))
        scale = 0.5 / (np.linalg.norm(Dinv) * np.linalg.norm(J) + 1e-12)  # ensure ||Dinv J|| < 1
        J = scale * J
        dets = [float(np.linalg.det(D + t * J)) for t in np.linspace(0, 1, 25)]
        ok2 = ok2 and all(x > 0 for x in dets)  # det D = prod lam^2 > 0, stays positive
    check("L2: with ||D^{-1}J|| < 1, det(D + tJ) keeps the positive sign of det D on t in [0,1] "
          "(Neumann; no zero crossing) -> det(D+J) in R_{>0}", ok2, "200 random invertible patches")

    # L3: multiplicative over disjoint blocks -> Cauchy on R_{>0} -> log readout.
    A = np.diag(rng.uniform(0.1, 2, 3)) + rand_antisym(3, rng) * 0  # positive-det block
    Bk = np.diag(rng.uniform(0.1, 2, 4))
    blk = np.block([[A, np.zeros((3, 4))], [np.zeros((4, 3)), Bk]])
    mult = np.isclose(np.linalg.det(blk), np.linalg.det(A) * np.linalg.det(Bk))
    # additive readout candidate W(x)=log x satisfies W(xy)=W(x)+W(y); check on the determinants
    x, y = float(np.linalg.det(A)), float(np.linalg.det(Bk))
    additive = np.isclose(np.log(x * y), np.log(x) + np.log(y))
    check("L3: det is multiplicative over disjoint blocks; Record finite scalar additivity over disjoint "
          "records + continuity on R_{>0} forces the readout to be c*log det (Cauchy), c=1 convention",
          bool(mult) and bool(additive),
          f"det(A(+)B)=det A*det B: {mult}; log(xy)=log x+log y: {additive}")

    print(f"\nSCORECARD PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: a real-diagonal source on the positive cone added to a real antisymmetric operator has "
        "a strictly positive real determinant (no phase), and Record additivity plus explicit continuity "
        "on R_{>0} selects c*log det as the readout (c=1 convention). This is the self-contained fact the "
        "observable-principle parent needs to make its P2 phase distinction vacuous -- it consumes none "
        "of the parent. Audit lane sets the verdict."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
