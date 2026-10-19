# C4f — An O-covariant (axis action) one-qubit U(1) QCA on Z^3 with frozen magnons and a speed-1 bound-pair glider

**Block:** C4f of `toe-scale-ladder-20261018`, following C4e (T-covariant glider, not O-covariant),
C4b (axis/full actions, Lemma 2), C4c (Observation M) and C4d (P1, spectator lemma, Prop. E).
**Date:** 2026-10-19. **Status:** author's work only; not yet reviewed. No axiom, primitive or
dynamics clause is adopted. The QCA below is a *constructed example* inside the premise class.

## Result up front

1. **What O-covariance under the axis action requires (proved).** Odd R ∈ O∖T act as
   β_R = γ ∘ C ∘ π_R, where π_R permutes sites, C is the global spin flip in the n-basis
   (particle–hole), and γ is a Q_n-rotation. For a Q_n-conserving α, covariance under all of O is
   therefore **equivalent** to two conditions:
   - [α, π_R] = 0 for all R ∈ T;
   - [α, C∘π_R] = 0 for one (hence every) odd R.

   The second condition maps the k-magnon sector over the vacuum Ω to the k-hole sector over the
   anti-vacuum Ω̄. So O-covariance puts **no constraint on the k-magnon dynamics beyond
   T-covariance**. Instead it *fixes* the k-hole dynamics: U_k-hole = Θ U_k Θ^{-1}, with Θ = Cπ_R.
   - C4c Observation M's "O" column, in which no face-pair moves are allowed, is the
     pure-permutation (full/trivial-action) case. Under the axis action the relevant column is T.
   - C4e failed O only because its U commutes with C. Then Θ-covariance would need [U, π_R] = 0,
     which its B-tetrahedron unit violates.
2. **Construction (proved; exact-checked).** U = L2 ∘ L1 has the following properties:
   - L1 is C4e's square layer.
   - L2 is **one** involutive layer of controlled tetra-axis units. It contains B-tetra-axes that
     fire only when the complementary tetrahedron A(k) of the same cube is **empty**, and A-tetra-axes
     that fire only when B(k) is **full**.
   - U is TI, one qubit per site, conserves N, and is **covariant under all 24 elements of O with
     the axis action, phases included**.
   - Single magnons and single holes are frozen.
   - The two-magnon sector is **exactly C4e's glider**: a face pair with zero coordinate a moves by
     v = ρ_bρ_c e_a at 1 site/tick, and all other pairs are static.
   - Hole pairs in the filled background glide with −v, the Θ-image.

   So the answer to the C4f target is **yes**: an axis-O-covariant moving bound pair exists.
3. **Range.**
   - Each layer has exact CA dependency radius 3, so U and U^{-1} have CA radius ≤ 6.
   - The empirical single-flip influence of U is 5, which is a witness that the radius is ≥ 5.
   - The QCA (automorphism) range is ≤ 2·6+6 = 18, by C4e's crude bound. Range 2 is **not** met
     and not addressed.
4. **Pair-move classification extended (exact, Observation-M criterion, `c4f_01`).** The table
   counts COM-changing, stabiliser-fixed, Lemma-K-related monomial images:

   | r | T (relevant for axis action) | O by permutation (trivial/full-type) |
   |---|---|---|
   | 1 | 6 of 13 | 0 of 13 |
   | 2 | 56 of 62 | 36 of 62 |
   | 3 | 162 of 171 | 132 of 171 |

   The r ≤ 2 rows reproduce C4c. Under O-by-permutation the face pairs (1,1,0) are frozen at
   r = 1 and r = 2. Under SU(2) (the full action, via C4b Lemma 2), monomial pair motion is
   impossible at **any** range. This is the elementary S^- argument below.

## Premises (named, supplied)

- Lattice and Qubit axioms; (D-QCA), TI finite-range automorphism; (S), soldering with C4
  conventions.
- The axis action is Q(R) = sgn(perm R)·|R| (`C4/scripts/c4lib.py: menu_Q`).
- (U1): Q_n is conserved, n = (1,1,1)/√3. The vacuum Ω has all spins along −n, and a magnon is a
  +n spin. A configuration is the set of magnon sites; the n-basis is the computational basis.

## Step 1 — how odd rotations act (proved; `c4f_01` Part A)

β_R = Ad(D_R^{⊗Z^3}) ∘ π_R, where D_R ∈ SU(2) lifts Q(R).
- **R ∈ T** (even permutation part): Q(R)n = n. So D_R is diagonal in the n-basis, and
  Ad(D_R^⊗) = γ_{θ_R}, the U(1) rotation e^{iθ_R Q_n}.
- **R odd:** Q(R)n = −n. So D_R is antidiagonal, D_R = e^{ia} e^{iφZ/2} X e^{−iφZ/2}, and
  Ad(D_R^⊗) = γ_φ C γ_{−φ} = γ_{2φ} C, where C = Ad(X^⊗) is the particle–hole map and
  Cγ_θC = γ_{−θ}.
- `c4f_01` checks both statements for all 24 R with explicit lifts (PASS).

If α conserves Q_n, then α commutes with every γ, and every γ commutes with every π_R. Hence:

> **(O-axis) ⟺ [α, π_R] = 0 ∀R ∈ T and [α, C π_{R₀}] = 0 for one odd R₀** (T and R₀ generate O).

**Consequences for the sectors.**
- Θ := Cπ_{R₀} maps the k-magnon sector H_k(Ω) onto the k-hole sector H_k(Ω̄). It does not act
  inside H_k(Ω).
- So on H_k(Ω), O-covariance reduces to T-covariance. In particular C4b Lemma 3's pair walk W(K)
  only needs to be T-covariant, which C4b already states (H_m = T).
- The hole walk is then *determined*: W_hole = Θ W Θ^{-1}.
- On a finite torus this links N_mag = k with N_mag = V − k. On Z^3 these are distinct
  superselection sectors of one QCA, and they are coupled only through its local rule.
- So the real constraint is this: **the local rule must treat "two magnons in empty space" and
  "two holes in filled space" as Θ-mirrors.** C4e's rule is complement-symmetric (UC = CU), so for
  C4e this would force U to commute with the pure permutation π_R, which it does not.

**SU(2) remark (proved, elementary; monomial only).** Under the full action, U(1) forces SU(2)
(C4b Lemma 2). Suppose U commutes with S^- = Σσ^-_x and freezes singles, U|x⟩ = e^{iφ}|x⟩. If
U|x,y⟩ = e^{iθ}|x',y'⟩, then
- S^-U|x,y⟩ = e^{iθ}(|x'⟩+|y'⟩), while
- US^-|x,y⟩ = e^{iφ}(|x⟩+|y⟩).

Hence {x',y'} = {x,y}, and monomial pairs are static at every range. On the torus this is exact.
On Z^3 it follows via C4b's compactification. Non-monomial SU(2) dynamics is not addressed.

## Step 2 — symmetry-allowed pair moves (exact; `c4f_01` Part B)

The criterion is exactly C4c `c4c_01`:
- c' is a near pair;
- all four cross distances from c to c' are ≤ r (Lemma K);
- c' is fixed by Stab(c) in G ⋉ Z^3;
- COM(c') ≠ COM(c).

The counts are in the table above. Regressions against C4c pass: r = 1 gives T 6/13 and O 0/13;
r = 2 gives 56/62 and 36/62.

Reading: under the axis action every T-allowed move is O-allowed, because odd elements impose no
condition inside the magnon sector. The C4e glider, the T-allowed face move at r = 1, is therefore
symmetry-allowed under axis-O. Whether a range-1 or range-2 *realisation* exists is a separate
question (C4d P1 forbids range 1).

## Step 3 — the construction

**Geometry.**
- K(k) = k+{0,1}^3 is the unit cube.
- B(k) = {z ∈ K(k) : par z ≠ par k} and A(k) = K(k)∖B(k) are its two tetrahedra.
- Square units (L1), exactly as in C4e: S = a plaquette, D and D' its two diagonals, no control.
- Tetra-axis units (L2), for each cube k and axis j:
  - **(B,j,k):** S = B(k), D = B(k)∩{x_j=k_j}, D' = B(k)∩{x_j=k_j+1}, control set Γ = A(k)
    required **empty**.
  - **(A,j,k):** S = A(k), D and D' the same way, Γ = B(k) required **full**.

**Rule.** Write F_u = S_u ∪ Γ_u for the read set of unit u.
- u is a *candidate* if c∩S_u ∈ {D_u, D'_u} and its control holds.
- N1(u) = {w ≠ u in the same layer : F_w∩S_u ≠ ∅ or F_u∩S_w ≠ ∅}.
- N2(u) = ⋃_{w∈N1(u)} N1(w) ∖ (N1(u) ∪ {u}).
- u is **active** if:
  - (a) u is a candidate;
  - (b) for both states of u, with the rest fixed, no unit of N1(u) is a candidate;
  - (c) no unit of N2(u) is a candidate.
- L(c) crosses every active unit, and U = L2 ∘ L1.
- For squares F = S, so L1 is literally C4e's L1. N1 and N2 sizes are 32 and 178 for squares, and
  149 and 588 for controlled tetra-axes (C4e's uncontrolled tetra-axes have 38 and 126).

**Lemma I′ (involution with read sets; proved, any configuration, finite or infinite).** Suppose
every unit has a two-state write set S_u ⊆ F_u and a candidacy predicate that depends only on
c|F_u and is invariant under crossing u (this needs Γ_u ∩ S_u = ∅). Then L∘L = id.

*Proof.* This is C4e's proof, with "shares a site" replaced by the N1 relation above. The one new
fact used is that crossing Q changes only S_Q, so it can change the candidacy only of units w with
F_w ∩ S_Q ≠ ∅, that is, of w ∈ N1(Q) ∪ {Q}. Let Q1 ≠ Q2 both be active in c, and set
c' = cross_{Q2} c.
- **(i) Q2 ∉ N1(Q1).** Otherwise Q2 is a candidate in N1(Q1), which contradicts (b) for Q1. So
  S_{Q1} ∩ S_{Q2} = ∅ and F_{Q1} ∩ S_{Q2} = ∅. The crossings commute, and Q1's own candidacy
  survives.
- **(ii) Q1 stays active in c'.**
  - (b) for Q1, in either state of Q1: suppose some w ∈ N1(Q1) changes candidacy. Then
    F_w ∩ S_{Q2} ≠ ∅, so w ∈ N1(Q2), and hence Q2 ∈ N2(Q1). But Q2 is a candidate, which violates
    (c) for Q1.
  - (c) for Q1: suppose some w ∈ N2(Q1) changes candidacy. Then w = Q2 or w ∈ N1(Q2).
    - w = Q2 would mean Q2 ∈ N2(Q1) is a candidate, which (c) for Q1 excludes.
    - w ∈ N1(Q2) is a non-candidate in both states of Q2, by Q2's (b), so it is a non-candidate in
      c'.
- **(iii) Q2 stays active in c'.**
  - (a) holds: D ↔ D', and Γ_{Q2} is untouched.
  - (b) is symmetric in the state of Q2.
  - (c) holds: units of N2(Q2) ∖ (N1(Q2) ∪ {Q2}) have F ∩ S_{Q2} = ∅, so they do not change.

Invariance of the active set, A(L c) = A(c), then follows exactly as in C4e. The argument is local,
because activity depends only on the finite set ⋃_{v ∈ {u}∪N1∪N2} F_v. ∎

**Consequences (proved).**
- **Reversible CA and QCA.** U is a TI reversible CA with inverse L1L2. As a permutation of the
  n-basis it defines a QCA automorphism.
- **U(1):** crossings permute sites, so N is conserved.
- **TI:** the unit families are translation invariant.
- **Frozen singles:** every candidacy needs two occupied sites in S, so a single magnon is in no
  candidate unit.
- **O-covariance (the T versus O mechanism).** Signed permutations preserve parity, and the lower
  corner k' of R·K(k) has par k' = par k + (number of sign flips of R) mod 2. Hence:
  - R ∈ T maps B-units to B-units and A-units to A-units, together with their Γ;
  - odd R maps (B,j,k) ↦ (A,j',k') and (A,j,k) ↦ (B,j',k'), again with their Γ.

  C exchanges "Γ empty" and "Γ full", and maps c∩S = D to c∩S = D'.
  - So **Θ_R = C π_R maps the candidate/crossing structure of L2 onto itself.** The geometric
    relations N1 and N2 are preserved too.
  - L1 commutes with every π_R and with C.
  - Hence [U, π_R] = 0 for R ∈ T, and [U, Cπ_R] = 0 for odd R. By Step 1, U is O-covariant with
    the axis action, phases included.
  - This holds although [U, π_R] ≠ 0 for odd R and [U, C] ≠ 0 (explicit witnesses).
- **Two-magnon sector = C4e's (proved).** With two magnons only, no A-unit is a candidate,
  because Γ would need four occupied sites.
  - A B-unit is a candidate only when the pair is its D or D' edge. That edge then lies in
    B(k), so Γ = A(k) is empty.
  - A face diagonal lies in exactly one plaquette, and is an edge of exactly one B-tetrahedron,
    on exactly one axis.
  - So, exactly as in C4e: {0, e1+e2} → (L1) {e1, e2} → (L2) {e3, (1,1,1)}. The general move is
    v = ρ_bρ_c e_a, and non-face pairs are untouched.
  - The pair band is E_ρ(K) = K·v(ρ), with |v_g| = 1.
- **Hole sector (proved via Θ).** U(Θc) = Θ(Uc). Single holes are frozen, and a hole face pair
  with relative position ρ moves by R v(R^{-1}ρ) = −ρ_bρ_c e_a (checked for C4z; the same holds for
  every odd R).

## Checks (`logs/`)

| script / section | what it checks | result |
|---|---|---|
| `c4f_01_axis_action.py` | D_R diagonal (T) / antidiagonal (odd) in the n-basis, all 24 R; pair-move classification r = 1, 2, 3 with regressions to C4c | PASS=10 FAIL=0 |
| `c4f_02 inv_sparse` | Z^3, sparse code: L1² = L2² = id, U^{-1}U = id, N conserved, on all 61,295 configurations with k ≤ 3 in the 4³ box plus k = 4 in the 3³ box (15,936 moved by U) | PASS=1 FAIL=0 |
| `c4f_02 inv_dense` | dense torus code (separate implementation: N1/N2 from sparse incidence matrices), L = 10 and 12; random densities 0.02–0.98 plus stress on empty/full/half/slab/random backgrounds; both L2 kinds crossed ≥ 100 times; sparse = dense | PASS=6 FAIL=0 |
| `c4f_02 sym` | N conservation; TI; [U, π_R] = 0 for 12 R ∈ T and [U, Cπ_R] = 0 for 12 odd R on 200 stress configurations (647 crossings); explicit SU(2) amplitudes; witnesses [U, π_R] ≠ 0 (odd R) and [U, C] ≠ 0 | PASS=7 FAIL=0 |
| `c4f_02 sectors` | single magnon and single hole fixed by U and U^{-1}; all 1098 magnon pairs with \|ρ\|∞ ≤ 6 over 3 ticks (6 move with v, 1092 static); all 364 hole pairs with \|ρ\|∞ ≤ 4 on L = 12 (6 move with −v, as predicted before the run, 358 static) | PASS=5 FAIL=0 |
| `c4f_02 radius` | exact dependency radius 3 per layer; empirical influence L1 3, L2 3, U 5 | PASS=2 FAIL=0 |
| `c4f_03_interface.py` | Θ-mirror along 8 interface trajectories; head-on pairs | PASS=2 FAIL=0 |
| `c4f_04_stress.py` | 1500 packed-candidate configurations on 5 backgrounds × 8 ticks (crossings: 58,925 L1, 24,958 B-type, 25,088 A-type): every layer is an involution on its input, U^{-8}U^{8} = id, sparse = dense on 60 | PASS=4 FAIL=0 |

`logs/SUMMARY.txt`: **TOTAL: PASS=37 FAIL=0**. No recorded run FAILed. One earlier version of the `c4f_01` classification used a wrong criterion: it required c′ to lie in the orbit of c. It disagreed with C4c's r = 1 count (one FAIL) and was replaced by C4c's exact criterion. That superseded log was overwritten, not kept, and is disclosed here.

**Descriptive (exact simulation, finite windows).**
- **Interface.** A (1,1,0) magnon pair moving +e3 into a filled slab z ∈ [7,10] on the L = 12
  torus is **reflected**, for all 8 tested start positions. After 12 ticks it is a (1,−1,0) pair
  below the slab; no magnon is left inside and no hole is created. This is the analogue of C4e's
  pair-single reflection.
- **Head-on pairs** in the empty background: 50 of 50 separate past each other, as in C4e.

**Disclosure.** The hole-glider prediction −v was derived from Θ-covariance and written in
`WORKLOG.md` before `sectors` ran. Both implementations are by the same author. The dense one was
written separately and builds N1/N2 by brute-force incidence. It is not independent in the §2.8
sense.

## Claim types

| claim | type |
|---|---|
| Step 1 equivalence (O-axis ⟺ T-perm + Θ) and sector consequence | proved; numerically checked lifts |
| SU(2) ⇒ monomial pairs static, any range | proved (elementary) |
| Pair-move classification table | exact finite enumeration (kinematic necessary conditions only) |
| Lemma I′ | proved; exhaustive small-sector and stress checks |
| U is TI, U(1), O-covariant (axis, phases), frozen singles/holes, C4e glider, hole glider −v | proved from Lemma I′ + geometry; exact checks |
| CA radius ≤ 6 (per layer exactly 3); radius ≥ 5 (witness); QCA range ≤ 18 | computed / proved bound / exact witness |
| interface reflection, head-on table | exact simulation, descriptive |

## No-go discipline / scope

- **Positive and exhibited:** within the premise class (one qubit per site, Z^3-TI, Q_n-conserving,
  covariant under all of O with the axis action), a QCA with frozen singles and a genuinely moving
  bound pair. This removes the "only under T" qualifier of C4e, C4c and C4d **for the axis
  action**.
- **No negative claim is made.** The full action remains different: there, U(1) ⇒ SU(2) ⇒
  monomial pairs static (proved). Non-monomial SU(2) pair motion is open.
- **Not achieved:** range 2. The QCA range is only bounded by 18. The k ≥ 3 sectors are not
  analysed beyond descriptive runs.
- **Not claimed:** finite-density transport, or any physical identification. The background
  dependence of the rule (empty versus full controls) is a feature of this example, not a derived
  necessity.

## Load-bearing steps for independent check

1. **Lemma I′**, especially (ii). Check that N1 must include *both* F_w∩S_u and F_u∩S_w. The
   first protects Q1's (b) and (c); the second protects Q1's own candidacy. A blind route is to
   implement the rule from this text and test L∘L = id on packed configurations near empty/full
   interfaces.
2. **The parity step:** odd R maps B(k) onto A(k') with Γ ↦ Γ, so that Cπ_R maps B-empty units to
   A-full units.
3. **Step 1:** the odd-R lift is antidiagonal in the n-basis, and phases drop out because U
   conserves N.

## Novelty

No literature search was done. The O-equivariance mechanism (rule ∘ particle–hole ∘ odd rotation)
is a magnetic-group-style symmetry. Novelty does not bear on correctness.

## Reproduction

```bash
cd blocks/C4f/scripts   # OMP_NUM_THREADS=1 nice -n 10, one core
python3 c4f_01_axis_action.py          # ~45 s
python3 c4f_02_verify.py inv_sparse    # ~4 min
python3 c4f_02_verify.py inv_dense     # ~20 s
python3 c4f_02_verify.py sym           # ~30 s
python3 c4f_02_verify.py sectors       # ~15 s
python3 c4f_02_verify.py radius        # ~35 s
python3 c4f_03_interface.py            # ~10 s
python3 c4f_04_stress.py 1500          # ~10 min
```
