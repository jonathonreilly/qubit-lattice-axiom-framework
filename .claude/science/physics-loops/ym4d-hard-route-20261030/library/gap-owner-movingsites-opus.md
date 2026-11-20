lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T00:34Z

# gap-owner-movingsites-opus: moving sites, sliding blocks and the mass gap

Queue row 1274 of `FINISH.md`, run on the Mac mini Claude worker 3 at commit fa2cf667b,
started 2026-11-20T12:34Z (date -u). Claude Opus 5.5, max effort.

Status of this file: in progress. Each section is appended as a step finishes.
Labels: PROVED, ARGUED, GUIDE, OPEN, as the row asks.

## 0. Task as read

The problem (row 1274): prove that four-dimensional SU(2) Yang-Mills theory has a mass gap
in the sense of Jaffe and Witten. The owner's hint (2026-11-20): "anything to the sites
themselves moving between lattice nodes in some interesting way?" Forms named in the row:
sliding or sheared blocks, shifted or translation-twisted boundary conditions, lattice
dislocations, comparisons with moved or random lattices. The record has only lattice
translations as a symmetry group (row 1201, no stiffness).


## 1. Repo search (12:34Z-13:05Z)

Read: `GOAL.md`; `FINISH.md` L1-84, L299-356 and rows 1201, 1218, 1258-1260, 1264-1275 (RESULT lines);
`parts/gap.md` L1-105; `library/gap-crux-restate.md` Sections 1-3.4 (setting, C1-C5, Theorem D, Theorem S);
`library/gap-mini-solve-k-fable.md` (row 1201, all); `library/gap-constraints-max.md` A4 (L185-198) and 7.4
(L411-440) (row 962); `library/gap-solve9-astra62.md` L42-75 (row 1161, fractional momentum);
`library/gap-mini-neutral2-fable.md` L60-80, L160-175 (the statement of (N-phys)).
Grepped `library/`, `library/prior/`, `parts/gap.md`, `FINISH.md` for each moving form.

The crux as I use it below (cited, not re-derived). Engine: Theorem S (row 697, checked rows 698-699): on
periodic tori one seed S(n; (2n)^3) < 1/5041 gives a uniform gap on all larger cubes, for every group. Open
content: the neutral premise (N-phys) (row 1161 L146-148; row 1184 L66-70): a physical side L and, at every fine
cutoff, a time u <= n/K with neutral excited trace s(u; n^3) <= 1/2. Row 1184 reads it as "the neutral gap of one
physical cube, in units of its inverse side, passes a threshold" between about K log 2 and 2K log(2 S_0); a free
massless field has the value 2 pi at every size. Row 1258 gives the one-coupling forms (SL)/(RR). The flux half (BS)
is a separate item.

### 1.1 Moving forms against the record

| Form | On file | What is there | Verdict on file |
|---|---|---|---|
| Sheared tori, translation-twisted periodic conditions, Tr(T^a tau_v) | row 962 A4 and 7.4 (`gap-constraints-max.md` L185-198, L411-440): Lemma SHIFT, projected doubling, projected crossing identity; row 1066 Lemma FR and I9 (`gap-outside-box-max.md` L113-120, L172, L190) | exact identities | blind; "changes a constant, not the crux" |
| Rotated and diagonal tori, boxes rotating in time | row 963 (`gap-rotgeom-opus.md` Lemmas R2, R3, D2) | diagonal tori are sheared axis tori | buy nothing for the seed |
| The symmetry group of the box (translations and signed permutations) as a rigid group | row 1201 Lemma G1 (`gap-mini-solve-k-fable.md` L64-91) | invariant and charged sums as group averages of twisted traces | no stiffness: a uniform displacement is removed by pulling back the field; reduces to routes RA and RB |
| Translations with a centre twist (compensated translations, fractional momentum) | row 1161 (`gap-solve9-astra62.md` L42-75); check `gap-channel-check-opus.md` L48 | D_i^(n_i) = -I in sectors with Mq != 0; even multiplicities; 42 sectors bounded | flux half only; the neutral sector q = 0, m = 0 is untouched |
| Twist weights under changes of basis (the modular group on twists) | row 1161 (same file, after L64) | near invariance of f_Q(B) under rank-preserving changes | flux half |
| Bond moving (Migdal-Kadanoff, Tomboulis decimation) | row 876 item 16; `gap-cr-tomboulis-max.md` 7.2 (Proposition SIGN) | bond moving bounds Z, not the twist ratio | no sign on the twist quotient (PROVED there for Z_2) |
| Dislocations (sliding blocks with a mismatch) | not as a moving form; "lattice dislocations" occur only as small-action instanton lumps (row 1013 K8, `gap-invent-selective-max.md` L258; row 1200, `gap-mini-solve-j-fable.md` L184-185) | - | NEW as a moving form |
| Moved lattices (offset against the continuum) and random lattices (Christ, Friedberg and Lee) | no hit for "random lattice", "Voronoi", "moved lattice" outside this item | - | NEW |
| Rotation of sites about a codimension-2 axis (corner transfer matrix, branched covers) | no hit for "branched cover", "disclination", "corner transfer"; "replica" hits are two-replica couplings (methods 34, 35) | - | NEW |
| Translations traded for colour (twist eaters, Eguchi-Kawai reduction) | twist eaters in 20 files (Fact T, C5, rows 930-938, 1200); Eguchi-Kawai in 6 files (`gap-lit-xvol.md` and others) | small-volume and large-N statements | flux half and small volume |

`library/open-core.md` holds the existence chain; grep for "dislocation", "shear", "random lattice", "branched"
there: no hit. So the new forms for this row are: dislocations (sliding blocks with a mismatch), moved and random
lattices, and rotation of sites about a codimension-2 axis.

### 1.2 What a moving form must do to matter (GUIDE; a reading of the record)

The record fixes two tests (parts/gap.md L36-50, row 998 6b; row 1201 Section 2.1):

- (SEL) The input must be selective. It must be false for compact U(1) at weak coupling (a massless photon,
  Guth; Frohlich and Spencer), for the free Maxwell field, for products with a massless factor, and for frozen
  groups in the periodic form. A statement that every compact group satisfies cannot give the seed.
- (NEU) The open premise (N-phys) is about the centre-neutral sector. The states it must exclude at one
  physical size are zero-momentum scalars (row 1201 Section 3.2): states of a one-dimensional representation of
  the box symmetry group.

A moving form can matter in two ways only: as a selective input that reaches the neutral sector, or as an engine
that lowers the seed threshold to a size where a provable input (asymptotic freedom at small coupling) holds.
Sections 2-5 test each new form against both.
