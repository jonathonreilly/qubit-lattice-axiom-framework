#!/usr/bin/env python3
"""Finite check: product factorization does not force a carrier-value bridge."""

from __future__ import annotations

import numpy as np

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"[{status}] {name}" + (f" -- {detail}" if detail else ""))


def comm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def acomm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b + b @ a


def section(title: str) -> None:
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


tol = 1e-9
i2 = np.eye(2, dtype=complex)
i3 = np.eye(3, dtype=complex)
i4 = np.eye(4, dtype=complex)

sx = np.array([[0, 1], [1, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
sp = np.array([[0, 1], [0, 0]], dtype=complex)

section("A. Value-side generation algebra on C^3")
c3 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
jcs = (c3 - c3 @ c3) / np.sqrt(3.0)
p_singlet = np.ones((3, 3), dtype=complex) / 3.0
p_doublet = i3 - p_singlet
value_axis = 2.0 * p_singlet - i3

check("Jcs squares to minus the C3 doublet projector",
      np.allclose(jcs @ jcs, -p_doublet))
check("value_axis is an involution on C^3",
      np.allclose(value_axis @ value_axis, i3))
check("Jcs commutes with the value involution",
      np.allclose(comm(jcs, value_axis), 0))

grid = [0.0, 0.5, -1.0, 2.0]
ok_circ = True
for real_a in grid:
    for real_b in grid:
        for imag_b in grid:
            b = real_b + 1j * imag_b
            h = real_a * i3 + b * c3 + np.conj(b) * c3 @ c3
            ok_circ = ok_circ and np.allclose(comm(h, jcs), 0, atol=tol)
check("all tested circulant generation masses commute with Jcs",
      ok_circ, "orientation stays on the C^3 value side")

section("B. Carrier-side site algebra on C^2 tensor C^2")
o0 = np.kron(sp, i2)
o1 = np.kron(i2, sp)
c0 = np.kron(sp, i2)
c1 = np.kron(sz, sp)
carrier_axis = np.array(
    [[1, 0, 0, 0],
     [0, 0, 1, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 1]],
    dtype=complex,
)

check("single-site sigma_plus is nilpotent",
      np.allclose(sp @ sp, 0))
check("native cross-site ladders commute",
      np.allclose(comm(o0, o1), 0))
check("Jordan-Wigner cross-site ladders anticommute",
      np.allclose(acomm(c0, c1), 0))
check("carrier exchange axis is an involution",
      np.allclose(carrier_axis @ carrier_axis, i4))

section("C. Product-space bridge tests")
value_full = np.kron(value_axis, i4)
carrier_full = np.kron(i3, carrier_axis)

check("value and carrier axes commute on C^3 tensor C^2 tensor C^2",
      np.allclose(comm(value_full, carrier_full), 0))
check("commuting axes are not equal",
      not np.allclose(value_full, carrier_full))
check("commuting axes are not sign-reversed equal",
      not np.allclose(value_full, -carrier_full))

def projector(axis: np.ndarray, sign: int) -> np.ndarray:
    dim = axis.shape[0]
    return (np.eye(dim, dtype=complex) + sign * axis) / 2.0


joint_dims: dict[tuple[int, int], int] = {}
for value_sign in (1, -1):
    for carrier_sign in (1, -1):
        p = projector(value_full, value_sign) @ projector(carrier_full, carrier_sign)
        joint_dims[(value_sign, carrier_sign)] = int(round(np.trace(p).real))

check("all four value/carrier sign sectors are nonempty",
      all(dim > 0 for dim in joint_dims.values()), str(joint_dims))
check("mixed sector value=+1 carrier=-1 exists",
      joint_dims[(1, -1)] > 0, f"dim={joint_dims[(1, -1)]}")
check("mixed sector value=-1 carrier=+1 exists",
      joint_dims[(-1, 1)] > 0, f"dim={joint_dims[(-1, 1)]}")

section("D. Spin-blind generation action")
rng = np.random.default_rng(7)
a = rng.standard_normal((3, 3))
d = a - a.T
h_gen = 1j * d
h_full = np.kron(h_gen, i4)
site_spin_x = np.kron(i3, np.kron(sx / 2.0, i2))

check("generation operator is Hermitian after H=iD",
      np.allclose(h_gen.conj().T, h_gen))
check("generation operator commutes with site spin operator",
      np.allclose(comm(h_full, site_spin_x), 0))
check("product algebra leaves a bridge as an extra relation",
      all(dim > 0 for dim in joint_dims.values())
      and not np.allclose(value_full, carrier_full)
      and not np.allclose(value_full, -carrier_full))

print()
print("=" * 72)
print("VERDICT")
print("=" * 72)
print("The product-factor algebra permits independent value and carrier signs.")
print("A C^2-to-C^3 bridge can be added by a later theorem or admission,")
print("but it is not forced by factorization or tensor-factor commutation.")
print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")

if FAIL:
    raise SystemExit(1)
