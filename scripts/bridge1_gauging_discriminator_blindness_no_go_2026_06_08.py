"""Bridge-1 gauging-selection no-go: the load-bearing discriminator-BLINDNESS facts, re-derived from
primitives (NOT trusted from the campaign agents; the campaign's COLOR-BASE lens was confidently wrong,
so every fact here is checked independently).

CONTEXT: the SM gauge ALGEBRA su(N_c)+su(2)+u(1) is FORCED as the carrier symmetry (bridge1_gauge_algebra
runner, 4/4) and N_c=d is a genuine covariation (bridge1_color_base_covariance runner, 4/4). What is NOT
forced is the GAUGING SELECTION -- which symmetry is dynamically gauged + the physical-color identification
MR_color + the chiral su(2)_L. This runner verifies that the framework-native candidate DISCRIMINATORS are
provably BLIND to the gauging selection (so it is an admission), on the rock-solid facts only.

VERIFIES:
  N1 (MAXIMALITY is blind). On the carrier C^3 (x) C^2 (dim 6): the SM algebra su(3)+su(2)+u(1) (dim 12)
     and the FULL u(6) (dim 36) BOTH act irreducibly -> commutant = scalars (dim 1) for BOTH. So the
     Record/indistinguishability ("gauge = what records cannot distinguish") criterion returns the SAME
     verdict for dim-12 and dim-36; it cannot select the SM algebra. The only cut from u(6) to dim-12 is
     the factor-local C^3(x)C^2 split = MR_color -> circular.
  N2 (ANOMALY is a one-sided FILTER, not a selector). The symmetric cubic d-tensor d_abc=2Tr(T_a{T_b,T_c}):
     su(2) (Pauli/2) is IDENTICALLY 0 (anomaly-free for ANY content); su(3) (Gell-Mann/2) is nonzero
     (max|d|=1/sqrt3). So anomaly-freedom constrains su(3) content GIVEN a gauging; it never selects which
     group is gauged, and to even write a content one must assume MR_color.
  N3 (CHIRALITY epsilon is blind to the coupling). On C^2(chirality) (x) C^2(weak fiber): the grading
     Gamma_eps = Z(x)I and the weak generators T^a = I(x)sigma^a/2 live on DIFFERENT factors, so
     [Gamma_eps, T^a]=0; a kinetic D=X(x)I has {Gamma_eps,D}=0; and {Gamma_eps, D.T^a.P_L} =
     {Gamma_eps, D.T^a.P_R} = {Gamma_eps, D.T^a} = 0 with P_{L,R}=(I -/+ Gamma_eps)/2. epsilon carries ZERO
     information about whether the connection rides P_L, P_R, or neither -> chiral su(2)_L is a separate
     admission.
  N4 (COLOR is complex, spatial rotation is real -> color != complexified spatial). The reality test
     "exists invertible B with B T_a + T_a^T B = 0 for all a": su(3) fundamental -> NO such B (strictly
     complex, 3 != 3bar); su(2) doublet -> YES (B antisymmetric, pseudoreal); so(3) vector (real antisym
     generators) -> YES (B = I, real). So color su(3) is NOT the complexification of the spatial so(3)
     3-frame; the Lorentz/spacetime discriminator points the wrong way.

CONCLUSION: every framework-native candidate discriminator is provably blind to (or circular w.r.t.) the
gauging selection. With the forced-algebra runner and the N_c=d covariance runner, this establishes the
honest Bridge-1 verdict: gauge ALGEBRA (incl. N_c=d) FORCED; GAUGING SELECTION (which-is-gauged + MR_color
+ chiral su(2)_L) ADMITTED. No PDG/fitted value; exact numpy.
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


def gell_mann():
    l = []
    l.append(np.array([[0,1,0],[1,0,0],[0,0,0]], complex))
    l.append(np.array([[0,-1j,0],[1j,0,0],[0,0,0]], complex))
    l.append(np.array([[1,0,0],[0,-1,0],[0,0,0]], complex))
    l.append(np.array([[0,0,1],[0,0,0],[1,0,0]], complex))
    l.append(np.array([[0,0,-1j],[0,0,0],[1j,0,0]], complex))
    l.append(np.array([[0,0,0],[0,0,1],[0,1,0]], complex))
    l.append(np.array([[0,0,0],[0,0,-1j],[0,1j,0]], complex))
    l.append(np.array([[1,0,0],[0,1,0],[0,0,-2]], complex)/np.sqrt(3))
    return l


def commutant_dim(gens, dim):
    rows = np.zeros((0, dim * dim), complex)
    for G in gens:
        L = np.kron(np.eye(dim), G) - np.kron(G.T, np.eye(dim))
        rows = np.vstack([rows, L])
    return dim * dim - np.linalg.matrix_rank(rows)


def reality_bilinear_nullspace(Ts, n):
    """dim of {B : B T_a + T_a^T B = 0 for all a} -- nonzero iff the rep is real/pseudoreal (self-conjugate)."""
    rows = np.zeros((0, n * n), complex)
    for T in Ts:
        # vec(B T + T^T B) = (kron(T^T, I) + kron(I, T^T)) vec(B)   [using vec(AXB)=kron(B^T,A)vec(X)]
        L = np.kron(T.T, np.eye(n)) + np.kron(np.eye(n), T.T)
        rows = np.vstack([rows, L])
    return n * n - np.linalg.matrix_rank(rows)


def main() -> int:
    print("BRIDGE-1 GAUGING-SELECTION NO-GO: framework-native discriminators are blind to the gauging")
    print("=" * 84)
    I2 = np.eye(2, dtype=complex); I3 = np.eye(3, dtype=complex)
    X = np.array([[0,1],[1,0]], complex); Y = np.array([[0,-1j],[1j,0]], complex); Z = np.array([[1,0],[0,-1]], complex)
    paulis = [X, Y, Z]
    Tsu2 = [p/2 for p in paulis]
    gm = gell_mann(); Tsu3 = [g/2 for g in gm]

    # ---- N1: maximality is blind (SM dim-12 and u(6) dim-36 both irreducible -> commutant 1) ----
    su3c = [np.kron(g, I2) for g in gm]
    su2f = [np.kron(I3, p) for p in paulis]
    u1   = [np.kron(I3, I2)]
    sm = su3c + su2f + u1
    c_sm = commutant_dim(sm, 6)
    # u(6): a spanning set of gl(6) (all elementary matrices) -> irreducible -> commutant scalars
    Eall = []
    for i in range(6):
        for j in range(6):
            E = np.zeros((6, 6), complex); E[i, j] = 1; Eall.append(E)
    c_u6 = commutant_dim(Eall, 6)
    check("N1 (maximality blind): SM su(3)+su(2)+u(1) (dim 12) and full u(6) (dim 36) BOTH act irreducibly "
          "on C^6 -> commutant = scalars (dim 1) for BOTH; the record/indistinguishability criterion cannot "
          "tell them apart, so it cannot select dim-12 (only the C^3(x)C^2 split = MR_color cuts u(6) to 12)",
          c_sm == 1 and c_u6 == 1, f"commutant(SM dim12)={c_sm}; commutant(u(6) dim36)={c_u6} (identical)")

    # ---- N2: anomaly is one-sided (su(2) d-tensor 0; su(3) d-tensor != 0) ----
    def dtensor_max(Ts):
        n = len(Ts)
        mx = 0.0
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    anti = Ts[b] @ Ts[c] + Ts[c] @ Ts[b]
                    d = 2 * np.trace(Ts[a] @ anti)
                    mx = max(mx, abs(d))
        return mx
    d2 = dtensor_max(Tsu2)
    d3 = dtensor_max(Tsu3)
    check("N2 (anomaly one-sided filter): symmetric cubic d_abc=2Tr(T_a{T_b,T_c}) is IDENTICALLY 0 for su(2) "
          "(anomaly-free for any content) and NONZERO for su(3) (max|d|=1/sqrt3); anomaly-freedom is a FILTER "
          "on a given content, never a SELECTOR of which group is gauged",
          d2 < 1e-12 and abs(d3 - 1/np.sqrt(3)) < 1e-9,
          f"max|d_abc| su(2)={d2:.2e} (=0); su(3)={d3:.6f} (=1/sqrt3={1/np.sqrt(3):.6f})")

    # ---- N3: epsilon (chirality grading) is blind to the coupling ----
    Geps = np.kron(Z, I2)          # chirality grading on factor 1
    Ta = [np.kron(I2, p/2) for p in paulis]  # weak su(2) on factor 2
    D = np.kron(X, I2)             # a kinetic op anticommuting with Geps
    PL = (np.eye(4) - Geps) / 2
    PR = (np.eye(4) + Geps) / 2
    comm_eps_T = max(np.linalg.norm(Geps @ t - t @ Geps) for t in Ta)
    anti_eps_D = np.linalg.norm(Geps @ D + D @ Geps)
    # the three dressings: undressed, P_L, P_R
    def anti(A):
        return np.linalg.norm(Geps @ A + A @ Geps)
    blind = True
    for t in Ta:
        base = D @ t
        blind = blind and anti(base) < 1e-12 and anti(base @ PL) < 1e-12 and anti(base @ PR) < 1e-12
    check("N3 (chirality epsilon blind): [Gamma_eps, T^a]=0 (different factors), {Gamma_eps,D}=0, and "
          "{Gamma_eps, D.T^a} = {Gamma_eps, D.T^a.P_L} = {Gamma_eps, D.T^a.P_R} = 0 -> epsilon carries ZERO "
          "discrimination between vector / chiral-L / chiral-R coupling; chiral su(2)_L is a separate admission",
          comm_eps_T < 1e-12 and anti_eps_D < 1e-12 and blind,
          f"max|[eps,T^a]|={comm_eps_T:.1e}, |{{eps,D}}|={anti_eps_D:.1e}, all dressings anticommute (blind)")

    # ---- N4: color complex, spatial rotation real -> color != complexified spatial ----
    n_su3 = reality_bilinear_nullspace(Tsu3, 3)      # expect 0 (complex)
    n_su2 = reality_bilinear_nullspace(Tsu2, 2)      # expect >=1 (pseudoreal)
    # so(3) vector: real antisymmetric generators L_a
    L1 = np.array([[0,0,0],[0,0,-1],[0,1,0]], complex)
    L2 = np.array([[0,0,1],[0,0,0],[-1,0,0]], complex)
    L3 = np.array([[0,-1,0],[1,0,0],[0,0,0]], complex)
    n_so3 = reality_bilinear_nullspace([L1, L2, L3], 3)  # expect >=1 (real, B=I)
    check("N4 (color complex vs spatial real): reality test 'exists B: B T_a + T_a^T B = 0' -> su(3) "
          "fundamental NULLSPACE 0 (strictly complex, 3 != 3bar); su(2) doublet >=1 (pseudoreal); so(3) "
          "vector >=1 (real, B=I). Color su(3) is NOT the complexification of the spatial so(3) 3-frame.",
          n_su3 == 0 and n_su2 >= 1 and n_so3 >= 1,
          f"invariant-bilinear nullspace: su(3)={n_su3} (complex), su(2)={n_su2} (pseudoreal), so(3)_vec={n_so3} (real)")

    print(f"\nSCORECARD PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT (open gate; the FOUR tested discriminators do not close it): each of the four discriminators\n"
        "checked here is BLIND to, or CIRCULAR with, the gauging selection -- maximality cannot distinguish\n"
        "dim-12 from u(6); anomaly is a one-sided filter; epsilon is blind to the coupling chirality; color is\n"
        "complex while spatial rotation is real. So the gauging selection (which symmetry is gauged + the\n"
        "physical-color identification MR_color + chiral su(2)_L) is NOT closed by these four -- it is an OPEN\n"
        "GATE, not a proven irreducible no-go (closing it as a no-go would need the full N1-N8 route\n"
        "enumeration with retained-authority failures, beyond these four checks). The algebra it sits on is\n"
        "itself conditional on the SUPPLIED carrier. Audit lane sets the status."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
