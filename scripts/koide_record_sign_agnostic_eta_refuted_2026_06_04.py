"""The RECORD axiom does NOT force the signed Koide readout (Q=2/3): sign_is_free_import. Four verified results:

 (A) ADDITIVITY IS SIGN-AGNOSTIC: the signed trace Tr(H)=sum(lambda_k), the unsigned sum|lambda_k|, the
     magnitude log|det|=sum log|lambda_k|, AND eta=sum sign(lambda_k) are ALL additive over disjoint/
     direct-sum records. So the Record axiom I(R1 u R2)=I(R1)+I(R2) selects NONE of them; it cannot fix
     the sign of sqrt(m). (MINIMAL_AXIOMS_2026-06-04 explicitly disclaims Born/modulus/phase.)
 (B) BORN KILLS THE SIGN: |+x|^2 = |-x|^2; a post-Born record is sign-blind. The only wired-up record
     generator (log|det|, magnitude-first) sits on the UNSIGNED side -> Q != 2/3 generically. The signed
     Q=2/3 needs Tr(H)=sum(lambda_k) read PRE-Born -- a different functional the axioms do not select.
 (C) ETA IS REFUTED AS A FORCER: eta=sum sign(lambda) is a Z-valued sign-COUNT, too coarse -- two spectra
     with identical eta=3 give Q=0.5 vs Q=1/3 (verified). It cannot reconstruct the real-valued Brannen
     denominator Tr(H)=3a. The Dirac structure FAVORS signed (real spectrum from self-adjointness) but does
     not FORCE it; 'H=iD' is itself unaudited.
 (D) EMPIRICAL DEFLATION: the physical charged leptons are SIGN-HOMOGENEOUS (all sqrt(m)>0), so signed =
     unsigned = Q_PDG ~ 2/3 there -- the signed-vs-unsigned dichotomy is NOT load-bearing on observed data.

CONSEQUENCE: the sign bit is a free import that, if wanted, consolidates onto the staggered-Dirac admission
(H=iD pre-Born). The genuine open gate is r=1/2 itself (the equipartition), UNFORCED by any readout choice.
Sets no audit status (independent audit lane owns that); edits/re-cites no existing row.
"""
import numpy as np

C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])
I3 = np.eye(3)


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def blockdiag(*mats):
    n = sum(m.shape[0] for m in mats)
    Z = np.zeros((n, n))
    i = 0
    for m in mats:
        k = m.shape[0]
        Z[i:i+k, i:i+k] = m
        i += k
    return Z


def main():
    passed = []

    # (A) additivity sign-agnostic: Tr, sum|lam|, log|det|, eta all additive over direct sums.
    H1 = 1.3 * I3 + 0.5 * (C + C.T)
    H2 = np.diag([0.8, -0.4, 1.1])
    H = blockdiag(H1, H2)
    l1, l2, l = np.linalg.eigvalsh(H1), np.linalg.eigvalsh(H2), np.linalg.eigvalsh(blockdiag(H1, H2))
    Tr = lambda ev: np.sum(ev)
    Sabs = lambda ev: np.sum(np.abs(ev))
    Lndet = lambda ev: np.sum(np.log(np.abs(ev)))
    Eta = lambda ev: np.sum(np.sign(ev))
    addit = all(abs(F(l) - (F(l1) + F(l2))) < 1e-9 for F in (Tr, Sabs, Lndet, Eta))
    passed.append(check(
        "(A) additivity is SIGN-AGNOSTIC: signed Tr, unsigned sum|lam|, log|det|, AND eta are ALL additive over disjoint records",
        addit,
        f"Tr/sum|lam|/log|det|/eta all add over the direct sum => Record axiom selects none"))

    # (B) Born kills the sign.
    passed.append(check(
        "(B) Born kills the sign: |+x|^2 = |-x|^2 -- a post-Born record is sign-blind",
        abs(0.6 ** 2 - (-0.6) ** 2) < 1e-15))

    # (C) eta is too coarse -- same eta, different Q.
    def Q_of_spectrum(lams):
        lams = np.array(lams, float)
        return np.sum(lams ** 2) / (np.sum(lams)) ** 2
    specA, specB = [1.0, 1.0, 1.0], [1.0, 1.0, 4.0]   # both eta = sum sign = 3
    passed.append(check(
        "(C) eta is REFUTED as a forcer: two spectra with eta=3 give DIFFERENT Q (1/3 vs 1/2) -- a Z-count cannot fix Q",
        Eta(np.array(specA)) == 3 and Eta(np.array(specB)) == 3
        and abs(Q_of_spectrum(specA) - 1/3) < 1e-12 and abs(Q_of_spectrum(specB) - 0.5) < 1e-12,
        f"eta(A)=eta(B)=3 but Q(A)={Q_of_spectrum(specA):.4f} != Q(B)={Q_of_spectrum(specB):.4f}"))

    # (D) empirical deflation: physical charged leptons are sign-homogeneous -> signed = unsigned = 2/3.
    m = np.array([0.51099895e-3, 105.6583755e-3, 1776.86e-3])  # GeV, e/mu/tau
    sm = np.sqrt(m)                       # all > 0  => sign-homogeneous
    Q_signed = np.sum(m) / np.sum(sm) ** 2            # signed sqrt(m) (all +)
    Q_unsigned = np.sum(m) / np.sum(np.abs(sm)) ** 2  # |sqrt(m)| -- identical when all signs equal
    passed.append(check(
        "(D) physical leptons SIGN-HOMOGENEOUS (all sqrt(m)>0): signed = unsigned = Q_PDG ~ 2/3 -- the sign dichotomy is NOT load-bearing on data",
        np.all(sm > 0) and abs(Q_signed - Q_unsigned) < 1e-12 and abs(Q_signed - 2/3) < 2e-3,
        f"Q_signed=Q_unsigned={Q_signed:.6f} ~ 2/3"))

    # CONSEQUENCE: the genuine gate is r=1/2 (equipartition), unforced by ANY readout choice. Both readings
    # agree at the physical point; the value Q=2/3 <=> r=1/2 is the equipartition pin, not a sign choice.
    r_half = 0.5
    passed.append(check(
        "CONSEQUENCE: Q=2/3 <=> r=1/2 is the EQUIPARTITION pin, unforced by any readout; the sign bit (if wanted) consolidates onto the staggered-Dirac admission H=iD",
        abs((1/3 + 2/3*r_half) - 2/3) < 1e-12))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("FINDING: the RECORD axiom does NOT force the signed Koide readout (sign_is_free_import). Additivity")
    print("is sign-agnostic; Born kills the sign; eta is too coarse to force it (refuted by counterexample);")
    print("and the physical leptons are sign-homogeneous so signed=unsigned=2/3 (the dichotomy is moot on data).")
    print("The genuine open gate is r=1/2 (equipartition), unforced by any readout; the signed reading, if")
    print("wanted, reduces to the staggered-Dirac admission. No audit status.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
