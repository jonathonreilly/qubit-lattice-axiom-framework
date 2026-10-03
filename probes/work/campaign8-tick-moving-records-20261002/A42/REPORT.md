**A42 report: does the hard limit (Theorem N) need the owner's Q3 gluing?**

The sandbox blocked writing `REPORT.md` (subagents may not write report files), so this message is the full report.

**Where things are**
- SP = `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad`
- Scripts and outputs are in `SP/c8/A42/` (`k1_…py` to `k5_…py`, each with `.out`).
- No git writes, no repo edits, no PRs.

**Sources read**
- On origin/main `b6fda5ae1d`:
  - the soldering menu note (2026-09-22);
  - `MINIMAL_AXIOMS_2026-06-29.md`;
  - `DEFERRED_DECISIONS.md` §2;
  - the archived Clifford census (cycle 40), the scalar CAR note (2026-07-11) and the compilation note (cycle 12).
- In scratch: A20 §3B, §3C, §3F, §6; A21 `REVIEW_FINAL.md`; `CHECK/G1.md` rows R1–R4 and §4 item 1.

**How the runs were made**
- Every run took `SP/c8/NUMLOCK`. On the first try another lane held it, so I did derivation work and retried.
- Every run used `nice -n 10`, the four BLAS caps at 1 and a 30 s alarm. The 1-minute load was below 6 at each start.
- The longest run took 3.6 s; peak memory was 73 MB.
- Some first attempts failed and were fixed before any result was used:
  - k1 failed twice: macOS has no `timeout` binary, and there was a half-turn lift bug.
  - The first k2 hit the 30 s alarm because sympy `simplify` was too slow. I rewrote it with the Weierstrass substitution and a gcd.

## 1. Question

**Setting (A20):**
- one qubit per site of Z³;
- a tick α is an automorphism of the quasi-local algebra, so it is reversible;
- nearest-neighbour (NN) reach: α(A_x) ⊆ A_{N̄(x)};
- α is covariant on every tick under translations and under the 24 proper rotations about each site, which act on the possibilities by a stated action ρ: O → SO(3).

**Theorem N (A20):** under full soldering, α = id.

The lane asks whether that needs Q3's full soldering:
1. Does adding possibility covariance give α = id?
2. What happens under axis soldering and under the sign twist?
3. What happens with no gluing, and which internal symmetry removes those ticks?
4. What changes with one fermion mode per site?
5. Which hypotheses exactly make "nothing can move" true?

## 2. Answer, graded

**Short answer.**
- Full soldering is one of several ways to freeze NN ticks, and it is needed only when nothing else ties the possibilities down.
- The outcome is decided by K, the group the symmetries induce on Bloch vectors: ρ(O) plus any imposed internal symmetry G. Two things matter:
  - whether K leaves any possibility axis in place;
  - whether K treats two distinct axes alike.

**A. Possibility covariance (Q1): EXACT, conditional on a reading.**
- Under every one of the four actions, an NN covariant tick that also commutes with every global internal turn is the identity.
- The proof uses N1, the axis-swapping half-turn and Schur's lemma. It needs no translations and no soldering.
- It works for any internal group acting irreducibly on Bloch vectors. The smallest such group is the 12-element tetrahedral group: the Pauli flips plus the relabelling X→Y→Z.
- Possibility covariance is a law-level reading of the Qubit sentence. Such readings are parked (DEFERRED §2, standing default "not adopted, either way"), so A is conditional on it.

**B. Per action, without possibility covariance.** EXACT; the explicit ticks are CHECKED (k1, k3).

| Action | α = id forced? | Can content move at NN reach? | Explicit NN covariant ticks |
|---|---|---|---|
| Full soldering (T1) | yes (Theorem N) | no | identity only |
| Axis soldering (A2+E) | **no** | **no**: no site's content ever leaves its closed neighbourhood | onsite half-turn about the body diagonal w = (1,1,1)/√3; w-controlled turns such as exp(iθΣσ^wσ^w) (non-Clifford) |
| Sign twist (A1+2A2) | **no** | **yes** | Clifford mover C_s′ = Ad(Π_edges CZ_z)∘Ad(H_yz^⊗), whose support spreads over 7, 13, 43, 49, 79, 85, 259, 265 sites; onsite turns about x; Ising ticks on x and on z |
| Unsoldered | no | yes | the census companions C_s and C_{1+s}; every uniform onsite turn; Ising ticks on any axis |

**C. One structure theorem and two criteria (EXACT).** They cover one qubit per site, NN reach and the four actions, with or without an internal group G. Let K = ⟨ρ(O), G⟩.
- **Structure.** Every covariant tick is one of two kinds:
  - (a) a uniform onsite turn that commutes with K;
  - (b) a fixed onsite turn taking an axis m to an axis n, followed by a turn of each site about n by an angle set by its neighbours' σ^n values. Here n and m are lines that K leaves in place, with the same sign under every element of K.
- **(I)** α = id for every such tick ⟺ K leaves no possibility axis in place (K is irreducible).
- **(II)** No such tick moves anything ⟺ K treats no two distinct axes alike (every sign-eigenspace of K has dimension at most 1).
- **What this means.** Moving at NN reach needs two different possibility axes that every symmetry treats identically: one that neighbours couple through (n), and one that the tick turns into it (m).
- **Per action:**
  - full: K = O, irreducible, so (I) holds;
  - axis: K = D₃; the only fixed line is w, so (II) holds and (I) fails;
  - sign twist: the whole plane ⊥ x has one sign, so both fail;
  - unsoldered: K = {1}, so both fail.

**D. Unsoldered action (Q3): EXACT; spot checks CHECKED.**
- Every nontrivial NN covariant tick fails possibility covariance.
- Each one privileges an axis of the possibilities; movers privilege two.
- Removing all of them needs an irreducible internal group; the smallest is tetrahedral, and the internal cubic group also works.
- Removing all movers needs only a group not contained in a single half-turn group. Examples are the Pauli group, which is the linear part of the parked Z₂³ flip group, or the single 3-fold relabelling.
- The total flip σ → −σ removes neither. It commutes with every global turn, and both movers pass it.

**E. Fermions, one mode per site with the graded product (Q4): EXACT.**
- The soldering menu becomes the homomorphisms O → O(2): signs, particle–hole swaps, and a D₃ type.
  - Three of them are distinct on parity-preserving ticks.
  - None is three-dimensional, so there is no analogue of full soldering.
  - All act trivially on the coordinate half-turns.
- N1 survives grading as a graded-commutation lemma.
- **Result:** every parity-preserving NN covariant tick is static. This holds whether it is interacting or not, number-preserving or not, and under every action.
- Majorana shifts are excluded at NN reach.
- Nontrivial static ticks exist.

**F. Cross-check against the archived census: consistent, with one corrected reading.**
- **Sign quotient.** The census's "sign quotient: 2, both involutions" is an artefact of the Clifford frame.
  - The menu's sign twist diag(1,s,s) is a twist about a Pauli axis, which falls in the census's site-only row.
  - In that row the spreading C_s class has an exactly covariant lift, C_s′.
- **Axis quotient.** "Full Pauli-axis quotient: 0" covers both full and axis soldering. The axis-soldering survivors are non-Clifford in that frame, so the census cannot see them.

**G. Plain verdict:** see §3.10.

## 3. Derivations

### 3.0 Tools

- **Support algebras.** S_x^(y) is the smallest unital *-subalgebra B ⊆ A_y with α(A_x) ⊆ B ⊗ A_{N̄(x)∖y}.
  - Let a symmetry act on sites by γ and onsite by r, and commute with α. Then S_{γx}^(γy) = r(S_x^(y)).
  - An internal turn Θ_g makes every S_x^(y) invariant under Ad g.
- **N1** (A20; A21 found it sound): commuting algebras on O∪P and O∪Q, with P∩Q = ∅, have commuting supports on O.
- **Lemma 0.** The unital *-subalgebras of M₂ are C1, span{1,σ^n} (one for each line n) and M₂.
  - Those invariant under a group H ⊆ SO(3) are C1, M₂, and span{1,σ^n} for the lines n that H leaves in place.
- **Relative commutant (standard).** The elements commuting with every site except y form A_y for qubits, and A_y^even for the CAR algebra.
- **The swap half-turn.** Take x, y = x+2e and m = x+e.
  - N̄(x) ∩ N̄(y) = {m}.
  - The coordinate half-turn H about m with axis ⊥ e swaps x and y.
  - H lies in V₄, the kernel of O → S₃. So ρ(H) = 1 under the trivial action, the sign twist and axis soldering; under full soldering ρ(H) is the Bloch half-turn about that coordinate axis.

### 3.1 Theorem P: possibility covariance (Q1)

**Statement.** Let G be a group of global internal turns acting irreducibly on Bloch vectors. Suppose α has NN reach and commutes with G and with the rotations about every site under any of the four actions. Then α = id.

**Proof.**
1. S := S_x^(m) is G-invariant, so S ∈ {C1, M₂}.
2. The swap half-turn gives S_y^(m) = ρ(H)(S) = S, because C1 and M₂ are invariant under every automorphism.
   - *Check under the trivial action:* ρ(H) = 1, the half-turn is a pure site map fixing m, and α(A_y) = Γ(α(A_x)) has the same support on m as α(A_x). The step applies unchanged.
3. By N1, S commutes with itself, so S = C1. This holds in all six directions, so α(A_x) ⊆ A_x.
4. **Onsite step.**
   - Comparing dimensions gives α(A_x) = A_x, and α restricted to A_x is Ad u_x, because every automorphism of M₂ is inner.
   - Ad u_x commutes with G. If Ad u_x ≠ id, its rotation axis would be a line fixed by G, which irreducibility excludes.
   - So α = id. ∎

**Notes.**
- **Neither translations nor ρ is used.** Under possibility covariance the four actions coincide.
- **Without rotations the result fails.** A shift α(A_x) = A_{x+e} commutes with every global turn; the swap half-turn is what removes it.
- **Irreducibility is necessary.** If K fixes a line n, Ad(σ^n)^⊗ and exp(iθΣσ^nσ^n) are nontrivial covariant ticks (CHECKED for the Pauli group and C₃).

**Stronger than the axiom text? Is a weaker invariance enough?**
- The Qubit sentences concern the one-site domain and do not mention laws.
- Taking them as "the law commutes with every automorphism of the supplied algebra" gives exactly possibility covariance. That is stronger than the text, and readings of this kind are parked.
- Qualification's "A law privileges no states" does not supply it, since "A state is a configuration of records".
- Weaker invariance is enough:
  - an irreducible group (12 elements) gives α = id;
  - a group not contained in one half-turn group gives "nothing moves";
  - under full soldering nothing extra is needed;
  - under axis soldering, one internal turn that moves the line w, such as one global Pauli flip, gives α = id.

### 3.2 N2–N6 redone with the correct onsite action (Q2)

**How each rotation acts on Bloch vectors** (CHECKED k1, menu matrices):

| Rotation | Trivial | Sign twist diag(1,s,s) | Axis s(g)·abs(g) | Full g |
|---|---|---|---|---|
| Quarter turn about z | 1 | half-turn about x | σ^x↦−σ^y, σ^y↦−σ^x, σ^z↦−σ^z: the half-turn about d_z = (e_x−e_y)/√2 | quarter turn about z |
| Coordinate half-turn | 1 | 1 | 1 | half-turn about that axis |
| 3-fold about (1,1,1) | 1 | 1 | cyclic X→Y→Z | cyclic |
| Face-diagonal half-turn | 1 | half-turn about x | the crossed diagonal: (1,1,0) acts as (1,−1,0) | itself |

The images are homomorphisms with det 1, splits 3A1, A1+2A2, A2+E and T1, and image orders 1, 2, 6 and 24. Their centralizers in SO(3) are SO(3), O(2)ₓ, {1, R_w(π)} and {1}.

**Steps**

| Step | Trivial | Sign twist | Axis | Full |
|---|---|---|---|---|
| N1 | holds | holds | holds | holds |
| N2: stabilizer of e_a | free | n = x or n ⊥ x | n = d_a or n ⊥ d_a | e_a only |
| N2: swap half-turn | abelian support | abelian | abelian | abelian |
| The six neighbour lines | all equal | all equal | equal only for n = w, otherwise a triple | the triple e_a |
| N3 | void | void | w: void; perpendicular triples: parity pair; every other angle: no commuting pair (k2, exact), so the branch is empty | parity pair |
| N4 | fails | fails | holds in the perpendicular triples | holds |
| N5 | replaced by Lemma C | Lemma C | triples: u_± ∈ {1, R_w(π)}; mixed controls are not automorphisms (k3b), equal controls are onsite, so the branches are empty; w: Lemma C | controlled turn |
| N6 | fails | fails | fails: R_w(π) survives | holds |

**Lemma C** applies when all six neighbour supports are span{1,σ^n} with one line n.
- (i) α(σ^m_y) = σ^n_y for one unit vector m and every site y.
  - Proof: σ^n_y commutes with every α(A_x), x ≠ y. So α⁻¹(σ^n_y) lies in the relative commutant A_y, and it is a self-adjoint unitary other than ±1.
- (ii) n and m are lines fixed by every symmetry, with equal signs.
  - Proof: let a symmetry act on sites by γ and onsite by r, with r(n) = χn. Then α(σ^{rm}_{γy}) = χα(σ^m_{γy}).
- (iii) If m = ±n, then α^t(A_x) ⊆ A_x ⊗ alg{σ^n_z : z ∈ N(x)} for every t: nothing ever leaves N̄(x).
- (iv) In general, α(a_x) = Σ_s R_n(φ_s) u₀ a u₀† R_n(φ_s)† ⊗ P_s, where:
  - u₀ is a fixed turn with u₀m = n;
  - P_s are the joint eigenprojections of the neighbours' σ^n;
  - R_n(φ) is a turn about n by angle φ. ∎

### 3.3 Unsoldered action (Q3)

- **Survivors.** K = {1}, so the survivors are every uniform onsite turn and Lemma C ticks with any n and m.
- **Movers.** When m ≠ ±n, content moves. This is the census's companion pair:
  - C_s = Ad(ΠCZ_z)∘Ad(H_xz^⊗), trace s; its support spreads over 1, 7, 13, 43, 49, 55, 85, 259 sites;
  - C_{1+s}, trace 1+s.
- **Control.** The shear L_s stays within 7 sites.
- **Scramblers, not gliders (EXACT, A20's C9 argument).** A rigid glider with velocity v would need tr M = z^v + z^{−v}, but tr M = s.
- **Every nontrivial survivor fails possibility covariance** (Theorem P). Each privileges at least one axis:
  - an onsite turn privileges its rotation axis;
  - a Lemma C tick privileges n, and a mover also privileges m.

**Weakest internal symmetry G:**

| G | Removes all nontrivial NN ticks? | Removes all movers? | Evidence |
|---|---|---|---|
| Total flip σ→−σ (antilinear) | no: it keeps every onsite turn and both movers, and only trims non-Clifford Ising angles | no | k1 |
| One half-turn {1, H_n} | no | no: the plane ⊥ n has one sign | §3.4 |
| Pauli group V₄ (linear part of the parked Z₂³) | no: Ising x, y, z and onsite Pauli half-turns survive | **yes**: x, y and z carry distinct signs | k1 |
| C₃ (X→Y→Z) | no: Ising w and turns about w survive | **yes** | k1 |
| Tetrahedral T (12 elements) | **yes** (Theorem P) | yes | k1: every tick fails |
| Internal cubic group, or SU(2) | yes | yes | they contain T |

**In plain words:** these ticks pick out one pair of opposite possibilities as a switch that the neighbours feel. Those that spread change also pick out a second pair and a fixed turn that carries it onto the first.

### 3.4 Sign twist (menu frame: odd rotations act as the half-turn about x)

- **Supports.** span{1,σ^n} with n = x or n ⊥ x, all six equal. N3 and N4 are void.
- **Lemma C:**
  - n = x carries the trivial sign, so m = ±x and nothing moves;
  - n ⊥ x carries the odd sign, so m can be any line ⊥ x, and movers exist.
- **The mover C_s′:**
  - CZ_z picks up only onsite Z factors under Ad σ^x, and these cancel because every site has degree 6;
  - Ad σ^x sends H_yz to −H_yz;
  - exact covariance, 0 failures out of 72 (k1);
  - skeleton X₀ ↦ −X₀Π_N Z, Z₀ ↦ Y₀Π_N Z; trace s; it spreads.
- **Verdict:** Theorem N fails, and so does "nothing moves".

### 3.5 Axis soldering (A2+E: odd rotations act as minus the axis permutation)

- **Branches.** Write n_z(θ) = cos θ e_z + sin θ (e_x+e_y)/√2, plus the d-branch. Then n_z·n_x = (√2/2)sin 2θ − (1/4)cos 2θ + 1/4 (k3a), giving:
  - **parallel** only at n_a = w;
  - **perpendicular** at n_a = e_a and at n_a = (I−2wwᵀ)e_a;
  - **all other angles**, including the d-branch at 120°: N3 has no commuting pair (k2, exact). These branches are empty.
- **Perpendicular triples.** N3 and N4 give α(A_x) ⊆ A_x ⊗ span{1,S^n_x}, with S^n_x invariant by a sign count.
  - By N5, u_± ∈ {1, R_w(π)}.
  - Mixed controls fail: [α(σ^w_x), α(b_y)] has max entry 1.217 or 0.354 (k3b), so the map is not an automorphism.
  - Equal controls are onsite, which contradicts nontrivial support. Both branches are empty.
- **Parallel branch (w).** w carries the sign A2, which appears once in A2+E, so m = ±w and nothing moves.
- **Verdict:**
  - α ≠ id is possible: Ad(σ^w)^⊗, the w-Ising tick and their products are exactly covariant (k1).
  - No content ever leaves its closed neighbourhood (EXACT).
  - A20's reach-4 mover A·B is also covariant under axis soldering: S_x and F_x are invariant under all 24 rotations (k5), and its layers are products of commuting invariant gates. So motion needs reach between 2 and 4.

### 3.6 Full soldering

- This is A20's N2–N6, which A21 found sound: n_a = e_a, then N3–N6 give α = id.
- G1 R2's remark is confirmed: N2 and N6 as written hold only for T1. Under A2+E the conclusion α = id really fails, while "nothing moves" survives.

### 3.7 The two criteria (EXACT)

For a sign character χ of K, let V_χ = {v : kv = χ(k)v for all k}.

**(I) α = id for every NN covariant tick ⟺ K fixes no line.**
- ⇐ (no fixed line gives α = id):
  - Lemma C has no branch;
  - the onsite centralizer is trivial;
  - the non-parallel branches are empty or give α = id.
- ⇒ (a fixed line n gives a nontrivial tick): Ad(σ^n)^⊗ is a nontrivial covariant tick.

**(II) No NN covariant tick moves ⟺ dim V_χ ≤ 1 for every χ.**
- ⇐ (no two-dimensional V_χ means no motion): n and m lie in one V_χ, so m = ±n.
- ⇒ (a two-dimensional V_χ gives a mover): suppose dim V_χ ≥ 2.
  - Pick orthonormal n and m in V_χ, with bisector b. K acts on V_χ as a scalar, so it fixes every line in V_χ.
  - Then α = Ad(Π_edges CZ_n)∘Ad(σ^b)^⊗ is covariant and takes m to n.
  - It is Clifford-conjugate to C_s, so it spreads.

### 3.8 Cross-check against the census (archived, no claim authority)

- **Frames.** The census sorts actions mod signs, up to onsite Clifford conjugacy. The menu sorts them up to SO(3) conjugacy.
  - The menu's twist about x is trivial mod signs, so it lands in the census's site-only row.
  - The census's sign-quotient row is a twist about a face diagonal. It is SO(3)-conjugate to the menu's twist, but not Clifford-conjugate.
- **Sign-quotient row.** In that frame the only Pauli axis ⊥ the twist axis is y. So a Clifford tick there has m = n = y and cannot move, which matches the census's two involutions I+sN and H+sN. Movers exist in that frame but are non-Clifford.
- **Site-only row.** C_s′ (trace s) is in the census's C_s class, and it lifts covariantly under the twist; C_s with H_xz does not (24 failures).
- **Axis quotient.** "Axis quotient: 0" agrees with Theorem N for T1. The A2+E survivors are non-Clifford there, which falls under the census's own stated exclusion of non-Clifford ticks and actions.

### 3.9 Fermionic combination (Q4)

**Menu.**
- Parity-preserving automorphisms of one mode form O(2) acting on (γ¹, γ²): phases are rotations, particle–hole swaps are reflections.
- The image of S₄ must be a cyclic or dihedral quotient of S₄, so it is 1, Z₂ or D₃. The four types are:
  - trivial;
  - odd ↦ −1: global parity on odd rotations, equivalent to trivial for parity-preserving ticks;
  - odd ↦ a particle–hole reflection;
  - D₃: 3-fold ↦ e^{±2πi/3}, odd ↦ reflections.
- V₄ always lies in the kernel (k4a: 156 homomorphisms, none with a² ≠ 1).
- In one-site Jordan–Wigner terms, these are the qubit actions that keep the parity axis z in place. Full soldering has no counterpart.

**Graded N1 (EXACT).**
- Expand b₁ = Σ o_i p_i and b₂ = Σ o′_j q_j in homogeneous pieces, with modes ordered O < P < Q.
- Graded commutation, compared on the independent products p_i q_j, gives o_i o′_j = (−1)^{|o_i||o′_j|} o′_j o_i.
- So the supports on O graded-commute.

**Graded N2 (EXACT).**
- S_x^(m) graded-commutes with itself, because the half-turn acts trivially.
- An odd self-adjoint s would need s² = −s², which is impossible.
- So S ∈ {C1, span{1,n}} (k4b). No Majorana reaches a neighbour.

**Graded Lemma C (EXACT).**
- The CAR relative commutant is A_y^even:
  - odd parts vanish by a norm argument with a far-away c_z;
  - even parts reduce to the finite commutant A_y^even ⊕ P_{F∖y}A_y^odd.
- So α(n_y) ∈ {n_y, 1−n_y}, and nothing leaves N̄(x).
- In qubit terms the grading forces m = n = the parity axis. Qubit movers need an onsite turn that mixes even and odd, which a parity-preserving tick cannot contain.

**Theorem F.**
- With one mode per site and the graded product, every parity-preserving NN covariant tick is static. This holds under every action, interacting or not, number-preserving or not.
- Nontrivial examples:
  - onsite phases;
  - particle–hole swaps, where the action allows;
  - exp(iθΣ(n_x−½)(n_y−½)).

**Quasi-free special case (EXACT).**
- M_e is the Majorana-symbol coefficient on the bond in direction e.
- Since M_{−e} = M_e, the coefficient of M†M at 2e is M_eᵀM_e = 0, so M_e = 0.
- This extends the archived number-preserving result to Bogoliubov ticks.

**Majorana shifts.**
- A covariant shift fails graded N2.
- The 1D two-way shift is a valid automorphism and is reflection-covariant only with an onsite swap γ¹↔γ² (k4d: True with the swap, False without). The 3D half-turns cannot carry that swap.

**COMPARATOR** (from memory, not adopted): the FPPV and GNVW indices are forced to 1 by the axis-reversing half-turns. Zero flow does not imply static, since C_s′ is a finite-depth circuit, so the support argument is what decides.

**Prior art:** the archived six-mode escape (not re-verified).

### 3.10 Plain verdict (Q5)

**One sentence.** Take a reversible tick on Z³ with one qubit, or one fermion mode, per site that reaches only nearest neighbours and is exactly covariant on every tick under translations and the 24 rotations about each site. Nothing can move exactly when the symmetries acting on the possibilities treat no two distinct possibility axes alike. That holds:
- under full soldering, where the tick is the identity;
- under axis soldering, where the tick is static but possibly nontrivial;
- under any action with possibility covariance, or with any internal group not inside one half-turn group;
- always for one graded fermion mode.

It fails for the unsoldered action and for the sign twist on their own.

**Escapes opened by each relaxation:**
- **Unsoldered:** NN movers C_s and C_{1+s} (scramblers, no gliders) and static ticks; each privileges an axis.
- **Sign twist:** NN movers whose axes are both ⊥ the twist axis.
- **Axis soldering:** static NN ticks; motion needs reach ≥ 2, and A20's reach-4 mover qualifies.
- **Full soldering:** identity at NN reach; movers at reach 4; reach 2–3 non-Clifford is open.
- **Possibility covariance, or an irreducible G:** identity at NN reach under every action; reach ≥ 2 is open.
- **Pauli-group or C₃ internal symmetry:** no motion, but static ticks survive.
- **One fermion mode:** static at NN reach; the escapes are more modes or longer reach.
- **A20's other relaxations are unchanged:** irreversible steps, quasi-local tails, statistical covariance, a supplied schedule, multi-qubit sites.

## 4. Checks

| Script | What it checks | Result |
|---|---|---|
| `k1_actions_ticks.py` | The menu actions, plus covariance of 11 explicit ticks on the 7-site star (24 rotations × 3 Paulis), and under SU(2), V₄, C₃, T and the flip | Homomorphisms with 0 failures; splits as stated; commutant dimensions 9/5/2/1; table below. 2.7 s, 41 MB. |
| `k2_n3_angles.py` | N3 over the 12×12 support pairs at angle g | Parallel: 144 commute. Perpendicular: 1 (the parity pair). Six other angles: 0. Exact: 143 pairs commute only at t = 0, the parity pair at t ∈ {−1, 0, 1}. 3.6 s. |
| `k3_branches_spread.py` | Branch angles; mixed controls; spreading | As in §3.5. C_s′ spreads 7…265, C_s 1…259, L_s stays at 7 or 1. 0.6 s, 73 MB. |
| `k4_fermion.py` | Homomorphisms into O(2); graded subalgebras; M_eᵀM_e; 1D two-way Majorana shift | As in §3.9. 0.14 s. |
| `k5_star_face_terms.py` | Invariance of A20's S_x and F_x | Trivial and sign twist: 20/24 fail. Axis and full: 0/24. 0.15 s. |

**k1 pass/fail table** (P = exactly covariant, F = fails; columns are trivial, sign twist, axis, full, then SU(2), Pauli, C₃, T, flip)

| Tick | triv | twist | axis | full | SU2 | Pauli | C3 | T | flip |
|---|---|---|---|---|---|---|---|---|---|
| onsite turn x (0.7) | P | P | F | F | F | F | F | F | P |
| onsite turn z (0.7) | P | F | F | F | F | F | F | F | P |
| onsite half-turn w | P | F | **P** | F | F | F | P | F | P |
| onsite half-turn (y+z) | P | P | F | F | F | F | F | F | P |
| Ising x (0.37) | P | P | F | F | F | P | F | F | F |
| Ising z (0.37) | P | P | F | F | F | P | F | F | F |
| Ising w (0.37) | P | F | **P** | F | F | F | P | F | F |
| Ising z (π/4) | P | P | F | F | F | P | F | F | P |
| C_s = CZ_z·H_xz | P | F | F | F | F | F | F | F | P |
| C_s′ = CZ_z·H_yz | P | **P** | F | F | F | F | F | F | P |
| w-controlled | P | F | **P** | F | F | F | P | F | F |

All 11 ticks are nontrivial.

## 5. Open edges

1. **Axis soldering at reach 2–3** (non-Clifford). Under full soldering this is A20's edge 1.
2. **Unit-cube (diagonal) reach.** The swap argument needs a single shared site, so Theorem P, Lemma C and Theorem F do not extend directly.
3. **Possibility covariance at reach ≥ 2.** Is there an SU(2)-covariant strict tick that moves anything?
4. **Whether the NN movers carry anything record-like.** Non-Clifford Lemma C movers at generic angles are untested.
5. **Antiunitary internal symmetries beyond the total flip** (single flips of the parked Z₂³) are only partly mapped.
6. **Fermions with 2–5 modes per site, and fermionic reach ≥ 2:** open.
7. **Which law-level reading of "No possibility is privileged", if any, applies.** That is the owner's decision; criteria (I) and (II) show what each reading would buy.

## 6. Plain-language summary

If a tick can only reach next-door sites and must look the same under every turn of the grid, whether anything can move depends on one thing: whether the rules treat two different directions of the possibilities exactly alike, one that the neighbours feel and one that gets turned into it. With your full gluing of possibilities to the grid's turns there is no such pair, so the tick does nothing at all. With the weaker "axis" gluing, a site may turn about one special diagonal direction depending on its neighbours, but nothing ever leaves its neighbourhood. With no gluing, or with the "sign twist" gluing, there are rules that spread change outward, but each one favours particular directions of the possibilities. If "no possibility is privileged" were taken as a rule about the law itself (a reading not adopted), everything freezes under every gluing, and asking it of a small family of twelve turns is already enough. With one fermion per site instead of a qubit, nothing can move next door under any gluing, whether or not particles are conserved.