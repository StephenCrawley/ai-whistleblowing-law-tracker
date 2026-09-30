# How AI was used

What AI generated, what I changed and what I verified, for each piece of work.

| Work | AI generated | I changed | I verified |
|---|---|---|---|
| `data/schema.json` | Refinements to my draft | Drafted it by hand | That yamls conform to schema with test fixtures |
| `pipeline/validate_schema.py` + fixtures | Guidance on approach; the test fixtures | Wrote the script myself | Passes the valid fixture, fails the invalid one and an empty directory |
| `data/sources/` | Converted to text from sources | n/a | Text was correct against sources |
| `laws.txt` research notes | None | Wrote myself | n/a |
| `data/laws/eu-ai-act-2024.yaml` | Verified my entry and made several edits for completeness | I added the original entry and tested against schema validator. This was a first pass and worked blueprint for remaining files. | The final submission against the Regulatory text |
