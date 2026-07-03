# SO(2) Embedding Framing Does Not Supply the Spinor Swap Sign

**Date:** 2026-06-02
**Claim type:** no_go
**Review provenance:** source theorem candidate; post-landing audit decides the
ledger grade. This note introduces no new axiom, primitive, Tier-A admission, or
matter-spinor postulate.
**Primary runner:**
[`scripts/koide_embedding_framing_writhe_so2_vs_spin_z2_decoupling_2026_06_02.py`](../scripts/koide_embedding_framing_writhe_so2_vs_spin_z2_decoupling_2026_06_02.py)
**Cached runner output:**
[`logs/runner-cache/koide_embedding_framing_writhe_so2_vs_spin_z2_decoupling_2026_06_02.txt`](../logs/runner-cache/koide_embedding_framing_writhe_so2_vs_spin_z2_decoupling_2026_06_02.txt)
(SCORECARD: PASS=24 FAIL=0)
**Completed runner cache:**
[`logs/runner-cache/koide_embedding_framing_writhe_so2_vs_spin_z2_decoupling_2026_06_02.txt`](../logs/runner-cache/koide_embedding_framing_writhe_so2_vs_spin_z2_decoupling_2026_06_02.txt)
(`SCORECARD: PASS=24 FAIL=0`; dependency-free graph helper)

## Claim

For the tested Abrams `UD_2(Gamma)` witnesses (`K_{3,3}`, `K_5`, and a genuine
non-planar `3x3x2` slab of the `Z^3` site graph), the embedding-framing route
does not supply the fermionic swap sign:

- a lattice edge embedded in `R^3` has a rank-2 normal bundle with structure
  group `SO(2)`;
- a normal-bundle framing/self-linking datum is therefore integer or `U(1)`
  abelian data (`pi_1(SO(2)) = Z`);
- the graph-braid swap class `t` is a 2-torsion class in `H_1(UD_2(Gamma); Z)`;
- every integer-valued 1-cocycle and every flat real `U(1)`/`SO(2)` connection
  pairs trivially with `t`;
- the vector/adjoint frame sees a `2pi` exchange rotation as `+I`, while the
  `-I` sign appears only in the spin-1/2 representation.

So the `R^3` embedding's `SO(2)` normal-bundle framing is blind to the swap
class. This is a scoped route-pruning no-go for abelian embedding-framing data
only. It does not claim fermionic statistics is impossible on the lattice, and it
does not decide any matter-state, spinor-attachment, or second-quantized
graded-locality route.

## Computation

The runner builds the same Abrams unordered two-token cubical complex used by
the graph-braid notes:

- `C_0`: unordered vertex pairs;
- `C_1`: one parked vertex plus one non-incident moving edge;
- `C_2`: vertex-disjoint edge pairs;
- `d_1` and `d_2`: exact integer cubical boundary maps.

It verifies four finite statements.

1. **Two-torsion swap.** On `K_{3,3}`, `K_5`, and the `Z^3` slab witness, the
   runner finds a swap generator `t` with `d_1 t = 0`, `2t in im(d_2)`, and
   `t notin im(d_2)`.
2. **Integer framing is blind.** A basis for the integral 1-cocycle space pairs
   to zero with `t` on every tested witness. Since a writhe/self-linking framing
   is integer-valued, it cannot evaluate to the fermionic `-1` swap sign.
3. **Flat real framing is blind.** The runner verifies `t = 0` in
   `H_1(UD_2; R)`, so every flat real `U(1)`/`SO(2)` connection gives holonomy
   `+1` on the swap. A non-flat connection is not a homotopy-invariant
   statistics sign.
4. **Vector versus spinor frame.** A `2pi` rotation is `+I_3` in the vector /
   adjoint frame and `-I_2` in the spin-1/2 representation. The embedding's
   `SO(2)` normal-bundle framing lies on the abelian/vector side of this split.

The runner also exhibits a `GF(2)` cocycle with value `1` on `t`; that class is
non-fibered and is not the reduction of an integral framing class. This is why
the swap sign is real configuration-space data but not `SO(2)` writhe data.

Current cache certificate:

```text
SCORECARD: PASS=24 FAIL=0
```

## Scope

This note claims only:

- `SO(2)` normal-bundle framing data of the embedded lattice edge is not enough
  to supply the swap sign;
- the obstruction is exact on the tested finite witnesses;
- the obstruction is group-theoretic (`SO(2)`/`U(1)` abelian framing versus the
  spinor double-cover sign) and homological (`t` is 2-torsion).

This note does not claim:

- that lattice fermions cannot be derived by another route;
- that a spinor-state law, graded-locality principle, or fermion-parity
  superselection rule is unavailable;
- that any Kawamoto-Smit, matter-attachment, or field-algebra row is accepted or
  rejected;
- that this no-go applies beyond the abelian embedding-framing sector.

## No-Go Discipline Gate

**Gate result:** PASS for the scoped abelian embedding-framing no-go only.

### N1 - Alternative Route Enumeration

| route | what it would attempt | why it fails for this scoped no-go | marker |
|---|---|---|---|
| Integer writhe | Source the swap sign from normal-bundle self-linking / writhe. | Writhe is an integer 1-cocycle, and every integral cocycle pairs to zero with the 2-torsion swap class on all tested witnesses. | ATTEMPTED |
| Flat real framing | Use a flat `U(1)`/`SO(2)` connection with holonomy `exp(i<A,t>)`. | `t = 0` in real homology, so every flat real connection gives holonomy `+1`; non-flat data is not a statistics invariant. | ATTEMPTED |
| Flat base-edge sign | Use a base-edge `Z_2` link-sign connection. | The swap class has zero base-edge projection in the graph-braid fibered test; the same blindness is recovered here as the abelian-framing shadow. | ATTEMPTED |
| Vector / adjoint transport | Carry the sign through the embedding's vector frame. | The vector/adjoint frame sees a `2pi` exchange as `+I`; the `-I` sign appears only in the spin-1/2 representation. | ATTEMPTED |
| Integral lift of the `GF(2)` swap cocycle | Detect `t` by a non-fibered `GF(2)` cocycle and lift that class to an integral `SO(2)` framing. | Such a `GF(2)` cocycle exists, but it is 2-torsion/Bockstein data and is not the reduction of any integral framing class. | ATTEMPTED |
| Spinor-state route | Supply the sign from a spinor matter-state law. | Not addressed by this note; this is outside abelian embedding-framing data. | OUT OF SCOPE |
| Second-quantized graded-locality route | Supply the sign from field-algebra grading or fermion parity. | Not addressed by this note; this is a different surface from first-quantized embedding framing. | OUT OF SCOPE |

### N2 - Wall-Independence Audit

The collapsed wall set has one wall: the swap class is 2-torsion/spinor
double-cover data, while embedding framing is abelian `SO(2)`/`U(1)` data.
Integer writhe, flat real holonomy, and flat base-edge signs are not independent
walls; they are different abelian probes of the same torsion class. The vector
frame check is the representation-theoretic side of the same split.

### N3 - Hidden-Wall Scan

The load-bearing inputs are explicit:

- finite graph witnesses (`K_{3,3}`, `K_5`, and the `3x3x2` `Z^3` slab);
- the Abrams `UD_2` cubical chain complex and exact integer boundary maps;
- integer and rational linear algebra;
- standard `SO(2)`, `SO(3)`, and `SU(2)` representation facts.

The words "embedding", "framing", and "swap sign" are not used as hidden
accepted premises. CAR, matter-state identification, observed charge, and
readout data are not assumed.

### N4 - Residual Matching

| cited witness | residual it names | residual attacked here | match? |
|---|---|---|---|
| `FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28` | Lattice-internal / framing routes remain separate from the continuum rotation-exchange route. | The abelian `R^3` embedding-framing form of that route is pruned. | yes |
| `GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29` | The graph-braid exchange class is a `Z_2` torsion class. | This note tests whether abelian embedding framing can evaluate nontrivially on that class. | yes |
| `PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02` | The adjoint/operator frame and the spinor-state law are distinct. | This note independently observes the same vector-versus-spinor split at the embedding-framing route. | yes |

No context row is used to close a different residual.

### N5 - Rhetoric Audit

"Blind to the swap" means: every tested integer cocycle and every tested flat
real connection evaluates trivially on the swap class. "Wrong group" means:
`SO(2)` framing data is abelian integer/`U(1)` data, while the swap sign is the
spinor double-cover sign. "Does not supply" is scoped only to the abelian
embedding-framing sector.

### N6 - Partial-Closure Path Scan

The spinor-state route and second-quantized graded-locality route remain open.
They are not called new axioms here, and this note does not accept or reject
them. Closing either route would not change the abelian-framing no-go, because
the abelian `SO(2)` pairing on `t` would remain trivial.

### N7 - Steelman

The strongest objection is that an `R^3` embedding really does give each edge a
transverse normal plane, so the abstract graph-braid analysis might have thrown
away the missing framing. This note grants that premise: the transverse plane is
real. The obstruction is that its structure group is `SO(2)`, so its framing
invariants are abelian writhe/holonomy data. The runner checks that those
abelian invariants are blind to the 2-torsion swap.

### N8 - Cross-Cycle Echo

The prior overclaim risk is to infer a spinor/statistics sign from the existence
of some nearby geometric datum. This note avoids that by computing the actual
group and homology class before making a negative claim. It prunes only the
`SO(2)` embedding-framing route and explicitly leaves the spinor-state and
graded-locality routes open.

## Cited Context

The following row names provide context and comparison targets, but the finite
homology and representation checks above are recomputed in the runner:

- `GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29`
- `FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28`
- `PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02`
- `BINARY_OCTAHEDRAL_DISCRETE_SPINOR_SIGN_NARROW_THEOREM_NOTE_2026-05-28`

## Command

```bash
python3 scripts/koide_embedding_framing_writhe_so2_vs_spin_z2_decoupling_2026_06_02.py
```

Expected output: `SCORECARD: PASS=24 FAIL=0`.
