# Supplied ordered-chain nonzero-current fixture

**Type:** bounded_theorem
**Status:** conditional finite algebra; physical current law open.
**Primary runner:** `scripts/frontier_dm_pmns_graph_first_ordered_chain_nonzero_current_closure_2026_04_21.py`

Supply ordered matrix units, cycle C=E12+E23+E31, the character current and
normalization min spec(N)=1. These are premises, not a physical source law.
The chosen A_ord=N+C has J_chi(A_ord)=1 on the specified response fixture.

## 2. Canonical ordered-chain law

Supply the ordered chain

```text
1 -> 2 -> 3
```

there is one unique normalized Hermitian grading element on that chain.

Let

```text
N = diag(n1,n2,n3).
```

Impose the exact local grading law on the adjacent chain generators:

```text
[N,E12] = -E12,
[N,E23] = -E23.
```

Because

```text
[N,E12] = (n1 - n2) E12,
[N,E23] = (n2 - n3) E23,
```

these conditions force

```text
n2 = n1 + 1,
n3 = n2 + 1.
```

With the minimal positive normalization

```text
min spec(N) = 1,
```

the grading is uniquely

```text
N = diag(1,2,3).
```

The graph-first cycle-frame theorem already fixes the exact forward cycle

```text
C = E12 + E23 + E31.
```

Choose the supplied unit-coefficient ordered-chain fixture

```text
A_ord = N + C.
```

This law uses no PMNS target values. It is built entirely from:

- the supplied ordered chain,
- the supplied ordered projectors,
- the supplied forward cycle,
- and the internal path-algebra grading.

---


## Response evidence and limits

The runner preserves chain_number_operator, the commutator checks, target-free
function-signature diagnostic, and supplied .31 active/.27 passive response
reconstruction. Reconstructing a chosen matrix establishes recovery, not physical
selection. N+C is a chosen combination; uniqueness of normalized N does not
prove uniqueness or physical admissibility of every active law.

The prior sole-axiom target-met claim and later scalar-selection claim are
withdrawn. Physical source selection, values of the currents, and admissibility
remain open. The coordinate-recovery companion does not close these obligations.

- [cycle definitions](PMNS_GRAPH_FIRST_CYCLE_FRAME_SUPPORT_NOTE.md)
- [chain algebra](DM_WILSON_TO_DWEH_LOCAL_CHAIN_PATH_ALGEBRA_TARGET_NOTE_2026-04-18.md)

For any nonzero supplied alpha, N+alpha C has the same normalized grading N
and diagonal-plus-forward-cycle support. For example alpha=2 differs from
alpha=1. Thus the stated premises do not select the cycle coefficient or a
unique active law.

## Numerical and documentary responsibilities

The numerical owner retains both Part5 inequalities `abs(j-1)<1e-12` and
`abs(j)>1e-12`. Its former downstream-native note read has moved to the native
reader's documentary contract. The old conjunction of numerical nonzero current
and a note substring is split into those same factors, with text consistency
explicitly distinct from mathematical evidence. No numerical condition or
physical open obligation is removed. Original source/captures are recoverable
at `51f45f63c30613713fec42d0b4917d16483558aa`.
