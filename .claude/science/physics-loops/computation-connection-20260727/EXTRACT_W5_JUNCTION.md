# W4/W5 junction extract — can the Cycle-741 archive feed the Cycle-693 Record readout?

This is a bounded extraction from exactly the three authorized files. Line
references use `path:line-line`. Cycle 741 is read as construction data only;
it was not run.

## 1. Cycle-693 input interface

### The theorem-level interface

The landed Record surface does **not** consume a fixed-width register. Its
general input is a finite pairwise-disjoint collection \(S\) of record
instances:

- a set `R` of possible record instances;
- a supplied content map `c:R -> O`;
- the realized singleton-content set `O_real`;
- a supplied additive scalar group `G`; and
- a content-determined scalar map `I` on finite pairwise-disjoint collections,
  with finite additivity and `I(empty)=0`.

These objects and their supply status are stated at
`docs/PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md:51-55`;
the singleton constructor and factorization are
`f(o)=I({r})` and
`I(S)=sum_{r in S} f(c(r))` at
`docs/PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md:57-66`.
The note explicitly says that `G` and `O_real` are supplied
(`docs/PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md:68-73`).

### The executable interfaces

Cycle 693 contains two finite executable realizations, neither of which is a
909-site register interface.

1. **Eight-coordinate clause fixture.** There are three record identities,
   indexed by the bits of masks `0..7`; identities 0 and 1 have content `"a"`
   and identity 2 has content `"b"`
   (`scripts/physical_record_readout_carrier_three_way_split_cycle693_2026_07_25.py:56-68`).
   A candidate readout is therefore an eight-entry
   `tuple[F, ...]`, one value for every subset mask. The empty coordinate,
   equal-content singleton equality, and disjoint-union additivity are tested
   directly
   (`scripts/physical_record_readout_carrier_three_way_split_cycle693_2026_07_25.py:71-83`).
   This fixture has two independent singleton weights
   (`scripts/physical_record_readout_carrier_three_way_split_cycle693_2026_07_25.py:86-91`).

2. **Concrete one-site \(M_2\) carrier.** The exact constructors are
   `Matrix = tuple[F,F,F,F]`,
   `Record(site: tuple[int,int,int], content: Matrix)`, and
   `record_readout(records: tuple[Record,...]) -> F`
   (`scripts/physical_record_readout_carrier_three_way_split_cycle693_2026_07_25.py:155-182`).
   Thus each executable record has one three-dimensional lattice site and one
   four-scalar \(2\times2\) matrix content; the input collection has arbitrary
   finite length; and this particular readout returns the sum of matrix traces.
   The tested family constructs 21 records, at `(3*index,0,0)`, with contents
   `(F(value),0,0,0)` for `value=-10,...,10`
   (`scripts/physical_record_readout_carrier_three_way_split_cycle693_2026_07_25.py:313-320`).
   The empty tuple, a disjoint split, and two equal-content/different-site
   singletons are checked at
   `scripts/physical_record_readout_carrier_three_way_split_cycle693_2026_07_25.py:331-352`.

The concrete countermodel declares/supplies the \(\mathbb Z^3\) lattice,
one-site \(M_2(\mathbb C)\), and a six-neighbor parity-dependent admissibility
rule (`docs/PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md:84-96`);
the Python realization represents the tested matrix subset over exact
`Fraction`s and takes six occupancy bits
(`scripts/physical_record_readout_carrier_three_way_split_cycle693_2026_07_25.py:155-168`).
The three-entry `Vector` in the runner is the later product
non-uniqueness fixture, not the Record input
(`scripts/physical_record_readout_carrier_three_way_split_cycle693_2026_07_25.py:155-156,185-199`).

## 2. Honest scope and firewalls

The note's claim boundary, verbatim, is:

> Record supplies the singleton-weight factorization of each finite additive
> content readout. It does not, by that fact alone, supply the parent's finite
> alphabet, complex scalar codomain/full operational carrier, or physical
> event-algebra identification. The original repair instruction remains open,
> but its carrier residual can be narrowed to those explicit structures rather
> than the additive factorization itself.

Evidence:
`docs/PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md:132-139`.

What is derived is only the unique singleton-weight factorization after
content determinacy, finite additivity, the empty value, `G`, and `O_real` are
in place. What remains supplied is the possible-record/content interface
`R,c,O_real`, the additive scalar group `G`, and any claim that the
mathematical rules are physically available. In particular, Record does not
choose `G=C`, complex-linear operational closure, or a product
(`docs/PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md:110-130`).

Two junction firewalls matter:

- **Record permanence is not an output of Cycle 693.** In the infinite-content
  countermodel, the records are allowed to “lock those contents, remain
  permanent” before the readout is applied
  (`docs/PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md:93-103`).
  The additive proof begins with possible record instances and a content map;
  it does not turn a reversible storage site into a permanent Record. A W5
  bridge therefore may not take archive permanence from Cycle 693 as a
  premise.

- **`C_source` is not supplied by the landed surface.** That name does not
  occur in any of the three authorized files. The only declared source/content
  interface on the Record side is `c:R -> O`
  (`docs/PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md:51-54`).
  Any W5 `C_source` that decodes an archive site, packet, or image into `O`
  must therefore be an explicit junction convention or a separately derived
  physical decoder, not something attributed to Record.

The general firewalls are also explicit: no dynamics, probability,
measurement rule, context selector, or physical carrier identification; no
identification of local \(M_2(\mathbb C)\) multiplication with multiplication
of readout rules; and no promotion of the mathematical rule class to a
physically available observable algebra
(`docs/PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md:141-150`).

## 3. Cycle-741 archive shape and the embedding

### Exact register schema

Cycle 741 supplies one initially blank finite archive, with three slots and no
new blank inventory between renewals
(`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:2-13`).
Its constructors are:

```text
FIXTURE_BANKS = 2
MATTER_WIRES = range(SOURCE_WIDTH)
BANK_WIRES = bank 0's complete N-wire interval
             followed by bank 1's complete N-wire interval
RECORD_WIRES = MATTER_WIRES + BANK_WIRES
RECORD_WIDTH = len(RECORD_WIRES) = 303
ARCHIVE_SLOTS = 3
ARCHIVE_WIDTH = 3 * RECORD_WIDTH = 909
slot(s,j) = DATA_WIDTH + 303*s + j,  s=0,1,2, j=0,...,302
```

The symbolic constructors are at
`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:35-57`; the
declared numeric supply is “one initially blank finite 909-M2 archive
register containing three 303-bit image slots” at
`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:1196-1205`
(also `scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:919-935`).
Each slot is exactly
`tuple(data[wire] for wire in RECORD_WIRES)`
(`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:89-90`), not
the whole operating state: links and all non-`RECORD_WIRES` operating wires
are excluded.

The four stored packet payloads in each 303-site image occur in the exact
decoder order

```text
(bank 0, cell 0), (bank 0, cell 1),
(bank 1, cell 0), (bank 1, cell 1),
```

because `cell_payloads` iterates banks outermost and cells innermost, selecting
`K.A.cell(cell)["payload"]`
(`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:93-100`), and
the file states that both banks have two payload cells
(`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:568-573`).
The authorized file does not materialize the numerical payload-width or
within-bank payload offsets: those remain symbolic imported `K.A.cell(...)`
data. It does, however, pin their order and their containment in the two
complete bank images.

The raw slot carries more than four payload subtuples: it carries all source
matter wires and all wires of both banks. Named source/bank state fields used
by Cycle 741 include `SOURCE_POINTER`, `POINTER`, `U_TO_V`, `V_TO_U`,
`DIRECTION_OK`, `FRESH`, `ZERO_WORK`, and `TOKEN_OK`
(`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:103-127`).
Cycle 741 checks those transient issues are absent in its exhausted clean
image (`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:548-557`;
the enforced check is
`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:1092-1098`).
Generation number, direction schedule, digests, and ordering checks exist in
the Python report row, not as separately identified in-register tag fields
(`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:693-710`).

Renewal shifts slots 1 to 2 and 0 to 1, then deposits the operating
`RECORD_WIRES` into slot 0
(`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:624-637`).
Therefore slot 0 is newest, and after three renewals the slots are the three
images in newest-first order
(`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:674-712,752-760`).

Physically, if `data_sites[w]=(x_w,y_w,z_w)`, archive site `(s,j)` is placed at

```text
(x_w, y_w + 11*(s+1), z_w), where w = RECORD_WIRES[j].
```

This is the literal constructor at
`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:1019-1030`;
the physical certificate calls all 909 positions \(M_2\) sites and reports the
layer translation `(0,11,0)`
(`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:1051-1056`).

### Embedding verdict

**Yes at the site-shape level, but only with an explicit content-encoding
declaration; no lawful Record identification follows yet.**

The exact direct schema is, for every `s=0,1,2` and `j=0,...,302`,

```text
w := RECORD_WIRES[j]
p := (data_sites[w].x, data_sites[w].y + 11*(s+1), data_sites[w].z)
b := archives[s][j]
E(s,j) := Record(site=p, content=(F(b),F(0),F(0),F(0)))
E(archive) := tuple(E(s,j) in lexicographic (s,j) order)
```

The choice `b -> diag(b,0)` matches Cycle 693's concrete matrix tuple and its
tested `diag(value,0)` constructor
(`scripts/physical_record_readout_carrier_three_way_split_cycle693_2026_07_25.py:171-182,313-320`).
It turns the 909-site archive into a 909-element finite
`tuple[Record,...]`. The Cycle-741 placement constructor supplies the sites,
and the Cycle-693 constructor supplies the target shape.

However, Cycle 741 represents the semantic register as integer bits
(`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:640-660`) and
never declares that its physical bit states have Cycle 693 content
`diag(b,0)`. The injection above is therefore a needed junction convention,
not a derived identity. Also, a four-payload or one-image **aggregate** cannot
be fed as one Cycle-693 `Record` without an additional packing/decoding map:
one Cycle-693 record has one four-scalar \(M_2\) content, whereas each payload
and each 303-site image is a multi-bit object. The direct shape-compatible
embedding is site-by-site; preserving packet/image semantics requires
`C_source` plus provenance/grouping metadata.

## 4. What a Cycle-742 junction must declare and derive

### Must be declared

1. **Record granularity:** whether each archive \(M_2\) site is a record
   instance (the direct 909-record embedding), or whether packets/images are
   intended as record instances. The latter choices need a new aggregate
   content carrier.
2. **Physical content encoding:** the injection from Cycle-741 wire values to
   Cycle-693 matrix contents, for example
   `0 -> diag(0,0)`, `1 -> diag(1,0)`, and the resulting equality convention
   in `O_real`.
3. **`C_source`:** an exact, total map from raw slot sites and/or the four
   decoded payloads, including any source/bank metadata used, to Record content
   `O`. It must state whether site location, slot age, generation, direction,
   and packet provenance are content or non-content.
4. **Collection convention:** which sites count as records (all 909 sites,
   only occupied cells, or decoded packets), how record identity is tracked
   when renewal shifts a byte to another physical slot, and what the empty
   collection means.
5. **Scalar/readout supply:** the additive group `G` and either a particular
   singleton-weight function `f` or the explicitly mathematical class of all
   such functions. `G=C` and physical availability may not be inferred.
6. **Bounded domain:** exactly three archived exhausted images, four packets
   per image, the stated newest-first ordering, and only the continuations
   actually checked. Cycle 741 explicitly makes no fourth-renewal claim
   (`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:769-772`).

### Must be derived/verified by the runner

1. A dimension and layout certificate:
   `3*303=909`, exact `(s,j)<->wire<->site` bijection, no placement collision,
   and pairwise-distinct one-site supports. Cycle 741 checks zero placement and
   routing failures
   (`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:1188-1194`).
2. Byte-exact archive provenance: newest image deposited exactly, older images
   shifted exactly, every slot exact, and operating state restored. Those are
   the existing Cycle-741 postconditions
   (`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:804-858`),
   but 742 must connect them to its declared `C_source`.
3. Decode exactness for every archived slot: two banks, two cells per bank,
   four occupied payloads in the stated order, with required bank/source
   metadata valid. Hashes alone are not a decoder or a content map.
4. Record-clause exactness for the chosen instances: content equality is
   independent of site/slot/provenance; the readout is additive on every
   finite pairwise-disjoint collection in scope; and the empty value is zero.
   Cycle 693 can then supply the singleton-factorization conclusion rather
   than 742 assuming it.
5. **A derived persistence/locking certificate, not a Record-permanence
   premise.** Cycle 741 establishes that the final archive is unchanged by one
   tested continuation
   (`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:759-762`),
   but its renewal word deliberately moves prior slot contents
   (`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:624-637`)
   and the archive is full after the bounded run. A lawful Record claim needs
   an invariant showing that a locked record's content cannot be changed by
   every future lawful evolution in the claimed domain, or an explicit
   write-once locking construction that makes this true.
6. Negative controls should independently corrupt the bit-to-\(M_2\) map,
   payload grouping, slot provenance, one archive byte, and the persistence
   condition, and show that the corresponding certificate fails.

### Honest claim ceiling

Without the missing locking result, the strongest current claim is:

> Given the declared sitewise bit-to-\(M_2\) injection, `C_source`, collection
> convention, and additive group `G`, the three exact Cycle-741 archive images
> embed into a finite mathematical collection accepted by the *shape* of the
> Cycle-693 executable readout carrier; every readout satisfying `(D)+(A)+(Z)`
> on that declared finite collection factors uniquely through singleton
> content weights.

It may **not** say that the archive sites are permanent framework Records, that
Record derived `C_source`, that the readout family is physically available,
that `G=C`, that there is a physical event-algebra product, or that storage or
readout persists through a fourth renewal or unbounded future. This keeps the
Cycle-693 physical-carrier firewall
(`docs/PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md:75-78,141-150`)
and Cycle-741 finite-capacity boundary
(`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:1206-1226`).

## 5. Feasibility verdict

**NEEDS-NEW-MECHANISM — a derived write-once Record-locking/persistence
mechanism (or an invariant subspace theorem showing that locked archive
contents are untouched by every future lawful evolution in scope).**

The register sizes and a site-by-site constructor match now, and a 742 runner
could certify layout, byte provenance, decoding, content determinacy,
additivity, and the empty value after declaring the encoding, `C_source`, and
`G`. The go/no-go is nevertheless **no-go for “archive feeds Record lawfully”
from the landed surfaces alone**. The strongest reason is that Cycle 693 does
not derive Record permanence, while Cycle 741 proves only a finite,
actively-shifted three-slot archive plus one unchanged checked continuation.
Calling those sites permanent Records would put the missing conclusion back
in as a premise, contrary to W5 discipline.
