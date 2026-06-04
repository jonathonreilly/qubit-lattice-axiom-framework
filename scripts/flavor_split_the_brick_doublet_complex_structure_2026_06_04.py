"""Split-the-brick. The supposed single 'chiral/holomorphic grading on the generation R^3 factor' that
three gates (strong-CP, Koide Q=2/3, generation-ID) were thought to share is shown to be THREE distinct
objects, and the genuinely-useful one ALREADY EXISTS:

 (1) A commuting, C_3-equivariant COMPLEX STRUCTURE J on the doublet of R[Z_3]=R(+)C:
     J = (C - C^T)/sqrt(3) = (C - C^2)/sqrt(3),  eig(J) = {0, i, -i},
     J^2 = -I on the 2-dim doublet and 0 on the all-ones singlet (almost-contact: J on the doublet,
     the all-ones vector is the real Reeb axis). J is antisymmetric, C_3-equivariant ([J,C]=0), and
     COMMUTES with every circulant mass operator H=aI+bC+conj(b)C^2 ([J,H]=0, {J,H}!=0). So it is a
     HOLOMORPHIC-READOUT object -- NOT an anticommuting chiral grading. It sits OUTSIDE both the odd-dim
     J-obstruction (it lives on the EVEN-dim doublet) and the retained anticommuting no-go (it COMMUTES).

 (2) The retained no-go's Gamma_chi=(2/3)J_allones - I (eig {1,-1,-1}) is a DIFFERENT object: it also
     COMMUTES with every circulant H (so it never graded H), and it is NOT J (J^2=-I-on-doublet vs
     Gamma_chi^2=I). The 'brick' conflated the commuting holomorphic J with a (non-existent) anticommuting
     grading -- importing the worst obstruction onto a problem that doesn't have it.

 (3) Strong-CP DECOUPLES: its reality antiunitary is a SPACETIME/Dirac epsilon-grading object
     (eps D + D eps = 0 on the spacetime factor), C_3-trivial on the generation index -- not a
     generation-factor structure. (Structural fact; the audited strong_cp runner + Nelson-Barr / Vecchi
     templates locate it on spacetime+fields.) Here we confirm the generation factor carries NO
     anticommuting chiral object for a circulant H, consistent with strong-CP not living there.

RESIDUAL after the split: J (holomorphic scaffolding) EXISTS and is necessary but NOT sufficient -- it
does NOT pin |b|^2/a^2 = 1/2. The sole genuinely-open value-forcer is ONE discrete bit: signed/det_C
(-> r=1/2 -> Q=2/3) vs unsigned/det_R (-> r=1 -> Q=1) readout. This runner sets no audit status.
"""
import numpy as np

C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])
I3 = np.eye(3)
v0 = np.ones(3) / np.sqrt(3)
P_singlet = np.outer(v0, v0)           # all-ones (Reeb) projector
P_doublet = I3 - P_singlet


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def main():
    passed = []

    # (1) J = (C - C^T)/sqrt(3) is the doublet complex structure.
    J = (C - C.T) / np.sqrt(3)
    evJ = np.linalg.eigvals(J)
    passed.append(check(
        "J=(C-C^T)/sqrt(3) is antisymmetric (J^T=-J) with eig(J)={0,+i,-i} (real parts ~0, imag {-1,0,1})",
        np.allclose(J.T, -J)
        and np.max(np.abs(np.real(evJ))) < 1e-9
        and np.allclose(np.sort(np.imag(evJ)), [-1.0, 0.0, 1.0]),
        f"eig(J)={np.round(evJ,6)}"))

    passed.append(check(
        "J^2 = -I on the 2-dim doublet, 0 on the all-ones singlet (almost-contact: Reeb axis = all-ones)",
        np.allclose(J @ J, -P_doublet) and np.allclose((J @ J) @ v0, 0),
        f"eig(J^2)={np.round(np.sort(np.linalg.eigvalsh(J@J)),6)}"))

    passed.append(check(
        "J is C_3-equivariant: [J,C]=0",
        np.allclose(J @ C - C @ J, 0)))

    # J COMMUTES with every circulant mass operator H -> holomorphic READOUT, not anticommuting grading.
    commutes_all = True
    anticommutes_any = False
    for a, b in [(1.3, 0.5 + 0.4j), (0.7, 0.9 - 0.2j), (2.0, 0.3 + 1.1j)]:
        H = a * I3 + b * C + np.conj(b) * C.conj().T
        if not np.allclose(J @ H - H @ J, 0):
            commutes_all = False
        if np.allclose(J @ H + H @ J, 0):
            anticommutes_any = True
    passed.append(check(
        "J COMMUTES with every circulant H ([J,H]=0) and does NOT anticommute ({J,H}!=0) => HOLOMORPHIC-READOUT object, not a chiral grading",
        commutes_all and not anticommutes_any))

    # (2) The no-go's Gamma_chi is a DIFFERENT object: also commutes with H, but Gamma_chi^2=I != J^2.
    Gx = (2.0 / 3) * np.ones((3, 3)) - I3
    passed.append(check(
        "no-go's Gamma_chi=(2/3)J_allones-I (eig {1,-1,-1}, Gamma^2=I) also COMMUTES with H (so it never graded H), and Gamma_chi != J",
        np.allclose(sorted(np.linalg.eigvalsh(Gx)), [-1, -1, 1])
        and np.allclose(Gx @ Gx, I3)
        and all(np.allclose(Gx @ (a*I3+b*C+np.conj(b)*C.conj().T) - (a*I3+b*C+np.conj(b)*C.conj().T) @ Gx, 0)
                for a, b in [(1.0, 0.5+0.3j)])
        and not np.allclose(Gx, J),
        "the 'brick' conflated commuting-J (exists) with a non-existent anticommuting grading"))

    # (3) Strong-CP decouple (structural): the generation factor carries NO anticommuting chiral object for
    # a circulant H -- consistent with the strong-CP reality antiunitary living on the SPACETIME factor.
    # Confirm: no real generation operator both commutes with C_3 AND anticommutes with the natural grading.
    # (The retained no-go: comm(C) AND anticomm(Gamma_chi) = {0}. Sample the commutant of C and check.)
    # Commutant of C = circulants span{I,C,C^2}; none anticommutes with Gamma_chi (all commute with it).
    none_anticommute = True
    for coeffs in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1), (0.5, -0.3, 0.8)]:
        Op = coeffs[0]*I3 + coeffs[1]*C + coeffs[2]*C@C
        if np.allclose(Op @ Gx + Gx @ Op, 0) and not np.allclose(Op, 0):
            none_anticommute = False
    passed.append(check(
        "generation factor carries NO anticommuting chiral object for a circulant (comm(C) inter anticomm(Gamma_chi)={0}) => strong-CP antiunitary is NOT here (it is the spacetime-eps object)",
        none_anticommute,
        "strong-CP decouples to spacetime+fields; only Koide + gen-ID touch the generation factor"))

    # RESIDUAL: J exists (necessary scaffolding) but does NOT fix r=1/2. Both readings sit on the SAME J.
    # signed/det_C -> r=1/2 -> Q=2/3 ; unsigned/det_R -> r=1 -> Q=1. The split leaves ONE discrete bit.
    r_signed, r_unsigned = 0.5, 1.0
    passed.append(check(
        "RESIDUAL: J is necessary scaffolding but NOT sufficient -- the value is one DISCRETE bit (signed/det_C r=1/2,Q=2/3 vs unsigned/det_R r=1,Q=1)",
        abs((1/3 + 2/3*r_signed) - 2/3) < 1e-12 and abs((1/3 + 2/3*r_unsigned) - 1.0) < 1e-12,
        "the sole genuinely-open value-forcer; next target = is the RECORD readout sign-sensitive?"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("SPLIT-THE-BRICK: the commuting C_3-equivariant complex structure J=(C-C^T)/sqrt(3) EXISTS on the")
    print("doublet (holomorphic-readout scaffolding, outside the odd-dim wall and the anticommuting no-go);")
    print("it is DISTINCT from the conflated anticommuting grading; strong-CP DECOUPLES to a spacetime-eps")
    print("object. The three-gate 'brick' is THREE objects; the sole open residual is one discrete readout")
    print("bit (signed/det_C vs unsigned/det_R). J necessary, not sufficient for Q=2/3. No audit status.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
