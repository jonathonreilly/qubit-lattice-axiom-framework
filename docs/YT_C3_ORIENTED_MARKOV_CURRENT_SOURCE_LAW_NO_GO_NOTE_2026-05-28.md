---
claim_id: yt_c3_oriented_markov_current_source_law_no_go_note_2026-05-28
claim_type: no_go
actual_current_surface_status: no-go / open oriented-current-to-top-row law
trace_class: negative_route_pruning
reachability_to_target: prunes
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
---

# Y_T C3 Oriented Markov-Current Source-Law No-Go

**Date:** 2026-05-28

**Status:** exact negative boundary for the shortcut from a nonreversible
oriented C3 Markov current to the missing coefficient-bearing top row. This
note does not claim positive `Y_T` closure.

**Runner:**
`scripts/frontier_yt_c3_oriented_markov_current_source_law_no_go.py`

**Output:**
`outputs/yt_c3_oriented_markov_current_source_law_no_go_2026-05-28.json`

## Question

The reversible C3 Markov/Laplacian shortcut is already pruned. A natural
next refinement is to keep the same finite C3 carrier but allow a circulating
nearest-neighbor current:

```text
Q_{p,q} = p(C-I) + q(C^2-I),        p,q >= 0.
```

For `p != q`, this is a real nonreversible Markov generator with an orientation
current. Can that current supply the missing non-mass physical top-line law
and the source matrix element

```text
dM_t/dell = A/sqrt(12)?
```

## Answer

No.

The oriented generator has the same C3 projectors as every circulant:

```text
P_0, P_omega, P_omega2.
```

Its spectrum is:

```text
Q_{p,q}:
  P_0       -> 0,
  P_omega   -> -3(p+q)/2 + i sqrt(3)(p-q)/2,
  P_omega2  -> -3(p+q)/2 - i sqrt(3)(p-q)/2.
```

Thus the Markov semigroup still has `P_0` as its stationary/Perron line.  The
two nontrivial modes have equal real decay rate; the orientation current
splits only their phase signs.  Choosing a nontrivial complex line from that
phase is an additional phase/readout convention, not a same-surface physical
top-line theorem.

Equivalently,

```text
Q_{p,q}
  = ((p+q)/2)(C+C^2-2I) + ((p-q)/2)(C-C^2).
```

The symmetric decay part is the already-pruned Markov/Laplacian route.  The
antisymmetric current part is anti-self-adjoint on the real carrier; converting
it into the Hermitian phase operator `i(C-C^2)` supplies only an oriented
`B_y` axis with a free current ratio.  It does not derive the physical
top-readout law excluding `P_0`, does not supply accepted pole/projector
authority, and does not fix the radial generator factor
`lambda_top=1/sqrt(2)`.

## Relation To Current Stack

This block is narrower than the earlier orientation-sign and phase-strength
no-go packets.  It tests a specific first-principles candidate for the missing
orientation-odd base dynamics:

```text
nonreversible C3 Markov current
  + connected source normalization
  -> accepted non-mass top-line law
  -> accepted coefficient-bearing physical top row.
```

That implication fails because:

1. The positive Markov stationary/Perron line is still `P_0`.
2. The nontrivial modes are tied in real decay rate.
3. The current term supplies only conjugate phase signs unless a physical
   phase/readout law is added.
4. The current ratio `(p-q)/(p+q)` is a free same-surface dynamics parameter.
5. Even after granting a nontrivial top line, the top radial factor remains
   free until an accepted same-surface generator theorem or strict pole-row
   certificate supplies it.

## Assumptions / Imports Exercise

Inputs used:

- finite C3 generation cycle `C`;
- nonreversible nearest-neighbor C3 Markov generator
  `Q_{p,q}=p(C-I)+q(C^2-I)`;
- C3 spectral projector algebra;
- existing C3 `B_x` source direction and nontrivial-block support packets;
- first-principles transfer/Feynman-Hellmann response boundary;
- strict sparse availability audit.

Inputs not used:

- `H_unit`;
- old Ward authority;
- `yt_ward_identity`;
- `y_t_bare`;
- observed top/W/Z masses or PDG targets;
- `alpha_LM`;
- plaquette/u0;
- Planck;
- alpha_s;
- fitted selectors or target value insertion.

New load-bearing imports exposed:

```text
accepted physical phase/readout law turning oriented current into the top
  pole label,
accepted physical top-readout law excluding P_0,
accepted radial generator factorization lambda_top = 1/sqrt(2),
or accepted strict same-source top/W pole rows.
```

## First-Principles / Elon Exercise

Minimal premise set `A_min`:

- one finite three-state C3 Markov dynamics with a circulation current;
- no hidden mass ordering, target value, old Ward row, or fitted selector;
- quotient identity normalizers and separate symmetric decay from current;
- combine only with existing same-source W support and C3 matrix elements.

Adversarial attempts:

1. **Use the Markov stationary/Perron line.** Fails. It is `P_0`, whose
   `B_x` response is the singlet row.
2. **Use the nontrivial decay space.** Fails as a non-mass top law. The
   nontrivial real decay rate is degenerate; choosing it is a decay/mass
   ordering premise, and it does not fix the radial factor.
3. **Use the current sign `p-q`.** Fails. It distinguishes the conjugate
   phase directions but supplies no accepted physical rule saying either
   phase line is the top pole.
4. **Normalize the current ratio.** Fails. The family contains every
   circulation ratio from zero to the one-way boundary. A chosen ratio is an
   extra dynamics law.
5. **Use a Hermitian `B_y` phase operator.** Conditional support only. It
   imports the map from nonreversible current to a physical Hermitian
   top-line readout and still leaves `lambda_top` open.
6. **Use target size to choose the line or radial factor.** Forbidden. That
   is coefficient insertion.

## Finite Oriented-Current Witness

Let `C` be the three-cycle.  For `p,q >= 0`,

```text
Q_{p,q} = p(C-I) + q(C^2-I)
```

has row and column sums zero and off-diagonal rates `p,q`.  With
`omega = exp(2 pi i / 3)`,

```text
lambda_0 = 0,
lambda_omega = p(omega-1) + q(omega^2-1),
lambda_omega2 = p(omega^2-1) + q(omega-1).
```

Therefore:

```text
Re(lambda_omega) = Re(lambda_omega2) = -3(p+q)/2,
Im(lambda_omega) = -Im(lambda_omega2) = sqrt(3)(p-q)/2.
```

The current selects a phase sign only when `p != q`.  It does not change the
real decay degeneracy of the nontrivial block and does not make the positive
stationary line nontrivial.

If one grants, for the sake of the route, that a supplied physical phase law
chooses a nontrivial line, the same-source top family

```text
V_top(lambda_top) = lambda_top A B_x
```

still gives

```text
|Tr(P_omega V_top)| = |Tr(P_omega2 V_top)|
                    = lambda_top A/sqrt(6).
```

The target row requires

```text
lambda_top = 1/sqrt(2).
```

The oriented Markov current does not derive that radial generator factor.

## No-Go Audit

This block prunes only:

```text
nonreversible C3 Markov current
  + connected/current normalization
  -> accepted non-mass physical top-line law
  -> accepted coefficient-bearing physical top row.
```

It does not prune:

- a future accepted same-surface phase/readout theorem that gives a physical
  meaning to the current sign and excludes `P_0`;
- a future radial generator theorem deriving `lambda_top=1/sqrt(2)`;
- an accepted backend/projector/source-generator matrix-element theorem;
- strict same-source top/W pole rows with contact, FV/IR, and model-class
  controls.

## Stuck Fan-Out Synthesis

| Frame | Result |
|---|---|
| Markov stationary line | selects `P_0`, not the target row. |
| Real decay ordering | nontrivial block is degenerate and uses a decay/mass premise. |
| Current phase sign | distinguishes conjugate nontrivial phases only after a readout law. |
| Current-ratio normalization | leaves a free parameter; no primitive phase angle is derived. |
| Radial response | still needs `lambda_top=1/sqrt(2)` or strict pole rows. |

## Literature / Math Search

No external numerical or phenomenological input is load-bearing.  The needed
mathematics is the finite spectral theory of a three-state circulant Markov
chain, including the standard split into stationary, symmetric decay, and
circulating-current parts.  The runner rederives the spectrum directly, so
external references would be background rather than proof input.

## What Remains Open

The rank-1 C3 route still needs an accepted same-surface theorem that supplies:

```yaml
physical_top_readout:
  excludes_P0: true
  non_mass_ordering_law: true
  phase_or_current_readout_accepted: true
radial_generator:
  lambda_top: 1/sqrt(2)
backend:
  same_surface_W_top_projectors: accepted
  source_generator_matrix_elements: accepted
```

The strict route still needs accepted coefficient-certified same-source top/W
pole rows with contact, finite-volume/infrared, and model-class controls.

## Non-Claims

This note does not:

- claim positive `Y_T` closure;
- refute a future accepted orientation-current physical readout theorem;
- refute strict top/W pole-response evidence;
- prove which C3 line is the physical top pole;
- derive `m_t`, physical-scale `g_2`, or numerical `y_t(v)`;
- use `H_unit`, `yt_ward_identity`, `y_t_bare`, observed W/Z/top masses, PDG
  values, `alpha_LM`, plaquette/u0, Planck, alpha_s, or a fitted selector as
  proof inputs.

## Claim-Status Certificate

```yaml
actual_current_surface_status: no-go / open oriented-current-to-top-row law
trace_class: negative_route_pruning
reachability_to_target: prunes
route_pruned: nonreversible C3 Markov current plus connected/current
  normalization derives accepted non-mass physical top-line law and the
  coefficient-bearing top row
proposal_allowed: false
proposal_allowed_reason: |
  The oriented C3 Markov current keeps P_0 as stationary/Perron line, leaves
  the nontrivial real decay rate degenerate, and supplies only conjugate phase
  signs until a physical phase/readout law is added. It also does not derive
  lambda_top=1/sqrt(2), accepted backend/projectors, or strict top/W pole rows.
bare_retained_allowed: false
audit_required_before_effective_retained: true
next_action: derive accepted same-surface readout/radial/backend laws, or
  produce accepted strict same-source top/W pole rows
```

## Verification

Run:

```text
python3 scripts/frontier_yt_c3_oriented_markov_current_source_law_no_go.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```
