# Native six-layer ground-sector selection

Status: conditional-support. Within the supplied one-qubit Hamiltonian and fixed even periodic R by R by 6 geometry, the previously prepared positive plane-character vacuum is selected by the microscopic ground for sufficiently small positive lambda. The smallness threshold depends on R. This is not a uniform thermodynamic assertion or an observed vacuum identification.

## Derivation from native spin counts

Use the Hamiltonian and matched canonical convention in SIX_LAYER_NEUTRAL_POLE_PROOF.md. First reduce across the order-J wall gap at fixed R. A wall-free off-diagonal matrix element changing k complete columns flips 6k spins. It therefore requires at least 3k native transverse insertions. Exact longitudinal Z-plane parity forces k even. At k=2, order six is possible only for adjacent columns, with one insertion at each longitudinal layer. Its coefficient is -gamma, gamma=63/8192. This is the existing winding vertex, not an added logical interaction.

The first background splitting is the order-four diagonal plaquette energy. Its flat code consists of signs s_xy=a_x b_y. Exact row/column plane flips act transitively on these signs, so all diagonal effective terms restricted to that code are scalar. At fixed R, subtract that scalar and divide by lambda^4 before the second analytic reduction. The complement has a nonzero order-one plaquette gap; four defects cost Delta=3/8 in these units.

For r off-diagonal jumps changing k_j columns, native powers and r-1 flux denominators give a lower weighted order

  3 sum k_j - 4(r-1) = sum k_j + 4 + 2 sum(k_j-2) >= m+4,

where m is the final changed-column count. Higher diagonal corrections increase order; the leading diagonal is already included in the flux resolvent. Equality requires every jump to be an adjacent two-column order-six winding and no column to repeat. Folded visits to the flat subspace cannot precede its first nonconstant transition.

A nonempty flat pattern has at least R changed columns. For R>=8 its only minimum supports are one complete row or column: a pattern with a rows and b columns has weight R(a+b)-2ab, modulo simultaneous complementation. Thus first nonconstant flat dynamics occurs at order R+4.

## Coefficient and sign

Cover the selected row cycle by n=R/2 disjoint adjacent pairs. Exactly two perfect matchings exist. For a proper subset of a matching with c occupied runs, the intermediate syndrome has 4c defects, costing Delta c. The exact ordering sum is

  sum_orders product_intermediate 1/c = binomial(2n-2,n-1).

This is the same cyclic component recurrence proved for the whole-column winding coefficient (WHOLE_COLUMN_MODE_PROOF.md); the runner independently evaluates its rational subset recursion. The matching's path graph is the n-cycle. Each hop has negative sign and each resolvent denominator is negative, leaving an overall negative transition. There is no proper flat intermediate state, hence no subtraction of this leading off-diagonal term. Therefore

  H_flat = scalar - J t_R lambda^(R+4) (sum_x R_x + sum_y C_y)
           + o_R(J lambda^(R+4)),
  t_R = 2 binomial(R-2,R/2-1) gamma^(R/2) / Delta^(R/2-1) > 0.

The row/column logical operators commute with the single relation product R_x=product C_y. Their regular flat-code representation has one state per compatible character. All characters positive uniquely minimize the displayed operator. At least two signs must change for another compatible character, so its leading gap is 4J t_R lambda^(R+4).

## Actual microscopic ground and honest limit

A sixth-order truncation cannot resolve this exponentially high-order splitting. Instead fix R first and carry finite-dimensional analytic block reduction to the needed order R+4, with remainder o_R(lambda^(R+4)). The spin-count lower bound exhausts all potentially competing leading paths. The positive leading splitting then selects the all-positive character for sufficiently small lambda. Nonflat states remain separated at order lambda^4 and wall states at order one.

Physical X planes give one family of logical flips. A physical Y plane contributes (-1)^R times the other logical flip on aligned six-spin columns, hence the same sign for even R. Every flat pattern has positive Z-plane product for even R. Exact symmetries preserve these labels under dressing. Thus the selected fibre in the preceding pole theorem is the actual ground fibre at fixed R sufficiently weak coupling.

This retires the explicit state preparation premise for the ordered weak-coupling-then-size limit. It does not establish ground selection along R proportional to log(1/lambda), because no uniform remainder relative to t_R lambda^(R+4) is proved. An existence-only diagonal sequence lambda_R can be chosen below each finite-size threshold and each finite-size pole/source error threshold; then global-ground source coefficients converge to the same pole residue. That sequence is not a derived scale relation or a fixed-lambda bulk limit.

The scalar-like pole remains repulsively bound with negative small-momentum curvature and planar dynamics. Hamiltonian, anisotropy, geometry and measurement identification are still premises. No empirical data are used or independently tested.
