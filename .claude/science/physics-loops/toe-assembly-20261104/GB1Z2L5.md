# GB1-Z2[L5]. The Z₂ rung in a five-mode law

## 0. Status

**Pass 2, not refereed.** The results are conditional on the algebras and readings below. They confer no retained or audit status.

**Proved.** The full invariant algebra of each `L5-U[m]`, 1 ≤ m ≤ 9, and `L5-O[S_+]` has a character (Theorem 2). The invariant algebra of the stated Z₂ source has none (Theorem 3). Hence no unital *-homomorphism between them exists (Theorem 4). This rules out the stated ZM1-INV readout, before dynamics, for both algebra and sector comparisons that require that same readout. Theorem 5 extends the obstruction to the specified finite abelian gauge sources. Theorems 6–9 give the locality, U(1), corner, subgroup and proposed-sector qualifications. The locked and oriented characters and the general character obstruction already appear in `ZM1INV.md` Theorem 2.1, R1 and R5; the odd-m application is made explicit here.

**GAP — R-SEC covariance.** The draft's candidate requires a cell-covariant map into a quotient but does not require the state class to make the quotient ideal cell invariant. The induced cell action therefore does not follow. Add cell-invariance of the ideal or of the state class. For an automorphic tick on the quotient, require invariance under both time directions. These are conditions on the proposed reading, not adopted law. The conditional obstruction in Theorem 9 does not need cell covariance.

**Open by name.** GB1-Z2[L5,SEC], under the proposed R-SEC or a similar quotient reading; the centre-Z₂ subgroup reading of (Z-c); GB1-O; GB1-U1 and GB1-SU2 beyond their proved sectors; GB1-H and its CA-I hand-off GAP; E-1, E-2, E-3, E-4 = Y3; GB1-SC; GB1-CF; T0-QLR[G], T0-start[G], T0-rate; Y1, Y2, Y2-W, VC1, TM1, ZM1-G and the observable dictionary. GB1-Z2[L5] is obstructed in the full-invariant-algebra reading specified here; other readings remain open. Correlator and universality bridges are not decided.

**Provenance.** Pass 1: Claude Opus 5.5, `GB1Z2L5_DRAFT.md`, SHA-256 `1406ac26626239adcdc70c13df879d4e75125fa04951570f9048e01442474a3b`. Pass 2: Codex `gpt-6.1-terra`; effort and session id: see run log. The draft reports checkout `4a0c580d67ec945d134cb319061c1fc6f9ce0c5b` and additional source revisions; this pass did not verify revisions by git. The digest is `prior/GB1Z2L5.md`, SHA-256 `5d6cadd308dc658a83202d8a5c9b094d6599afd8624b578e5e8b469c03df91f3`. The scratch checks below are pass-1 reports, not independently reproduced. No proposed law or reading is adopted.

## 1. Definitions inferred by the distiller

1. A finite region R comprises finitely many site matter factors and link factors; S(R) consists of those sites and all endpoints of its links. The quasi-local algebra is the norm closure of their union. Matter factors use the CAR grading; link registers are ordinary tensor factors. The region algebra includes the unit.
2. For `L5-U[m]`, each site has five CAR modes and each link is `Λ^m C^10`, with five rishon modes per end. The local gauge group is U(5), acting on matter and all link ends at each site by the Gauss generators of `LW1_5.md` §2. For `L5-O[S_+]`, each link is the even half-spin representation of Spin(20), and the local group is Spin(10), acting by the stated matter and end bilinears. Let A^G be the fixed algebra under every local gauge action; A^G(R)=A^G ∩ A(R). These are full-group invariants under conjugation, not a zero-charge sector.
3. A character is a nonzero *-homomorphism to C. It sends 1 to 1. A state defined by the empty matter vacuum and a chosen occupation vector on each link is called a product vector state; finite restrictions use the corresponding product vectors.
4. A Z₂ source is the invariant quasi-local algebra on Z³, or a coarse copy, with one qubit per link, Gauss operators G_x=P_x∏_{ℓ∋x}X_ℓ, and either no matter (P_x=1), one matter mode, or five modes (P_x=(-1)^N_x). For each square p put Z_p=∏_{ℓ∈∂p}Z_ℓ. Its named Trotter tick is given in `GB1.md` Definition 6 and Theorem 5M. A nonzero Gauss-sector representation or quotient is included when stated.
5. A ZM1-INV readout here is the unital injective cell-covariant *-homomorphism of `GB1.md` Definition 1, with its uniform support-radius exponential locality. Its target is A^G. Sector-level equality means the integer-time expectation identity of `GB1.md` Definition 2 on a fixed state class. It still requires this readout. A quotient target is a different, proposed reading.
6. A separating block map has, for every R, two source sites whose R-neighbourhoods in the fine lattice are disjoint. The usual finite cube zoom has this property. Uniform locality includes the unit viewed as supported at any source site, with common constants for support radius zero.
7. A full-rank subgroup reading replaces each local gauge group K by a closed H containing the diagonal torus used in Theorem 2. R-SEC is the proposed quotient reading in §7. Neither is adopted here.

The law parameters, NN-a and any GA1-P-5 update are as in `TOE_ASSEMBLY.md` §§3.4–3.9 and `LW1_5.md` §2. The obstruction does not use the update or the state. The owner keeps both five-mode laws live. R-form assigns a five-mode law to the coarse sites; it does not by itself identify a Z₂ source with that coarse law.

## 2. Characters of the named laws

**Theorem 1 (local invariant density).** The union of A^G(R) is norm dense in A^G. Averaging A(R) over the local gauge groups at S(R) maps it contractively onto A^G(R).

*Proof.* Each local gauge action factors over matter and incident link ends. Its outside factor commutes with A(R), so it preserves A(R); sites outside S(R) fix A(R). Haar averaging over the compact product group projects A(R) onto its invariants and is contractive. Given invariant A, approximate it by B in A(R); the average of B remains within ||A−B|| of A. □

**Theorem 2 (characters).** Each named-law invariant algebra has a character. The witnesses have empty matter and, on every positively oriented link, the following occupied end flavours:

- U, m=2k: {1,…,k} at both ends.
- U, m=2k+1: {1,…,k} at the lower and {1,…,k+1} at the upper end.
- O: all link modes empty.

*Proof.* On O links the ten-mode empty vector has even chirality and lies in S₊. Let A be invariant and localized in R. It commutes with the in-region parts of the diagonal Gauss generators: outside terms commute with A. Thus A preserves their joint occupation-weight spaces. We show that the witness's space is one-dimensional.

For U let d_x be the number of R-link ends at x and u_x the number of their upper ends. At even m the weights are d_x for flavours j≤k and zero for the others. No end contains a higher flavour; each link contains 2k particles. Thus both ends contain exactly the first k flavours, and the remaining matter occupations vanish.

At odd m the weights are d_x for j≤k, u_x for j=k+1, and zero above. Their total is m times the number of R-links. Since each such link already has m particles, matter is empty. Every end contains the first k flavours; each link has the (k+1)st flavour at exactly one end. Orient each link toward that end. Its indegrees equal those of the original positive orientation. On the edges where the orientations differ, the positive orientation therefore has equal in- and out-degrees at every vertex. A nonempty finite balanced directed graph contains a directed cycle, but every positive lattice edge strictly increases the coordinate sum. Thus no edge differs.

For O the diagonal generators are sums of n−1/2. The empty vector minimizes every term, so its joint weight forces all modes empty. In each case the joint weight space is one-dimensional. Therefore every local invariant acts on the witness by a scalar. Its expectation is multiplicative, unital and bounded on the local invariants; Theorem 1 extends it uniquely to a character. □

The witness is a state, not a selected vacuum, a singlet or a stationary state. `ZM1INV.md` Theorem 2.1 and R1 already state these characters; R1 also records base-tick invariance of the oriented state. `GA15PHI.md` Theorem 8 records a related frozen oriented sector at m=1,9.

## 3. The obstruction

**Theorem 3 (source).** Every Z₂ source of Definition 4 and every nonzero quotient or nonzero sector image has no character.

*Proof.* For a plaquette p and an edge ℓ in its boundary, X_ℓ commutes with every Gauss operator. Z_p also commutes: each corner contributes two anticommutation signs. Both are self-adjoint unitaries and X_ℓZ_p=−Z_pX_ℓ. A character would send each to ±1, contradicting that relation. Their images retain the relation and the unit in any nonzero quotient or nonzero unital representation. □

**Theorem 4 (plain-reading GB1-Z2[L5]).** There is no unital *-homomorphism from any characterless unital C*-algebra to either named law's A^G. In particular no ZM1-INV readout exists from any source or nonzero source quotient in Theorem 3. This holds for any admissible update, zoom, block map, state class and free parameters.

*Proof.* Composition with the character of Theorem 2 would give a character of the source. Theorem 3 excludes it. Injectivity, covariance, locality and dynamics are not needed. □

The first failing step in GB1(a), on the wider reading that permits a Z₂ source inside a larger frame group, is the unital readout into full A^G. Under the literal premise that the exact frame group itself be Z₂, neither named law meets that premise. A link-only invariant target is a unital subalgebra of A^G and inherits its character. Restricting the class of states does not change the target algebra. A sector quotient does; §7 treats it separately. `GB1.md` Theorem 5M already proves the proposed five-mode Z₂ test-law result, and Theorem 5U the stated U(1) frozen-sector result; neither is a readout into full A^G, and neither is overturned. `GA2_Y2.md` Theorem N4 constructs finite-group links on another carrier, not this embedding.

**Theorem 5 (electric–magnetic pairs).** A^G contains no invertible a,b satisfying ab=λba for scalar λ≠1. In particular it contains no anticommuting self-adjoint unitaries. Theorem 4 also applies to the standard Z_N lattice gauge invariant algebra, N≥2, and to the standard finite nontrivial abelian-group analogue, with regular link registers and the usual Gauss action.

*Proof.* A character sends invertible elements to nonzero scalars, so the relation forces λ=1. On Z_N links the shift X and clock Z have ZX=ωXZ, ω=e^{2πi/N}. X_ℓ is invariant; an oriented clock plaquette Z_p is invariant because its phases cancel at each vertex. For ℓ in its boundary, X_ℓZ_p=ω^{±1}Z_pX_ℓ. A finite abelian group is a product of cyclic groups; choose a nontrivial factor. The source consequently has no character, and Theorem 4 applies. □

The previously attempted (Z-a) fails its tick comparison in `GB1.md` §7. Its frozen qubit operators are not full-group invariants; Theorem 5 excludes a repair using a global-unit anticommuting pair in A^G. (Z-b) fails at the O-law matter layer, although its plaquette step works. (Z-c), the centre-only reading, failed the stated tests 1 and 4; centre invariants are larger than A^G and are not excluded by Theorem 5. A centre, a proposed exact remnant with such an electric–magnetic pair, and frozen U(1) charges all fail to supply the required full-A^G readout. This says nothing against an emergent remnant as a phase property or a correlator-level bridge.

## 4. Locality and the unit

**Theorem 6 (parity and locality).** Every invariant element is even under matter parity. A nonzero *-homomorphism Φ into A^G with Definition 5's uniform exponential locality and a separating block map is unital, even if unitality is not assumed.

*Proof.* For a local invariant take S=S(R). On U, the product over x∈S of the local gauge transformations exp(iπQ_x) equals matter parity P_S times link-end parities. Each link in R has both ends in S and contributes the scalar (−1)^m; boundary links outside R commute with the observable. Thus it commutes with P_S. On O, the product of the local torus rotations by π has site factor −iP_x and each end factor (−i)^5(−1)^{N_end}; the two ends of a link in R multiply to the scalar −1 on S₊. Boundary factors again commute. Density extends evenness to A^G.

Put P=Φ(1). It is a nonzero projection. Uniform locality applied to the unit at two arbitrarily separated source sites gives approximants A,A′ in disjoint finite algebras, each within δ of P, for arbitrarily small δ. Average each with its matter-parity transform; the approximants remain local, even and within δ. Average over the unitary group of the full matrix algebra containing A. It sends A to a scalar and fixes the even disjoint A′. Hence P lies within 3δ of a scalar. If δ<1/6, spectral calculus forces a projection so close to a scalar to be 0 or 1. Since P≠0, P=1. □

This conclusion uses uniform constants for the unit at all source sites; weaker element-dependent or nonseparating locality is not covered.

## 5. Scope and non-unital corners

**Theorem 7 (U(1) source).** The invariant algebra of the spin-S U(1) quantum-link source, with no matter or with the stated nonnegative-number matter, has a character. The character obstruction alone does not decide its readout.

*Proof.* Take empty matter and E_ℓ=S on every positively oriented link. In a finite region another occupation with the same local Gauss weights has E′_ℓ=S−δ_ℓ, δ_ℓ≥0, and N′_x=∑out δ−∑in δ. Sum over all endpoints: every N′_x vanishes. The finite nonnegative flow δ is balanced. Every positive edge increases coordinate sum, so a nonzero balanced flow would contain an impossible directed cycle. Thus δ=0 and the weight space is one-dimensional. Gauge averaging and the argument of Theorems 1–2 yield a character. □

**Theorem 8 (corners and subgroups).** (a) For every U-law m, A^G has a nonzero corner containing anticommuting self-adjoint unitaries with the corner projection as their unit. Thus it admits a non-unital embedding of M₂. (b) Theorem 4 holds for any closed local subgroup containing the torus used in Theorem 2, with A^G replaced by its invariant algebra.

*Proof.* (a) Pick three link ends at one vertex and project each onto end number q=1 for m≤6, q=4 for m≥7; these occupations are allowed. Write E^e_ab=r†_{e,a}r_{e,b} and T_ij=∑ab E^{e_i}_ab E^{e_j}_ba. These operators and the projection P are gauge invariant. On P, T_ij is the colour swap for q=1 and 3 plus the hole-colour swap for q=4. Subtract the respective scalar to obtain transpositions s,t. They represent S₃. Let P_std be the central projection onto its standard component. It is nonzero, for instance on a nontrivial cyclic Fourier combination of the three states with colours 112, 121, 211. On it, c=st obeys c+c²=−P_std. Set X=sP_std and Z=(2t+s)P_std/√3. The S₃ relations give X²=Z²=P_std and XZ=−ZX. Their Pauli representation gives M₂ in that corner. `GA15PHI.md` Theorem 2 already finds the standard S₃ multiplicity in a cube corner.

(b) Haar averaging works for closed H. Theorem 2 used only torus invariance to isolate the witness weight, so its character and Theorem 4 persist. □

Examples covered in U are T⁵, U(4)×U(1) and U(3)×U(2). This argument does not cover SU(5), S(U(3)×U(2)), the Standard Model SU(2), or the finite centre. It does not assert an obstruction for these smaller subgroups. The rishon link of the one-rishon example is nilpotent rather than unitary (consolidated #9926, cited by `prior/GB1Z2L5.md`); this is consistent with the distinction between U(1) quantum links and a unitary clock plaquette.

## 6. Prior work and checks

`prior/GB1Z2L5.md` records searches of the local and reference trees, including the finite-group carriers, the Z₂ and U(1) test laws, the path-sector result and failed routes. In particular, `ZM1INV.md` R5 already proves the characterless-source obstruction for even-m U and O; R1 supplies the odd-m character. Its Theorem 3.4's good path sector does not supply a unital global extension. `GB1.md` F4 already gives the finite-box transfer dictionary; it does not select a Euclidean law. `GA1_5.md` Proposition C already compiles its named plaquette class under NN-a, with gauge invariance required of the complete update. These source results retain their own stated status and hypotheses.

Pass 1 reports a bounded literature search for Wegner, Kitaev, Fradkin–Shenker, Krauss–Wilczek, Preskill–Krauss, Horn, Orland–Rohrlich and Chandrasekharan–Wiese. These provide context, not a proof input. Its record and fetched/unchecked distinctions are in `GB1Z2L5_DRAFT.md` §Literature. It found no statement of Theorem 4 in that search; this is not a novelty claim. Pass 1 reports occupation-weight counts of one on a plaquette for m=1,…,9 and on a cube for m=1,…,8; the cube m=9 run timed out. Scripts were `/tmp/toe-GB1Z2L5/check_weights.py` and `check_cube.py`. They were not rerun in this pass and are not proof.

## 7. Proposed reading R-SEC

**R-SEC, proposed, not adopted.** Fix a state class S in advance. Define J_S={A∈A^G: ω(A* A)=0 for all ω∈S}. The candidate replaces the target by A^G/J_S, asks for a unital injective cell-covariant exponentially local *-homomorphism into that quotient, and compares quotient dynamics in the sense of Definition 5. Locality uses images of local algebras. Require S to be stable under nonzero normalized operations ω(B* · B)/ω(B*B). For an induced cell action, additionally require J_S to be invariant under each cell symmetry and its inverse; invariance of S under those transformations suffices. For an automorphic tick require the analogous two-sided tick invariance. A nonempty S ensures a nonzero quotient.

The original draft gives tests **C C P P**: it changes the owner's readout without stating the desired rung; the freely chosen class can be tailored; it does not decide VC1 membership or continuum questions; it removes a requirement while using a class already present in sector comparison. These are pass-1 assessments of the original proposal, not an owner decision. The added covariance condition above repairs a missing well-definedness hypothesis; it has not received a fresh four-test review.

**Theorem 9 (conditional quotient obstruction).** Under the operation-stability condition, J_S is a closed two-sided ideal. If some ω∈S dominates λχ̃ for λ>0 and a state χ̃ whose restriction to A^G is a character, then A^G/J_S has a character and admits no unital Z₂-source readout.

*Proof.* J_S is closed and a left ideal since ω(A*B*BA)≤||B||²ω(A*A). For A∈J_S, operation stability gives ω(B*A*AB)=0, including the case ω(B*B)=0 by the same norm bound, so AB∈J_S. Thus it is two-sided. If A∈J_S, λ|χ̃(A)|²=λχ̃(A*A)≤ω(A*A)=0. The character factors through the quotient; Theorems 3–4 apply. □

In particular S cannot contain a witness state of Theorem 2 if such a readout is to exist. The corner in Theorem 8 gives kinematic room away from those witnesses, not a Z₂ dynamics or readout. **GB1-Z2[L5,SEC] remains open** if R-SEC or a similar reading is adopted. GB1-SC separately asks whether VC1 lies in a relevant sector. If invariance of S under the tick means only forward invariance, it yields at most an induced endomorphism; equality of the ideal under both time directions is needed for the integer-time automorphism stated above.

## 8. No-go discipline and limits

The negative statement is the explicit algebraic Theorem 4, not a classification of all possible physical bridges. Five proposed routes and their outcomes: (1) centre-only invariants leave the theorem's target and remain open; (2) an exact full-algebra electric–magnetic pair is excluded by Theorem 5; (3) frozen charge states retain the same target and are excluded by Theorem 4; (4) a non-unital but uniformly local map is excluded under the separating-block hypothesis by Theorem 6; (5) a sector quotient changes the target and is open except for Theorem 9. These routes do not establish five independently closed route families. N1's five-family packet requirement is not met; no gate PASS is claimed.

N2: the character obstruction is one wall; locality and quotient conditions are separate scope hypotheses, not asserted independent walls. N3: the carrier, full local group, source plaquette pair, unit, and locality quantifiers are explicit above. N4: `ZM1INV.md` R5 matches the even-U/O character residual; its R1 supplies the odd-U witness, while `GB1.md` 5U and the path sector address different, restricted-sector residuals. N5: Theorems 3–5 use one edge and one plaquette but apply to the infinite quasi-local algebra via its unit; Theorem 2 treats every finite region and its norm closure. They do not classify individual site or mode encodings in other target algebras. N6: quotient, subgroup and correlator readings are possible reframings; no claim says a new axiom is required. N7: the strongest counterroute is a physically relevant, cell-covariant quotient sector excluding character states, with an invariant local embedding and exact tick intertwining; Theorems 8–9 leave that terminal obligation open. N8: `ZM1INV.md`'s good path sector and `GB1.md` 5U show how restriction to a sector can recover structure despite a global obstruction. Their sector mechanism is explicitly retained here; no exhaustive cross-cycle search or packet certification was performed. No runner certificate or independent referee is claimed.
