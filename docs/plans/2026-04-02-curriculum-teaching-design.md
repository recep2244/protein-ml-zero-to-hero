# Curriculum Teaching Design

**Goal:** Make the curriculum substantially more teachable for students with no ML background while preserving the advanced technical depth.

**Design Summary:** The curriculum already has strong technical coverage. The main weakness is uneven pedagogy: early notebooks are scaffolded, while later notebooks increasingly assume research fluency. The fix is not a rewrite of the technical content. The fix is a consistent teaching layer across the full curriculum: clearer beginner framing, explicit mastery checks, more canonical resources, and a sharper separation between core path, advanced electives, and conceptual-only first passes.

## Decisions

### 1. Add notebook-level teaching scaffolding

Every notebook should state:
- who should fully work through it vs skim it
- what prerequisites really matter
- what parts are optional on a first pass
- what “mastery” means before moving on
- what common mistakes beginners should watch for

This should be lightweight and placed near the top so students see it before the heavy material.

### 2. Add notebook-level canonical resources

Many resource sections are already good, but they vary in quality and beginner-friendliness. Add a short, curated “canonical resource upgrade” block pointing students to official or canonical sources where possible.

### 3. Make the root docs honest about learning paths

The curriculum should explicitly separate:
- zero-to-core path
- core-to-advanced path
- conceptual-only path for research-heavy modules
- compute expectations and optional-package expectations

### 4. Strengthen the weakest teaching surfaces

The newest modules and shortest notebooks need the most help:
- Module 8 practical notebooks
- Modules 12-16 advanced electives
- AI-assistant navigation docs
- module README files for advanced modules

## Scope

In scope:
- root docs
- module README files
- notebook-level teaching cells for all notebooks
- resource upgrades

Out of scope for this pass:
- fully rewriting technical code
- splitting giant notebooks into many smaller files
- executing every notebook end-to-end

## Success Criteria

- A zero-background student can identify a realistic starter path and understand what to skip on first pass.
- Every notebook contains beginner-support framing and a mastery check.
- Resource guidance becomes more canonical and less uneven.
- Advanced modules are clearly marked as electives or conceptual-first material.
