# Independent local-clock extension route

Selected scientific/procedural source: `7146fe17a76de41badcaca3c3c7cac6d11eb2a00`. Refreshed main searched for this pass: `65db84dea820af90a8b359448c07be3ba4ff37dd`; relevant clock, action, constraint and primitive sources are unchanged. PR9363 remains provisional at `fd51a1f4c7f38c124d6f0f7dde396198eadf8b36`. This is a mathematical route pass with an explicitly enlarged classical carrier, not adoption, an audit, or a claim that canonical clocks are native to M_2(C).

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
reachability_to_target: supports
conditional_surface_status: exact parametrization of supplied finite Hamiltonian systems on an enlarged canonical phase space
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

**Result.** Independent canonical clocks can be added to any supplied finite Hamiltonian system to produce an exact flat multi-time connection, even when the original local Hamiltonians do not commute. One simultaneous canonical transformation gives the construction and proves every constraint bracket and Jacobi identity. The synchronous-clock gauge recovers the original interacting Hamiltonian exactly. Individual clock generators generally acquire longer support; an exact sparse chain exhibits all distances through its end. Eliminating the new clocks does **not** impose the original local Hamiltonians as constraints. It returns the original unconstrained phase space. Therefore this construction is useful first-class parametrization, but does not complete block112's gravity constraint system.

## 1. Family, target and relation to the actual sources

Family tuple:

`(finite canonical phase space extended by one (T_a,Pi_a) pair per local Hamiltonian; one simultaneous Hamiltonian canonical transformation and its flat clock connection; a physical reduction to the original gravitational constraint ideal with the required locality)`.

The exact constructive target here is: given a finite canonical phase space z=(q,p), and autonomous local Hamiltonians H_a(z), construct C_a=Pi_a+h_a(T,z) with h_a(0,z)=H_a(z), `{C_a,C_b}=0` for all a,b, and synchronous recovery of H_total=sum_a H_a. Quantifiers are all clock vectors and phase points where the canonical flow exists. For finite quadratic/affine-quadratic Hamiltonians the flow is complete, so no small-clock restriction is needed. For general smooth nonlinear Hamiltonians the statement is local on a common flow domain; neither analyticity nor global completeness is silently assumed.

The distinction from the actual source is substantive:

- Block60 supplies positive site rates w_x and actions with no rate velocities. Rates are multipliers in the stated field sector, not canonical clock coordinates T_x with conjugate Pi_x. Its hopping content is also not generally linear in independent rates.
- Blocks62/101 supply the quadratic strain action and a nondynamical lapse perturbation u. They do not supply independent local-time embeddings or their canonical momenta.
- Block112 supplies a flat-strain, momentum-linear lapse bracket for a chosen staggered stencil. It does not supply the full nonlinear Hamiltonian densities. Its sign correction in the independent seed check remains in force: with C=T-KR1 and `{h,P}=+1`, the bond field has orientation `K/(4alpha)[N_x M_(x+e_j)-N_(x+e_j)M_x]`.

This pass openly adds real canonical pairs (T_a,Pi_a). They are extra mathematical carrier content. No mapping of them to site M_2(C) or to Record is supplied. The primitive registry and current primitive sources were read in the earlier passes at the same selected revision; units, matter kinetic-form isotropy and pointwise state evaluation do not supply this new carrier or its physical identification.

## 2. Three cases that must be kept separate

**One global clock.** For any autonomous H(z), add one pair (T,Pi) and action

`S=integral ds [p qdot+Pi Tdot-N(Pi+H)]`.

The one constraint C=Pi+H is first-class. Gauge T=s and solve Pi=-H to recover the original Hamiltonian dynamics. This adds no local lapse algebra and places no condition H=0 on the original variables.

**Independent clocks with fixed local Hamiltonians.** Take

`C_a=Pi_a+H_a(z)`.

Then `{C_a,C_b}={H_a,H_b}_z`. This family is first-class if and only if all H_a commute strongly. Necessity is immediate: its constraint surface contains every original z, with Pi_a=-H_a(z), so a nonzero function `{H_a,H_b}(z)` cannot vanish merely on that graph. Commutativity does not imply absence of interactions; commuting nearest-neighbour Ising energies, for example, are interacting supplied models. It is nonetheless an extra structural restriction and does not hold for arbitrary energy splits.

A positive two-site harmonic example is

`H0=p0²/2+kappa(q1-q0)²/4`, `H1=p1²/2+kappa(q1-q0)²/4`, kappa>0.

Direct differentiation yields

`{H0,H1}=-kappa(p0+p1)(q0-q1)/2`.

At q0=1,q1=0,p0=0,p1=1,kappa=1 it is -1/2. Choosing the clock momenta to cancel H0,H1 makes both C vanish without removing this bracket. Thus the unmodified independent-clock construction fails in an ordinary positive interacting example. This is a scoped counterexample, not a no-go on local-clock theories.

**Embedding-dependent local Hamiltonians.** Allow h_a(T,z). With `{T_a,Pi_b}=delta_ab` and no Pi dependence in h,

`{C_a,C_b}=-partial_a h_b+partial_b h_a+{h_a,h_b}_z`.

Thus exact Abelian first-classness requires

`partial_a h_b-partial_b h_a={h_a,h_b}_z`.                         (1)

The clock derivatives are not optional corrections. They can cancel noncommuting initial H_a. The construction below does this without fitting a truncated bracket.

## 3. Exact flat connection from one canonical map

Define the function on the extended phase space

`F(T,z)=sum_a T_a H_a(z)`,

and the left Poisson adjoint `ad_F g={F,g}`. This is a derivation of the full canonical Poisson bracket. Its exponential denotes the corresponding time-one canonical flow, not a formal divergent series. Let

`Phi=exp(ad_F)`.

F does not depend on Pi, so Phi fixes every T_a, and

`ad_F Pi_a=H_a`.

Consequently

`C_a=Phi(Pi_a)=Pi_a+h_a(T,z)`,

`h_a(T,z)=integral_0^1 exp(s ad_F) H_a(z) ds`.                    (2)

When a Taylor series is valid, the same formula reads

`h_a=sum_(n>=0) ad_F^n H_a/(n+1)!`.

In particular,

`h_a=H_a+(1/2)sum_b T_b {H_b,H_a}+O(T²)`.

Since all C_a are images under the **same** canonical transformation,

`{C_a,C_b}=Phi({Pi_a,Pi_b})=0`                                  (3)

exactly. This proves (1) at every point in the flow domain, not just at T=0. The canonical Jacobi identity is unchanged; the C algebra is Abelian. Gauge flows generated by different C_a commute, so the local-clock connection is flat. This construction also avoids choosing an order for the sites. If the initial family transforms covariantly under lattice symmetries and the clocks transform by the same label permutation, F and the construction are covariant too.

At T_a=t for every a, F=t H_total, and `ad_F H_total=0`. Summing (2) therefore gives

`sum_a h_a(t,...,t;z)=H_total(z)`                                (4)

for every t in the domain. This is exact synchronous recovery, not a splitting approximation.

The action is

`S_ext=integral ds [p qdot+sum_a Pi_a Tdot_a-sum_a N^a C_a]`.

Varying Pi gives Tdot_a=N^a. Eliminating Pi and N gives the multi-time action

`S_multi=integral [p dq-sum_a h_a(T,z)dT_a]`.

Gauge T_a=s for every a recovers `p qdot-H_total` by (4). Initial data in z are otherwise unrestricted. All statements concern supplied autonomous Hamiltonians. A prescribed external source e(t) is not automatically converted into a closed autonomous matter system by this formula.

## 4. An exact polynomial interacting lattice example

On an open three-site canonical chain let

`H0=p0 q1`, `H1=p1 q2`, `H2=p0 q2`.

Then `{H0,H1}=H2`, and H2 commutes with H0,H1. Equation (2) terminates:

`C0=Pi0+H0-T1 H2/2`,

`C1=Pi1+H1+T0 H2/2`.

The matter part of `{C0,C1}` is H2. The two clock derivatives contribute -H2/2 each, so the bracket is exactly zero. These Hamiltonians are supplied quadratic cross-site interactions; positivity is not claimed for this directed transport example. Their linear Hamiltonian flows are complete.

For an N-site open chain take `H_i=p_i q_(i+1)`, i=0,...,N-2. Write H_i=p^T A_i q with A_i=E_(i,i+1), and A(T)=sum_i T_i A_i. The matrix form of (2) is

`B_i(T)=sum_(n>=0) ad_A^n A_i/(n+1)!`, `h_i=p^T B_i q`.

The matrices are strictly upper triangular, so the sums terminate. The bracket equation becomes

`-partial_i B_j+partial_j B_i+[B_i,B_j]=0`.

`check.py` proves every one of the ten independent matrix equations for six sites and five independent symbolic clocks, using exact rational polynomials. It also directly differentiates the three-site canonical constraints and a mixed coordinate/constraint Jacobi triple. No finite-order remainder is omitted.

## 5. The exact support price

At equal clocks T_i=t, the endpoint density of that same chain is

`h0(t)=sum_(n=0)^(N-2) [(-t)^n/(n+1)!] p0 q_(n+1)`.              (5)

Proof: with S=sum_i E_(i,i+1), `[S,E_(0,r)]=-E_(0,r+1)` until the chain end. Substitute into (2). For every t!=0, the coefficient at every distance 1,...,N-1 is nonzero. The six-site check finds

`1, -t/2, t²/6, -t³/24, t⁴/120`.

The sum of all dressed densities is still the nearest-neighbour H_total by (4); their long terms cancel only in that synchronous sum. Independent local-clock updates use individual h_i, so this cancellation is not a uniform finite-range property of the connection.

For initially finite-support H_a, a nested Poisson bracket vanishes when the relevant supports are disjoint. Surviving terms in (2) join overlap-connected clusters of local densities. Their support can grow at each order, as (5) demonstrates exactly. This refutes a uniform finite-radius assertion for this specific general construction; it does not prove every possible flat connection must have that support.

For a fixed finite quadratic system one can also bound the Taylor tail. Writing F=(1/2)z^T A_F z and a homogeneous quadratic H_a=(1/2)z^T A_a z, the Poisson adjoint acts on Hessians as `B -> A_F J B-B J A_F`, whose operator-norm bound is `2||A_F|| ||B||` when ||J||=1. Hence the omitted Hessian tail after n<r is bounded by

`||A_a|| sum_(n>=r) (2||A_F||)^n/(n+1)!`.

This is a finite-dimensional control, not an asserted volume-uniform infinite-lattice estimate. Affine terms can be included in the exact finite flow, but no additional uniform bound for the full source action is claimed here. General nonlinear Hamiltonians require actual flow-domain and derivative estimates; a formal series alone would not prove convergence.

## 6. A concrete application to the supplied gravity comparator

One can apply (2) to a fully specified finite-torus quadratic comparator without assuming that its original lapse constraints close. Use the six canonical strains and momenta with independent shear momenta P_ij and full-matrix entries pi_ij=P_ij/2. Choose beta=-alpha, four-corner timing, and the per-tick convention of block112. Let tkin_a be the site diagonal DeWitt kinetic term plus the face terms distributed to their four corners, so

`sum_a tkin_a = [sum P_jj²-(sum P_jj)²/2]/(4alpha)+sum_(i<j)P_ij²/(8alpha)`

with the sums over the corresponding slots.

Let R be block62's actual linear curvature map, and Q its symmetric Hessian for the uniform quadratic R2, so `R2_total=(1/2)h^T Qh`. A concrete supplied local density split is

`r2_a=(1/2)sum_A omega_(aA) h_A (Qh)_A`,

where omega_(aA)=1 for a site strain at a, and omega_(aA)=1/4 for each corner a of a face strain A, zero otherwise. Then sum_a omega_(aA)=1 and sum_a r2_a=R2_total. This is a definite finite-range density convention; it is **not** derived from the uniform mode polynomial as a unique lapse placement.

Take

`H_a = tkin_a-K(Rh)_a-K r2_a`.                                    (6)

Every H_a is affine-quadratic and local on the finite torus. At h=0 its momentum-linear bracket is the corrected block112 seed because the R2 gradient vanishes there. The uniform sum is `T_total-K R2_total`, since the periodic sum of R1 vanishes. It therefore reproduces the supplied vacuum uniform quadratic Hamiltonian in per-tick units. A fixed wbar rescales the ambient-time Hamiltonian; no identification of K/alpha with a measured speed is made.

Equations (2)–(4) now give an exact flat clock extension of **this supplied comparator**, with global finite-dimensional existence because its flow is affine linear. No extra claim that the original H_a bracket closes into the original G is needed. The new clock derivatives cancel the entire original bracket, including any terms outside the old constraint ideal. This is why the construction cannot be credited as a derivation of that ideal.

The chosen r2_a also displays a limit: different local decompositions of the same uniform R2 produce different independent-clock connections, while preserving synchronous H_total. The source does not select a unique such decomposition. Nothing here derives a nonlinear physical gravity action, a matter coupling, or a Record interpretation of the added clocks.

## 7. Eliminating clocks does not recover the original constraints

There are m extra canonical clock pairs and m independent first-class constraints C_a. They are independent because `partial C_a/partial Pi_b=delta_ab`. Their gauge quotient leaves the original 2n-dimensional physical phase space. Gauge T=0 and solve C=0:

`Pi_a=-H_a(z)`.

Every original z remains allowed. In the explicit two-clock example, q1=p0=1 with all other q,p zero, T=0, Pi0=-1,Pi1=0 gives C0=C1=0 while H0=1. Thus the extended constraint surface does not impose H_a=0.

Imposing both T=0 and Pi=0 would add the original H_a=0 equations; it is not simply removal of the m auxiliary pairs by the one available clock gauge. More generally, a gauge using Pi rather than T still leaves the same number of physical degrees of freedom and needs its own admissibility/regularity analysis. It cannot be identified with the original gravitational constraint reduction by relabeling.

Canonical invariants `Z=Phi(z)` commute with every C_a; they are the original unrestricted initial data in a dressed description. If one also wants original constraints Psi(z)=0, dressing them as Phi(Psi) makes them commute with the new C_a, but their mutual brackets are

`{Phi(Psi_A),Phi(Psi_B)}=Phi({Psi_A,Psi_B})`.

Their original closure problem remains exactly. Dressing a nonclosing gravitational constraint ideal does not repair it.

The precise missing lemma is therefore: construct a local, symmetry-compatible physical reduction or identification of the enlarged system whose reduced constraint surface and presymplectic structure are those of the desired six-strain gravity theory, with the block112 seed and all required lapse/shift brackets, without importing those very constraints as already closed. This lemma is **target-equivalent** for the requested gravity completion; a strict exact locality requirement may make this particular realization stronger than the unrestricted target. The flat extension theorem itself is weaker than that target and supplies a new mechanism, not its discharge.

## 8. Prior art, source scope and current-main refresh

Complete source reading relevant to this pass: block60's rate/action definitions, multiplier and kinetic claims; block62/101/112 and the independent seed check read in prior passes at the same revision; current primitive sources as described above. The June17 single-time open-gate note and N5 clock-exchange note were read completely for their exact commuting-generator witness. Their older Record-additivity prose is not current foundation content and is not imported. Their finite witness uses two commuting Pauli generators and does not construct this interacting classical flat clock connection.

Before construction, a bounded statement search on selected main used `(multi.time|multitime|independent.clock|embedding.variable|parametrized/parametrised ... clock/lattice|clock ... first.class|clock ... flat ... connection)`. Current-main search at `65db84...` repeated the matching multi-time/embedding/first-class patterns over the actual clock/time/constraint/admissibility science sources. Hits were the commuting-clock witness, finite-clock matter correlators and formation clock/order rules. Those are context or different target classes. No matching interacting canonical extension proof was found in that scope. The canonical construction is elementary standard Hamiltonian mathematics derived here; no broad novelty claim is made.

Read-only main refresh returned `65db84dea820af90a8b359448c07be3ba4ff37dd`. The complete intervening path list after the prior `d84eacf...` check concerns composite-network band/sign sources, runners, caches and the citation manifest. It changes none of this pass's scientific/procedural inputs. No fetch/ref mutation was performed. PR9363's exact head was refreshed via `gh pr view`; the viability-map and gravity-wall exercise sources were searched for embedding, parametrization, multi-time and first-class clocks. The only displayed “embedding” match concerned parity typing, not a clock extension. Prior A1 proposal coverage is recorded in the discrete report. No unrelated proposal's full contents or novelty absence are certified.

## 9. Verification and scoped negative-claim discipline

Run with capped numerical-library threads:

`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 -u .claude/science/physics-loops/toe-gravity-law-24h-20260929/independent-clock-extension/check.py`

Final result: exit 0, `TOTAL: PASS=7 FAIL=0`. The check is exact SymPy sparse/polynomial arithmetic; it imports no primary runner and launches no unmanaged worker. It checks all ten flatness equations of the six-site connection, direct two-clock symplectic brackets and Jacobi, synchronous Hamiltonian recovery, distance-five support, the positive harmonic counterexample, and a constraint-surface witness to failure of H_a=0 recovery.

The first run stopped at an incorrect expected formula in the harmonic cross-check. Direct differentiation gives `-kappa(p0+p1)(q0-q1)/2`; the earlier checker expected a difference of momenta. That expectation was corrected, the failed run was preserved in `initial_check_failure.txt`, and the entire check was rerun successfully. The error did not affect the independently checked flat connection or its signs. No earlier partial run is counted as a final PASS.

The report's negative claims concern the frozen-clock construction, this construction's exact support, and the failure of automatic original-constraint recovery. It is not a target-wide no-go and does not claim the selected no-go skill's five-distinct-defeated-family packet PASS.

- **N1:** Fixed H_a clocks, embedding-dependent canonical dressing, synchronous reduction, support analysis and physical constraint reduction are distinguished; the successful dressing is an affirmative escape. Five defeated gravity approaches are not claimed.
- **N2:** Clock-support growth and failure to impose H_a=0 are different properties, but no independent-wall count or unproved non-implication is asserted.
- **N3:** Extra continuous canonical pairs, autonomous supplied H_a, common flow domain, local density split and pairing are explicit. They are not asserted to follow from M_2(C).
- **N4:** The June commuting-clock witness is prior art only for commuting kinematics. Block112 is prior art only for the specified tangent bracket. Neither proves a no-go for this extended carrier.
- **N5:** Sparse element/block tests and general canonical proof are separated; no gravitational Fourier closure or full native-carrier claim follows from the chain.
- **N6:** No approved primitive is called a wall and no axiom amendment is demanded. A physical clock/embedding realization remains an open derivation or explicit supplied model condition.
- **N7:** Strongest alternative is a different flat connection with a genuinely local physical embedding law and a proved gravitational reduction. Equation (5) does not exclude it. The terminal reduction lemma in section 7 makes its obligation explicit.
- **N8:** Existing source repeatedly distinguishes clock kinematics, dynamical selection and physical identification. This construction follows that distinction; exact first-class auxiliary constraints do not ratify a physical gravity law.
