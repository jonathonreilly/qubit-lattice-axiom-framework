# LIB1 finite-check criteria — before implementation and execution

These are author checks of finite graph identities. The written proof must
carry all volume, scale and source quantifiers. No finite check grants an
independent review or a Yang–Mills estimate.

Use exact Python integers and fractions, no numerical libraries or pools.
Run with `nice -n 10` and `OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=VECLIB_MAXIMUM_THREADS=NUMEXPR_NUM_THREADS=1`.
The script must itself require all reported load averages below 20, the
macOS `memory_pressure -Q` system-wide free percentage at least 50%, and
its maximum RSS below 2,000,000,000 bytes. Check these before enumeration,
periodically, and at completion. Refuse execution with a recorded reason
if the platform/gate cannot be checked. No multiprocessing. A 60-second
computation deadline is sufficient; resource/deadline refusal is not a
mathematical failure or a successful test.

1. Enumerate all connected supports and every nested pair Λ⊆Ω in a
   six-vertex path, six-cycle and 2×3 box. These are finite graph tests of
   the degree≤8 proof, not full-volume sampling. Compute minimal ambient
   Steiner-tree edge counts independently as the minimum |C|−1 over every
   connected vertex superset C.
2. For every admissible X∈P_Ω meeting Λ, check connectedness, old/new
   saturation, containment, preservation of the active set and decrease of
   the ambient-tree length. Compare one-step component filling against
   iterative addition of adjacent inactive vertices to closure.
3. Assign distinct rational polynomial coefficients to each support, with
   its monomial containing every source in that support. Check the exact
   coefficient identity after regrouping, including the inactive remainder,
   and containment of every original monomial support in the output label.
4. Use positive coefficients 2^(−20 d_Ω(X)) to check the explicit rooted
   count at a=16 log 2 and decay output with κ_B=20 log 2. The mathematical
   majorant 1024 is justified in the written proof, not fitted to these
   finite graphs. Check active-norm contraction at μ=log 2. Also verify
   the bounded-hole full-norm inequality with the exact maximum component
   size M of each Λ-complement.
5. Include empty/full active regions and singleton supports. For a native
   four-dimensional 2×2×2×2 block torus, check all singleton/pair supports
   against all active sets that remove at most two vertices, with Ω=Γ.
   Periodic edge duplicates are collapsed, so the graph degree stays ≤8.
6. Mutation controls: an implementation that drops the inactive remainder
   must fail on a nonempty inactive term; a projection that deletes a
   source in an inactive block must fail a mixed-monomial check; filling
   only intersected (not adjacent) inactive components must fail the stated
   closure rule; replacing the full norm by its active counterpart must
   fail the explicit singleton/large-hole full-norm comparison.

Report counts, exact witnesses, resource observations and any failures.
No number of predicates is a completion percentage. The script's source
and outputs stay under `checks/lib1_*`.
