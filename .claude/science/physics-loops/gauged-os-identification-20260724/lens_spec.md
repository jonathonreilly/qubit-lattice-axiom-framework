# Adversarial lens — reflected-Gram extension boundaries

You are a hostile referee. Report only findings, labeled
BLOCKER / MAJOR / MINOR, with exact quotes and line references. If a
claim survives your attack, say so in one line. End with a one-line
overall verdict.

## Files

- docs/FREE_STAGGERED_3PLUS1_REFLECTED_GRAM_EXTENSION_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-07-24.md  (under review)
- scripts/free_staggered_3plus1_reflected_gram_extension_boundaries_2026_07_24.py  (its runner)
- docs/FREE_STAGGERED_3PLUS1_REFLECTED_GRAM_CAR_FOCK_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-07-12.md  (the landed theorem whose boundaries these are — and which this note CORRECTS)
- docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md
- docs/MICROCAUSALITY_CORNER_CLASS_FACTORIZATION_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-07-18.md
- docs/CORNER_TRANSFER_EXTENDS_TO_FIXED_GAUGE_BACKGROUNDS_BOUNDED_NOTE_2026-06-12.md

## The claims to attack

The note makes two corrections to a LANDED theorem and two new
statements. Correcting a landed note is a serious act; hold it to a
correspondingly high bar.

1. **(A3) THE CORRECTION.** It claims the landed note's generalization
   clause ("for a complex anti-Hermitian hop the same formulas hold
   with H replaced by conj(H) in the frames") is *incomplete*: it
   repairs the frames but not the transfer intertwiner, because T_2 is
   built from h and is not a frame. And it asserts the exact identity
   T_2[conj U] = T_2[U]^T. VERIFY THE IDENTITY YOURSELF from
   h^dag = -h. Then decide: is the landed clause genuinely incomplete,
   or is the note attacking a strawman reading of it? Read the landed
   clause in full context. If the landed note is fine as written, this
   is a BLOCKER.
2. **(A4) THE NEW HYPOTHESIS.** It claims static links are NECESSARY
   and that reflection positivity fails outright otherwise, gated by a
   chain-inverse instance with a negative eigenvalue. Attack: is the
   runner's reflected reading (gate A4, the `chain_inverse_block`
   function) actually the landed note's reflected Gram, or a different
   object that merely resembles it? If the reading is the note's own
   invention, the "necessity" claim does not bear on the landed
   construction and must be rescoped. This is the gate I most suspect.
3. **(B1) PSD on the full algebra**, via an explicit anticommuting-ring
   computation of -S_seam = sum Theta(u)u. Check the Grassmann
   implementation (`gmul` sign bookkeeping, the Theta action on barred
   fields, the 1/2 vs (1/sqrt2)^2 coefficient) and whether the gate
   proves what the prose claims. Does a seam factorization on ONE bond
   actually establish PSD of the whole Gram, or is that a leap?
4. **(B2) The representation obstruction** — that the full-algebra OS
   quotient has dimension 4^|Lambda| (Hilbert-Schmidt operators on
   Fock), so the landed Wick-determinant/exterior identification is
   FALSE there. Attack: gate B2 checks 4^L = (2^L)^2 and 64 != 8,
   which is arithmetic. Where is the actual evidence that the quotient
   dimension IS 4^|Lambda|? Is the prose claim supported by any gate at
   all, or is the arithmetic gate a fig leaf? Be blunt about this.

## Also check

- Every gate A1..B2: does the checked statement match the prose? Any
  tautology, self-subtraction, or vacuous quantifier? (Two gates were
  already rebuilt after the author found exactly those defects — look
  for more.)
- Needles N1-N5: do the quoted strings exist and MEAN what the note
  uses them for? N1 quotes the landed clause the note corrects —
  verify the quote is complete and not truncated to change its sense.
- Scope hygiene: the note disclaims U-integration, interacting
  transfers, continuum limit, and flags a "multi-mode vs one-mode
  Gaussian kernel" gap as open. Is that disclaimer adequate, or does
  some sentence still implicitly claim the fixed-background
  identification is complete?
- Does the note anywhere set or predict an audit verdict? Any new
  vocabulary? Frontmatter deps complete and correctly slugged?
