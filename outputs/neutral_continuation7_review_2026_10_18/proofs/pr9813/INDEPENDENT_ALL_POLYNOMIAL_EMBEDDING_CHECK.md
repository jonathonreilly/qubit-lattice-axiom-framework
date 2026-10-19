<!-- Original PR9813 source SHA256 c26c365a2fe8fb92c7f6bb57a36fac335fb82f588c55d48e5dc4cd91f157a004. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Focused check: low-energy embedding on arbitrary fixed polynomial boxes

Disposition: the proposed positivity argument is valid under the same termwise local normal-form hypotheses already used in the polynomial-grid proof. It removes the p<2 restriction from the *low-energy wall embedding*. It does not construct an exact identification of the entire N=0 band, and it does not by itself prove the proposed Q8 dispersion/source theorem.

## Global Q-relative positivity

Write the retained N0 Hamiltonian as Hcol. Apply its finite-order local bad-plaquette normal form to obtain

W Hcol W^dagger = e0 I + J lambda^4[a Q+sum_(j>=2) lambda^j D_j]+R_Q,

where a=L/64>0, Q=sum B_p, and the retained local terms are individually Q-preserving and plane invariant. Complete each tested neighborhood with the bounded collar needed to determine its local plaquette constraints. The established flat-neighborhood argument gives, for each retained order,

|<psi,D_j psi>| <= C_j <psi,Q psi>

for arbitrary psi, not merely psi in Q=4. This follows by summing the local projector sandwiches and bounded overlaps. The form inequality is global across all charge sectors. It is stronger than a finite-Q operator-norm bound.

For any fixed truncation order, take lambda small enough that sum_(j>=2) C_j lambda^j <=a/2. Then

W Hcol W^dagger >= e0 I +(a/2)J lambda^4 Q -epsilon_Q I,

epsilon_Q=||R_Q||<=C J R^2 lambda^M.

In particular Hcol>=e0-epsilon_Q globally. The constants depend on the chosen finite order and fixed height, not on R. This is a lower bound, not a claim that the full bandwidth becomes small. It requires no upper bound on Q.

## Extension to wall labels

The reference-spin/wall-bit labeling is unitary on each fixed-height column. Extending Hcol by identity on the wall labels preserves its global lower bound exactly. Likewise W can be lifted by acting on reference spins and as identity on those labels; it commutes with N. Therefore conjugating a wall-relative form bound by this lift does not change its right-hand side C lambda N.

Starting from the retained first normal form

|B-2JN-Hcol_ext| <= C J lambda N

in the quadratic-form sense, one obtains

B-e0 >= J(2-C lambda)N-epsilon_Q I.

The same follows directly by inserting the lower bound on Hcol_ext, without actually lifting W. The lifting construction is useful for subsequent low-Q reductions. For the even-height application, the physical plane actions on reference spins differ from their N0 actions only by conserved wall-label factors; an equivariant reference-spin construction can therefore retain the desired exact plane sectors.

Because the retained B commutes with N, its restriction to N>=2 is bounded below by e0+J(4-O(lambda))-epsilon_Q. Meanwhile the selected Q0, Q4 and Q8 retained levels lie e0+O(J lambda^4), with their already established finer splittings. Thus low-energy wall separation does not require the whole N0 spectrum to lie below every N>=2 level.

## Exact microscopic transfer

Let epsilon_N be the global tail of the first local normal form. For each fixed p>0 and R comparable to lambda^-p, choose a sufficiently large fixed construction order so epsilon_N+epsilon_Q <=C J lambda^(M-2p) is smaller than the particular low-energy gap or signal to be resolved. All subsequent denominator losses must be included when specifying the final absolute M, as in the existing proof.

The retained block-diagonal Hamiltonian has a fixed order-J separation between the target low-energy windows and its N>=2 part. Adding the global microscopic tail then transfers the low-energy spectral projectors by ordinary bounded-perturbation estimates. For internal Q0/Q4/Q8 subclusters, use their actual smaller retained fibre gaps and choose M accordingly. Weyl/minmax bounds transfer eigenvalues; projector conclusions additionally require those stated gaps and cannot be obtained from minmax alone.

One must replace the old wording 'exact N0 identification' by 'exact low-energy spectral identification with the retained N0 states' here. High-Q N0 states can overlap wall-sector energies, so an exact unitary separating the entire N0 band is neither justified nor needed. Exact momentum and plane symmetries allow all small-gap estimates in the relevant fibre rather than across neighboring momenta.

## What this does and does not remove

For every chosen finite p, polynomial volume factors can be beaten by choosing a sufficiently large but still fixed normal-form order. Fixed-order support remains bounded while R tends to infinity, so the local flat-neighborhood and no-full-row arguments remain applicable. This removes the artificial p<2 bandwidth obstruction to low-energy embedding.

It does not give a uniform statement in unbounded p, an infinite-volume theorem at fixed lambda, or a uniform global-ground character selection. The normal-form constants can grow strongly with order. Nor does it automatically prove a Q8 pole at q much smaller than lambda^4: the full Q8 low-energy classification, separation from competing channels, spatial-moment bounds, source cancellation and the appropriate orientation gap still require their own proof. If those are established, the wall embedding itself no longer prevents choosing a fixed p>4 and making the absolute tail sufficiently small.
