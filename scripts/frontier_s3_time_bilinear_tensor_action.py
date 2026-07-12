#!/usr/bin/env python3
"""Exact current-form action/carrier variational-disconnection no-go.

The source note proves that

    I_TB(f,a) = I_R(f) + 1/2 ||a-k||^2

has tensor equation ``a=k`` and tensor Hessian ``I_4``, whereas

    Xi(t) = k tensor exp(-t Lambda)u

lives in ``R^4 tensor R^n`` and has generator ``I_4 tensor Lambda``.
This runner checks the structural identities on an exact rational witness and
includes the generator-bearing completion action as a falsifier/control.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.linalg import expm


TOL = 2.0e-12


@dataclass
class Check:
    name: str
    ok: bool
    detail: str
    status: str = "EXACT"


CHECKS: list[Check] = []


def record(name: str, ok: bool, detail: str, status: str = "EXACT") -> None:
    CHECKS.append(Check(name=name, ok=bool(ok), detail=detail, status=status))
    print(f"[{status}] {'PASS' if ok else 'FAIL'}: {name}")
    if detail:
        print(f"    {detail}")


def action_gradient(
    Lambda: np.ndarray,
    f: np.ndarray,
    j: np.ndarray,
    a: np.ndarray,
    k: np.ndarray,
) -> np.ndarray:
    """Gradient of 1/2 f^T Lambda f-j^T f + 1/2 ||a-k||^2."""

    return np.concatenate((Lambda @ f - j, a - k))


def action_hessian(Lambda: np.ndarray) -> np.ndarray:
    n = Lambda.shape[0]
    return np.block(
        [
            [Lambda, np.zeros((n, 4), dtype=float)],
            [np.zeros((4, n), dtype=float), np.eye(4, dtype=float)],
        ]
    )


def carrier(k: np.ndarray, Lambda: np.ndarray, u: np.ndarray, t: float) -> np.ndarray:
    """Row-major vectorization of outer(k, exp(-t Lambda)u)."""

    return np.kron(k, expm(-t * Lambda) @ u)


def main() -> int:
    print("CURRENT-FORM TENSORIZED ACTION / CARRIER VARIATIONAL-DISCONNECTION NO-GO")
    print("=" * 86)

    # Exact integer SPD witness.  Its eigenvalues are positive and no fitted or
    # observed value enters the calculation.
    Lambda = np.array(
        [
            [3.0, -1.0, 0.0],
            [-1.0, 3.0, -1.0],
            [0.0, -1.0, 2.0],
        ]
    )
    n = Lambda.shape[0]
    eigvals = np.linalg.eigvalsh(Lambda)

    u_e, u_t, delta = 2.0, -1.0, 3.0 / 5.0
    K = np.array([[u_e, u_t], [delta * u_e, delta * u_t]], dtype=float)
    k = K.reshape(-1)
    u = np.array([1.0, 2.0, -1.0], dtype=float)
    u /= np.linalg.norm(u)

    f_star = np.array([1.0, -2.0, 3.0], dtype=float) / 7.0
    j = Lambda @ f_star
    a_star = k.copy()

    H = action_hessian(Lambda)
    mixed_norm = float(np.linalg.norm(H[:n, n:], ord="fro"))
    tensor_hessian_error = float(np.linalg.norm(H[n:, n:] - np.eye(4), ord="fro"))
    grad_at_star = action_gradient(Lambda, f_star, j, a_star, k)

    G = np.kron(np.eye(4), Lambda)
    A0 = np.kron(k, u)
    xi0 = carrier(k, Lambda, u, 0.0)
    dxi0 = -G @ xi0
    t = 0.7
    xi_t = carrier(k, Lambda, u, t)
    xi_from_generator = expm(-t * G) @ A0
    semigroup_error = float(np.max(np.abs(xi_t - xi_from_generator)))

    # Independent centered finite difference inside the t>=0 semigroup domain.
    h = 1.0e-6
    t_fd = 0.4
    xi_fd_center = carrier(k, Lambda, u, t_fd)
    dxi_fd = (
        carrier(k, Lambda, u, t_fd + h)
        - carrier(k, Lambda, u, t_fd - h)
    ) / (2.0 * h)
    ode_error = float(np.max(np.abs(dxi_fd + G @ xi_fd_center)))

    # The original a-sector gradient flow da/dt=-(a-k) is static at its
    # stationary value.  It cannot equal the nonzero carrier derivative.
    da_current = -(a_star - k)

    # The control action S_gen(A)=1/2 A^T G A does carry the missing generator.
    control_gradient_error = float(np.max(np.abs((G @ A0) + dxi0)))

    K_det = float(np.linalg.det(K))
    K_rank = int(np.linalg.matrix_rank(K, tol=1e-13))
    Xi_matrix = xi_t.reshape(4, n)
    Xi_rank = int(np.linalg.matrix_rank(Xi_matrix, tol=1e-13))

    record(
        "the witness Lambda is symmetric positive definite",
        np.array_equal(Lambda, Lambda.T) and float(np.min(eigvals)) > 0.0,
        f"eigenvalues={np.array2string(eigvals, precision=12)}",
    )
    record(
        "the displayed action has Hessian diag(Lambda, I_4) and no f-a coupling",
        mixed_norm == 0.0 and tensor_hessian_error == 0.0,
        f"mixed Frobenius norm={mixed_norm:.3e}, tensor-Hessian error={tensor_hessian_error:.3e}",
    )
    record(
        "the current stationary equations are Lambda f=j and a=k",
        float(np.max(np.abs(grad_at_star))) < TOL,
        f"max stationary-gradient residual={np.max(np.abs(grad_at_star)):.3e}",
    )
    record(
        "the declared carrier has a nonzero I_4 tensor Lambda time derivative",
        float(np.linalg.norm(dxi0)) > 1.0e-6 and ode_error < 2.0e-9,
        f"||dXi/dt at t=0||={np.linalg.norm(dxi0):.6e}, finite-difference ODE error={ode_error:.3e}",
    )
    record(
        "the displayed tensor penalty is static at a=k and does not contain the carrier generator",
        float(np.linalg.norm(da_current)) == 0.0
        and H[n:, n:].shape == (4, 4)
        and G.shape == (4 * n, 4 * n),
        f"||da/dt||={np.linalg.norm(da_current):.3e}, penalty Hessian shape={H[n:, n:].shape}, carrier generator shape={G.shape}",
    )
    record(
        "the generator-bearing completion control reproduces Xi exactly",
        semigroup_error < TOL and control_gradient_error < TOL,
        f"exp(-tG) factorization error={semigroup_error:.3e}, gradient-flow error={control_gradient_error:.3e}",
        status="CONTROL",
    )
    record(
        "the named bilinear K_R and reshaped Xi_TB are rank at most one",
        abs(K_det) < TOL and K_rank <= 1 and Xi_rank <= 1,
        f"det(K_R)={K_det:.3e}, rank(K_R)={K_rank}, rank(Xi_TB)={Xi_rank}",
    )
    record(
        "for n>=2 the current action domain and carrier field have different dimensions",
        all((m + 4) != 4 * m for m in range(2, 33)),
        f"verified n=2..32; witness action-domain dimension={n + 4}, carrier dimension={4 * n}",
    )

    print("\nExact boundary:")
    print(
        "The displayed I_TB supplies only the algebraic equation a=k.  The "
        "displayed Xi_TB evolves in a larger field space under I_4 tensor "
        "Lambda.  A generator-bearing tensor-field action reproduces Xi_TB, "
        "but that action and field are additional structure, not a consequence "
        "of the current I_TB definition."
    )
    print("This is a current-form no-go, not a no-go against enlarged tensor actions or GR in general.")

    print("\n" + "=" * 86)
    n_pass = sum(c.ok for c in CHECKS)
    n_fail = sum(not c.ok for c in CHECKS)
    print(f"SUMMARY PASS={n_pass} FAIL={n_fail} TOTAL={len(CHECKS)}")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
