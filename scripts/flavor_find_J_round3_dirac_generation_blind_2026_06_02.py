"""J-hunt ROUND 3 conditional finite-generation algebra.

This runner does not derive the charged-lepton Dirac reality operator's action
on generation space. It checks the restricted finite packet conditional on the
explicit generation-space input U_gen = i*I_3. Under that input, the central
generation scalar and the C-eigenbasis phase centralizer are spectators to the
C3-circulant Hermitian family H, while the two checked doublet-J routes remain
outside the C3-preserving packet.

Verified finite findings:
(1) Conditional input U_gen=i*I_3 leaves every tested C3-circulant H fixed.
(2) The continuous centralizer diag(1,e^{iphi},e^{-iphi}) in the C-eigenbasis
    also leaves H fixed and therefore does not alter the singlet/doublet ratio.
(3) A generic rephasing C->e^{i theta}C breaks C^3=I except at cube-root phases.
(4) Solving the Hermitian C3-circulant anticommutator equations exactly gives
    only the zero operator, so any Gamma_chi anticommutant is outside the
    C3-circulant packet.
"""
import numpy as np
import sympy as sp


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


w = np.exp(2j * np.pi / 3)
C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])
I3 = np.eye(3)
GX = (2.0 / 3.0) * np.ones((3, 3)) - I3
F = np.array([[1, 1, 1], [1, w, w ** 2], [1, w ** 2, w]]) / np.sqrt(3)  # C-eigenbasis


def rephased_c_breaks_cubic_identity():
    theta = sp.pi / 7
    c_sp = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    m_sp = sp.exp(sp.I * theta) * c_sp
    m3_sp = sp.simplify(m_sp ** 3)
    expected = sp.exp(3 * sp.I * theta) * sp.eye(3)
    phase_not_one = abs(complex(sp.N(sp.exp(3 * sp.I * theta) - 1))) > 1e-12
    return m3_sp == expected and phase_not_one


def no_nonzero_circulant_anticommutant():
    a, x, y = sp.symbols("a x y", real=True)
    i3_sp = sp.eye(3)
    c_sp = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    gx_sp = sp.Rational(2, 3) * sp.ones(3, 3) - i3_sp
    h_sp = a * i3_sp + (x + sp.I * y) * c_sp + (x - sp.I * y) * c_sp.T
    anticomm = sp.simplify(h_sp * gx_sp + gx_sp * h_sp)
    sol = sp.solve([sp.Eq(entry, 0) for entry in anticomm], [a, x, y], dict=True)
    return sol == [{a: 0, x: 0, y: 0}]


def main():
    passed = []
    a, b = 1.0, 0.6 + 0.2j
    H = a * I3 + b * C + np.conj(b) * C.conj().T

    print("SCOPE: finite C3-circulant matrix packet conditional on U_gen=i*I_3.")
    print("SCOPE: no spinor-to-generation bridge is asserted by this runner.\n")

    # (1) conditional generation-space central scalar leaves H fixed.
    U1 = 1j * I3
    passed.append(check(
        "R3-1 conditional U_gen=i*I_3 leaves the C3-circulant H fixed",
        np.allclose(U1 @ H @ U1.conj().T, H),
        "finite algebra only: this does not prove the physical charge-conjugation bridge"))

    # (2) the continuous centralizer diag(1,e^iphi,e^-iphi) also leaves H fixed (b unchanged) -> doesn't touch kappa
    phi = 0.8
    Uph = F @ np.diag([1, np.exp(1j * phi), np.exp(-1j * phi)]) @ F.conj().T
    passed.append(check(
        "R3-2 C-eigenbasis centralizer diag(1,e^iphi,e^-iphi) leaves H fixed and does not alter r",
        np.allclose(Uph @ H @ Uph.conj().T, H),
        "within the finite packet, this centralizer is a spectator to the block-count question"))

    # (3) the b-rotating map C->e^{i theta}C breaks C^3=I for generic theta.
    passed.append(check(
        "R3-3 exact check: C->e^{i theta}C breaks C^3=I for generic theta",
        rephased_c_breaks_cubic_identity(),
        "(e^{i*pi/7}C)^3 = e^{3i*pi/7}I != I, so only cube-root phases preserve C^3=I"))

    # (4) no Hermitian C3-circulant anticommutes with Gamma_chi except zero.
    passed.append(check(
        "R3-4 exact solve: no nonzero Hermitian C3-circulant anticommutes with Gamma_chi",
        no_nonzero_circulant_anticommutant(),
        "solving {H,Gamma_chi}=0 for H=aI+(x+iy)C+(x-iy)C^2 gives a=x=y=0"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: bounded finite-algebra support conditional on U_gen=i*I_3.")
    print("The runner does not assert that physical charge conjugation acts as I_3 on")
    print("generation space, does not close the Dirac/Majorana lane assignment, and")
    print("does not prove an exhaustive continuous-lever theorem. Remaining bridge:")
    print("derive the charged-lepton Dirac reality operator's generation action.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
