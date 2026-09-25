# Blind PRE: selected original mark and instantaneous mean-energy power

This is an independent reconstruction before access to the author energy-accounting packet. The conditional result concerns the supplied **common rotor GKLS generator**, its full Hermitian energy `h_g=K_g D+delta_g H4`, and the exact charged preparation in section B of the pinned prepared-observation note. It is not a theorem about the derivative of a bare finite-spin density, a total energy flux, heat, or photon absorption. No new dynamical assumption, author builder or other active checker result is used.

**Result.** At each fixed finite even cubic torus, the selected-channel power on the declared compact vacuum and finite one-excitation packets has a finite `g->0` limit. The electric part tends to zero. The magnetic limit is a quadratic reference-field moment, obtained only after retaining the gain and anticommutator and the Haar average over harmonic angles. For every even side `L>=16`, my exact local calculation gives

`lim P_j(g) = kappa/(4 tau_*) <(ell.X)(r.X)>_psi`,                 (P1)

where `ell=e_ac-e_dc+e_de-e_ae` is the prepared plaquette circulation and the fixed 67-edge integer circulation `r` is specified below and in the coefficient table. Both resolved signs give the same answer, in fact the same selected power before this limit. For the reference vacuum and one-excitation wavepacket `f`, respectively,

`P_0^lim = kappa s_L/(4 tau_*),`

`P_f^lim-P_0^lim = kappa/(2 tau_*) Re(chi_ell(f)^* chi_r(f)),`    (P2)

with `s_L=(1/2) ell^T Omega_L^(-1) r`. The added-one-excitation quadratic form has both positive and negative directions: `r` is not proportional to `ell`. Thus the original mark's positive initial rate contrast does not imply a universally positive added-energy power. At `L=16`, finite Fourier arithmetic gives `P_0^lim ≈311.33810094362974 kappa/tau_*`; its strict positivity at this one size also follows from a coarse analytic bound below. Numerical values here are controls without interval enclosures.

## 1. Exact inputs and premise boundary

`SOURCE_PINS.json` freezes the three authorized main notes, the authorized prepared-observation note, my unchanged earlier prepared-probe PRE/POST and their seals, and the unchanged applicable workflow/AGENTS. The main scientific source identities are:

- Local pair form: `7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a`.
- Common compensated limit: `c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b`.
- Weak-field packets: `651fa7cfd816ca5df8c401959458b7590c2f6ec706af437ef3ce31accb7d3ccf`.
- Prepared observation: `14ed0194fefd18eeee711e733bb76c75ce4a88832b01bc55dc41e6e058ba612b`, using section B and the already checked preparation distinctions in C.2.

The main revision is `0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`. These are conditional supplied-model parents, not audited physical-selection premises. My earlier PRE/POST are explicit prior background for the preparation and original primitive, not a second discovery of those inputs. No new result from their author controls is used to determine the power coefficient.

Use A-to-B oriented edges, and the exact coordinates and charges from the prepared note:

`a=(0,0,0), d=(1,1,0), h=(2,2,0), c=(1,0,0), e=(0,1,0), b=(-1,0,0)`;

`v1=(0,-1,0), v2=(0,0,1), v3=(0,0,-1)`.

Every A site is occupied, `q_d=q_h=-1`, all other A signs are positive, and `v1,v2,v3` are occupied with positive charge. The two words `m_c,m_e` respectively occupy c or e with positive charge. The common fixed integer flow has divergence `-delta_d-2delta_h+sum_i delta_vi`. With its shift `V_com`,

`J_c phi=|m_c> V_com U_dc^-1 phi,`

`J_e phi=|m_e> V_com U_de^-1 phi,  J_-=(J_c-J_e)/sqrt(2)`.

The common flow is fixed as `g->0`; a growing electric dressing is not included. Each branch is separately Gauss physical, has four occupied B sites, and the two branches are orthogonal before the mark. The exact selected original resolved channel is `B_j=P j_(a,b,sigma) F_a P`, with `sigma=+1` or `-1` fixed.

Set `tau_*=a_spacing/c_speed`, `K_g=g^2/(2 tau_*)`, `delta_g=1/(4 tau_* g^2)` and fixed `kappa>0`. The full electric term on P is

`D(q,E)=sum_(x in A,y~x,q_y=0) E_xy(E_xy-q_x)`.                (P3)

Occupied B sites remove **all incident summands**. It is not `sum E^2` in these charged words. The full magnetic coefficient is the main local identity

`H4=-2 sum_{unordered u,v in A, dist(u,v)=2} S_uv^* S_uv,`

`S_uv=F_v F_u P`.                                            (P4)

All relevant matter sectors in P are retained by (P3)–(P4). The chosen packet does not turn their evolution into vacuum field dynamics.

## 2. Actual adjoint dissipator and domain

For `Psi_g=J_- phi_g`, the selected contribution to the time derivative of the ordinary mean of the physical `h_g` is

`P_j(g)=kappa [<B_j Psi_g,h_g B_j Psi_g>`

`                         - Re <B_j Psi_g,B_j h_g Psi_g>]`.    (P5)

Equivalently it is the expectation of `kappa(B_j^*h_gB_j-{B_j^*B_j,h_g}/2)`. The second term is the anticommutator subtrahend. It is not generally the event rate times the mean energy of the unselected input. Replacing it that way discards input energy/matter coherence.

The compact packet is smooth, with finite electric moments of every order. Fixed shifts and the finite sums of shifts in H4 and B preserve the domains of every power of `N_E=1+sum E_e^2`. On this stronger domain `D` is controlled by `N_E`, even though D itself can leave some electric directions unconfined. The initial pure density therefore has enough moments for both terms of (P5). A precise differentiability justification is available on these domains: the diagonal `K_gD` commutes with `N_E`; H4 and all jumps/losses are bounded on each `N_E` graph norm because they shift finitely many electric integers by bounded amounts and have finite matter matrices. The interaction-picture Dyson construction thus preserves the corresponding weighted trace spaces at fixed g, and an extra electric moment permits the derivative paired with `h_g` at zero. This establishes (P5) for these packets without asserting energy continuity from ordinary trace-norm convergence. The Hamiltonian part contributes zero to the derivative of its own mean; other channels contribute their own terms and are not summed here.

The original path calculation gives

`B_j J_- phi = |m_out> V_com U_ab^sigma`

`                  (U_ae^-1 U_dc^-1-U_ac^-1 U_de^-1)phi/sqrt(2)`,

and `J_-^* B_j^*B_j J_-=1-cos(ell.A)`. In particular `||B_j Psi_g||=O(g)`. At fixed volume the smooth packet bounds give `||D Psi_g||=O(g^-2)`. Writing the born vector as a fixed shift times the difference of the two route phases times `phi_g`, two angular derivatives give `||D B_j Psi_g||=O(g^-1)`; terms differentiating the cutoff have exponentially small tails. This yields

`0<=kappa K_g <B_j Psi_g,D B_j Psi_g>=O(g^2),`

`|kappa K_g Re<B_j Psi_g,B_j D Psi_g>|=O(g)`.                  (P6)

The weaker `O(g)` bound for both terms would already suffice. Hence the electric contribution vanishes in the asserted limit. No flat-sector electric substitution or uniform confinement was needed.

For this exact input the selected power is sign-independent before the limit. `B_j^*B_j` is independent of the resolved sign. The born matter word occupies every B neighbor of a. Thus its D diagonal has no edge incident to a, and its `S_uv` norm is zero if u or v is a; otherwise neither the A sign at a nor the B sign at b affects the diagonal born H4 expectation. The birth phase `U_ab^sigma` also cancels there. These facts make the gain equal for the two signs, while the anticommutator already has the same effect operator. This statement does not compare the two full instruments at later times.

## 3. Exact local magnetic difference, with gain and loss

Let `Q_j=J_-^*(B_j^*H4 B_j-{B_j^*B_j,H4}/2)J_-`, a bounded operator on the reference field. It is a finite real symmetric Laurent polynomial of divergence-free shifts. The common `V_com` commutes with all rotor shifts and cancels in these magnetic matrix elements. This cancellation is not used to remove it from D.

Only pair terms whose stars intersect the selected a-star need be computed in `Q_j`. Indeed

`Q_j=<...>` is obtained from `Re <B_j Psi,[H4,B_j]Psi>`,

and any disjoint pair term commutes with B_j and cancels exactly between gain and anticommutator. On the infinite cubic local lift there are 19 A centers whose stars intersect the selected star, and 264 unordered distance-two pairs with at least one such center. Pair endpoints are within distance four of a; all primitive vertices in the calculation are within distance five. This is a statement of operator locality, not a volume-uniform limit of the full GKLS dynamics.

For a transparent finite algorithm, write `v=sqrt(2) J_-` for the two unnormalized signed words, and let `b=B_j v`, `w=B_j^*b`. There are two b words with the same final matter and ten w words over five prebirth matter configurations. For each retained pair,

`G_uv(A)=<S_uv b,S_uv b>,  Z_uv(A)=<S_uv w,S_uv v>`.

The correct normalization and `-2 S^*S` coefficient give

`Q_j(A)=sum_uv[-G_uv(A)+Re Z_uv(A)]`.                         (P7)

This computes both parts; it does not use only the born vector's energy. `primitive_power.py` implements unsigned legal outward hops, the original creation and its adjoint, exact matter-word matching and integer electric shifts. The stored polynomial is `2 Q_j`; its coefficient of a shift f is an integer. For the infinite local lift there are 303 nonzero Laurent terms, with maximum electric `l1` shift length eight. Every term has zero divergence and zero winding, and their coefficient sum is zero. Every cancellation used to omit far pairs is exact at arbitrary field angles.

There is a second, separately written exact reduction. Label the five relevant prebirth words by their vacant B site in the order `(c,v1,e,v3,v2)`. At fixed angles let `H(A)` be the H4 matrix on these five words and let `h_out(A)` be its diagonal on the born word. Each pair contributes `-2` times a Gram matrix of its two-outward-hop images. In the local 264-pair sum, at zero angle,

```
H0 = [-13884,  -364,  -172,  -360,  -360
        -364,-13912,  -172,  -370,  -370
        -172,  -172,-13900,  -366,  -366
        -360,  -370,  -366,-13912,  -172
        -360,  -370,  -366,  -172,-13912],
h_out(0)=-11708.
```

For each common two-hop output of words i,j, let `N_i` count its paths and `L_i` be the sum of their outward edge costs `q_u A_ux+q_v A_vy`. Its matrix jets are `H0_ij=-2 N_i N_j` and `H1_ij=-2(L_i N_j-N_i L_j)` in `H(A)=H0+i H1(A)+O(A^2)`. Summing these finite expressions defines all entries directly, without using the first program's Laurent maps.

Let `u0` have +1 at vacant e and -1 at vacant c, `Arow_i=A_ai`, and `Droute_e=A_dc,Droute_c=A_de`. Define

`t0=1^T H0 u0=164,`

`t1'=1^T H1 u0 - Arow H0 u0 - 1^T H0 Droute u0`.

The selected born amplitude has Taylor coefficients `i(ell.A)/sqrt(2)` and `(ell.A)(A_ae+A_dc+A_ac+A_de)/(2 sqrt(2))`. Inserting them in the actual gain-minus-subtrahend expression gives

`Q_j(A)=(ell.A)(r.A)+O(|A|^4),`

`4 r=2 h_out(0) ell - 2 t1' - t0(e_ae+e_dc+e_ac+e_de)`.       (P8)

The even remainder follows also from the exact real symmetric Laurent polynomial. `jet_coefficient_check.py` independently computes this first-jet expression using only path counts and first edge costs. Its 67 integer r coefficients agree exactly with the Laurent calculation for both signs. The complete `t1'` and r table is in `COEFFICIENT_TABLE.md` and `JET_CHECK_RESULTS.json`. Notable exact checks are

`r_ac=1381, r_ae=-1469, r_dc=-1675, r_de=1675,`

`ell.r=6200,  ||r-1675 ell||^2=227520,  div r=0`.

The finite algorithm and table specify the coefficient, including all occupied-B and matter-coherence effects. They do not replace H4 by its empty-sector plaquette form.

## 4. Haar fiber and the torus-size restriction

The reference weak-field preparation is constant in the harmonic link-angle directions because its electric winding is zero. Those directions must be integrated with their Haar measure, not set to zero along with the small transverse coordinate. A relative shift f between equal physical matter words has zero divergence, but it contributes to this expectation only if it also has zero electric winding. Nonzero-winding Fourier characters integrate to zero exactly. The common charged dressing does not change this relative-shift rule.

For an arbitrary fixed allowed torus, take the exact finite-graph Laurent polynomial of `Q_j`, discard its nonzero-winding terms, and call the remaining coefficients `c_f` (not the doubled integer convention). The averaged polynomial still vanishes at the transverse origin: the selected amplitude vanishes on every flat connection before the averaging. It is real and even. Its general quadratic limit is therefore

`Q_j(gX)/g^2 -> -(1/2) sum_(winding f=0) c_f (f.X)^2`.          (P9)

This proves existence and specifies the coefficient at any fixed even side at least six, without importing large-size coefficients.

For every even `L>=16`, the radius-five local primitive region embeds without identified vertices or extra periodic adjacency. Every relative shift of `l1` length at most eight is nonwinding at such a side. Therefore the infinite local coefficient (P8) applies unchanged. This support argument justifies all `L>=16` instances independently of the finite checks; no optimal size threshold is asserted.

The side-six calculation exposes why this condition matters. Its selected local pair set has 261 pairs, compared with 264 on the infinite lift and L16. Its full polynomial differs from the mapped infinite-lift polynomial in seven terms, four of which have nonzero winding. Even after Haar averaging its coefficient is

`r_(L=6)=r_mapped-(3/2) ell`,                                 (P10)

and its flat born H4 correction is 7146 rather than 7152. `L6_WINDING_DIFFERENCE.json` records the exact seven-term discrepancy. Simply dropping winding terms from a presumed large-size result, or setting the harmonic angles to zero, is not a valid shortcut. The independently evaluated L16 polynomial matches the infinite-lift polynomial exactly, while L6 does not.

## 5. Compact-packet limit and full gain/anticommutator coefficients

Let `M_L=(C^T C)|_S` on the transverse, zero-harmonic real space S, and let `Omega_L=M_L^(1/2)>0`. Here C denotes curl, not the electric operator D. The normalized compact packet is the pinned cutoff construction `phi_g=I_g psi/||I_g psi||`, with psi either the oscillator vacuum or a finite normalized one-excitation combination. Its coordinate density has Gaussian polynomial tails. Every nonwinding Laurent term has the Gaussian characteristic expansion with exponentially small cutoff error. The even finite polynomial remainder in (P8) has expectation `O(g^4)` at this fixed lattice. Multiplication by `delta_g` changes this to `O(g^2)`; the cutoff error remains exponentially small after any fixed inverse power. Combining with (P6) gives (P1), with the safe overall error `O(g)` plus exponentially small terms. This is a fixed-L limit only.

The reference covariance is `Sigma_L=(1/2) Omega_L^-1`. In a real orthonormal eigenbasis `Omega_L e_nu=omega_nu e_nu`, write

`psi_f=sqrt(2) sum_nu f_nu sqrt(omega_nu) x_nu psi_0`,

`sum |f_nu|^2=1,  chi_l(f)=sum_nu f_nu (l.e_nu)/sqrt(2 omega_nu)`.

Then

`<(l.X)(r.X)>_0=l^T Sigma_L r,`

`<(l.X)(r.X)>_f=l^T Sigma_L r+2 Re[chi_l(f)^* chi_r(f)]`,

which proves (P2). No harmonic evolution in the charged sector is assumed; these are exact descriptions of the initial reference wavefunctions and their limiting moments.

For completeness the **full**, rather than locally truncated, gain and anticommutator have limits too. At `L>=16`, the born diagonal at flat connection is

`h_out,full(0)=-321 L^3+7152`.                                (P11)

This count follows from a distance-two pair with `d_u,d_v` vacant B destinations and `r_uv` common vacant destinations: its outward norm at zero angle is `d_u d_v-r_uv+1_(q_u=q_v) r_uv(r_uv-1)`. The all-empty/all-plus baseline has three collinear pairs per A, contributing 35 each, and six diagonal pairs, contributing 36 each. Multiplication by -2 gives `-321 L^3`. The finite changed-occupancy/sign pair count gives 7152. Only that finite correction is enumerated, and its validity for large tori follows from the same lift argument.

For `V_psi=<(ell.X)^2>_psi` and `S_psi=<(ell.X)(r.X)>_psi`, equations (P5)–(P6) imply

`gain_limit = kappa/(4 tau_*) [h_out,full(0) V_psi/2],`

`anticommutator_subtrahend_limit`

`           = kappa/(4 tau_*) [h_out,full(0) V_psi/2-S_psi]`.   (P12)

The extensive negative pieces cancel in their difference. A scalar multiple of the identity added to the energy would cancel as well, as an adjoint dissipator must. The two raw terms in (P12) should not be mistaken for the local difference alone.

## 6. Signs and finite arithmetic

Set `u=Omega_L^-1/2 ell/sqrt(2)`, `v=Omega_L^-1/2 r/sqrt(2)`. The one-excitation added-power form is `kappa/(2 tau_*) f^*[(u v^T+v u^T)/2] f`. Its two nonzero eigenvalues before the prefactor are

`(s_L ± ||u|| ||v||)/2`.                                    (P13)

Both signs occur because u,v are independent: r and ell are nonproportional, divergence-free, nonwinding vectors and the transverse weighting is invertible. Their normalized eigenvectors specify two valid finite one-excitation preparations. This exact finite-dimensional argument needs no floating sign test. It excludes a universal positive added-power rule for this selected probe; it does not rule out detection, a positive total flux or absorption in a separately supplied model.

Finite Fourier controls use the positive-axis link convention and check transversality explicitly. They yield the following values in units `kappa/tau_*`:

| L | selected vacuum power | range of added one-excitation power | full one-excitation power range |
|---|---:|---:|---:|
| 6, actual Haar coefficient | 310.84404174806934 | [-2.691888263491876, 624.3799717596305] | [308.15215348457747, 935.2240135076999] |
| 16 | 311.33810094362974 | [-2.690524691437986, 625.3667265786975] | [308.64757625219175, 936.7048275223272] |
| 20 | 311.34035762601394 | [-2.6905412775891477, 625.3712565296171] | [308.6498163484248, 936.711614155631] |

These are computed covariances, not interval-certified full-model simulations or a volume limit. At L16 the vacuum variance of `ell.X` is `0.7958588527704437`, and (P12) gives gain `-130089.49635615118` and anticommutator subtrahend `-130400.83445709481` in those same units. Their difference is the displayed positive power. Omitting the anticommutator would even give the opposite sign in this example.

A coarse nonnumerical positivity check is possible at L16. Put `d_r=r-1675 ell`; its exact norm squared is 227520. Here the smallest eigenvalue of Omega is `2 sin(pi/16)>0.38`, and its largest is `<4`. Therefore `a_0=ell^T Sigma ell>1/2` and `d_r^T Sigma d_r<300000`. Cauchy–Schwarz gives `s_L>=1675 a_0-sqrt(300000 a_0)>450`; the last function is increasing for `a_0>=1/2`. Thus the vacuum selected-channel power is rigorously positive at L16, independently of the quoted decimals. I make no all-volume sign claim from the table.

## 7. Separate checks, corrections and unresolved scope

Three original implementations support the load-bearing coefficient:

1. Exact matter/electric Laurent paths on the infinite local lift, L6 and L16. The signed coefficient sum, Hermitian symmetry, divergence, winding, factorization and the full per-pair inventory are retained.
2. A separate exact five-word matrix value/first-jet calculation, independent of the Laurent builder, matches every one of the 67 r coefficients. It also prints the integer H0 matrix, t0, t1' and h_out above.
3. A separate complex-matrix calculation includes all 972 H4 pairs on L6 and evaluates the actual gain and anticommutator on four angle inputs, for both signs. It agrees with the complete L6 Laurent polynomial, including its winding terms, within `5.01e-12`. The flat/harmonic-angle inputs check the dark configuration, and the generic inputs would detect omission of the anticommutator or destructive branch coherence.

The finite Fourier script evaluates the already computed coefficients, including the covariance/extremal quantities and five vacuum-characteristic convergence rows at L16. The scaled magnetic values for `g=.2,.1,.05,.025,.0125` approach the limiting `311.33810094362974` as `308.42605065460367,310.60641130302497,311.15494753558363,311.29229813570834,311.32664933786515`. This checks the characteristic expansion; it is not compact Hamiltonian propagation or an electric-power simulation.

One bookkeeping/scientific-scope correction is preserved: the initial Fourier output incorrectly used the large-torus `+7152` offset for its L6 **raw gain and anticommutator**, despite the already detected L6 correction `+7146`. The full L6 matrix check gives `h_out=-62190`, confirming the latter. The initial code, complete output and receipt remain available. The corrected result changes only that L6 raw offset and the associated two raw terms; the local net power and all L16/20 results are unchanged. All scientific runs exited zero. The subsequent evidence verifier did fail an erroneous uniform 264-pair inventory assertion: the actual L6 set has 261 pairs. That verifier assumption was corrected against the preserved outputs, with its first version and complete failure log retained; no polynomial or scientific result changed. All commands, executions and stderr/stdout are retained, and the evidence verifier binds each run to its exact script version.

The result has several necessary limits. It concerns the exact compact preparation at its preparation time. It does not show that the original process prepares this state or that the charged state retains its response during transport. General `O(g^2)` vector approximation alone is not a license to transfer this power: magnetic operator norms grow as `g^-2`, and the electric part is unbounded. The latter needs appropriate electric graph-norm control. The declared compact construction supplies that control here; an arbitrary trace-norm approximation need not.

The prior microscopic target convergence is also insufficient to transfer the time derivative. For a bare finite-spin P initialization the original microscopic `j_S P=0`, so this selected microscopic dissipator annihilates the initial density and its instantaneous power is zero. That fact is compatible with the common generator's nonzero power and forbids an unproved derivative/limit interchange. No finite-spin power-convergence theorem is asserted.

Finally, (P5) is one selected channel's instantaneous contribution to the mean of the full physical energy. A conditional born energy divides its gain by a small event probability and is a different quantity. The total mean derivative sums every channel. Heat or absorption would require additional physical reservoir/energy-transfer structure and empirical identification not supplied in these premises. The conditional source Hamiltonian and formation law remain the ones given by the parent; no instrument or absorption coupling was changed.

## Appendix: complete local coefficient table

All edges are oriented A to B. The second column is r; the third is the independently computed t1-prime edge coefficient in (P8). Unlisted coefficients are zero. This is the L>=16 local lift, not the side-six coefficient.

a -> b | r | t1_prime
--- | ---: | ---:
(-1, -1, 0) -> (-1, 0, 0) | -1 | 2
(-1, -1, 0) -> (0, -1, 0) | 1 | -2
(-1, 0, -1) -> (-1, 0, 0) | -1 | 2
(-1, 0, -1) -> (-1, 1, -1) | -2 | 4
(-1, 0, -1) -> (0, 0, -1) | 3 | -6
(-1, 0, 1) -> (-1, 0, 0) | -1 | 2
(-1, 0, 1) -> (-1, 1, 1) | -2 | 4
(-1, 0, 1) -> (0, 0, 1) | 3 | -6
(-1, 1, 0) -> (-1, 0, 0) | 8 | -16
(-1, 1, 0) -> (-1, 1, -1) | 2 | -4
(-1, 1, 0) -> (-1, 1, 1) | 2 | -4
(-1, 1, 0) -> (0, 1, 0) | -12 | 24
(0, -2, 0) -> (0, -1, 0) | -1 | 2
(0, -2, 0) -> (1, -2, 0) | 1 | -2
(0, -1, -1) -> (0, -1, 0) | -2 | 4
(0, -1, -1) -> (0, 0, -1) | -2 | 4
(0, -1, -1) -> (1, -1, -1) | 4 | -8
(0, -1, 1) -> (0, -1, 0) | -2 | 4
(0, -1, 1) -> (0, 0, 1) | -2 | 4
(0, -1, 1) -> (1, -1, 1) | 4 | -8
(0, 0, -2) -> (0, 1, -2) | -1 | 2
(0, 0, -2) -> (1, 0, -2) | 1 | -2
(0, 0, 0) -> (-1, 0, 0) | -5 | 10
(0, 0, 0) -> (0, -1, 0) | 97 | -194
(0, 0, 0) -> (0, 0, -1) | -2 | 4
(0, 0, 0) -> (0, 0, 1) | -2 | 4
(0, 0, 0) -> (0, 1, 0) | -1469 | 14564
(0, 0, 0) -> (1, 0, 0) | 1381 | -14552
(0, 0, 2) -> (0, 1, 2) | -1 | 2
(0, 0, 2) -> (1, 0, 2) | 1 | -2
(0, 1, -1) -> (0, 0, -1) | 92 | -184
(0, 1, -1) -> (0, 1, -2) | 1 | -2
(0, 1, -1) -> (0, 1, 0) | -96 | 192
(0, 1, -1) -> (0, 2, -1) | -1 | 2
(0, 1, -1) -> (1, 1, -1) | 4 | -8
(0, 1, 1) -> (0, 0, 1) | 92 | -184
(0, 1, 1) -> (0, 1, 0) | -96 | 192
(0, 1, 1) -> (0, 1, 2) | 1 | -2
(0, 1, 1) -> (0, 2, 1) | -1 | 2
(0, 1, 1) -> (1, 1, 1) | 4 | -8
(0, 2, 0) -> (0, 1, 0) | -2 | 4
(0, 2, 0) -> (0, 2, -1) | 1 | -2
(0, 2, 0) -> (0, 2, 1) | 1 | -2
(1, -1, 0) -> (0, -1, 0) | -93 | 186
(1, -1, 0) -> (1, -2, 0) | -1 | 2
(1, -1, 0) -> (1, -1, -1) | -2 | 4
(1, -1, 0) -> (1, -1, 1) | -2 | 4
(1, -1, 0) -> (1, 0, 0) | 97 | -194
(1, -1, 0) -> (2, -1, 0) | 1 | -2
(1, 0, -1) -> (0, 0, -1) | -91 | 182
(1, 0, -1) -> (1, -1, -1) | -2 | 4
(1, 0, -1) -> (1, 0, -2) | -1 | 2
(1, 0, -1) -> (1, 0, 0) | 97 | -194
(1, 0, -1) -> (1, 1, -1) | -4 | 8
(1, 0, -1) -> (2, 0, -1) | 1 | -2
(1, 0, 1) -> (0, 0, 1) | -91 | 182
(1, 0, 1) -> (1, -1, 1) | -2 | 4
(1, 0, 1) -> (1, 0, 0) | 97 | -194
(1, 0, 1) -> (1, 0, 2) | -1 | 2
(1, 0, 1) -> (1, 1, 1) | -4 | 8
(1, 0, 1) -> (2, 0, 1) | 1 | -2
(1, 1, 0) -> (0, 1, 0) | 1675 | -15140
(1, 1, 0) -> (1, 0, 0) | -1675 | 14976
(2, 0, 0) -> (1, 0, 0) | 3 | -6
(2, 0, 0) -> (2, -1, 0) | -1 | 2
(2, 0, 0) -> (2, 0, -1) | -1 | 2
(2, 0, 0) -> (2, 0, 1) | -1 | 2
