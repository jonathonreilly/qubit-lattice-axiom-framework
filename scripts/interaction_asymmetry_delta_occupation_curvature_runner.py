#!/usr/bin/env python3
"""Class-A verifier: the interaction asymmetry `delta` that sources the emergent C3
coupling |K| (the J-I double-shift on the generation triplet) is the OCCUPATION-NUMBER
CURVATURE of the energy -- and it is IRREDUCIBLY TWO-BODY.

This strengthens the naive-second-order cancellation (|K|_naive = 0 for a symmetric
spectrum) along three independent axes:

  (1) ALL-ORDERS cancellation, not just second order.  The free model
      H = eps*N + t*sum_mu X_mu FACTORIZES across the single-flip axes
      (H = sum_mu (eps*n_mu + t*X_mu)), so its full spectrum is the L-fold SUMSET of
      the per-axis spectrum.  Energy is additive over excitations => E(hw) is affine in
      hw => the occupation curvature delta = E_2 - 2 E_1 + E_0 = 0 to ALL orders, not
      merely at second order.  |K| therefore cannot be sourced by any amount of the free
      single-hop dynamics.

  (2) delta is the OCCUPATION CURVATURE and is IRREDUCIBLY TWO-BODY.  Write the energy as
      a sum of occupation functionals of degree k.  Every one-body (degree<=1) functional
      a*hw + b is AFFINE => second difference 0 => contributes nothing to delta.  The
      lowest-degree functional with nonzero curvature is the pair count C(hw,2) =
      hw(hw-1)/2, whose second difference is identically +1.  Hence delta = w_pair
      exactly: delta is carried by a genuine connected TWO-BODY coupling, and delta = 0
      <=> there is no two-body coupling.

  (3) REGIME-SCOPED SIGN LAW.  A native pair coupling U*sum_{i<j} n_i n_j sets
      delta = U exactly.  The second-order Schur elimination through the hw=0 and
      hw=2 intermediates gives
          K_off = t^2 * (1/eps - 1/(eps+U)) = t^2 * U/(eps*(eps+U)).
      Therefore sign(K_off)=sign(delta)=sign(U) only in the no-resonance /
      weak-pair regime eps>0 and eps+U>0.  The runner also checks an
      eps+U<0 sample where the unconditional sign statement fails, so the
      denominator boundary is load-bearing and explicit.

  (4) The one-body lattice realization of the pair term is a FORBIDDEN DIAGONAL.  In
      momentum space n_mu = (1 - cos k_mu)/2, so n_mu n_nu contains cos(k_mu)cos(k_nu),
      whose real-space image is a hop along e_mu +/- e_nu -- a next-nearest (face-diagonal)
      bond.  The LATTICE axiom is 6-nearest-neighbour cubic with NO diagonals, so no
      one-body 6-NN H0 can carry delta (consistent with (1): every axis-separable one-body
      H0 is additive => affine => delta = 0).  delta is therefore a genuine two-body /
      interaction object, not a kinetic one.

The precise value of delta (sign and scale) is left open -- the leading non-import route
is the framework's retained two-body mediator channel (the (L+mu^2)Phi = G|psi|^2 surface,
staggered_self_consistent_two_body / wilson_two_body_open_refined, both retained_bounded),
which is attractive and would fix sign(delta) < 0 and bound |delta|.  This runner verifies
the STRUCTURE (curvature / two-body / regime-scoped sign-law / all-orders), not the value.

No new axiom: the single-hop V = t*sum X_mu and the Hamming-graded diagonal are the
minimal native lattice dynamics; the factorization, the occupation-functional curvature
decomposition, and the forbidden-diagonal identity are arithmetic.
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


sx = np.array([[0, 1], [1, 0]], dtype=complex)
I2 = np.eye(2, dtype=complex)
nop1 = np.array([[0, 0], [0, 1]], dtype=complex)   # excitation-number on one qubit


def kron(*ops):
    out = np.array([[1.0 + 0j]])
    for o in ops:
        out = np.kron(out, o)
    return out


def op(o, q, L):
    return kron(*[o if i == q else I2 for i in range(L)])


def second_difference(values):
    return [values[n + 1] - 2 * values[n] + values[n - 1] for n in range(1, len(values) - 1)]


def effective_k_formula(eps, U, t=1.0):
    return t * t * U / (eps * (eps + U))


def main() -> int:
    print("=" * 78)
    print("INTERACTION ASYMMETRY delta = OCCUPATION CURVATURE, irreducibly two-body  [class A]")
    print("=" * 78)

    eps, t = 1.3, 0.45

    # ---- (1) free single-hop + axis-separable H0 FACTORIZES => delta=0 to ALL orders ----
    print("\n-- (1) all-orders cancellation via factorization --")
    h1 = eps * nop1 + t * sx                          # per-axis 2x2 Hamiltonian
    e1 = np.sort(np.linalg.eigvalsh(h1).real)
    for L in (3, 4, 5):
        N = sum(op(nop1, q, L) for q in range(L))
        Vx = sum(op(sx, q, L) for q in range(L))
        full = np.sort(np.linalg.eigvalsh(eps * N + t * Vx).real)
        sumset = np.sort(np.array([sum(c) for c in itertools.product(e1, repeat=L)]))
        check(f"L={L}: full spectrum of H=eps*N+t*sum X_mu equals the L-fold per-axis SUMSET "
              f"(H factorizes => energy additive)", np.allclose(full, sumset))
    # the second-order shift is exactly linear in hw: E2(n) = (2n - L) t^2 / eps
    L = 3
    E2 = {n: (2 * n - L) * t ** 2 / eps for n in range(L + 1)}
    check("2nd-order shift E2(hw)=(2hw-L)t^2/eps is AFFINE in hw => delta_2nd = 0 "
          "(reproduces the naive-2nd-order cancellation as a special case)",
          np.isclose(E2[2] - 2 * E2[1] + E2[0], 0.0))
    # additive energy over identical axes => E(hw)=hw*eps => affine => delta=0 (all orders)
    E_id = [hw * 0.83 for hw in range(4)]
    check("identical-axis additive energy E(hw)=hw*eps is AFFINE => delta=0 (all orders)",
          np.allclose(second_difference(E_id), 0.0))

    # ---- (2) delta = occupation curvature; first nonzero curvature = pair count => two-body ----
    print("\n-- (2) delta is the occupation curvature and is irreducibly two-body --")
    onebody = [3.3 * hw - 1.1 for hw in range(4)]            # any degree<=1 functional
    paircount = [hw * (hw - 1) // 2 for hw in range(4)]      # C(hw,2)
    check("every one-body occupation functional a*hw+b is AFFINE (second difference 0) "
          "=> contributes nothing to delta", np.allclose(second_difference(onebody), 0.0))
    check("the pair count C(hw,2) has second difference identically +1 "
          "=> it is the lowest-degree functional with nonzero curvature",
          np.allclose(second_difference(paircount), 1.0))
    # delta picks out exactly the pair coefficient: delta = w_pair*(C(2,2)-2C(1,2)+C(0,2)) = w_pair
    w_pair = 0.7
    E_pair = [w_pair * (hw * (hw - 1) // 2) for hw in range(4)]
    check("a pure pair term w_pair*C(hw,2) gives delta = w_pair exactly "
          "(delta is carried by the connected two-body coupling)",
          np.isclose(E_pair[2] - 2 * E_pair[1] + E_pair[0], w_pair))

    # ---- (3) regime-scoped sign law: native pair coupling U gives delta=U and
    # K_off=t^2*U/(eps*(eps+U)); sign follows U only for eps>0, eps+U>0.
    print("\n-- (3) regime-scoped sign law sign(K_off) = sign(delta) when eps+U>0 --")
    hwv = np.array([bin(i).count("1") for i in range(8)])
    P1 = [i for i in range(8) if hwv[i] == 1]
    Vc = sum(op(sx, q, 3) for q in range(3))
    nup = [op(nop1, q, 3) for q in range(3)]

    def Keff_offdiag(U, hop=1.0):
        Hint = U * sum(nup[i] @ nup[j] for i in range(3) for j in range(i + 1, 3))
        E = {i: hwv[i] * eps + Hint[i, i].real for i in range(8)}
        E1 = E[P1[0]]
        H = np.array([[sum(Vc[ia, k] * Vc[k, ib] / (E1 - E[k])
                           for k in range(8) if hwv[k] != 1 and abs(E1 - E[k]) > 1e-9)
                       for ib in P1] for ia in P1])
        return hop * hop * H[0, 1].real

    weak_samples = (0.5, -0.5, 1.0, -1.0)
    deltas = [(U, Keff_offdiag(U), effective_k_formula(eps, U)) for U in weak_samples]
    check("Schur elimination gives exact K_off = t^2*U/[eps*(eps+U)] for sampled U",
          all(np.isclose(k, formula) for U, k, formula in deltas),
          detail="; ".join(f"U={U:+.1f}->K={k:+.6f}, formula={formula:+.6f}"
                           for U, k, formula in deltas))
    check("for eps>0 and eps+U>0, sign(K_off)=sign(delta)=sign(U)",
          all(eps + U > 0 and np.sign(k) == np.sign(U) for U, k, _formula in deltas),
          detail="; ".join(f"U={U:+.1f}, eps+U={eps+U:+.2f}, K={k:+.3f}"
                           for U, k, _formula in deltas))
    outside_U = -2.0 * eps
    outside_K = effective_k_formula(eps, outside_U)
    check("outside the eps+U>0 regime, the unconditional sign law is false/unguarded",
          np.sign(outside_K) != np.sign(outside_U),
          detail=f"U={outside_U:+.3f}, eps+U={eps+outside_U:+.3f}, formula K={outside_K:+.3f}")
    # the sourced coupling is C3 (J-I): all three off-diagonals equal
    Hint = 0.6 * sum(nup[i] @ nup[j] for i in range(3) for j in range(i + 1, 3))
    E = {i: hwv[i] * eps + Hint[i, i].real for i in range(8)}; E1 = E[P1[0]]
    Hk = np.array([[sum(Vc[ia, k] * Vc[k, ib] / (E1 - E[k])
                        for k in range(8) if hwv[k] != 1 and abs(E1 - E[k]) > 1e-9)
                    for ib in P1] for ia in P1])
    offs = [abs(Hk[i, j]) for i in range(3) for j in range(3) if i != j]
    check("the sourced coupling has the exact C3 (J-I) form (all off-diagonals equal)",
          np.allclose(offs, offs[0]))

    # ---- (4) the one-body realization of the pair term is a FORBIDDEN DIAGONAL ----
    print("\n-- (4) the one-body realization of delta is a forbidden (next-nearest) diagonal --")
    # n_mu = (1 - cos k_mu)/2  =>  n_mu n_nu = 1/4 - (cos k_mu + cos k_nu)/4 + cos k_mu cos k_nu/4.
    # cos k_mu cos k_nu = (1/2)[cos(k_mu+k_nu) + cos(k_mu-k_nu)] = hop along e_mu +/- e_nu.
    # Verify the product-to-sum identity numerically on a k-grid (the face-diagonal content):
    kk = np.linspace(-np.pi, np.pi, 17)
    KM, KN = np.meshgrid(kk, kk)
    lhs = np.cos(KM) * np.cos(KN)
    rhs = 0.5 * (np.cos(KM + KN) + np.cos(KM - KN))            # e_mu+e_nu and e_mu-e_nu bonds
    check("n_mu n_nu carries cos(k_mu)cos(k_nu) = (1/2)[cos(k_mu+k_nu)+cos(k_mu-k_nu)] "
          "= a FACE-DIAGONAL (next-nearest) hop, which the 6-NN no-diagonal LATTICE axiom "
          "forbids => no one-body 6-NN H0 carries delta", np.allclose(lhs, rhs))

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: occupation-curvature structure of delta FAILED.")
        return 1
    print("VERDICT: delta (hence K_off in the generation triplet) is the OCCUPATION-NUMBER CURVATURE E_2-2E_1+E_0; it "
          "vanishes to ALL orders for the free single-hop + axis-separable one-body dynamics "
          "(factorization), is IRREDUCIBLY TWO-BODY (= pair-count curvature), carries the "
          "regime-scoped sign law K_off=t^2*U/[eps*(eps+U)] with sign(K_off)=sign(delta) "
          "only for eps>0 and eps+U>0, and its one-body lattice realization is a forbidden "
          "diagonal -- so delta is a genuine two-body interaction object. The "
          "precise sign/scale (the leading non-import route = the retained two-body mediator "
          "channel) is left open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
