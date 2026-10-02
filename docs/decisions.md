# Decisions

Short records of technical choices and their trade-offs.

## Data

- **Dates are quoted strings in YAML** (`"2026-10-01"`). JSON has no date type, so the schema defines a date as a string with `format: date`. Unquoted, PyYAML (YAML 1.1) turns dates into `datetime.date` objects, which fail the schema. Quoting needs no extra code, and the validator rejects any unquoted date.
- **The schema checks dates twice:** `pattern` (shape, always enforced) and `format: date` (a real calendar date, enforced only with format checking on). JSON Schema treats `format` as an annotation by default.
- **YAML is loaded with `yaml.safe_load`**, which builds only plain data. Entries may later be drafted from untrusted source text.

## Validation (`pipeline/validate_schema.py`)

- **`Draft202012Validator` with `iter_errors`** reports every error in a file in one pass; `jsonschema.validate()` stops at the first.
- **Format checking is on**, so impossible dates like `2026-02-30` fail.
- **An empty or missing directory fails.** Otherwise a wrong path in CI would pass while checking nothing.
- **Fixtures prove it works both ways:** `pipeline/tests/fixtures/valid` must pass and `invalid` must fail.

## Python environment

- **A project virtualenv (`.venv/`, gitignored).** Ubuntu's Python is managed by the OS, so `pip install` into it is blocked (PEP 668). The venv keeps project dependencies separate from the system.
- **Dependencies:** `jsonschema` (with 5 transitive packages, including the compiled `rpds-py`) and `PyYAML`.

## Site

- **Astro.** It builds plain static HTML (no server-side code to attack or patch), ships no JavaScript unless a page opts in (easy to keep a strict Content-Security-Policy), and reads YAML files directly.
  - Trade-off: about 188 npm packages, all build-time only. Nothing from npm runs on the server.
- **No schema in the Astro content collection.** `data/schema.json`, checked by the Python validator, is the single source of truth; a second (Zod) schema in the site would have to be kept in sync with it.
- **Filters hide pre-rendered items; no data is fetched.** All entries are in the HTML. Without JavaScript (e.g. Tor Browser's Safest mode) visitors see the full list, and the filter controls stay hidden.
- **Scripts are never inlined** (`assetsInlineLimit: 0` in `astro.config.mjs`). Astro inlines small scripts by default, which a Content-Security-Policy of `script-src 'self'` would block. External script files keep the CSP strict, with no `'unsafe-inline'` or hashes.
- **Node LTS pinned in `site/.nvmrc`,** so local builds and CI use the same version.
- **Supply-chain controls for npm:**
  - `package-lock.json` pins every package, and CI installs with `npm ci`, which uses exactly the lockfile.
  - `allowScripts` in `package.json` lets only `esbuild` run an install script.
  - The `^` range on `astro` only affects `npm install`, never `npm ci`.
