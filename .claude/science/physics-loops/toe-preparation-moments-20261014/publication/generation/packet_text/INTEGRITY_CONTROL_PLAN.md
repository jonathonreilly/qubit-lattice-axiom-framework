# Proposed root-only corruption controls

These fixtures are a plan, not an execution claim. Apply each independently to a disposable copy after root accepts the complete primary helper and its inputs. Preserve every original, mutant, command, stdout, stderr and exit code. A rejection is an integrity discriminator only, never a mathematical falsification test.

| Integrity family | Selected mutation and expected failure |
|---|---|
| Fixed manifest anchor | Change one byte in IDENTITY_INPUTS.json; reject its literal SHA pin. |
| Primary input drift | Change one byte in the canonical note while retaining its manifest; reject the note identity. |
| Full proof mapping | With the manifest/anchor consistently regenerated in a disposable source derivative, move a body endpoint by one byte; reject exact body hash/line/EOF or note reconstruction. This is a deeper structural control than the ordinary outer hash check. |
| Archive object/recipe | With disposable outer pins regenerated consistently, truncate an object or redirect a recipe to a different content address; reject decompression/content identity or full logical reconstruction. |
| Whole accepted source closure | With disposable outer pins regenerated, omit one group member record; reject frozen exact membership. |
| Canonical parent | Change the supplied canonical parent byte at the unchanged raw be8 interval; reject its input identity and exact historical comparison. |
| Declared read closure | In a disposable helper derivative, remove one consumed input declaration; reject undeclared read/closure. |

Root may use fewer structurally redundant outer-hash mutations but must preserve at least one actual countercheck for each distinct changed check family it relies on. This packet supplies no claim that these future helper fixtures have run. The accepted mathematical controls remain separately archived and are not replayed for packaging.
