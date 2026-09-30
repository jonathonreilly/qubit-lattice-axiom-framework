# Finite control derivation and limits

These are author controls of the rewritten unit. They complement the complete
analytic proofs; they neither approximate the thermodynamic ground state nor
compute the fifteen-channel threshold form. The literal word and boundary code
openly reuse the earlier campaign algorithms archived in CAMPAIGN_SOURCE_MAP.json.
The new runner is not an independent checker of this author's proofs.

The standard-library primary has seven finite check families. All numerical
equalities use integers or rational complex pairs. No floating arithmetic,
bosonic replacement of the carrier, matrix eigensolver or fitted limit occurs.

1. **Literal hard-core word.** Expand the actual five collective lowering
   channels into their six-neighbor two-site words. Annihilation requires both
   sites occupied; creation requires both absent from the residual occupation.
   The number plus triple term is diagonal; the pair mass and nearest-center
   gradients are applied as separate mu and tau coefficients. At the explicit
   four-site occupation, the only occupied central axial-y pair gives diagonal
   `4mu-4mu/3+4tau`, and contraction with all three actual pairings of `C_E1^2`
   gives `tau/3`. Reverse columns test Hermiticity. Minimizing the one-word
   quartic correction gives the exact improvement `tau²/(96mu+144tau)` at
   three rational positive couplings. The pulse vector is `C²/2`, while the
   threshold vector is `C²/sqrt(2)`; the energy ratio is therefore one half.
   This last arithmetic assertion supports, rather than replaces, the
   canonical source's full norm and vacuum-cancellation derivation.

2. **Physical boundary rows.** For cubes of side 5 and 6 enumerate every
   individual complete S row. Each plane has four pairs of words sharing a
   vertex and two opposite pairs. The independent count is
   `(L-2)^3+3[4(L-2)(L-1)L+2(L-2)^2 L]`. On side 5 this is 1017. Requiring
   all four plane words before retaining any plane row instead gives the
   historical 837-row strict subset. Both counts are reported; the current
   primary tests the full individual-row family. Constant-amplitude rows
   have rank four: a nonzero minor modulo 101 gives the lower rank, and five
   explicit independent soft null vectors give the upper rank. Adding every
   physical edge incident at each site gives rank nine. Literal gradient
   enumeration gives axial multiplicity one and plane multiplicity two when
   reducing fifteen raw words to nine forward orientations. Weighted row
   incidence is at most 15. Forward rectangle sizes and radius-two boundary
   counts are checked directly. These small cubes do not establish a
   large-volume spectral gap; the source proves that by explicit Poincare
   and finite corner-pin arguments.

3. **Safe diagonal.** With q omitted graph neighbors and m internal occupied
   neighbors, minimize `phi(m+j)` over all `0<=j<=q`, for every allowed
   `m+q<=18`. This equals `phi(m)-1_(q>0,m=0)`, is nonnegative, and lies below
   every possible completed value. This finite identity is the actual
   nonmonotone boundary deletion repair. Its Boolean polynomial degree is
   at most 19 after multiplying by the center occupation.

4. **All-particle counting.** Enumerate all 8192 occupations on a thirteen-site
   fixture containing isolated dimers, rejected dimers, connected clusters
   and singletons. Literal graph degrees determine D; all occupied vertices
   in the b=10 Chebyshev cube determine F_b. Good dimers must have no third
   particle in either endpoint cube. Check `B_b<=D+2F_b`. The fixture includes
   rejected dimers with only one endpoint seeing a third particle, so the
   factor-two mutation is discriminating. The general proof, separately in
   the lower appendix, assigns singletons to D, cluster vertices to F_b,
   and two endpoints of every rejected isolated dimer to one F_b endpoint.
   The same fixture does not prove the subsequent energy pin inequality.

5. **Centered removal source.** For every one of the nine actual forward
   anchor rectangles, prescribe a rational compact kernel and a residual
   two-particle occupation. Subtract the mean on the WHOLE rectangle, then
   impose the physical intersection holes on the annihilated amplitude.
   The centered source has zero sum and its pairing plus the removed mean
   equals the original pairing exactly. Centering after deleting holes is
   a different construction and fails the zero-sum assertion. The finite
   test does not compute the Neumann Green, Sobolev or Schur limiting error.

6. **Complex sphere.** Work in the unnormalized physical five-mode Fock
   basis, whose occupation monomial norm is `prod alpha_i!`, solely for
   the finite internal space proved to arise in the source. Three sparse
   complex vectors at n=2,3,5 have normalized one- and two-body matrices
   from literal annihilation. Direct sphere integration uses
   `integral z^p conjugate(z)^q = delta_pq (d-1)! prod p_i!/(|p|+d-1)!`.
   Compare all 625 ordered matrix entries at each n with
   `[n(n-1)gamma2 + n(gamma1_ik delta_jl + gamma1_il delta_jk +
   gamma1_jk delta_il + gamma1_jl delta_ik) + delta_ik delta_jl +
   delta_il delta_jk]/[(n+5)(n+6)]`.
   Nonreal entries test index/conjugation order. The exact coefficient four
   in the symmetric operator form is thus tested beyond diagonal states.
   The analytic source, not this finite identity, proves the actual carrier
   cell embedding and the high-particle tail bound.

7. **Exact number and seams.** Use three even number-sector probabilities,
   including zero weight at the full sector. Rounding can populate that
   sector. Test large cubes with and without a leftover strip, both signs
   of subextensive target deviations, and odd exact N. Reserve enough
   sites to realize the integer deficit after deterministic frequency
   rounding, checking both nonnegativity and capacity. Separately enumerate
   the actual radius-two supports on sides 5,6,8; compare both original
   and artificial-periodic seam counts with `24 ell²`. The mathematical
   source proves the general arbitrary fixed-rho sequence and ordered
   thermodynamic limits. No direct number projection is used here.

## Declared negative controls

Scratch copies test operator, geometry, formula, or oracle coefficient sensitivity.
The plane-multiplicity control changes its expected coefficient, while the
pulse/threshold divisor changes a standalone formula compared with a literal
vector-ratio oracle. These are coefficient-sensitivity checks, not two changes
to the physical operator implementation. Each mutation must reach the assertion
listed here; timeout, import failure or resource exhaustion is not a kill.

| Mutation | Expected discriminating assertion |
|---|---|
| gradient weight 1 to 2 | literal hard-core diagonal/source |
| retain only complete four-word plane families | individual S-row count |
| remove incident pins | rank nine after actual physical pins |
| plane gradient multiplicity 2 to 1 | raw-word to forward-row multiplicity |
| safe boundary subtraction 1 to 0 | completed diagonal minimum |
| bad-particle F charge 2 to 1 | rejected-dimer count |
| center after intersection holes | full-rectangle zero mean |
| symmetric Husimi coefficient 4 to 2 | complex ordered sphere entries |
| omit number reserve | exact integer capacity |
| seam width 2 to 1 | actual radius-two center count |
| pulse/threshold quartic divisor 2 to 1 | actual squared vector ratio |

Planned resource price per primary or sequential scratch mutation: 30 CPU
seconds, 180 wall seconds, 200 MiB aggregate resident-memory polling threshold;
all BLAS/OpenMP variables one. Size: two cubes at most 216 sites, at most a few
thousand sparse rows, 8192 small occupation masks, 1875 rational complex matrix
entries from five-term vectors. Expected work is seconds, not a large sparse
Hamiltonian diagonalization. The resource wrapper records actual CPU, wall,
resident memory, termination and the exact command. No control has executed
when this document is first frozen.
