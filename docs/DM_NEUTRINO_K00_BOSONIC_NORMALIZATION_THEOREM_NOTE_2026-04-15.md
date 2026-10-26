# Conditional scalar-baseline response correspondence for K00

**Type:** bounded_theorem
**Status:** supplied finite algebra/evidence; physical bridge open
**Primary runner:** `scripts/frontier_dm_neutrino_k00_bosonic_normalization_theorem.py`

For the supplied breaking-triplet matrix H with core entries A,b,c,d, the specified heavy-basis transform gives

    K00=Tr(H*F00)=(A+4b+2c+2d)/3, F00=J3/3.

The breaking triplet cancels from this linear functional. F00 is a rank-one projector in dimension 3; FROW=J2/2 is a rank-one projector in dimension 2. They have the same NONZERO spectrum {1}, with different zero multiplicities. Their scalar-baseline relative determinants coincide:

    det(mI+jF)/det(mI)=1+j/m

for either projector, m!=0. The log-absolute response equals log|1+j/m| where m+j!=0. The corresponding full J2 generator gives 1+2*tau/m. Equality of the full determinant responses would identify j=2*tau on the common baseline; equality of log-absolute responses additionally has a sign ambiguity unless one fixes a connected nonsingular branch containing zero.

This is a correspondence between supplied source coefficients. It does not identify the independent target functional K00(H) with j. The equation K00=2*tau_+ is an additional physical coefficient-identification premise, not a consequence of equal generator spectra or the logdet observable alone. For example H=3I gives K00=3 while an independently supplied tau_+=1 gives 2*tau_+=2, without changing the generator spectra.

If the extra identification is imposed and tau_E=tau_T=1/2 are separately supplied, then tau_+=1 and K00=2 follows arithmetically. The runner labels those as supplied inputs; it does not derive their values. The physical observable principle, source amplitudes and coefficient matching remain open. The swap-even row-sum representation also requires its own operator-domain premise; no unrestricted weak-even equivalence is assumed here.

## Provenance

Prior text is recoverable at Git `f24d17d97d372df977476e4a69674577f31af575` under this path. Related definitions/context (no blanket status endorsement):

- [`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)
- [`DM_NEUTRINO_WEAK_EVEN_SWAP_REDUCTION_THEOREM_NOTE_2026-04-15.md`](DM_NEUTRINO_WEAK_EVEN_SWAP_REDUCTION_THEOREM_NOTE_2026-04-15.md)
- [`DM_NEUTRINO_TRIPLET_CHARACTER_SOURCE_THEOREM_NOTE_2026-04-15.md`](DM_NEUTRINO_TRIPLET_CHARACTER_SOURCE_THEOREM_NOTE_2026-04-15.md)
