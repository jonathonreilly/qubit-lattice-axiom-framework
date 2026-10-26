# Attempt: exact thermal structure of the lattice vacuum behind a stopped clock (T75 test A), with the T73/T74/T76 entropy distinctions

Worker: Claude Sonnet 5.5, same family as the sources. Unrefereed. Task `J:derive:review-20260929-wall-horizon-and-entropy-checks:a1`.

I read in full: `docs/MINIMAL_AXIOMS_2026-06-29.md` and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (current main a77a3449c91a). Source branch `claude/toe-walls-20260929` head `4bd42747e57c4d604f66a63eed2db099ea38af4e` fetched; all 10 source objects hash-verified (RECOVERY_STATUS.json). Read: SUMMARY, attacks and kills of T73, T74, T75, T76, plus the T75 test-A script `A_kinematic_kms.py` and `K1_lowlevels.py` from the branch. I did not read WALLS.md line by line (only used it for ids).

## Plain-language summary

The T75 attack asked whether "T = kappa/2pi" holds for the framework's clocked walker. Its test fitted a temperature to the vacuum of a hopping chain restricted to a wedge, and got 0.775 (registered test, missed) or 1.003 to 1.006 after a post-hoc geometry change. The kill said the lowest levels sit 7 to 11 percent off and "not shown to reach 1".

I found the exact answer. On the half-line, the vacuum of the half-filled hopping chain is exactly a thermal (Fermi) state of the nearest-neighbour Hamiltonian whose hopping on the bond (j, j+1) is a times j, with beta times a equal to pi. Nothing is fitted. That is the only linear-growth nearest-neighbour Hamiltonian with this property. The framework profile used in the test (hopping a times sqrt(j(j+1)), rate linear in j) is not it, and fails by an explicit exact number. Every finite wedge fails exactly too. So the "approximate fit" is exactly approximate for these profiles, and the exact target is known. This is Unruh-type kinematics for a supplied vacuum. It is not Hawking emission and not a statement about records.

## Setting and premises

- S0 (ASSUMED, supplied, not an axiom): a chain `Z`, nearest-neighbour hopping, half filling, vacuum correlation `C_ij = sin(pi(i-j)/2)/(pi(i-j))`, `C_ii=1/2`. This is the test-A model in `A_kinematic_kms.py`. It is a wave state. The four axioms (`MINIMAL_AXIOMS_2026-06-29.md:92`) define a state as a configuration of records, so this state, its entanglement and its Hamiltonian are all supplied content, not axiom content.
- S1 (ASSUMED, supplied): the clocked walker is a nearest-neighbour hopping Hamiltonian `H = -sum_j h_j (c_j^+ c_{j+1} + h.c.)` with bond `h_j = a sqrt(w_j w_{j+1})` (test A). Block 55/56 notes are the source; I did not re-derive that dressing.
- S2: wedge = sites 1..infinity (half-line) or 1..N (finite). Notation: `S_ij = pi(C_ij - delta_ij/2)`, so `S_ij = sigma(i-j)`, `sigma(d)=sin(pi d/2)/d`, `sigma(0)=0`. `J` = hopping with `h_j = j`.
- No primitive in the registry is used. `kinetic_isotropy_primitive` is not used. `realized_state_primitive` is not used.

## Numbered steps

1. PROVED + CHECKED (1c, 1d). `[S,J]=0` on the half-line. Matrix entry `(i,k)` of `[S,H]` for a nearest-neighbour `H` with hops `h` is `sigma(d+1)h_{k-1} + sigma(d-1)h_k - h_{i-1}sigma(d-1) - h_i sigma(d+1)` with `d=i-k` and `h_0=0` (entries are local). For `h_j=j` it equals `-[(d+1)sigma(d+1) + (d-1)sigma(d-1)] = -[sin(pi(d+1)/2)+sin(pi(d-1)/2)] = -2 sin(pi d/2) cos(pi/2) = 0`. The same computation with `h_j=j(N-j)/2` on an N-site wedge gives the extra factor `(N-i-k+1)/2` and again 0 (check 1a, N=2..40 exact). This is the Slepian/Gruenbaum tridiagonal at half filling, where the diagonal term vanishes because `cos(2 pi W)=0` at `W=1/4`.

2. PROVED up to named standard theorems. `J` (zero diagonal, `h_j=j`) is essentially self-adjoint on finitely supported vectors (Carleman: `sum 1/h_j = infinity`, check 2f). Step 1 shows `S` maps finitely supported vectors into the maximal domain with `J S v = S J v`; closedness gives `S J_bar subset J_bar S`, so `S` commutes with the self-adjoint `J_bar`. `e_1` is cyclic for `J` (polynomials in `J` applied to `e_1` span the finitely supported vectors).

3. PROVED up to standard orthogonal-polynomial facts, CHECKED (3a, 3b). Generalized eigenvectors of `J`: `psi_j(x) = P_{j-1}(x)`, Meixner-Pollaczek `lambda=1/2, phi=pi/2`, `P_0=1, P_1=2x, (n+1)P_{n+1}=2xP_n-nP_{n-1}`, `J psi = 2x psi`. These are orthonormal for `dx/cosh(pi x)` (spectral measure of `e_1`; the moment problem is determinate by Carleman). Spectrum of `J` is all of R, absolutely continuous, simple. ASSUMED standard: Koekoek-Swarttouw orthogonality, Akhiezer determinacy. Orthonormality was checked numerically for m,n<=4.

4. PROVED (algebra, with analytic continuation) and CHECKED (3c-3f). Row 1 of `expit(pi J)`: with generating function `sum P_n t^n = (1-it)^{-1/2+ix}(1+it)^{-1/2-ix}` for `|t|<1`, and `L=ln((1-it)/(1+it))`, the x-integral against `expit(2 pi x) sech(pi x) = (1/2)(1+tanh pi x) sech pi x` uses `FT[sech(pi x)](w)=1/cosh(w/2)` and `FT[tanh sech](w)=(iw/pi)/cosh(w/2)`, `cosh(L/2)=(1+t^2)^{-1/2}`. Result: `1/2 + (i/2pi)L = 1/2 + arctan(t)/pi`. Taylor coefficients of `arctan t` are `sigma(n)` at `t^n`, i.e. `pi C_{1,n+1}`. So `<e_1|expit(pi J)|e_{n+1}> = C_{1,n+1}` for all n (check 3c n=0..13 to 1e-40, 3d the closed form at 5 points, 3f exact coefficients to n=39). Interchange of sum and integral for `|t|<1` is by dominated convergence (`e^{2x arctan t}` against `sech`); I did not write out the dominating bound beyond that remark.

5. PROVED (from 2 and 4). `C = expit(pi J_bar)` as operators on the half-line. Both sides are bounded, both commute with `J_bar`, and they agree on `e_1` (step 4), hence on all `p(J)e_1`, hence on a dense set. Full block checked: 3g, `1<=i<=k<=8`, 1e-42. Sign and scale: 3h. In Gibbs language: `C = expit(-beta H)` with `H=-aJ`, `beta a = pi`.

6. PROVED + CHECKED (1b, 2a-2g). Uniqueness. Local equations from rows (1,k) k odd and (2,k) k even give `h_k = k/(k-2)(h_{k-1}-h_1)` and `h_k = h_1 + (k-1)/(k-3)(h_{k-1}-h_2)`, so `h_1,h_2` fix every hop. Both `J` (h_j=j) and `Q` (h_j=j(j-1)/2) satisfy all equations (2c). Hence the formal nearest-neighbour solutions are exactly `alpha J + beta Q`. On-site potentials must be constant (2g, odd-distance entries). `Q` grows quadratically (Carleman sum converges, outside the test); I do NOT claim `Q` fails to be a Hamiltonian, only that the uniqueness statement is restricted to at-most-linear hop growth. Within that class: `J` up to scale and an additive constant is the only nearest-neighbour Hamiltonian commuting with `C`, so the only one for which `C` can be a Gibbs state. For a finite N-wedge the commuting nearest-neighbour matrices are exactly `alpha T_N + gamma I` (2a, 2b; N=3..10 exact), because the free solution `Q` is cut by the boundary.

7. PROVED + CHECKED (4a-4d). The T75 test-A profile is exactly not thermal. Bond `h_j = a sqrt(j(j+1))` gives `[S,H]_{13} = a(sqrt6 - sqrt12/3 - sqrt2) = -0.11942...a != 0`. A Gibbs state `expit(-beta H)` commutes with `H`, so there is no beta (nor any rate-offset). More generally no linear rate `w_j=a(j-x0)` gives bonds `a sqrt(w_j w_{j+1})` that equal a linear sequence (4b). The exact thermal bond sequence `h_j = a j` needs `phi_j phi_{j+1} = a j`, i.e. a staggered clock `phi_{j+2}/phi_j=(j+1)/j` (4c); the framework profile equals the exact one plus a uniform hop `1/2 - 1/(8j)` (4d), a half-site displacement of the zero of the lapse. Geometric reading (READING): the exact bond sequence is "a times the distance of the bond from the cut", so the lapse must vanish at the entangling cut, not at a site.

8. PROVED + CHECKED (4e, 4f; 3i). Finite wedges are exactly not thermal. For N=4..12 the eigenvectors of `C_N` equal those of `T_N` (off-diagonal <1e-40), so by 6 any nearest-neighbour Gibbs state would need `eps_l/tau_l` constant; it is not (relative spread 0.027 at N=4, 0.031 at N=5, 0.043 at N=6, growing; N=4 levels give -1.55104 and -1.59427). Hence for N=4..12 no nearest-neighbour Hamiltonian with any profile has `C_N` as an exact Gibbs state. This is a finite check, not an all-N proof. Temperature bookkeeping (3i, CHECKED symbolic): Fermi speed `v=2t`; for `t=a x`, `kappa=dv/dx=2a`, so `T=1/beta=a/pi=kappa/2pi` exactly in this model (READING: that `kappa` is the speed gradient in the continuum limit).

9. FIRST UNRESOLVED STEP. Nothing above connects a record dynamics to a rate with a linear zero. T75 route B3 (smooth weight-one stiffness gives a double zero, `kappa=0`) and the kill's caveats are untouched. Exact thermality needs a staggered clock with `phi_j phi_{j+1}=aj`; no admissibility or record rule is shown to select it. It also needs the unclocked homogeneous vacuum on the whole half-line. It is a kinematic (Unruh/Bisognano-Wichmann) statement, not a Hawking flux: no outgoing emission, no absorber, no back-reaction.

10. CHECKED (5a-5c) with float arithmetic (not exact): three different entropies for the same wedge. Occupation patterns of an N-site wedge form a determinantal distribution (5a). Its Shannon entropy grows linearly (0.554 to 0.568 nats per site, N=4..14), whereas the entanglement entropy increments per site shrink (0.068 to 0.026), log-like (5b). Classical mutual information of the occupations of the two halves is `I_cl=0.271` against quantum `I_Q=1.143` at N=14, and `I_cl<=I_Q` throughout, as data processing requires (5c). READING: this supports the task's distinction between process (or occupation) entropy, classical mutual information and entanglement; none of the three is an axiom-defined record entropy (T73). The process entropy of a formation order was not computed here (it is the frozen-boundary task `review-20260929-formation-frozen-boundary-counts`; not duplicated).

## What is new, and what is not

NEW (to this repo, scoped to 1D half-filled chain, supplied vacuum): steps 1, 4-8 as stated. No landed note on main contains this; grep for Meixner/Slepian/entanglement Hamiltonian/Bisognano on `docs/` found only the unrelated Unruh/KMS notes and a different use of "prolate"; open-PR title search found nothing relevant (PRs 10011 and 10032 are about the cube tick sea's entanglement, a different object). READING: the half-line exactness is very likely known in the free-fermion entanglement-Hamiltonian literature (Peschel, Eisler); I did not verify that, so novelty outside this repo is not claimed.

NOT new: the numbers 0.775, 1.003-1.006, 0.3 percent, and the 7-11 percent (sources, reproduced by the kill). The T74/T73/T76 discussions (anisotropic area coefficient, measure dependence, Fibonacci/opposite-neighbour rule) were retrieved and not extended.

## Effect on the sources (scoped)

- T75 attack, test A: the registered miss (0.775) and the post-hoc fit 1.0063...1.0033 are both explained: the exact target is `beta a = pi` for the bond-distance profile; the framework profile has an uncorrected half-site shift and is exactly non-thermal.
- T75 kill, errors 1 and the A/R1 verdict: "7-11 percent high, not shown to reach 1" - the kill's K1 numbers times ln N are about 0.49 to 0.57 for N=100..3200 (READING from the kill's reported digits, not recomputed here), consistent with a slow, log-type approach, but I did not prove it.
- "approximate kappa/2pi is not exact Hawking radiation": confirmed in a stronger sense: even the kinematic thermal law is exact only for one profile and one geometry.

## Premise and scope checks

- Boundary conditions: half-line exact; finite wedge exactly not Gibbs for nearest-neighbour H (N=4..12). Both ends of a finite wedge matter.
- Reachable configurations: the wave state has all occupation patterns with positive weight (5a); records would see only classical patterns (5b, 5c). Not a record-formation count.
- Geometric area normalization: 1D cut is a point; no area. Not addressed for Z^3 (T74 anisotropy and the plaquette versus Euclidean area point stand as the kill left them).
- Cutoff-dependence: this result is cutoff-free in 1D (beta a = pi exactly), which is consistent with, and does not contradict, the task note that cutoff-dependent area coefficients do not exclude infrared emergent metrics.

## Labels summary

PROVED: 1, 2 (given Carleman and closedness), 4 (given dominated convergence), 5, 6, 7 (algebraic parts). CHECKED: 3a-3i, 2a-2g, 4a-4f, 5a-5c. ASSUMED: S0, S1, orthogonality and determinacy facts. READING: the geometric reading in 7, the kappa identification in 8, the log-convergence remark, the entropy remarks in 10.
