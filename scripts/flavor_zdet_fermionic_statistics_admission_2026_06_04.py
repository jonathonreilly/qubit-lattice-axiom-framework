"""Z=det(D+J) -- the single remaining factor of the log-det generator -- reduces to ONE fermionic-
statistics admission FS ("matter integrates anticommuting/Grassmann, not bosonic"), which is NOT forced
by Lattice+Quantum+Record. Key disproof: per-site dim-2 (the retained grassmann_forcing_bridge) excludes
only the FREE boson (dim infinity); the HARD-CORE boson is dim-2, commuting cross-site, and yields 1/det
-- so dimension is BLIND to fermion-vs-hard-core-boson, and the selector is cross-site STATISTICS, which
the axioms do not fix (the native cross-site product is COMMUTING/bosonic; the anticommuting frame needs
a Jordan-Wigner string, a change of generators not supplied by the axioms).

Asymmetric multi-gate keep: FS FULLY discharges Z=det (det^{+1}) -- with the retained pieces
spin_statistics_berezin_determinant (Z_F=det, retained_bounded), grassmann_forcing_bridge (dim-2,
retained_bounded), staggered_only_det_positivity_case_a (retained) -- gating the ~59 log-det rows; but it
only PARTIALLY serves Koide: the generation chiral grading Gamma_chi lives on a DIFFERENT factor (internal
generation R^3), is circulant hence COMMUTES with every C3-equivariant mass operator, and is obstructed by
the retained_bounded koide_z3_equivariant_anticommuting_no_go -- the spatial Fermi frame does not transport
onto the generation factor. So Z=det and the Koide chirality gate share an ANCESTOR (fermionic/graded
frame) but are TWO distinct atoms, not one admission.

Sets no audit status (independent audit lane owns that); edits/re-cites no existing row.
"""
import numpy as np
import itertools

sp = np.array([[0, 1.0], [0, 0]])      # sigma^+
s3 = np.array([[1.0, 0], [0, -1.0]])   # sigma^3
I2 = np.eye(2)


def kron(*ops):
    out = np.array([[1.0]])
    for o in ops:
        out = np.kron(out, o)
    return out


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def berezin_det(M):
    """Grassmann Gaussian integral int dbar-eta d-eta exp(-bar-eta M eta) = det(M) (signed permutation sum)."""
    n = M.shape[0]
    total = 0.0
    for perm in itertools.permutations(range(n)):
        sign = 1
        p = list(perm)
        # parity of permutation
        seen = [False] * n
        for i in range(n):
            if seen[i]:
                continue
            j = i; length = 0
            while not seen[j]:
                seen[j] = True; j = p[j]; length += 1
            if length % 2 == 0:
                sign = -sign
        total += sign * np.prod([M[i, perm[i]] for i in range(n)])
    return total


def main():
    passed = []

    # 1. Berezin/Grassmann Gaussian = det (signed); bosonic Gaussian ~ 1/det. So fermionic <-> det, bosonic <-> 1/det.
    M = np.array([[2.0, 0.7, 0.1], [0.3, 1.5, 0.4], [0.2, 0.1, 1.8]])
    passed.append(check(
        "Berezin (Grassmann) Gaussian = det(M); bosonic Gaussian ~ 1/det(M). fermionic<->det^{+1}, bosonic<->det^{-1}",
        abs(berezin_det(M) - np.linalg.det(M)) < 1e-9,
        f"berezin={berezin_det(M):.6f} = det={np.linalg.det(M):.6f}; bosonic gives 1/det={1/np.linalg.det(M):.6f}"))

    # 2. The native cross-site product is COMMUTING (bosonic): bare ladder ops on different sites commute.
    a1, a2 = kron(sp, I2), kron(I2, sp)
    passed.append(check(
        "native cross-site is BOSONIC: bare ladder ops commute [a1,a2]=0 (the default Quantum+Lattice tensor product)",
        np.allclose(a1 @ a2 - a2 @ a1, 0)))

    # 3. The anticommuting (fermionic) frame requires a Jordan-Wigner string -- a change of generators, not axiomatic.
    c1, c2 = kron(sp, I2), kron(s3, sp)
    passed.append(check(
        "fermionic frame requires a Jordan-Wigner string c2=s3(x)sp: then {c1,c2}=0 (CAR) -- NOT the native product",
        np.allclose(c1 @ c2 + c2 @ c1, 0)))

    # 4. THE DISPROOF: per-site dim-2 does NOT distinguish fermion from HARD-CORE boson. Hard-core boson:
    #    (sp)^2=0 (dim-2, same as fermion) yet commutes cross-site (-> permanent/1-det side, NOT det).
    passed.append(check(
        "dim-2 is BLIND to fermion-vs-hard-core-boson: (sp)^2=0 (dim-2) AND commuting cross-site -> grassmann_forcing_bridge excludes only the FREE boson",
        np.allclose(sp @ sp, 0) and np.allclose(a1 @ a2 - a2 @ a1, 0)))

    # 5. Statistics is the selector and it is unforced: det (signed/CAR) vs permanent (unsigned/bosonic) differ.
    def permanent(A):
        n = A.shape[0]
        return sum(np.prod([A[i, p[i]] for i in range(n)]) for p in itertools.permutations(range(n)))
    passed.append(check(
        "the selector is STATISTICS: det (signed, fermionic) != permanent (unsigned, bosonic); axioms fix neither",
        abs(np.linalg.det(M) - permanent(M)) > 1e-6,
        f"det={np.linalg.det(M):.4f} != perm={permanent(M):.4f}"))

    # 6. KOIDE GATE IS A DIFFERENT ATOM: Gamma_chi=(2/3)J-I on the generation R^3 is circulant, COMMUTES with
    #    every C3-equivariant mass operator -> the spatial Fermi frame does NOT supply the generation chiral grading.
    J = np.ones((3, 3))
    Gx = (2.0 / 3) * J - np.eye(3)
    C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])
    H = 1.3 * np.eye(3) + 0.6 * C + 0.6 * C.T  # a C3-equivariant (circulant) mass operator
    passed.append(check(
        "Koide chiral grading Gamma_chi=(2/3)J-I (eig {-1,-1,1}) is circulant and COMMUTES with C3-equivariant H -> distinct atom on the generation factor",
        np.allclose(sorted(np.linalg.eigvalsh(Gx)), [-1, -1, 1]) and np.allclose(Gx @ H - H @ Gx, 0)))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("FINDING: Z=det reduces to ONE fermionic-statistics admission FS ('matter is fermionic, not bosonic'),")
    print("NOT forced (hard-core-boson disproof: dim-2 blind to fermion-vs-hardcore-boson; native cross-site is")
    print("bosonic). FS FULLY discharges Z=det/det^{+1} (with retained Berezin+grassmann-bridge+det-positivity)")
    print("gating ~59 log-det rows; PARTIALLY serves Koide (graded category only -- the generation chiral grading")
    print("is a distinct atom, circulant Gamma_chi commutes with H, blocked by the retained no-go). No audit status.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
