# Periodic matching geometry and residual-charge review

2026-09-21. Bounded independent scientific review of the two frozen supplied
notes. This is not a production-simulator review, an audit verdict, or a phase
or wave result. No primary file, Git state, or prior sealed evidence was changed.

**Result:** the periodic jam, local escape, count-parity obstruction, and
Hermitian Fourier bound check under their stated hypotheses. One activity
scope clarification is required for the named pilot endpoint: it is frozen
in readable contents, but not in identities if the optional identity-only
swap channels are retained. The displayed mathematics needs no correction.

## Finding and narrow correction

**F1 — distinguish projected activity from identity transport.** In
`PAIRED_RECORD_PARITY_AND_RESIDUAL_VACANCIES.md`, lines 47–55, the sentence
saying `N4_jam_extended_s21092102` has “no enabled event” needs the qualifier
**“no content-changing event in the projected content process.”** The periodic
note explicitly permits either retaining or omitting identity-only swaps.
These two conventions cannot share an unqualified identity-level jamming claim.

Direct enumeration from the preserved final state gives:

| Channel family | Content-changing exits |
|---|---:|
| Paired births | 0 |
| Original dimer translations | 0 |
| Original full-cube exchanges | 0 |
| Added parallel swaps | 0 |

There are nevertheless **115 accepted identity-changing parallel-swap
attempts**, counted with the supplied per-cube channel multiplicities.
For example, the two sites `(0,0,2)` and `(0,1,2)` both contain `+x` records.
Swapping those distinct identities is one allowed single-edge channel; all
contents and reciprocal matching relations stay unchanged. Thus its positive
identity-level rate is present when those optional moves are retained.

The final counts `(12,10,9)` and their parity `(0,0,1)` are correct. The all-odd
two-vacancy obstruction does not explain this projected jam, exactly as the
note says. `zero_active_rate` in the parity output should be understood as the
projected activity flag used for those stored endpoints. A short explicit
scope statement in the paragraph/output documentation suffices; no simulation
rerun or theorem change is needed. This finding was sent to the parent author.

**Optional precision:** name the **squared longitudinal norm** in the
two-vacancy `O(N^-1)` sentence after equation (2). Equation (2) itself is right.
The norm can be order `N^-1/2`; the independent sharpness control below rules
out reading that sentence as an `O(N^-1)` amplitude estimate.

## Independent mathematical reconstruction

On every even periodic side `N>=4`, the vacancies of the period-two pattern
are precisely the parity classes `000` and `111`. They are not nearest
neighbors. Each dimer's axial line is fully occupied because its two other
coordinate parities differ. Hence an axial translation cannot acquire its
new empty endpoint. A transverse translation would need an adjacent vacant
pair. Every unit cube contains both vacant parity classes, preventing the
original full-cube exchange. These exhaust the original generator's exits.

The pattern can be formed on a finite torus by creating its disjoint dimers
in a specified order, before any competing effective move. Every requested
birth is enabled and has positive rate; competing total rates are finite.
This finite sequence therefore has positive probability. It disproves
almost-sure full packing for that original finite process, without giving
a lower probability bound uniform in volume or a typical-density statement.
The uniform translation/proper-rotation orbit mixture is an absorbing
symmetry-invariant law. Its vacancy covariance at every even displacement
is `3/16`, so it has periodic long-range order; this is not a formation-selected
or ergodic phase.

For a reflecting cube with one dimer per axis, each coordinate cut has exactly
one crossing dimer. Each face then has an odd number of holes. With only two
holes, there is one per face in every direction; they are opposite corners.
This proof applies to every confined count-preserving rearrangement, not just
the original available moves.

The new family has `3(2^4-1)=45` attempted channels per cube. Each is a product
of disjoint nearest-neighbor transpositions and is its own inverse. Global
matching acceptance is symmetric between its two valid endpoints. Equal rates
therefore give detailed balance for finite uniform matching laws, including
their invariant count sectors. Duplicate channel representations retain this
property. Translation/cubic transformations permute the channel multiset and
preserve reciprocity. Acceptance only needs changed sites and their neighbors;
the update support and the decision's reading neighborhood are distinct.
An infinite “uniform law,” if used, needs its ordinary local conditional-uniform
interpretation; uniqueness or mixing is not a consequence of this argument.

The stated three simultaneous y-swaps move the z-pair from `010,011` to
`000,001` and the x-pair from `001,101` to `011,111`. Exactly four old identities
move one unit, the y-pair stays fixed, and all contents survive. The new hole
`010` is adjacent to the untouched neighboring hole `020`, enabling the stated
paired birth. The supplied construction and subsequent rebirth work on every
even `N>=4`. No general accessibility or all-jam repair follows.

The new family preserves individual contents and identities, but need not
preserve permanent partner identities: swapping equal-label records can change
their identity-labeled partners. The notes' acceptance condition uses readable
reciprocity and does not claim this stronger invariant. None is assumed here.

For direction counts, summing `x_i mod 2` over occupied sites modulo two gives
one from each i-dimer and zero from every other dimer. Summing over all sites
gives `N^3/2`, even for even N. Therefore

    M_i = sum_{x vacant} (x_i mod 2)  (mod 2).

With two holes and three odd counts, the holes differ in every coordinate
parity and cannot be adjacent. Any conservative content-preserving matching
rearrangement preserves that fact, however nonlocal. The last paired birth
is impossible, even if conservative activity continues. The given columnar
replacement is a valid configuration specification with counts
`(N^3/2-3,1,1)`; it is not an allowed conservative conversion of already formed
columnar identities. Its finite birth-only construction again has positive
probability. A single odd count is not a converse adjacency criterion.

Finally, let `n_i(x)` indicate a `+e_i` record at x. Integer real-space
reciprocity implies

    sum_i [B_i(x)-B_i(x-e_i)] = -sigma_x 1{x vacant},
    B_i(x)=sigma_x[n_i(x)-1/6].

For normalized Fourier components with phase `exp(-ik.x)`, the constraint is
`d.Bhat=qhat`, where `d_i=1-exp(-ik_i)`. Its Hermitian normal is `conjugate(d)`,
giving exactly

    Bhat_L = conjugate(d) qhat / ||d||^2,
    ||Bhat_L||^2 <= m^2 / [4 N^3 sum_i sin^2(k_i/2)].

At `k=K/N`, `K=2 pi ell != 0` fixed, the denominator is asymptotic to
`N|K|^2`; for `N>=2 max_i |ell_i|` it is at least `16 N|ell|^2`.
Thus the deterministic `m_N=o(sqrt(N))` and random `E m_N^2=o(N)` hypotheses
suffice exactly as stated, with no stationary or independence assumption.
The zero mode is excluded; fixed nonzero modes avoid small-volume aliasing
eventually. Finitely many fixed modes follow by summing the bounds.

This controls the discrete longitudinal projection. Obtaining a continuum
field distribution still needs tightness and a field-limit argument; no
transverse covariance or field-size bound is supplied by the vacancy estimate.

## Decisive controls and comparison coverage

The independent code was sealed before either author runner or its outputs
were opened. It uses record dictionaries and direct global reciprocity,
without importing the author implementation. Its first execution passed;
there were no failed attempts to discard.

- On `N=4,6,8`, it enumerates every original event and finds zero exits. It
  checks all identities in the escape/inverse/rebirth, with populations
  `48->50`, `162->164`, and `384->386` and unchanged old record contents.
- It enumerates all 108 reflecting-cube matchings; the eight with one dimer
  per axis all have opposite holes. It tests all 2880 attempted extension
  channels on five `N=4` configurations for accepted inverse and count
  preservation. On the all-odd constructed sector, three channels change
  contents, giving an independent nonfrozen obstruction example.
- It checks the complete channel multiset under all 48 signed coordinate
  permutations and three unit translations, including the claimed proper
  subgroup. Its 1920 distinct site permutations have multiplicities one,
  two, or four; an implementation must not silently discard those supplied
  per-cube clock multiplicities.
- An exact complex-mode control has `N=4`, `ell=(1,2,0)`,
  `d=(1+i,2,0)`, `q=(-1+i)/8`, and
  `Bhat=(-1/8,i/8,1/8)`. The squared longitudinal norm is `1/192`, below
  the bound `1/96`. Using `d` instead of its conjugate in the projector
  leaves residual `-i/12`, detecting that normalization/sign error.
- A valid two-hole sequence has holes separated by `L=N/2-1` along one
  coordinate for `N` divisible by four. At `K=2 pi e_x`,
  `N ||Bhat_L||^2 -> 1/pi^2`. Valid explicit matchings on `N=4,8,16,32`
  confirm the sharp squared-norm order. An excluded `N=5` wrapped-edge
  example demonstrates why the even-period parity hypothesis matters.

After this seal, both complete author runners, both result files, and both
logs were inspected. The periodic output's seven groups and saved tracked
displacements agree with the independent results. No author runner was executed
or imported, and no production simulator source was opened.

For the parity artifact, an independent FFT applied to the exact integer
field reproduces all **255** reported Fourier rows: five constructed sizes
and all **80** saved pilot/screen endpoint states. Every endpoint was checked
for label range, reciprocity, direction counts, coordinate parity, integer
Gauss identity, and agreement with the final CSV count fields. Maximum
power/bound discrepancy is `1.7053e-13`; maximum independent Fourier constraint
residual is `2.0935e-16`. These FFT comparisons are numerical checks; the parity
and real-space Gauss checks use exact integers.

For the **11** all-odd two-hole endpoints, independent event enumeration finds
a positive original translation or full-cube channel in every case. This
verifies the note's distinction between count obstruction and frozen readable
configuration without trusting the simulator's activity flag. The named pilot
was exhaustively checked for original exits and all added channels, yielding F1.
For other endpoints, activity flags were checked only as arithmetic on the
recorded metadata; their channel census was not independently reconstructed.

## Source identities, reproduction, and limits

The parent supplied raw commit `20fc8c7562`; no Git operation was used to
resolve it. The following complete source bytes were authenticated:

| Source | SHA-256 |
|---|---|
| Periodic note | `cf03eaff8ea4effc674881e5807fa3449b5211a487308360b0f0e448f19a0bdd` |
| Parity note | `fe6f9a4f71bdeac7f971b233ce6def6ef918bf29476ea4e48641a881f2ee8257` |
| Periodic runner | `51a31337880a4613ebfc2981100f821d5410bc8299c178c117141e52aa545e05` |
| Parity runner | `30e503d581e77469a83b4be031aa9c101379d8cc80f80c3b281e6b395e6b64ba` |
| Original paired-model note | `ed48192900501781ead6d60f17aedc1e9470746e65f449c5d75eccb6a66188ca` |
| Periodic results | `e291f3419a8f3eecf949f912c8a4cc61edefbcb296776243ef403822b9eebe33` |
| Periodic run log | `75fe1220e75592b80a276559ff0d44de864aea12d3725f46a8a401363b60fffd` |
| Parity results | `153bd4cb5fc5aefb1f13799f5e239169192cc0890b47433f20e188f264f9f94b` |
| Parity run log | `d18b6bde016aeaa9b7b3352071dd0c37efaf3999534feba6ef3cd11e78bd3488` |

`PRE_COMPARISON_SEAL.json` has SHA-256
`09996a94b28de3199d92157d2f0e4db9eb3e1c995e1bf9b733aed4200f794585`.
It preserves the independent derivation, checker, full logs, results and read
boundary. Its seven artifacts remain unchanged. Identity-matched prior paired
review and workflow dependencies are recorded there; no unrelated source or
literature was imported.

`INPUT_MANIFEST.json` has SHA-256
`87353004b9fcf6757e7cee4d65e371ff50c6bce9b585d5d78c46236b543ea43f`.
It binds all 171 post-seal inputs, including the 80 endpoint files and 80 CSVs.
CSV bytes were hashed completely, but only their header/final count fields
were evaluated; their trajectories and stochastic kinetics were not reviewed.
The author output binds its two source files; this manifest additionally
binds the actual data consumed in this independent comparison.

To reproduce without overwriting sealed artifacts, run `independent_check.py
--out <fresh-json-path>` and `compare_sources.py --out <fresh-existing-directory>`
inside this evidence directory. The comparison script checks the frozen source
identities, preserves the initial seal, and never executes author runners or
writes outside its specified output directory. Its full stdout/stderr and
receipt are `COMPARISON_RUN.*` and `COMPARISON_RECEIPT.json`.

No simulation generator, event-time law, kinetic scaling, mixing, general
accessibility, thermodynamic phase, Coulomb law, physical-field assignment,
quantum operation, or oscillatory wave claim was assessed or established.
The vacancy scaling remains a separate obligation. F1 is a scope correction;
there is no unresolved error in the displayed geometric or Fourier identities
within this review boundary. `FINAL_SEAL.json` binds this report and the complete
independent evidence at the frozen source identities.
