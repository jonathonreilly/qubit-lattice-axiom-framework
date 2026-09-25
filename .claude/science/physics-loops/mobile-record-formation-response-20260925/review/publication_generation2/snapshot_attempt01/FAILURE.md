# Preserved receipt-filename lookup failure

The first generation2 snapshot pass copied the eleven manifest-listed public files and six explicitly named external sources, then tried the abbreviated receipt name FORMATION_RESPONSE_GENERATION1_READONLY_RESULT.json. That path does not exist. The intended released root result is FORMATION_RESPONSE_GENERATION1_ROOT_READONLY_RESULT.json, found by a filename-only search restricted to FORMATION_RESPONSE_GENERATION1*.

No verifier or scientific program ran. The partial seventeen read-only snapshots were retained, checked again and reused; no previous packet was changed. The corrected continuation adds the intended root result and writes the source inventory. No scientific discrepancy is inferred from the filename failure.

The returned error was:

    Traceback (most recent call last):
      File "<stdin>", line 14, in <module>
      File "/opt/homebrew/Cellar/python@3.13/3.13.5/Frameworks/Python.framework/Versions/3.13/lib/python3.13/pathlib/_abc.py", line 625, in read_bytes
        with self.open(mode='rb') as f:
             ~~~~~~~~~^^^^^^^^^^^
      File "/opt/homebrew/Cellar/python@3.13/3.13.5/Frameworks/Python.framework/Versions/3.13/lib/python3.13/pathlib/_local.py", line 537, in open
        return io.open(self, mode, buffering, encoding, errors, newline)
               ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    FileNotFoundError: [Errno 2] No such file or directory: '/Users/jonreilly/Documents/Codex/physics-sync-2026-09-24-fifth/FORMATION_RESPONSE_GENERATION1_READONLY_RESULT.json'

No stdout was produced. A start timestamp and isolated elapsed time were not captured by this snapshot pass; neither is reconstructed.
