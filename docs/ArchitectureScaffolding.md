# Architecture Scaffolding — HierIN

## Purpose

This document captures the **initial architectural intent** of the HierIN project. It is not a final design, but a **scaffolding**: a set of guiding boundaries and responsibilities meant to keep the PoC technically honest, evolvable, and analyzable.

The primary goal is to avoid accidental coupling between:

* data acquisition (I/O)
* semantic interpretation (parsing)
* decision-making logic (algorithms)
* structural representation (domain)

---

## High-level Pipeline

The system is organized as a **one-way transformation pipeline**, from raw data at the boundaries to pure structural representations at the core:

```
Raw Image (bytes)
  ↓  io
Image Object (in-memory representation)
  ↓  parsing
Structured Data (semantic representation)
  ↓  algorithms
Quadtree (domain model)
  ↓  parsing / io
HierIN / Output
```

Each step narrows responsibilities and reduces external dependencies.

---

## Layer Responsibilities

### 1. IO Layer (`io/`)

**Role:** Physical boundary of the system.

Responsibilities:

* Read raw image files (PNG, JPG, etc.)
* Deal with external libraries (PIL and etc.)
* Convert raw bytes into a usable in-memory image object

Non-responsibilities:

* No semantic interpretation
* No structural decisions
* No domain knowledge

This layer is intentionally considered "dirty" and replaceable.

---

### 2. Parsing Layer (`parsing/`)

**Role:** Semantic boundary.

Responsibilities:

* Interpret image objects
* Extract structured representations (e.g. pixel grids, regions, statistics)
* Normalize data for algorithmic consumption

Parsing prepares data but **does not decide**.

Additionally, parsing is also responsible for:

* Encoding domain structures (trees) into the HierIN
* Decoding representations back into domain objects (if applicable)

---

### 3. Algorithms Layer (`algorithms/`)

**Role:** Decision-making and experimentation.

Responsibilities:

* Decide *when* and *how* to subdivide the image object
* Apply heuristics and criteria
* Implement alternative strategies

Inputs:

* Structured data from parsing

Outputs:

* Fully constructed **domain objects** (e.g. a Quadtree)

Algorithms **use** the domain, but never define it.

---

### 4. Domain Layer (`domain/`)

**Role:** Core conceptual model.

Responsibilities:

* Define structural entities
* Enforce invariants
* Provide neutral structural operations

Non-responsibilities:

* No I/O
* No image knowledge
* No heuristics or thresholds

The domain must remain:

* deterministic
* dependency-free
* valid even when manually constructed

If the domain breaks, the project has no meaning.

---

### 5. CLI Layer (`cli/`)

**Role:** Orchestration and user interface.

Responsibilities:

* Expose commands via Typer
* Wire the pipeline together
* Handle user input and configuration

The CLI must not:

* Contain business logic
* Implement algorithms
* Manipulate domain internals directly

It is a coordinator, not a participant.

---

## Dependency Direction Rules

Allowed dependency direction:

```
cli → io → parsing → algorithms → domain
```

Additional allowed paths:

* `cli` may call any layer
* `parsing` may depend on `domain` for encoding/decoding

Forbidden dependencies:

* `domain` depending on anything
* `algorithms` depending on `io`
* `domain` knowing about images or formats

These rules are more important than folder names.

---

## Design Intent

This architecture is intentionally:

* conservative
* explicit
* slightly over-structured for a PoC

That is a deliberate trade-off to:

* enable benchmarking
* allow algorithmic comparison
* keep the domain stable while experimentation happens around it

The architecture should evolve **only when pressure appears**, not preemptively.

---

## Status

This document represents the **initial scaffolding**. Changes are expected.
