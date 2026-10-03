All checks pass. The face gate F₀ is exactly invariant under all 24 rotations, the F's commute, and the two circuits reproduce the enumerated symbols. The tick α = Ad_A∘Ad_B has 0 exact-covariance failures over 24 rotations × 3 Paulis, satisfies α(Y)=iα(X)α(Z), and has reach 4. I have what I need for the report.

# A20 report: can anything move under a tick that is exactly covariant on every tick?

Scratch directory: `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A20/`. No git, no repo edits. Every run used `nice -n 10`, a 60 s alarm and all four thread caps at 1. Each took under 10 s; peak memory was 257 MB.

## 1. Question

Is there a reversible tick on Z³ with one qubit per site that has all four properties below? If not, what exactly blocks it, and what is the smallest relaxation?
- **Strictly local:** finite reach.
- **Exactly covariant on every tick:** under unit translations and the 24 soldered proper rotations.
- **Non-trivial:** something moves.
- **No privileged sublattice or schedule.**

**Supplied model class** (not framework content):
- A tick is an automorphism α of the algebra of local observables.
- Reach r means α(A_x) lies in the algebra of sites within r of x.
- Nearest-neighbour reach means α(A_x) ⊆ A_{N̄(x)}, where N̄(x) is x plus its 6 neighbours.
- Soldering: a rotation R sends site x to Rx and turns σ·n into σ·(Rn) on the site.

## 2. Answer

**Conditional: the answer splits sharply on the tick's reach.**

**(a) Nearest-neighbour reach: NO (EXACT).**
- Every nearest-neighbour tick that commutes with the soldered rotations about every site is the identity.
- The proof uses no number conservation, no Clifford structure and no gate decomposition. So it covers compass gates, closing the gap A16 flagged in A3 Step 10, and every other kind of gate.
- If I2's "one grid space per tick" means nearest-neighbour reach, then nothing moves on any tick: not records, excitations, domain walls or Majorana-type content.

**(b) Reach 4: YES (EXACT).** There is a tick with all the required properties.
- The tick is U = A·B, with two layers:
  - A = Π_x e^{−iπ/4 S_x}, where S_x = Π_a σ^a_{x+e_a}σ^a_{x−e_a}. S_x is the product of the six compass bond terms meeting at x.
  - B = Π_x e^{−iπ/4 F_x}, where F_x = Π over the 12 face-diagonal neighbours x+d of σ^{⊥(d)}_{x+d}. Here ⊥(d) is the axis perpendicular to the face containing d.
- Each layer is a product of commuting gates that are exactly invariant under the rotations. So the tick is exactly covariant, with signs. It is reversible and has no sublattice and no schedule.
- Local content spreads ballistically at 4 sites per tick.

**(c) What moves is not a record (EXACT, Clifford class).**
- No local Pauli content travels intact.
- One tick turns a single-site lock into a pattern of links spread over 145 sites.
- No translation-invariant stabilizer state survives any moving covariant Clifford tick. That includes every covariant quiet vacuum of that kind.
- Within Clifford ticks, moving needs reach ≥ 4 (EXACT), and reach 4 is attained.
- Whether a non-Clifford tick can move things at reach 2–3 is OPEN.

## 3. Derivation

### A. Gate products and compass gates (task 1)

**A1. How a gate product can be covariant (EXACT).**
- A symmetry maps an ordered product of gates to the product in the permuted order. Per-tick covariance needs the two to be equal.
- Two clean ways to get this:
  - all gates commute, so the order does not matter;
  - covariant layers, each a product of commuting covariant gates. A product of covariant layers is covariant whether or not the layers commute with each other. The layer order is a time order, not a spatial pattern.
- A10's layers fail because a disjoint-pair layer cannot be covariant: it gives each site one partner, and a quarter turn about the site moves that partner.

**A2. Compass gates (EXACT; CHECKED).**
- Take anticommuting Paulis A = σ^x_0σ^x_{e_x} and B = σ^y_0σ^y_{e_y}. Two gates α1+βA and γ1+δB commute up to a phase iff one is ∝1 or both are ∝ Paulis.
- So e^{−iθA} and e^{−iθB} commute up to phase iff θ ∈ (π/2)Z.
  - Residual: 0.49 at θ=0.3, 2.45 at π/4, 4.9e−16 at π/2 (phase −1).
- At θ=π/4 (Clifford) the two orders differ even as maps:
  - one order gives Z₀ ↦ +X₀Y_{e_y};
  - the other gives Z₀ ↦ −Y₀X_{e_x}.
- At θ=π/2, each σ^b_x anticommutes with exactly 4 bond terms, so the product over all bonds is the identity map.

**A3. Commuting ticks never transport (EXACT).**
- If α = Πg_j with all g_j commuting, then α^t = Πg_j^t.
- So the support of α^t(O) stays inside the union of the gates touching O, for every t. Content only oscillates inside a fixed window.

**A4. A covariant commuting family exists: S_x (EXACT; CHECKED).**
- S_x is fixed with sign by all 24 rotations about x, and all S_x commute.
- So e^{−iθΣS_x} is covariant for every θ, non-trivial for θ ∉ (π/2)Z, and has reach 2.
- By A3 it never transports. The S_x are conserved, so star defects never move.

### B. Theorem N: nearest-neighbour covariant ticks are trivial (EXACT)

**Statement.** Suppose α(A_x) ⊆ A_{N̄(x)} for every x, and α commutes with the soldered rotations about every site. Then α = id.

**Proof.**
- **N1, support lemma.** Suppose B₁ ⊆ A_O⊗A_P and B₂ ⊆ A_O⊗A_Q commute, with P∩Q = ∅. Then their supports on O commute. (Expand in product bases of A_P and A_Q; the coefficients of the commutator are commutators of the O-parts.) This is self-contained.
- **N2, axis neighbours.** x and y = x+2e_a share only m = x+e_a.
  - The quarter turn about the a-axis through x fixes m. So the support of α(A_x) on m is one of C·1, span{1,σ^a}, M₂.
  - The half turn about m perpendicular to e_a swaps x and y.
  - By N1 the two supports commute, so neither is M₂.
  - So α(A_x) touches its neighbour x±e_a only through σ^a.
- **N3, perpendicular pairs.** x and z = x+e_a+e_b share m₁ = x+e_a and m₂ = x+e_b.
  - The rotation about m₁ with axis e_a−e_b maps x to z.
  - Suppose the neighbour supports are non-trivial. The two-site supports T_x ⊆ span{1,σ^a_{m₁}}⊗span{1,σ^b_{m₂}} and T_z ⊆ span{1,σ^b_{m₁}}⊗span{1,σ^a_{m₂}} must commute.
  - Expanding the commutator shows both must be the parity algebras span{1,σ^aσ^b}.
  - CHECKED by brute force over all 15×15 subalgebra pairs: exactly one pair survives, the parity pair.
- **N4.** Every Pauli string in α(A_x) therefore touches perpendicular neighbour pairs together. Perpendicularity connects all six neighbours (an octahedron). So each string touches all six neighbours, with σ^a at x±e_a, or none of them. Hence α(A_x) ⊆ A_x ⊗ span{1,S_x}.
- **N5.** A unital copy of M₂ inside A_x ⊗ span{1,S_x} = M₂⊕M₂ is a controlled turn:
  - A ↦ u₊Au₊†P₊ + u₋Au₋†P₋, with P± = (1±S_x)/2.
- **N6.** Rotations about x fix S_x exactly. So Ad u± commutes with the soldered O action on M₂. That action is irreducible on Bloch vectors, so Ad u± = id, and α = id. ∎

**Corollaries.**
- **N-a (EXACT).** A3 Step 10 holds without number conservation. Every covariant layer of commuting 2-site bond gates is the identity map. Bonds form one orbit, so such a layer covers all bonds and has nearest-neighbour reach.
- **N-b (EXACT, same proof).** In every covariant commuting family of star-local terms, each term is T_x = a + bS_x. So layers built from star-local pieces all commute and never transport.
  - Moving therefore needs gate pieces that reach second neighbours, such as F_x.
- **N-c (EXACT).** This holds tick by tick, so laws that change from tick to tick are covered too.
- **N-d.** The soldering is load-bearing (N2, N6). If rotations moved sites only, Ising-type commuting ticks of nearest-neighbour reach would survive (ARGUED). They privilege a direction, which conflicts with "No possibility is privileged".

### C. Clifford ticks (task 2)

**C1. Encoding (EXACT).**
- A translation-invariant Clifford tick is a 2×2 matrix M(z) over F₂[z^±]. Its columns are the images of X₀ and Z₀, mod signs.
- It is a valid tick iff M^†ΛM = Λ.

**C2. Consequences of covariance (EXACT).**
- det M = 1, because it is a monomial invariant under O.
- With det M = 1, validity ⇔ M(z⁻¹) = M(z).
- The axis half-turns act trivially on labels mod 2. So M is a polynomial in w_i = z_i + z_i⁻¹, and the remaining S₃ permutes axes and labels together.

**C3. Classification (EXACT; cross-checked on all 8 solutions found in the small-reach enumeration).**
- **Notation.**
  - u₀ = (w₁+w₂, w₂+w₃) is the symbol of S_x.
  - u₂ = u₀ squared entrywise is the symbol of the star at distance 2.
  - P = [u₀, u₂].
  - Δ = det P = (w₁+w₂)(w₂+w₃)(w₁+w₃).
  - R = F₂[e₁,e₂,e₃].
- **Statement.** Every covariant Clifford tick is M = 1 + P·N₀·adj(P), with N₀ ∈ M₂(R) and tr N₀ = Δ·det N₀. Conversely, every such M is valid and covariant mod 2.
- **Key steps.**
  - The equivariant vectors form the free module Ru₀ ⊕ Ru₂.
  - Integrality plus det = 1 force M₀ ≡ 1 mod Δ.
  - In R/Δ ≅ F₂[e₁,e₂], the relation (1+m₁₁)² = m₂₁²(e₁²+e₂) requires m₂₁ = 0.

**C4. Moving versus not moving (EXACT).** tr M = Δ²·det N₀.
- If det N₀ = 0, then M² = 1. The tick is an involution (a commuting covariant circuit) and content stays bounded.
- If det N₀ ≠ 0, the trace is non-constant, and content spreads without bound.

**C5. Reach bound (EXACT).** Δ² has degree 4 in each w_i. So any moving covariant Clifford tick reaches 4 sites along some axis in one tick.

**C6. Small reach (EXACT for these finite classes; all candidates checked).**

| Reach class | Candidates | Valid ticks |
|---|---|---|
| Nearest neighbour | 1 | identity only |
| Unit cube (3×3×3) | 1 | identity only |
| L1 ≤ 2 | 2 | {1, A} |
| Cube 5×5×5 | 512 | 1 plus 3 involutions |
| L1 ≤ 3 | 32 | 1 plus 3 involutions |

**C7. The reach-4 mover (EXACT; CHECKED).**
- Symbols: N_A = E₁₂ and N_B = [[e₁,e₁²],[1,e₁]]. These do not commute.
- AB has det N₀ = 1, trace Δ², and reach exactly 4.
- Light cone: radius 4t for t = 1…8.
- Support of α^t(X₀): 145, 633, 2449, 4369, 5921, 12841, 25089, 33697 sites. That is about 12% of the light-cone cube at t = 2, 4, 8.
- Exact sign lift:
  - all 24 rotations × 3 Paulis, 0 failures;
  - α(Y) = iα(X)α(Z).
- A second mover, built directly from the formula with N₀ = [[0,1],[1,Δ]], has reach 5 and light cone 4t+1; it also lifts exactly.

**C8. Flow index (EXACT, using the cited Clifford index formula).** det M = 1 gives zero net flow on every axis, consistent with A1 D12.

**C9. How content moves (EXACT).**
- **No gliders.** If a Pauli string moved rigidly by v, then z^v would be an eigenvalue of M and tr M = z^v + z^{−v}. That is O-invariant only for v = 0, which gives trace 0 and no motion. The same holds for a return up to a shift after n ticks.
- **No invariant stabilizer vacuum.** An invariant translation-invariant stabilizer state is a line Ru with Mu = λu. Covariance forces λ = 1, and then tr M = 0.
- **Quiet vacua exist only under non-moving ticks.** Two covariant quiet vacua exist:
  - the star state, S_x = +1 everywhere;
  - the face state, F_x = +1 everywhere.

  Each is pure, frustration-free with F = (1−S_x)/2 (or (1−F_x)/2), and has single-site odds ½; this is EXACT, since their symbols are primitive vectors. Unlike A9's (e3) state, neither privileges an axis. Each survives only non-moving ticks.

### D. Non-Clifford ticks (task 3)

- **D1 (EXACT).** U(θ,φ) = Πe^{−iθS_x}·Πe^{−iφF_x} is exactly covariant for all real θ, φ, reversible, and has reach ≤ 4.
  - It tends to the identity as θ, φ → 0.
  - A two-phase smooth film (ΣS_x switched on, then ΣF_x) is exactly covariant and of finite reach at every instant.
- **D2 (ARGUED).** Generic angles move content.
- **D3 (EXACT).** A single generator e^{−iτH} with non-commuting covariant H (compass, Heisenberg, or ΣS+ΣF) is covariant but has tails, so it leaks past one site (A3 Step 3).
- **D4 (OPEN).** Non-Clifford transport at reach 2–3.

### E. Record motion and quiet vacua (task 4)

- **E1 (EXACT).** Every moving covariant tick has reach ≥ 2 (Theorem N); for Clifford ticks it is ≥ 4. So A3's one-site Hall condition for a just-formed record fails: under AB, a lock's content reaches 4 sites in one tick.
- **E2 (ARGUED).**
  - A single lock spreads over a pattern of links spanning about 145 sites.
  - Whether later records register it depends on correlations across many sites.
  - A3's guided-record machinery assumes number conservation, which these ticks do not provide.
- **E3 (EXACT, Clifford class).** Moving and keeping a quiet stabilizer vacuum exclude each other (C9).

### F. Obstruction and minimal relaxations (task 5)

**The obstruction (EXACT, narrow).** It is Theorem N, and it holds when all of the following apply:
- one qubit per site;
- soldered rotations about sites;
- reversible ticks;
- nearest-neighbour reach;
- exact covariance on each tick.

**Relaxations, each a named conditional:**
1. **Longer reach per tick (records may jump ≥ 2 sites).**
   - At reach 2, covariant ticks exist, but Clifford ones do not move anything.
   - At reach 4 there is a moving, schedule-free tick (EXACT).
   - Alternatively, alternate A and B ticks: reach 2 per tick, each tick exactly covariant, a front speed of 2 sites per tick, and a supplied global tick parity.
2. **Supplied sublattice or schedule (A10).** Moves at reach 1, but loses covariance once records interact (A16).
3. **Quasi-locality.** Exact covariance at every instant, but the tails break I2.
4. **Statistical covariance.** The law is covariant, but each realization breaks it, and records can register the realized schedule (A16: TV 0.04–0.39). (ARGUED)
5. **Multi-qubit sites.** This changes the Qubit axiom's M₂(C); see A1 D27.
6. **Irreversible covariant moves.** A1 D23's lock-and-move channel is covariant at reach 1, but needs a six-possibility menu.

Majorana-type splitting needs a grading, which is not covariant (A1 D28).

**Comparators (not adopted; cited from memory, not re-verified):**
- Schumacher–Werner 2004: support algebras.
- Skolem–Noether theorem.
- Schlingemann–Vogts–Werner 2008 and Gütschow–Uphoff–Werner–Zimborás 2010: the Clifford symbol formalism, with the trace sorting ticks into periodic, glider and fractal.
- GNVW 2012: flow index.
- Haah 2021: Clifford QCAs in 3D.
- The 3D quantum compass model.

## 4. Checks

All integer and Pauli algebra is exact over F₂ with tracked signs, unless a tolerance is stated.

| Script | What it checks | Result |
|---|---|---|
| `t1_compass.py` | Compass commutation; θ=π/2 product; star family | Residuals as in A2; each σ^b anticommutes with 4 bond terms; S₀ fixed 24/24; all S commute (|d|∞ ≤ 3) |
| `cliff_lin.py`, `cliff_lines.py`, `cliff_enum.py` | Mod-2 covariant candidates per box, then the validity check | As in C6 |
| `t2_orders.py` | Trace and order of every valid solution | All trace 0, order ≤ 2 |
| `t3_trace_lemma.py` | Linearity alone allows a non-zero trace | Yes; the bound comes from det = 1 |
| `t4_transport.py` (+ `dbg_trace.py`) | Reach-5 mover from the formula | det 1, equivariant, trace Δ², radius 4t+1 |
| `t5_lift.py` | Exact sign lift for A, B, AB and the reach-5 mover | All succeed |
| `t6_nn_lemma.py` | Brute force of step N3 | Only the parity pair survives |
| `t7_classify_check.py` | All 8 enumerated solutions against C3 | Every N₀ is polynomial, symmetric, with the trace relation and det N₀ = 0 |
| `t8_product.py` | The AB tick | Numbers as in C7 |
| `t9_gates.py` | F_x invariance; circuits reproduce the symbols; full exact covariance | As in C7 |

Notes:
- The line "equals Delta^2: False" in `t4` is a sympy false negative. `dbg_trace.py` prints the two expressions, and they are identical term for term.
- **Not run (too big for the 8 GB machine): spreading at generic angles θ, φ.** Range-4 layers need tori of 9³ sites or more. A Pauli-path sampler or a 2D analogue would be the way to test D2.

## 5. Real-physics match

**What it implies.**
- Consider a law that is reversible, uses one qubit per site, is exactly soldered-covariant on each tick, and has nearest-neighbour reach. That law is static. So at least one of those properties must give if anything is to move.
- The movers found are scramblers:
  - fractal, cube-shaped light cones at the maximal speed;
  - no particle-like excitations;
  - no quiet vacuum.

  This does not resemble known physics; continuous-angle versions are untested.

**What would falsify these results:**
- a non-trivial nearest-neighbour covariant tick on qubits (against Theorem N);
- a moving covariant Clifford tick of reach ≤ 3 (against C5);
- a covariant Clifford glider, or a moving tick that preserves a stabilizer vacuum (against C9).

## 6. Open edges and next steps

1. Non-Clifford covariant transport at reach 2–3. Extend the support-algebra method to reach 2.
2. The unit-cube (diagonal) version of Theorem N for non-Clifford ticks. In the Clifford class it holds by enumeration.
3. Spreading at generic angles for U(θ,φ). Does any angle carry quasi-particles?
4. A non-Clifford tick that both moves content and keeps a quiet vacuum.
5. Formation (R1) on top of a moving covariant tick: where do records reappear?
6. Whether the alternating A/B tick parity is readable from records (compare A5 and A15 on out-of-step ticks).

## 7. Plain-language summary

Suppose every tick must treat every site and every turn of the grid exactly alike, and one tick can pass influence only to a site's nearest neighbours. Then the tick can change nothing at all, so no record, and nothing else, can ever move; this holds for every reversible rule of that kind, not just the ones tested before. If one tick can reach four sites away, there are rules that treat every site and turn alike on every tick and still carry change outward at a fixed top speed, with no special sub-grid and no timetable. But what travels under them is a spreading web of links among many sites, not a record stepping from place to place, and under them no calm empty background stays calm. So with your choice of gluing the change to the grid's turns, records that step one site per tick need something extra: a longer reach per tick, a rule that is the same everywhere only on average, more room per site, a supplied pattern of partners, or steps that cannot be undone.