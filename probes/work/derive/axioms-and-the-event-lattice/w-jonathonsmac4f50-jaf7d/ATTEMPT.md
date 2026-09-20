# axioms-and-the-event-lattice: derivation attempt 3 of 3

Worker `w-jonathonsmac4f50-jaf7d` (claude-opus-5), unit `J-derive-axioms-and-the-event-lattice-a3`.

**Provenance, stated because it bears on independence.** The prior attempt, `a1`
(`w-jonathonsmac4f50-j8065`), is by the same model family, machine and running worker. It reads
the axioms, builds the map the task asks for, cites 21 lines of
`docs/MINIMAL_AXIOMS_2026-06-29.md`, and verifies each against `origin/main`. I do not re-build
its map.

**What this attempt is.** For a **reading** task exactly two things can be wrong: the citations,
and the coverage. `a1` checks the first — its `check.py` pins each quote to a line. Nobody checks
the second. So this attempt scans the memo line by line and asks what a map of "what the axioms
say about the past of a record" ought to contain and does not.

Three passages are missing, and one of them changes the cost of the clause `a1` proposes.

## 1. The statements attempted

> **(i)** `a1`'s citations are sound: every quoted line I re-checked is verbatim at its cited
> line on `origin/main` (`b1cb232e68`).
>
> **(ii)** 57 lines of the memo carry the question's vocabulary; `a1` cites 21. Most of the rest
> are the change log and the policy rows. **Three are not**, and all three bear on the task.
>
> **(iii) `L166–168`** — *"Record names the fixed locking of one admissible local possibility,
> one-record-per-site uniqueness, permanence, content-determined readout, and the unreadability
> of a site with no record."* The memo states the permanence rule **twice**: at `L79–80`, which
> `a1` cites and proposes to change, and again here, in its own summary of what the Record axiom
> names. **`a1`'s clause therefore has to change two places, not one**, and an audit row citing
> `L166–168` would still read the old rule.
>
> **(iv) `L199–202`** — the 2026-07-04 history entry: the formation sentence "Records form." made
> *occurrence* axiom content "while every formation rule (which admissible possibility, at which
> site, with what weight, at what rate) at that time remained downstream supplier content." This
> is the same gate `a1` finds at `L183–184`, but it is the **history**, so a clause that moves
> the gate must amend it too or the memo contradicts itself about what 2026-07-04 decided.
>
> **(v) `L228–233`**, the memo's closing paragraph — *"The distribution's form and values,
> **dynamics**, readout contexts, and physical observable bridges remain downstream."* One word,
> and it is the task's question: **the predecessor structure of a record is dynamics**, so this
> is the memo's own, most direct statement that the axioms do not fix the past. The task's (c)
> is answered in the memo's last paragraph.

## 2. Steps

**S1 (CHECKED `T1`). The citations.** Eight of `a1`'s 21 lines re-fetched and compared verbatim;
all match. (I sampled rather than re-listing all 21, since `a1`'s own script checks them and the
point here is coverage.)

**S2 (CHECKED `T2`). The scan.** Every non-heading, non-table line of the memo is tested against
the question's vocabulary — record, past, predecessor, neighbour, formation, permanence, time,
clock, tick, dynamics, order, history, lattice, adjacency, causal. 57 hits, 40 uncited.

**S3 (CHECKED `T3`). The three.** Each is quoted exactly, joined across its lines, and compared
character for character with the file; and each is confirmed absent from `a1`'s cited set.

**S4 (`T4`). What they change.** As in (iii)–(v) above.

## 3. Where this stops

- **This is an audit of a map, not a second map.** `a1`'s structure — which predecessor
  structures the text permits, which it excludes, and the clause it would take — stands; I found
  nothing wrong in it, only three things absent.
- **The scan is vocabulary-based.** A sentence that constrains the past without using any of the
  listed words would not be found. Having read the memo, I do not think there is one, but the
  check cannot say that.
- **Only `MINIMAL_AXIOMS_2026-06-29.md`.** `a1` also cites the primitive notes and the policy;
  their coverage is not audited here, and the same question could be asked of each.
- **(v) is a reading of one word.** "Dynamics" is not defined in the memo, and a reader who takes
  it to mean only the *distribution's* time-dependence, not the predecessor structure, would not
  draw the same conclusion. That reading is worth stating either way, because it is the sentence
  a lane would cite.

## 4. What would finish it

1. `a1`'s clause proposal should carry both locations (`L79–80` and `L166–168`) and note the
   history entry at `L199–202`.
2. The same coverage audit for the primitive notes `a1` cites.
3. If the owner ever fixes the past, `L228–233` is the sentence that has to lose the word
   "dynamics" — which is the cheapest possible statement of what the change costs, and the kind
   of one-line insight the repository's axiom-update criterion asks for.

## 5. Running it

```
python3 probes/work/derive/axioms-and-the-event-lattice/w-jonathonsmac4f50-jaf7d/check.py
```
from the repository root; it fetches `origin/main`. Standard library only, a few seconds.
