<!-- Original PR9819 source SHA256 c2d8e32ef8eb9e2e2866f3ed5ed73f324973e8be0d0fc00b03e5b28c702642e0. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# An actual native neutral pole at resolved long wavelength

Status: conditional-support. This block seeks to remove the logarithmic-grid restriction in `TEN_LAYER_NEUTRAL_BOUND_PROOF.md`. The Hamiltonian, fixed ten-layer periodic slab, weak anisotropy and selected exact plane fibre remain premises. There are no new physical qubits or interactions.

## 1. Statement and scales

Set L=10 and choose even R comparable to lambda^(-p), with any fixed 1<p<2 (use p=3/2 for the concrete controls). Fix the all-positive exact plane-character fibre and its ground state. For a fixed nonzero integer vector n, take transverse q=2pi n/R and Qz=0. Thus q/lambda tends to zero. Let E_-(q) denote the lower endpoint-bound neutral excitation in its exact momentum fibre. The result is

    E_-(q)-E_-(0) = J(kappa/2)lambda^12 |q|²[1+o(1)],
    kappa=4gamma²/v > 0,
    gamma=12155/33554432, v=45/16384.

The original normalized ZZ readout has an atom at this pole with weight

    (2gamma² beta²/L)lambda^20[1+o(1)],
    beta=6(L-1)(L-2)/(2(2L-3))-3.

The pole is isolated within each momentum/plane fibre; its nearest orientation partner is separated by 2J eta lambda^14[1+o(1)], eta=4gamma²/D, D=15/512. This is not a claim that the full band has a uniform gap between neighbouring momenta. The global ground character is not selected uniformly. Neither three-dimensional propagation nor relativistic/cosmological identification follows.

## 2. First local normal form: broken vertical bonds

For any fixed large order, the existing local N normal form writes UHU^dag/J=2N+sum_j lambda^j D_j+Remainder. The coefficients are sums of connected bounded-support terms, individually N-preserving after local charge averaging, and plane invariant after finite symmetry averaging. The interaction-norm tail is bounded by C lambda^M; its global norm on fixed-height R² sites is at most C R²lambda^M. One can choose M=40 here and construct both Hamiltonian and readout transformations to sufficient fixed order. Constants may be large but are independent of R. No assertion of convergence of an infinite normal-form series is needed.

The fixed-height column can be encoded by one reference spin and L-1 independent wall bits, the last wall being fixed by even wall parity. This is a unitary labeling of the original spins, not additional degrees of freedom. Extend each N0 coefficient to act on reference spins and as identity on wall labels. Away from columns with walls, it agrees with the original coefficient. Enlarge each support to whole columns; L is fixed. The difference is sandwiched by the projector onto at least one wall in those columns. Bounded overlap therefore gives a form bound C_j N. Summing j>=1 gives

    2N + H_col - C lambda N <= B <= 2N + H_col + C lambda N.

After removing its scalar, H_col begins at lambda^4 and has bandwidth O(lambda^4 R²). Since p<2, this tends to zero. N is even, so the whole N0 band is separated from N>=2 by 4-O(lambda)-O(lambda^4R²). The small global remainder consequently permits an exact microscopic N0 identification, with error controlled by C R²lambda^M. This argument includes full-column flips in H_col; it does not incorrectly treat them as impossible at fixed L.

## 3. Second local normal form: bad plaquettes

Inside N0 define B_a=(1-P_a)/2 and Q=sum_a B_a. These commuting local projectors have integer total charge. After subtracting scalar and dividing by lambda^4,

    K_col = (L/64)Q + lambda² K_2 + lambda^4 K_4 + ... .

The first off-diagonal column-changing terms occur at lambda^6 in this normalization. Work directly in the physical column-spin algebra, restricted to the chosen invariant sector. A dual plaquette representation may illustrate the charge, but is not needed as an enlarged Hilbert space. Physical row/column syndrome parity and even enclosed-area restrictions must be retained.

For a local operator, averaging exp(itQ) A exp(-itQ) over a period projects its charge-zero part. Only plaquettes meeting its support act nontrivially. Inverting ad_Q on nonzero integer charge differences therefore also preserves bounded support after a fixed enlargement. The usual finite-order nested-commutator construction gives another local unitary, with individually Q-preserving connected coefficients and arbitrarily high fixed-order local remainder. All translations, plane symmetries, real structure and spatial reflections can be retained by equivariant construction. Restoring lambda^4, arrange the global tail again below C R²lambda^40.

The key bound is termwise. For a Q-preserving plane-invariant local coefficient t, enlarge its support by all affected plaquettes. If there is no bad plaquette in this neighborhood, t cannot create any: it cannot change Q elsewhere. A finite-support operation preserving all local plaquettes cannot be a nontrivial flat row/column flip once R exceeds that fixed support. Its remaining diagonal action on a flat neighborhood is background-independent by the plane symmetries. Write that scalar as alpha_t. Then

    t-alpha_t I = Pi_t(t-alpha_t I)Pi_t,
    Pi_t <= sum_(a near t) B_a.

Bounded overlap yields |sum_t(t-alpha_t I)| <= C Q as quadratic forms. On Q=m its norm is bounded by Cm, independently of area. This argument is made in the constrained physical algebra, not inferred from the summed Q0 block alone.

Thus, after subtracting the flat vacuum energy, the normal form is

    J lambda^4[(L/64)Q + O(lambda²)Q].

The selected Q0 state is unique in its fixed plane fibre. Q4 is uniformly separated from every other allowed charge sector by order Jlambda^4. Its higher coefficients have uniform norm. Disconnected vacuum-return terms, including apparently volume-enhanced off-diagonal hopping, cancel inside the connected local normal form. Subtracting only a diagonal vacuum energy would not suffice.

A direct second-order check makes the cancellation explicit. Two distant local four-flux patterns A and B communicate via Q0 with denominator +4 and via their disjoint eight-flux union with denominator -4. The sum is zero. The companion exact-rational runner checks the entire vacuum-subtracted second-order row on increasing periodic grids, not just that example.

## 4. Uniform low-defect reductions and momentum moments

Four bad plaquettes satisfying row/column parity are rectangle corners; physical column parity further requires even enclosed area. The inherited sixth-order diagonal coefficient separates thin rectangles from nonthin ones by JDlambda^6. The eighth-order straight-triple term lowers the two shortest thin orientations by Jv lambda^8. These are uniform separations after subtracting common energies, because all higher Q4 coefficients have volume-independent norm.

Perform finite-order reductions first across the thin/nonthin separation and then across the shortest-thin/rest separation. Divide by the relevant leading power before constructing each finite-order transformation. The perturbations are smaller by positive powers of lambda. At every fixed order a coefficient is a finite sum of paths of local operations and diagonal denominators. Each path can move the feature center by only a bounded distance at that order. Its row sum and its row sum weighted by the square (or any fixed power) of center displacement are bounded independently of R. This supplies uniform second and fourth momentum derivatives of the retained two-orientation matrix. A norm bound without these spatial moments would not suffice.

The subsequent two low-defect reductions are also carried to sufficiently high fixed order, after accounting for their lambda^6 and lambda^8 denominators, so their absolute tails are bounded by C R²lambda^40. Diagonal projectors and resolvents do not move configurations, so the stated spatial-moment bounds survive those reductions.

The charge reduction first changes the Hamiltonian at order lambda^16: its generator begins at lambda^6 and the off-diagonal winding at lambda^10. Thus it leaves the previously derived leading dispersion lambda^12 and orientation mixing lambda^14 intact. Native spin counting excludes a direct lower-order endpoint translation. Keep every common diagonal correction, including orders ten, twelve and fourteen, in an unspecified common scalar e(lambda); none is silently set to zero.

On the even periodic lattice, the product of Z on one bipartite sublattice sends lambda to -lambda. Its restriction to N0 is either identity or the conserved whole-column Z parity, hence a scalar in the selected parity sector. The equivariant effective Hamiltonian is therefore even in lambda; there is no order-thirteen dispersive term.

Using centered translated endpoint states, inversion and real symmetry make the effective 2 by 2 matrix real and even in q. C4 equates its diagonal entries at q=0. Its trace-half difference is

    tr[h(q)-h(0)]/2
      = J(kappa/2)lambda^12 |q|²
        + O(Jlambda^12 |q|^4 + Jlambda^14 |q|²).

Its off-diagonal entry at zero is -Jeta lambda^14[1+O(lambda²)], and its q-change is O(Jlambda^14 |q|²). Its diagonal difference vanishes at zero and is O(Jlambda^12 |q|²). The lower eigenvalue therefore obeys

    E_eff(q)-E_eff(0)
      = J(kappa/2)lambda^12 |q|²
        + O(Jlambda^14 |q|² + Jlambda^10 |q|^4)
        + O(JR²lambda^40).

The lambda^10 |q|^4 term is the orientation-mixing correction: divide the squared diagonal imbalance by the lambda^14 gap. For q comparable to lambda^p with p>1 all displayed errors are relatively small. At p=3/2 the leading power is 15, the anisotropic correction power is 16, and the global tail power is 37. This resolves the earlier logarithmic-grid limitation while preserving the distinction between a selected fibre and a global ground theorem.

## 5. Original-source transfer

Apply the same local transformations to the original normalized Fourier ZZ source C_Q. In the selected flat vacuum the centered Q0-to-Q4 part first occurs at lambda^10. The diagonal-source/vacuum-mixing subtraction and direct winding term give the coefficient derived previously: at q=0 it is -gamma beta(A+B)/sqrt(L). At small q its finite local form factors approach that vector continuously. Every higher fixed-order normalized source coefficient acting on the flat vacuum is a sum of translated finite patterns. Distinct translates overlap only a bounded number of times; the finite-pattern Gram bound is therefore O(1), not O(R). Ground components are removed before using this bound.

The lower orientation eigenvector tends to (A+B)/sqrt2 because q²/lambda² tends to zero. The leading source norm and atom are consequently those in section 1. Exact microscopic projector errors are estimated separately: within the exact momentum/plane fibre the smallest relevant gap is order lambda^14, so the Hamiltonian tail gives state error O(R²lambda^(40-14)). Even the crude ||C_Q||<=sqrt(V)=O(R) then gives source error O(R³lambda^26)=O(lambda^21.5) at p=3/2, negligible compared with lambda^10. The ground error uses its larger lambda^4 gap. Source-transform tails are constructed to the same sufficient order. No unresolved full-band momentum spacing is used as a denominator.

## 6. Limits

This is a fixed-height weak-anisotropy asymptotic statement about a specified native Hamiltonian, selected exact plane sector and original operator. It retires a grid-resolution limitation, not the slab or state premise. It does not identify J, lambda or a cosmological field, establish three-dimensional Lorentz symmetry, give an observed particle mass, or prove a universal heavy coupling. The finite-order constants do not provide a practical numerical lambda threshold. Independent local-reduction, spatial-moment, embedding and source checks pass; independent repository audit remains required before retained status.


## 7. Reproducible controls and a finite-parameter limitation

The exact-rational second-order winding control gives 33 nonzero entries, diagonal -7/2 and row absolute sum 35/2 after subtracting the vacuum scalar, identically on R=10,12,16,20. The apparently nonlocal transition to a distant pair cancels exactly. This tests the connected reduction mechanism; it is not a substitute for the arbitrary fixed-order locality argument.

The 400-digit two-orientation control resolves actual discrete q=2pi n/R for p=3/2. At lambda=1e-8 the dispersion/leading-curvature ratios for n=(1,0),(1,1),(2,1) differ from one by at most 1.90e-6. At lambda=.01 the axial ratio is only .369: the asymptotic isotropic formula is not accurate there. Both outputs are preserved. These calculations test the derived leading matrix and error scaling, not the enormous full microscopic grids or an experimentally calibrated lambda.
