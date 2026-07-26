# Cycle 703 local-Gauss held-patch grammar addendum

**Date:** 2026-07-25

**Authority:** none

**Audit:** unset
**Dependency:** `CYCLE703_LOCAL_GAUSS_REFERENCE_ADVERSARIAL_NOTE_2026-07-25.md`

## Result

The independent local-Gauss package established the exact two-cell CAR
formula, its full 4,096-column common-E restriction, full off-code involution,
odd/even capacity, and 24/576 covariance.  This addendum asks the narrower
overlap-fixture question left by that result:

> Does one target-independent local gate grammar compile every onsite and
> bond operand of the training L and held 2x2/3x3 fixtures without an exterior
> order table, and can the auxiliary reference stream be removed?

The answer is **yes at the even operator-algebra layer**.

- Every Cycle-219 coin factor and every Cycle-230 diagonal contact factor on
  the three fixtures is mapped by the same local even-generator grammar.
- Every undirected fixture bond is tested in both orientations with the exact
  spectator-parity-dressed local-D FSWAP grammar.
- The abstract parallel reference generator `A(r_x,r_y)` is represented by
  the already present bounded path `r_x-u-v-r_y`.  This removes the extra
  parallel reference-stream M2 used by the direct construction.
- All mapped terms commute with the local loop and `D` projectors.  The
  transformed four-term path word itself, not merely its A/B ingredients,
  passes all 24 proper-cubic frames on L, 2x2, and 3x3.  The 576 ordered frame
  products also close on addresses and A/B words.
- The one-particle mass fixture and local contact block are unchanged.

This closes a resource and composition question.  It does **not** close the
physical BKSF state encoder.  No route-independent no-go or axiom pressure is
claimed.

## Exact retained residuals

| Control | L | held 2x2 | held 3x3 |
| --- | ---: | ---: | ---: |
| cells | 16 | 20 | 39 |
| physical edge M2 | 304 | 380 | 744 |
| code exponent / target | 96 / 96 | 120 / 120 | 234 / 234 |
| coin factors | 176 | 220 | 429 |
| contact factors | 240 | 300 | 585 |
| directed bond operands | 32 | 40 | 84 |
| stream Pauli terms per operand | 4 | 4 | 4 |
| maximum onsite Pauli weight | 12 | 12 | 12 |
| maximum stream Pauli weight | 17 | 17 | 17 |
| maximum stream site diameter | 28 | 28 | 28 |
| corrected dressed-stream covariance failures | 0 | 0 | 0 |
| projector commutator failures | 0 | 0 | 0 |
| work M2 / returned-work failures | 0 / 0 | 0 / 0 | 0 / 0 |

Across all fixtures:

- maximum onsite unitary expansion residual:
  `2.4830808498869886e-16`;
- maximum onsite Hermitian-log expansion residual:
  `7.397092656394907e-18`;
- non-Hermitian mapped terms: `0`;
- one-particle coin eigen residual: `2.594441202963249e-16`;
- mass: `0.45340565417488515` versus the Cycle-219 fixture
  `0.4534056541748851`, residual `5.551115123125783e-17`;
- contact vacuum/one-particle residual: `0`;
- contact double-occupation phase residual: `0`;
- extra reference-stream M2: `0`;
- runtime exterior-order table: absent;
- runtime global parity query: absent.

The raw fixed-incidence port words disagree under frames, as expected
(`6592`, `8240`, and `16104` mismatches).  After the declared local order
gauge, A/B, projectors, physical positions, and dressed path words have zero
failures.  This is operator-family covariance.  Transformed physical common-E
covariance remains unexecuted.

## Gate grammar and resource reduction

For a directed matter bond `u=(x,a)` to `v=(y,b)`, the retained exact formula
from the dependency is

```text
P_(y,not b) = product_(c != b) B(m_y,c)
H_uv = -P_(y,not b) (1-B_u B_v) A_uv A_(r_x r_y) / 2
FSWAP_uv = (B_u+B_v)/2 + H_uv.
```

The addendum replaces the dedicated edge representative of `A_(r_x r_y)` by

```text
A_(r_x r_y) = path_A(r_x, u, v, r_y)
```

on the local loop code.  `path_A` carries the required CAR composition phase.
The resulting four coefficient-free Pauli words are Hermitian and commute
with every local loop and `D` row on every tested bond.  Maximum Pauli weight
is `17` and maximum site diameter is `28`, independent of held size.  A bare
matter edge anticommutes with exactly the two endpoint `D` rows on all 156
directed fixture operands, so the dressing is active.

This orientation is local operand data transported with the directed port.
Both orientations of every bond are compiled.  No volume-wide mode order or
exterior lookup table is queried.

## Deletion and lawful-domain controls

On the L fixture:

- all 193 independent loop basis rows are deletion-active;
- the full family of 16 displayed `D_x` rows has rank increment 15;
- deleting any one displayed `D_x` changes no rank, because their product is
  the fixed-even identity;
- deleting any two displayed `D_x` rows releases one logical bit;
- deleting any one of the three periodic Wilson selectors releases one
  topological logical bit;
- deleting the contact phase gives residual `0.36789306705608243`.

The exact seam companion separately supplies the stronger lawful-domain
controls: deleting the reference dressing violates the endpoint `D` laws,
omitting spectator parity produces 36,864 phase failures, and omitting the
number-sector projector produces 73,728 pair failures.

## Supplied versus derived structure

Supplied:

- one scalar reference fermion per cell;
- the onsite law `D_x=B(r_x) product_a B(m_x,a)=+1`;
- BKSF edge incidence, local loop projectors, and the local CZ/Z port-order
  gauge;
- three Wilson characters on a periodic three-torus;
- Cycle-219 coin data, Cycle-230 contact coupling, and the declared factor
  schedule;
- a directed local port operand for each stream factor.

Derived and executed here:

- exact 6N code capacity on L and held 2x2/3x3;
- one onsite gate grammar for every coin/contact factor;
- one spectator-dressed stream grammar for both orientations of every bond;
- removal of the dedicated reference-stream M2 by a bounded existing path;
- mass/contact preservation, deletion controls, and transformed word
  covariance.

## Remaining wall

The canonical logical algebra can be oriented locally with `Z=B_m` and a
local `X` built from `A_(m,r)` and earlier local `B` operands.  That gives a
logical Pauli presentation; it is not a state-preparation circuit.

The remaining common wall is therefore sharply state-side:

1. construct an explicit BKSF edge-qubit common E, including phases, from the
   matter basis into one fixed loop/D/Wilson code sector;
2. execute `U_BKSF E - E U_matter` and leakage residuals for the actual
   physical words;
3. distinguish a supplied fixed-Wilson resource from bounded autonomous
   preparation;
4. compare the transformed common E, not only the transformed operator
   family.

The present evidence supports no claim that this wall is impossible or
axiomatic.  It is an unfinished constructive layer with a concrete next
probe.

## Reproduction

```bash
PYTHONPATH=scripts python3 -u \
  scripts/frontier_cycle703_local_gauss_bksf_full_parity_2026_07_25.py
```

Expected terminal:

```text
LOCAL_GAUSS_HELD_PATCH_GRAMMAR_CLOSED_BKSF_COMMON_E_OPEN
```

The retained run passed 7 checks, failed 0, used 100.0 MB peak RSS, and took
618.4993827501312 seconds.  Certificate SHA-256:
`1c1aa58c255d263e2926c6cdc3e8cbc5f198e77dc36733371ab3606b7a97d5d8`.
