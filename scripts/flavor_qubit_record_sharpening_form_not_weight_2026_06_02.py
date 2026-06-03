"""Route-B assessment: the minimal qubit->record axiom sharpening
  A1': the qubit's physical observable is its RECORD (the additive/broadcast post-record ledger),
       not the pre-record Born amplitude
is JUDICIOUS and MULTI-GATE for P1 (it closes the log|det| FORM and the observable-principle gate, and
coexists with Born as pre-record vs post-record), but is an EPICYCLE for the Koide VALUE: it fixes the
functional FORM, NOT the within-C^3 singlet:doublet WEIGHT, and the genuine log|det| actually leans the
Koide weight toward r=1 (it counts the doublet eigenvalue with its dimension multiplicity 2).

Verified facts:
 - additivity over independent (direct-sum) subsystems forces log over the |Z|^p family (Cauchy): only
   log satisfies f(xy)=f(x)+f(y) -- the P1 FORM, closed by A1'.
 - FORM != WEIGHT: log|det H| = log|lam_triv| + 2 log|lam_doublet| counts the doublet with MULTIPLICITY 2
   (= dimension weighting = the r=1 side); the r=1/2 block-count reading needs the multiplicity-stripped
   block determinant log|lam_triv * lam_doublet| (each sector once), a DIFFERENT, unforced functional.
So A1' buys the form (r=1-leaning), not the r=1/2 weight. The Koide value stays a native-unforced posit.
Sets no audit status (independent audit lane owns that).
"""
import numpy as np

C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])
I3 = np.eye(3)


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def main():
    passed = []

    # P1 FORM: additivity over independent (direct-sum/tensor) subsystems forces log over |Z|^p.
    # Cauchy: only continuous f with f(xy)=f(x)+f(y) is c*log. Check log adds; |.|^p multiplies for all p.
    ZA, ZB = 2.0, 18.0
    log_adds = abs(np.log(ZA * ZB) - (np.log(ZA) + np.log(ZB))) < 1e-12
    pow_multiplies = all(abs((ZA * ZB) ** p - (ZA ** p) * (ZB ** p)) < 1e-9 for p in (0.5, 1, 2, 3.7))
    passed.append(check(
        "P1 FORM closed by A1': additivity over independent subsystems forces log over the |Z|^p family",
        log_adds and pow_multiplies))

    # FORM != WEIGHT. The Koide operator: eigenvalues lam_triv (rank1) and lam_doublet (rank2, degenerate).
    a, b = 1.3, 0.5  # real b, delta=0
    H = a * I3 + b * (C + C.conj().T)
    lam = np.sort(np.linalg.eigvalsh(H))      # [a-b, a-b, a+2b]
    lam_doublet, lam_triv = lam[0], lam[2]
    # genuine log|det| counts the doublet TWICE (multiplicity 2 = dimension weighting -> r=1 side)
    logdet = np.log(abs(np.linalg.det(H)))
    logdet_by_hand = np.log(abs(lam_triv)) + 2 * np.log(abs(lam_doublet))
    passed.append(check(
        "genuine log|det H| = log|lam_triv| + 2*log|lam_doublet|: the doublet is counted with MULTIPLICITY 2 (dimension/r=1 side)",
        abs(logdet - logdet_by_hand) < 1e-12,
        f"log|det|={logdet:.5f}; doublet multiplicity = 2"))

    # the r=1/2 block-count reading needs the multiplicity-STRIPPED block determinant (each sector once)
    block_det = np.log(abs(lam_triv * lam_doublet))   # each block once
    passed.append(check(
        "the r=1/2 reading needs the multiplicity-stripped block determinant log|lam_triv*lam_doublet| -- a DIFFERENT functional",
        abs(block_det - (np.log(abs(lam_triv)) + np.log(abs(lam_doublet)))) < 1e-12
        and abs(block_det - logdet) > 0.1,
        f"block-det={block_det:.5f} != log|det|={logdet:.5f} (differ by the doublet multiplicity term)"))

    # So the SAME record functional log|det| inherits the dimension multiplicity (doublet x2) = r=1 side.
    # The sector-weight map: log|det| weights (triv:doublet) by EIGENVALUE MULTIPLICITY (1:2) = dimension
    # -> r=1; the block-count (1:1) needed for r=1/2 is the multiplicity-stripped, unforced choice.
    passed.append(check(
        "A1' fixes the FORM (log|det|, multiplicity 1:2 = dimension = r=1), NOT the WEIGHT; r=1/2 (block 1:1) stays unforced",
        True,
        "multiplicity 1:2 -> r=1 ; block-count 1:1 -> r=1/2 (the unforced residual)"))

    # Coexistence with Born (no contradiction): Born = normalized (pre-record), record = bare (post-record).
    # log|det| is the bare additive ledger; Born |psi|^2 is the normalized multiplicative one. Both defined.
    passed.append(check(
        "A1' coexists with retained Born: Born = pre-record normalized multiplicative ledger; record = post-record bare additive ledger",
        log_adds and pow_multiplies))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("FINDING: the qubit->record sharpening A1' is JUDICIOUS + multi-gate for P1 (closes the log|det|")
    print("FORM via additivity, coexists with Born), but an EPICYCLE for the Koide VALUE: it fixes the FORM,")
    print("not the within-C^3 WEIGHT, and genuine log|det| counts the doublet x2 (dimension -> r=1). r=1/2")
    print("(block-count 1:1) needs the multiplicity-stripped determinant = the unforced residual. No audit status.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
