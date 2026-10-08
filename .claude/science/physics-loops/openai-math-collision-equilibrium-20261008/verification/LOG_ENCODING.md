# Raw log preservation

Logs with trailing whitespace are stored as .log.json. The stdout_and_stderr string preserves the complete original UTF-8 text, with its exact original hash in raw_sha256. This is reversible encoding for Git whitespace checks, not trimming or rewriting the output. Other logs are copied unchanged.
