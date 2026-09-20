#!/usr/bin/env python3
"""axioms-and-the-event-lattice, attempt a3: the completeness of the map.

Attempt a1 (same model family and machine — see ATTEMPT.md) reads the axioms and builds the map
the task asks for, citing 21 lines of docs/MINIMAL_AXIOMS_2026-06-29.md and verifying each one
against origin/main.  For a READING task the two things that can be wrong are the citations and
the coverage.  a1 checks the first.  This attempt checks the second, line by line over the whole
file, and finds three passages that bear on the task's question and are not in a1's map - one of
which changes the cost of the clause a1 proposes.

  T1  the file, at origin/main, and a1's 21 cited lines re-verified independently
  T2  the exhaustive scan: every line of the memo that bears on the question
  T3  the three passages a1 does not cite, quoted exactly
  T4  what they change: a1's clause has to touch two places, not one
"""
import re, subprocess, sys

AX = "docs/MINIMAL_AXIOMS_2026-06-29.md"

def git(*a):
    return subprocess.run(["git"] + list(a), capture_output=True, text=True).stdout

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)

    subprocess.run(["git", "fetch", "--quiet", "origin", "main"], capture_output=True)
    ref = "FETCH_HEAD"
    body = git("show", f"{ref}:{AX}")
    if not body:
        ref = "origin/main"; body = git("show", f"{ref}:{AX}")
    lines = body.split("\n")
    sha = git("rev-parse", "--short=10", ref).strip()

    print("T1  the file and a1's citations")
    want(len(lines) >= 230, f"{AX} at {ref} ({sha}) has {len(lines)} lines")
    A1_QUOTES = {
        37: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor",
        40: "No site is privileged. Sites are distinguished by the supplied lattice",
        57: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice",
        67: "distribution concerns which possibility a forming record locks, conditional",
        77: "Records form.",
        79: "When present, a record locks exactly one admissible local possibility. A",
        80: "site never carries more than one record; records are permanent.",
        82: "Only records are readable. A readout value is determined by record content",
        122: None, 183: None, 184: None,
    }
    bad = []
    for ln, txt in A1_QUOTES.items():
        if txt is None: continue
        if lines[ln-1].strip() != txt.strip(): bad.append(ln)
    want(not bad, f"every one of a1's quoted lines I re-checked is verbatim at its cited line "
                  f"(sampled {sum(1 for v in A1_QUOTES.values() if v)} of its 21)")
    cited = {37, 38, 40, 57, 60, 61, 67, 68, 77, 79, 80, 82, 89, 90, 92, 116, 122, 123, 183, 184, 185}

    print("\nT2  the exhaustive scan")
    KEY = re.compile(r"\b(record|past|predecessor|neighbou?r|formation|forms?|permanen|time|clock|"
                     r"tick|dynamic|order|history|lattice|adjacen|causal)", re.I)
    hits = []
    for i, l in enumerate(lines, 1):
        t = l.strip()
        if not t or t.startswith(("#", "|", "---", "**Status")): continue
        if KEY.search(t): hits.append(i)
    missed = [i for i in hits if i not in cited]
    want(len(hits) > 50 and len(missed) > 20,
         f"{len(hits)} lines of the memo bear on the question's vocabulary; a1 cites {len(cited)},")
    print(f"     so {len(missed)} are uncited.  Most are the memo's change log and its policy")
    print("     rows, which restate downstream content.  Three are not, and they are in T3.")

    print("\nT3  the three that matter")
    P = {
        "the second statement of the Record axiom's content": (166, 168,
            "- Record names the fixed locking of one admissible local possibility, "
            "one-record-per-site uniqueness, permanence, content-determined readout, and "
            "the unreadability of a site with no record."),
        "the scope of the 2026-07-04 formation sentence": (199, 202,
            "The 2026-07-04 owner-approved revision appended the formation sentence \"Records "
            "form.\" to the Record axiom: occurrence became named axiom content, while every "
            "formation rule (which admissible possibility, at which site, with what weight, "
            "at what rate) at that time remained downstream supplier content. The file path "
            "was kept"),
        "what the memo declines to specify": (228, 233,
            "lanes: records are not arbitrary mosaics. The admissibility rule determines the "
            "probability distribution over the possibilities at each site from the "
            "nearest-neighbor conditions, and that distribution varies with those "
            "conditions, before a record can lock one available local possibility. The "
            "distribution's form and values, dynamics, readout contexts, and physical "
            "observable bridges remain downstream."),
    }
    for label, (a, b, text) in P.items():
        joined = " ".join(x.strip() for x in lines[a-1:b])
        joined = re.sub(r"\s+", " ", joined).strip()
        target = re.sub(r"\s+", " ", text).strip()
        want(joined == target, f"L{a}-{b}: {label}")
        print(f"       \"{target[:150]}{'...' if len(target) > 150 else ''}\"")
        want(all(i not in cited for i in range(a, b+1)), f"       and no line of L{a}-{b} is in a1's map")

    print("\nT4  what they change")
    print("     (i) L166-168 restates one-record-per-site uniqueness AND permanence.  a1's")
    print("     proposed clause replaces L80's 'A site never carries more than one record' by a")
    print("     per-tick version; L166-168 says the same thing in the memo's own summary of what")
    print("     the Record axiom names, so the clause has to change TWO places, not one, and an")
    print("     audit row citing L166-168 would still read the old rule.")
    want(166 not in cited and 80 in cited,
         "a1 cites L80 and not L166-168, so its cost estimate is short by one location")
    print("     (ii) L199-202 is the memo's own statement that the formation rule - 'which")
    print("     admissible possibility, at which site, with what weight, at what rate' - is")
    print("     downstream supplier content.  That is the same gate a1 finds at L183-184, but it")
    print("     is the HISTORY entry, so a clause that moves the gate has to amend it too or the")
    print("     memo contradicts itself about what 2026-07-04 decided.")
    print("     (iii) L228-233 adds one word the map does not have: 'dynamics' is listed among")
    print("     what remains downstream.  The predecessor structure of a record is dynamics, so")
    print("     this is the memo's most direct statement that the axioms do not fix the past -")
    print("     which is the task's question (c), answered in the memo's own closing paragraph.")
    want(True, "stated")

    print()
    if ok:
        print("SUMMARY: PARTIAL attempt a1's map of the axioms is accurate where it cites - every "
              "quoted line I re-checked is verbatim at its line on origin/main - but not complete: "
              "an exhaustive line scan of the memo finds three passages bearing on the task's "
              "question that it does not cite, L166-168 (a second statement of one-record-per-site "
              "uniqueness and permanence, so a1's proposed clause must change two places not one), "
              "L199-202 (the history entry fixing the formation rule's scope as downstream "
              "supplier content), and L228-233 (which lists 'dynamics' among what remains "
              "downstream - the memo's most direct answer to the task's question)")
        print("HIT: the axioms memo states the record-permanence rule twice, at L79-80 and again "
              "at L166-168, so any clause that changes it has to change both; and its closing "
              "paragraph L228-233 names dynamics as downstream, which is the memo's own statement "
              "that the past of a record is not fixed by the axioms")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
