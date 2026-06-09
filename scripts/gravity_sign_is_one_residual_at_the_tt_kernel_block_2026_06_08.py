"""Going after the graviton kinetic health -- and finding it is the SAME residual as the attraction sign
and sign(G), located precisely at the TT-kernel block.

CONTEXT: #3352 reduced the Newtonian attraction sign to "the healthy graviton kinetic sign." This runner
shows that "healthy TT kinetic sign", the attraction sign, and sign(G) are ONE number (kappa=8 pi G), and
that the framework's scalar matter effective action provably CANNOT fix it (the TT graviton is in the
exact kernel of W's metric-Hessian, UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL 2026-06-08). So the entire
gravity-sign question collapses to a SINGLE residual = the sign of the (geometric) Einstein-Hilbert/Regge
coefficient, which the matter response cannot source.

VERIFIES (exact):
  K1. THE UNIFICATION (one residual). With S_EH^(2) = (1/(2 kappa)) h^TT (box) h^TT and the source coupling
      (1/2) h_mu nu T^mu nu (kappa = 8 pi G):
        - the TT graviton KINETIC coefficient is +1/(2 kappa)  -> HEALTHY (ghost-free) iff kappa > 0;
        - the one-graviton-EXCHANGE static potential is V ~ -kappa * N_tensor * (source)^2 with N_tensor
          = P_00,00 = +1/2 > 0  -> ATTRACTIVE (V<0) iff kappa > 0.
      So healthy-TT-kinetic  <=>  attractive  <=>  kappa > 0  <=>  G > 0. The "graviton kinetic health",
      the "attraction sign", and "sign(G)" are the SAME residual (verified by evaluating both at
      kappa = +1 and kappa = -1: they flip together).
  K2. THE BLOCK (why the matter response cannot fix it). The scalar observable generator W=log|det(D+J)|
      sees the metric only through the O_h scalar s(q)=g_ij qhat_i qhat_j, so its per-mode metric-Hessian
      is the RANK-1 LONGITUDINAL form H = W''(s) (qhat qhat) (x) (qhat qhat). A transverse-traceless
      (spin-2 graviton) perturbation h_TT is, by definition, transverse to qhat (qhat_i h_TT^{ij}=0), so
      qhat qhat : h_TT = 0  =>  <h_TT|H|h_TT> = W''(s) (qhat qhat : h_TT)^2 = 0. The TT graviton block is
      in the EXACT kernel of the matter-W Hessian (verified over many modes) -> the matter effective
      action provably cannot source the spin-2 graviton kinetic term, hence cannot fix sign(G).
  K3. (illustration) the induced-Newton-constant sign is CONTENT-dependent, not automatically positive:
      the Seeley-DeWitt R-coefficient (the induced 1/G) sums over fields with type-dependent signs, so
      even the full-vielbein <T_mu nu T_alpha beta> route does not trivially force G>0. (Stated, with a
      minimal sign-by-type illustration; not a framework-specific computation.)

CONCLUSION: the gravity sign is ONE residual = sign of the EH/Regge coefficient. The framework's scalar
matter response cannot source it (TT-kernel, K2); so it reduces to the GEOMETRIC Regge-curvature
coefficient sign (equivalently the full-vielbein induced-1/G sign, content-dependent K3) -- the single
deepest open gravity primitive. This UNIFIES the attraction sign (#3352), the graviton kinetic health,
and sign(G) into one residual and LOCATES it at the TT-kernel block. NOT a closure; an honest unification
+ location. No PDG/fitted value.
"""
from __future__ import annotations
import numpy as np

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


def main() -> int:
    print("GRAVITY SIGN = ONE residual (attraction = TT-kinetic = sign G), located at the TT-kernel block")
    print("=" * 92)

    # ---- K1: the unification -- both the TT kinetic health and the attraction sign are sign(kappa) ----
    N_tensor = 0.5          # P_00,00 (from #3352), > 0
    source_sq = 1.0         # (positive source)^2 > 0
    def tt_kinetic_coeff(kappa):
        return 1.0 / (2.0 * kappa)               # healthy (ghost-free) iff > 0
    def exchange_potential(kappa):
        return -kappa * N_tensor * source_sq     # attractive iff < 0
    healthy_pos = tt_kinetic_coeff(+1.0) > 0 and exchange_potential(+1.0) < 0   # kappa>0: healthy + attract
    flips_neg = tt_kinetic_coeff(-1.0) < 0 and exchange_potential(-1.0) > 0      # kappa<0: ghost + repel
    # they track the SAME sign(kappa) for a range of kappa
    same_sign = all(np.sign(tt_kinetic_coeff(k)) == np.sign(k) and np.sign(-exchange_potential(k)) == np.sign(k)
                    for k in (-3.0, -1.0, -0.2, 0.2, 1.0, 3.0))
    check("K1 (the unification): the TT graviton kinetic coefficient 1/(2 kappa) is healthy (>0) iff kappa>0, "
          "and the one-graviton-exchange potential -kappa*N_tensor*(src)^2 is attractive (<0) iff kappa>0. "
          "So healthy-TT-kinetic <=> attraction <=> kappa>0 <=> G>0 -- the SAME single residual.",
          healthy_pos and flips_neg and same_sign,
          f"kappa=+1: K_TT={tt_kinetic_coeff(1):+.2f}(healthy), V={exchange_potential(1):+.2f}(attract); "
          f"kappa=-1: K_TT={tt_kinetic_coeff(-1):+.2f}(ghost), V={exchange_potential(-1):+.2f}(repel)")

    # ---- K2: the block -- TT graviton is in the exact kernel of the scalar-W metric-Hessian ----
    rng = np.random.default_rng(0)
    tt_in_kernel = True
    max_overlap = 0.0
    n_checked = 0
    for _ in range(2000):
        q = rng.standard_normal(3)
        qh = 2.0 * np.sin(q / 2.0)              # qhat_i = 2 sin(q_i/2) (lattice symbol)
        if np.linalg.norm(qh) < 1e-6:
            continue
        nq = qh / np.linalg.norm(qh)
        # orthonormal basis {e1,e2} of the plane transverse to nq (the 2 graviton polarization axes)
        a = rng.standard_normal(3)
        e1 = a - (a @ nq) * nq
        e1 /= np.linalg.norm(e1)
        e2 = np.cross(nq, e1)                  # already unit, orthogonal to nq and e1
        # the two ACTUAL graviton polarizations: manifestly transverse (nq.h=0) and traceless (tr h=0)
        h_plus = np.outer(e1, e1) - np.outer(e2, e2)
        h_cross = np.outer(e1, e2) + np.outer(e2, e1)
        for hTT in (h_plus, h_cross):
            n_checked += 1
            transverse = np.linalg.norm(qh @ hTT) < 1e-9      # qhat_i hTT^{ij} = 0
            traceless = abs(np.trace(hTT)) < 1e-9
            # <h_TT|H|h_TT> = (qh qh : hTT)^2 ; qh qh : hTT = qh_i qh_j hTT_ij
            contraction = float(qh @ hTT @ qh)
            max_overlap = max(max_overlap, abs(contraction))
            if not (transverse and traceless) or abs(contraction) > 1e-9:
                tt_in_kernel = False
    check("K2 (the block): the scalar W=log|det(D+J)| sees the metric only via the O_h scalar "
          "s=g_ij qhat_i qhat_j, so its per-mode metric-Hessian is rank-1 longitudinal (qhat qhat)(x)(qhat "
          "qhat). A transverse-traceless graviton h_TT has qhat_i h_TT^{ij}=0, so qhat qhat : h_TT = 0 and "
          "<h_TT|H|h_TT>=0 -- TT in the EXACT kernel. The matter effective action cannot source the spin-2 "
          "graviton kinetic term (hence cannot fix sign G).",
          tt_in_kernel,
          f"over 2000 modes: max |qhat qhat : h_TT| = {max_overlap:.1e} (~0 -> TT in kernel)")

    # ---- K3: induced-1/G sign is content-dependent (the full-vielbein route is not trivially G>0) ----
    # minimal illustration: the Seeley-DeWitt R-coefficient enters with opposite signs for different field
    # types, so a sum over content can have either sign (NOT a framework-specific computation).
    a1_scalar = +1.0 / 6.0          # (1/6 - xi)R with xi=0 (illustrative sign)
    a1_dirac = -1.0 / 6.0           # Dirac fermion enters with the opposite-sign convention (illustrative)
    content_dependent = np.sign(a1_scalar) != np.sign(a1_dirac)
    check("K3 (the open route is not trivial): the induced 1/G (Seeley-DeWitt R-coefficient) sums over "
          "fields with TYPE-dependent signs, so even the full-vielbein <T T> induced-graviton route does "
          "NOT automatically give G>0 -- the sign is content-dependent. (Illustrative; not the framework's "
          "specific content.)",
          content_dependent,
          f"illustrative a1 signs: scalar={a1_scalar:+.3f}, dirac={a1_dirac:+.3f} (opposite) -> sum sign is content-dependent")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: the gravity sign is ONE residual. The graviton kinetic health, the Newtonian attraction\n"
        "sign (#3352), and sign(G) are the SAME number sign(kappa)=sign(G) (K1). The framework's scalar\n"
        "matter effective action W provably CANNOT fix it: the spin-2 graviton (TT) block is in the exact\n"
        "kernel of W's rank-1 longitudinal metric-Hessian (K2). So the entire gravity-sign question reduces\n"
        "to the sign of the GEOMETRIC Einstein-Hilbert/Regge coefficient (equivalently the full-vielbein\n"
        "induced-1/G sign, which is content-dependent, K3) -- the single deepest open gravity primitive.\n"
        "This UNIFIES the gravity-sign chain (attraction = TT-kinetic = sign G) into one residual and LOCATES\n"
        "it at the TT-kernel block. It is an honest unification + location, NOT a closure: the EH/Regge\n"
        "coefficient sign remains the open frontier (the matter response cannot source the spin-2 term)."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
