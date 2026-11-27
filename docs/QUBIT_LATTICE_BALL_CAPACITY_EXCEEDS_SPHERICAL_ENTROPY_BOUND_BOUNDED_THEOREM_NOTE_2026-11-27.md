# Under tensor-product composition, every large enough qubit-lattice ball can hold more entropy than the spherical entropy bound allows, for every lattice-to-Planck ratio

**Date:** 2026-11-27
**Type:** bounded_theorem
**Primary runner:** [`scripts/qubit_lattice_ball_capacity_exceeds_spherical_entropy_bound_2026_11_27.py`](../scripts/qubit_lattice_ball_capacity_exceeds_spherical_entropy_bound_2026_11_27.py)
**Runner cache:** `logs/runner-cache/qubit_lattice_ball_capacity_exceeds_spherical_entropy_bound_2026_11_27.txt`

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: "Conditional on the tensor-product composition hypothesis stated in section 1, which the four axioms do not supply. The spherical entropy bound enters only as an imported comparator."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Exact lattice-point bounds, an elementary rational inequality chain and a standard maximum-entropy lemma prove that, if the sites of a region compose by tensor product, the maximum entropy of a lattice ball exceeds the spherical-entropy-bound value of an enclosing sphere for every ratio a/l_P > 0 once the ball radius is at least max(7, 6 (a/l_P)^2) lattice units. A convex set of states that obeys the bound therefore contains fewer mutually orthogonal pure states than the region's Hilbert-space dimension. No gravitational dynamics, no entropy bound and no physical identification is derived."
target_claim_id: null
target_blocker_text: "GR2-ii: refinement together with collapse"
source_of_blocker_text: handoff
artifact_role: theorem
next_trace_action: "The owner of the TOE assembly skeleton decides whether its general-relativity part states the necessary condition of section 7; a candidate realization of collapse then names the convex set of states it admits in a ball and proves its orthogonal-state count."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## 0. Target claim, premises and obligation graph

**Target claim (one sentence).** If the sites of every finite region compose by tensor product, then for every ratio $\lambda = a/l_P > 0$ and every integer $R \ge \max(7, 6\lambda^2)$ the maximum von Neumann entropy of the lattice ball $B_R$ is larger than $\pi r^2/l_P^2$ for every sphere radius $r \le (R+1)a$.

The route this prunes: a lattice realization of general relativity in which every state of a region's tensor-product algebra stays admissible and the spherical entropy bound also holds. It does not prune realizations that restrict the admissible states, or that drop tensor-product composition.

**Premises read.**

- Lattice axiom and Qubit axiom, quoted from `docs/MINIMAL_AXIOMS_2026-06-29.md` at `origin/main` commit `8b11ae2bb95`: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency" and "The full one-site possibility domain has algebraic presentation `M_2(C)`."
- Hypothesis H-tensor (section 1). Not supplied by the axioms. Named in every statement that uses it.
- The ratio $\lambda = a/l_P$ is a free parameter. `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` states that the primitive "does not assert `a/l_P = 1` as a derived theorem". Every statement here holds for all $\lambda > 0$.
- Comparator, imported and not derived: the spherical entropy bound $S \le A/(4 l_P^2)$ (section 6).

| Obligation | Status here | Scope |
|---|---|---|
| Lemma A: the maximum entropy of a state on $M_D(\mathbb{C})$ is $\ln D$, reached only at the tracial state | Standard; proof given | All $D \ge 1$ |
| Theorem 1: $N(R) \ge (2m+1)^3$; and $N(R) > R^3$ for $R \ge 7$ | Proved here; exhaustive check $R \le 160$ | All integers $R \ge 1$ |
| Theorem 2: capacity of $B_R$ exceeds $\pi r^2/l_P^2$ | Proved here, given H-tensor | All real $\lambda > 0$, integers $R \ge \max(7, 6\lambda^2)$, radii $0 < r \le (R+1)a$ |
| Corollary 3: refinement at fixed physical radius | Proved here, given H-tensor | All $a \le \min(r/7, (r l_P^2/12)^{1/3})$ |
| Corollary 4: orthogonal-state count of a convex set that obeys the bound | Proved here, given H-tensor | Convex sets of states on the algebra of $B_R$ |
| The spherical entropy bound itself | Imported comparator; open in the repo | Not used as a premise of Theorems 1 and 2 |
| H-tensor from the axioms | Open | Not attempted |

**Strongest missing lemma.** A derivation, from the four axioms, of the algebra of a finite region of sites. With tensor-product composition the theorems apply. With another composition rule they need a new count.

## 1. Definitions and the composition hypothesis

For an integer $R \ge 1$ let
```math
B_R = \{x \in \mathbb{Z}^3 : x \cdot x \le R^2\}, \qquad N(R) = |B_R| .
```
Write $a$ for the lattice spacing, $l_P$ for the Planck length and $\lambda = a/l_P$.

**Hypothesis H-tensor (tensor-product composition).** For every finite $\Lambda \subset \mathbb{Z}^3$, the algebra of the region is
```math
\mathcal{A}_\Lambda = \bigotimes_{x \in \Lambda} \mathcal{A}_x, \qquad \mathcal{A}_x \cong M_2(\mathbb{C}),
```
so $\mathcal{A}_\Lambda \cong M_{2^{|\Lambda|}}(\mathbb{C})$.

The axioms do not state how the possibility domains of several sites combine. Their Qualification section says that "Further physical structure requires a retained derivation or bridge, or explicit approved-primitive registration, before use as a premise", and it defines "A state is a configuration of records." So H-tensor is a hypothesis here. The repo note `docs/CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02.md` (ledger: `positive_theorem`, `unaudited`) uses the same composition in its statement (D3), "the total Hilbert space is `⊗_{x ∈ Λ} H_x`", as a stated construction, not as a derivation. Fermionic composition of $N$ modes gives the same algebra $M_{2^N}(\mathbb{C})$ through the Jordan–Wigner map; this note does not use that fact.

**Capacity.** For a state $\omega$ on $M_D(\mathbb{C})$ with density matrix $\rho$ (so $\omega(X) = \operatorname{Tr}(\rho X)$), let $S(\omega) = -\operatorname{Tr}\rho\ln\rho$. The capacity of a region is $C(\Lambda) = \sup_\omega S(\omega)$ over all states on $\mathcal{A}_\Lambda$.

Capacity is a property of the algebra. It is not the entropy of any state the framework realizes.

## 2. Lemma A (maximum entropy)

**Lemma A.** On $M_D(\mathbb{C})$, $S(\omega) \le \ln D$ for every state, with equality exactly at the tracial state $\rho = I/D$. Under H-tensor, $C(\Lambda) = |\Lambda|\ln 2$.

*Proof.* Let $p_1,\dots,p_k$ be the nonzero eigenvalues of $\rho$, so $k \le D$ and $\sum_i p_i = 1$. Since $\ln$ is strictly concave, Jensen's inequality gives $S = \sum_i p_i \ln(1/p_i) \le \ln \sum_i p_i (1/p_i) = \ln k \le \ln D$. Equality needs all $p_i$ equal and $k = D$, which is $\rho = I/D$. With $D = 2^{|\Lambda|}$, $C(\Lambda) = |\Lambda| \ln 2$. $\square$

## 3. Theorem 1 (lattice-point count)

**Theorem 1.** Let $R \ge 1$ be an integer and let $m$ be the largest integer with $3m^2 \le R^2$.

1. $N(R) \ge (2m+1)^3$.
2. If $R \ge 7$, then $2m+1 > R$, and so $N(R) > R^3$.

*Proof.* (1) Every $x$ with $|x_i| \le m$ for $i = 1,2,3$ has $x\cdot x \le 3m^2 \le R^2$, so the cube $\{-m,\dots,m\}^3$ lies in $B_R$. (2) By the choice of $m$, $3(m+1)^2 > R^2$, so $m + 1 > R/\sqrt{3}$ and $2m+1 > 2R/\sqrt{3} - 1$. Since $3 \cdot (8/7)^2 = 192/49 < 4$, $2/\sqrt{3} > 8/7$. So $2m+1 > (8/7)R - 1 \ge R$ when $R \ge 7$. Then $N(R) \ge (2m+1)^3 > R^3$. $\square$

The runner checks both parts for every $R \le 160$. It also shows that part 2 needs a lower limit: $2m+1 \le R$ exactly at $R = 1, 3, 5$ in that range.

## 4. Theorem 2 (capacity versus the spherical-bound value)

**Theorem 2.** Assume H-tensor. Let $\lambda > 0$ be real and let $R$ be an integer with $R \ge \max(7, 6\lambda^2)$. Then for every radius $0 < r \le (R+1)a$,
```math
C(B_R) = N(R)\ln 2 \;>\; \frac{\pi r^2}{l_P^2}.
```

The spheres covered include the smallest sphere around the sites of $B_R$ (radius at most $Ra$) and the smallest sphere around their unit cells (radius at most $(R + \sqrt{3}/2)a$).

*Proof.* Two rational bounds are used.

- $\ln 2 > 69/100$. With $\ln 2 = \sum_{k \ge 1} 1/(k\,2^k)$, a series of positive terms, the partial sum to $k = 6$ is $1327/1920 > 69/100$.
- $\pi < 22/7$. Polynomial division gives $x^4(1-x)^4 = (1+x^2)(x^6 - 4x^5 + 5x^4 - 4x^2 + 4) - 4$. So $\int_0^1 x^4(1-x)^4/(1+x^2)\,dx = 22/7 - \pi$, and the integrand is positive on $(0,1)$.

Now $\pi r^2/l_P^2 \le \pi\lambda^2(R+1)^2$. Since $R \ge 7$, $R+1 \le (8/7)R$. Since $R \ge 6\lambda^2$, $R^3 \ge 6\lambda^2R^2$. With Theorem 1,
```math
N(R)\ln 2 > \tfrac{69}{100}R^3 \ge \tfrac{207}{50}\lambda^2R^2 > \tfrac{1408}{343}\lambda^2R^2
= \tfrac{22}{7}\left(\tfrac{8}{7}\right)^2\lambda^2R^2 \ge \tfrac{22}{7}\lambda^2(R+1)^2 > \pi\lambda^2(R+1)^2 .
```
The third step is $207 \cdot 343 = 71001 > 70400 = 1408 \cdot 50$. Lemma A gives $C(B_R) = N(R)\ln 2$. $\square$

**The threshold is not sharp.** The runner finds the exact smallest $R$ with $N(R)\ln 2 > \pi\lambda^2(R+1)^2$, with $\ln 2$ and $\pi$ in certified rational brackets of width below $10^{-15}$:

| $\lambda^2$ | smallest $R$ | Theorem 2 threshold $\max(7, \lceil 6\lambda^2\rceil)$ |
|---|---|---|
| 1 | 3 | 7 |
| 2 | 4 | 12 |
| 4 | 6 | 24 |
| 10 | 13 | 60 |
| 100 | 111 | 600 |

Each row also shows no return below the bound up to $R = 160$. Since $N(R)/R^3 \to 4\pi/3$, the crossover radius grows like $(3/(4\ln 2))\lambda^2 \approx 1.082\lambda^2$. That limit is a remark from the classical lattice-point asymptotics; it is not proved here and nothing uses it.

## 5. Corollary 3 (refinement at fixed physical radius)

**Corollary 3.** Assume H-tensor. Fix $r > 0$ and $l_P > 0$. For a lattice spacing $a$ let $R_a = \lfloor r/a \rfloor$. If $a \le r/7$ and $a^3 \le r\,l_P^2/12$, then $C(B_{R_a}) > \pi r^2/l_P^2$, and $C(B_{R_a}) - \pi r^2/l_P^2 \to \infty$ as $a \to 0$.

*Proof.* $r < (R_a + 1)a$. From $a \le r/7$, $R_a \ge 7$, so $R_a \ge r/a - 1 \ge r/(2a)$. From $a^3 \le r l_P^2/12$, $r/(2a) \ge 6a^2/l_P^2 = 6\lambda^2$. So Theorem 2 applies to $B_{R_a}$ and $r$. Its chain gives $C(B_{R_a}) - \pi r^2/l_P^2 > \tfrac{69}{100}R_a^3 - \tfrac{22}{7}\lambda^2(R_a+1)^2$. As $a \to 0$, $R_a \to \infty$ and $\lambda^2 = a^2/l_P^2 \to 0$, so the right side tends to $\infty$. $\square$

So refining the lattice at fixed physical size makes the excess larger, as $(r/a)^3$ against a fixed $\pi r^2/l_P^2$.

## 6. The comparator and where it comes from

The spherical entropy bound $S_{\rm matter} \le A/4$ (Planck units) is due to Susskind (1995), from the generalized second law applied to collapse of a shell onto a system. Bousso (2002, Sec. II.C) states its conditions: an asymptotic structure that permits black holes, an approximately spherical metric near the system, and a system stable on a time scale much greater than $A^{1/2}$. His footnote adds that the argument assumes the shell can be brought in without radiating or ejecting mass. Bousso (1999) proposed the covariant entropy bound, on light-sheets, and showed that it implies a spacelike bound (the spacelike projection theorem). That theorem needs a closed surface with a future-directed light-sheet $L$ that has no boundary other than the surface, and a spatial region $V$ contained in the causal past $J^-(L)$ of that light-sheet.

Role here: comparator only. The repo does not derive any of these bounds. `docs/AXIOM_FIRST_BEKENSTEIN_BOUND_THEOREM_NOTE_2026-05-01.md` records that its former entropy-bound inference was withdrawn and that the area bound is "a conditional external target". Theorems 1 and 2 do not assume the bound. They compare a number to it.

## 7. Corollary 4 and the necessary condition it gives

**Corollary 4.** Assume H-tensor. Let $\mathcal{K}$ be a convex set of states on $\mathcal{A}_{B_R}$ and let $s \ge 0$ with $S(\omega) \le s$ for every $\omega \in \mathcal{K}$. If $\psi_1,\dots,\psi_M$ are mutually orthogonal unit vectors whose vector states all lie in $\mathcal{K}$, then $M \le e^{s}$. If, in addition, $R \ge \max(7, 6\lambda^2)$ and $s = \pi r^2/l_P^2$ with $r \le (R+1)a$, then $M < 2^{N(R)}$. So $\mathcal{K}$ contains neither the tracial state nor the vector states of any orthonormal basis, and
```math
\frac{M}{2^{N(R)}} < \exp\!\Big(\tfrac{22}{7}\lambda^2(R+1)^2 - \tfrac{69}{100}R^3\Big).
```

*Proof.* The uniform mixture $\frac1M\sum_j \omega_{\psi_j}$ lies in $\mathcal{K}$ by convexity. Its density matrix has eigenvalue $1/M$ with multiplicity $M$, so its entropy is $\ln M \le s$. Only closure under uniform mixtures is used, not full convexity. Theorem 2's chain gives $s < \tfrac{22}{7}\lambda^2(R+1)^2 < \tfrac{69}{100}R^3 < N(R)\ln 2$. $\square$

This is 't Hooft's counting statement $e^S = \mathcal{N}$ (1993, eqs. (2)–(3)) made exact on this lattice. A set of states defined by an upper bound on a mean energy, $\{\omega : \omega(H) \le E\}$, is convex, so the corollary applies to it.

**Proposed necessary condition (for the owner of the TOE assembly skeleton; not adopted here).** The skeleton (`TOE_ASSEMBLY.md` on PR #10139) lists the open input "refinement together with collapse" (alias GR2-ii) for its general-relativity part. Suppose that part keeps H-tensor, and that it admits a family $\mathcal{K}$ of horizon-free states in $B_R$ with two properties: (i) $\mathcal{K}$ contains the uniform mixtures of its members, for example because it is convex; and (ii) the von Neumann entropy of every member of $\mathcal{K}$ obeys the spherical bound $S \le \pi r^2/l_P^2$. Then by Corollary 4 a candidate mechanism must name $\mathcal{K}$ and must show that it has at most $e^{\pi r^2/l_P^2}$ mutually orthogonal pure states. Both premises are needed. Without (i) there is a counterexample: the set of all pure states has zero entropy in each member, yet it contains a full orthonormal basis. Premise (ii) reads the imported bound as a bound on the von Neumann entropy of each admitted state. That reading is an identification, not derived here. Corollary 3 shows that refinement at fixed radius makes the required reduction stronger. The alternatives are to give up H-tensor for gravitating regions, or to give up the spherical bound as a target. Whether to state this condition is that owner's decision.

## 8. Literature and credit

- G. 't Hooft, "Dimensional reduction in quantum gravity", gr-qc/9310026 (1993). Eq. (2) identifies $e^S$ with the Hilbert-space dimension $2^n$ of $n$ Boolean degrees of freedom. Eqs. (4)–(11) argue that the states inside a closed surface number at most $e^{A/4}$. The text after eq. (11) observes that a regularized theory with a Planck-scale cutoff gives far too many states, which grow with the volume, and that most of them would collapse to a black hole.
- L. Susskind, "The world as a hologram", hep-th/9409089, J. Math. Phys. 36 (1995) 6377. Section 1 takes a three-dimensional lattice of two-state spins at Planck spacing, counts $2^n$ states, and contrasts $n \log 2$ with the area law.
- R. Bousso, "A covariant entropy conjecture", hep-th/9905177, JHEP 07 (1999) 004.
- R. Bousso, "The holographic principle", hep-th/0203101, Rev. Mod. Phys. 74 (2002) 825. Sec. II.C (spherical entropy bound and its conditions); Sec. III.A–E (degrees of freedom, the Planck-grid count $\mathcal{N} \sim n^V$, and why gravity invalidates it). Bousso notes that this argument "does not provide independent quantitative confirmation" that the maximum entropy is the area.

What this note adds to those arguments: exact statements on $\mathbb{Z}^3$ with explicit thresholds, valid for every value of the open ratio $a/l_P$, and the orthogonal-state count of Corollary 4. The idea is theirs.

## 9. Repo search record

At `origin/main` commit `8b11ae2bb95` (2026-11-27), `grep` over `docs/` and `research/` for `volume law`, `Bousso`, `spherical entropy`, `holographic bound`, `holographic principle`, and filenames containing `BEKENSTEIN`, `AREA_LAW`, `ENTROPY`, `HOLOGRAPH`, `BH_`. Of the 20 open PRs, four have entropy, holography, area, gravity or TOE in the title (#10128, #10139, #10140, #10172); their changed-file lists were searched for entropy, holography, capacity and count. Hits read:

- PR #10128, `A_CUBE_TICK_THAT_READS_ITS_OWN_LAPSE_AND_EDGES_IS_WEYL_BLIND_SO_ITS_VACUUM_ENTROPY_COUNTS_CUT_BONDS_NOT_PROPER_AREA_BOUNDED_THEOREM_NOTE_2026-10-22.md`: the entanglement entropy of a vacuum state across a cut. Not the capacity of the interior.
- PR #10172, `agents/capacity/note_draft.txt`: how many records relays can form before the sites of a block are used up. A different object.
- `docs/AXIOM_FIRST_BEKENSTEIN_BOUND_THEOREM_NOTE_2026-05-01.md`: geometric identities for $S_{BH}$ and a qubit countermodel to a withdrawn inference. No state count of a lattice region.
- `docs/HOLOGRAPHIC_PROBE_NOTE_2026-04-11.md`: floating-point fits of Schmidt rank against boundary and volume for chosen states. No capacity bound.
- `docs/AREA_LAW_*` notes: the coefficient of an edge or boundary entropy, not the capacity of the interior.
- `docs/CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02.md`: the block dimension $2^{|\Lambda|}$ under the same composition (section 1). No comparison with any entropy bound.

No repo statement of this comparison was found.

## 10. What the runner checks

All PASS decisions use exact integers and `fractions.Fraction`.

- The rational constants: $\ln 2 > 69/100$ from the partial sum; $\ln 2 < 7/10$ from the tail bound $1/((K+1)2^K)$, so a mutated constant $7/10$ is rejected; the polynomial identity behind $\pi < 22/7$ and the exact integral $22/7$; the Gaussian-integer form of Machin's formula, $(5+i)^4(239-i) = 114244(1+i)$, and alternating-series brackets that give $\pi$ to better than $10^{-15}$.
- $N(R)$ two ways: a column count with exact integer square roots, and a brute-force triple loop for $R \le 12$. Hand counts $N(1) = 7$ and $N(2) = 1+6+12+8+6 = 33$.
- Theorem 1 for every $R \le 160$, and the exact set $\{1,3,5\}$ where part 2 fails.
- Each rational step of Theorem 2, and the theorem's inequality on $R \in [\max(7,\lceil 6\lambda^2\rceil), 160]$ for six of seven rational values of $\lambda^2$. For $\lambda^2 = 100$ the threshold 600 exceeds 160, so that range is empty; the runner says so and checks the inequality instead at the spot values $R = 600$ and $R = 1000$.
- The three printed entropy gaps of Corollary 4 at $\lambda = 1$ ($R = 10, 20, 40$): each is a certified lower bound, printed rounded down to 0.001.
- The crossover table of section 4, with every $R \le 160$ decided by the certified brackets.
- The conditions of Corollary 3 on a grid of rational $r$ and $a$ ($l_P = 1$).

**Controls that fail when the statement is perturbed.**

- With the constant 5 in place of 6, the rational step of Theorem 2 fails.
- With threshold $\lambda^2/2$ in place of $6\lambda^2$, the conclusion is false: at $\lambda^2 = 100$, $R = 50$, $N(R)\ln 2 < \pi\lambda^2(R+1)^2$.
- With only the boundary sites of $B_R$ counted (sites with a neighbour outside), the conclusion fails for $\lambda^2 = 4$ at every $R = 7,\dots,60$. So the theorem depends on the volume count that H-tensor gives. The boundary count is checked against a brute-force count for $R \le 10$.

**Independent path.** The brute-force recount and the hand counts do not share the column-count code. The proofs in sections 2–5 are by hand and do not depend on the runner.

Lemma A and the mixture argument of Corollary 4 are standard finite-dimensional facts with complete proofs above. The runner does not check them; a floating-point check would prove nothing. It checks only the numerical gaps of Corollary 4.

## 11. Boundary of the claim

- The theorems are conditional on H-tensor. They say nothing about a composition rule other than the tensor product.
- Capacity is the supremum over all states of the region's algebra. The note does not claim that any state the framework realizes, or any configuration of records, has this entropy.
- The spherical entropy bound is a comparator. The note does not derive it, does not assume it for Theorems 1 and 2, and does not claim the framework must obey it.
- Theorem 2 covers $R \ge \max(7, 6\lambda^2)$. Smaller $R$ are covered only by the finite table for the listed $\lambda^2$.
- No statement here touches the Newton constant in lattice units or the nonlinear limit of the gravity response. No gravitational dynamics is derived.
