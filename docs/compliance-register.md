# elect-rix Compliance Register

**Owner:** Director, RixBot Technologies Inc.  
**Trade name:** elect-rix Technology Solutions  
**Last updated:** 2026-07-20  
**Next review:** 2026-10-05  
**Regulation doctrine:** `~/elect-rix/reports/elect-rix-regulation-integration-pathway-2026-07-20.md`  

> This register maps each public compliance claim on elect-rix.tech to its underlying requirement, evidence, and owner. It is a living document. Nothing here is legal advice; formal positions should be confirmed with qualified counsel or assessors.

---

## How to read this register

| Column | Meaning |
|--------|---------|
| Claim | What the safety page says |
| Applies because | Law, regulation, contract, or market requirement driving it |
| Status | `Verified` = evidence exists; `In progress` = being implemented; `Design intent` = planned architecture; `Advisory` = positioning, needs engagement |
| Evidence | File, record, or proof that supports the claim |
| Owner | Person accountable for keeping this current |
| Review | When this row must be checked again |

---

## 1. Data Sovereignty & Residency

| Claim | Applies because | Status | Evidence | Owner | Review |
|-------|-----------------|--------|----------|-------|--------|
| Primary lab in New Brunswick, Canada | Corporate presence; marketing | Verified | Director knowledge; Domo reference rig in NB | Director | 2026-10-05 |
| All client data processed/stored in Canada unless explicitly requested otherwise | PIPEDA; FOIPOP; PSPC/Protected workload expectations; client contracts | Design intent | No standard client deployment SOP yet; must be documented per engagement | Director | 2026-08-05 |
| Cloud deployments use Canadian regions only | Data sovereignty commitments | Design intent | Cloudflare CDN only; compute must be local or Canadian-hosted | Director | 2026-08-05 |
| No US-managed cloud services for Protected workloads | CCCS/ITSG cloud guidance; procurement | Design intent | Written architecture decision needed | Director | 2026-08-05 |
| Client data not sent to foreign AI APIs unless explicitly requested and approved in writing | PIPEDA consent; solicitor-client privilege; contractual confidentiality | In progress | Template: `~/elect-rix/01-legal-corporate/ops-templates/CLIENT-FOREIGN-AI-CLOUD-AUTHORIZATION.md` (use on first paid egress exception) | Director | 2026-08-05 |
| Work product delivered to client-controlled infrastructure | Contract handover; risk reduction | Design intent | Need standard delivery checklist | Director | 2026-09-05 |

## 2. Security Architecture

| Claim | Applies because | Status | Evidence | Owner | Review |
|-------|-----------------|--------|----------|-------|--------|
| Dedicated hardware in access-controlled space | Physical security baseline | Verified | Domo lab is local and physically controlled | Director | 2026-10-05 |
| No co-location or shared data centers | Sovereignty positioning | Verified | No third-party colo currently used | Director | 2026-10-05 |
| Hardware owned, not leased | Asset and supply-chain control | Verified | Purchase records for Domo/proff hardware | Director | 2026-10-05 |
| Local-only development; no remote access to build machines | Supply chain / build integrity | Verified | Build machine is local; remote access not enabled | Director | 2026-10-05 |
| Firewall default-deny; only required ports open | CCCS/ITSG network controls | In progress | Need documented firewall rule review | Director | 2026-08-05 |
| VPN required for any remote administration | Secure administration | Design intent | No remote admin currently; policy needed if scope changes | Director | 2026-09-05 |
| Static site output (Astro + Bun); no server-side attack surface at runtime | Application security; marketing | Verified | Build output is static; `astro.config.mjs` confirms | Director | 2026-10-05 |
| Lockfile-controlled dependencies (`bun.lock`) | Supply chain; SBOM readiness | Verified | `bun.lock` exists; build reproducible from repo | Director | 2026-10-05 |
| No third-party JS trackers or analytics on public pages | PIPEDA; marketing | Verified | Network tab inspection; source has no trackers | Director | 2026-10-05 |
| Git commit hash = deployment identifier | Audit trail; procurement | Verified | GitHub Actions deploy links commit SHA | Director | 2026-10-05 |
| Named principal with full accountability | Procurement; insurance | Verified | Incorporation records name director | Director | 2026-10-05 |
| NDA/confidentiality binding on personnel | Contractual duty | Design intent | No employees/subcontractors yet; template needed | Director | 2026-09-05 |

## 3. Cybersecurity Posture

| Claim | Applies because | Status | Evidence | Owner | Review |
|-------|-----------------|--------|----------|-------|--------|
| Designed to map to ITSG-33/37 baselines where applicable | Government procurement | Advisory | No formal control mapping produced yet; available per engagement | Director | 2026-08-05 |
| Access control, audit, system integrity controls documented | ITSG-33 control families | In progress | Controls described on site; need internal policy documents | Director | 2026-08-05 |
| Security categorization available for Protected B workloads upon request | PSPC/SSC requirements | Advisory | Would require formal categorization per engagement | Director | 2026-08-05 |
| Defined incident response plan: detect → contain → eradicate → recover → document | CCCS; cyber insurance; contracts | In progress | Draft runbook: `~/elect-rix/01-legal-corporate/ops-templates/IR-RUNBOOK.md` (OPS-IR-001); tabletop still due | Director | 2026-10-05 |
| Client notification within 24 hours of suspected breach | Contractual SLA; privacy law | In progress | IR-RUNBOOK §6 + SOW privacy block OPS-SOW-PRIV-001; live only with SOW+deposit | Director | 2026-10-05 |
| RCMP and CCCS reporting channels documented | Breach reporting | In progress | IR-RUNBOOK §6.2–6.3 (priv.gc.ca, rcmp-grc.gc.ca, cyber.gc.ca) | Director | 2026-10-05 |
| Local system logs retained for forensic analysis | Incident response; ITSG audit | In progress | Need retention policy and log locations documented | Director | 2026-08-05 |

## 4. Access Control & Identity

| Claim | Applies because | Status | Evidence | Owner | Review |
|-------|-----------------|--------|----------|-------|--------|
| 2FA enforced on admin and third-party accounts wherever supported | CCCS/ITSG; cyber insurance | In progress | Need account inventory and 2FA verification list | Director | 2026-08-05 |
| No shared credentials; individual accounts only | Access control baseline | Verified | Current practice; document if team grows | Director | 2026-10-05 |
| Password managers used for secure credential storage | Credential hygiene | Verified | Bitwarden/KeePass in use | Director | 2026-10-05 |
| RBAC for client environments | Least privilege | Design intent | Need role definitions per engagement | Director | 2026-09-05 |
| Access revoked on project completion/termination | Lifecycle management | Design intent | Need offboarding checklist | Director | 2026-09-05 |
| No standing admin access to client production systems | Least privilege; liability | Design intent | Need policy and process | Director | 2026-09-05 |

## 5. Privacy & Data Handling

| Claim | Applies because | Status | Evidence | Owner | Review |
|-------|-----------------|--------|----------|-------|--------|
| Data minimization | PIPEDA principle | In progress | Need client intake data inventory template | Director | 2026-08-05 |
| Purpose limitation | PIPEDA principle | In progress | SOW block: `~/elect-rix/01-legal-corporate/ops-templates/SOW-PRIVACY-CLAUSE-BLOCK.md`; wired into downstream-packet SOW §8 | Director | 2026-08-05 |
| Explicit documented consent before personal data processing | PIPEDA; PHIPA | In progress | Foreign AI/cloud auth form OPS-AUTH-001; engagement intake still needs full PI consent line | Director | 2026-08-05 |
| Clients can request all data elect-rix holds | PIPEDA access principle | Design intent | Need data request response procedure | Director | 2026-09-05 |
| No telemetry/analytics cookies on public site | PIPEDA; marketing claim | Verified | Cookie/network inspection; privacy page states this | Director | 2026-10-05 |
| Client data retained only for duration of engagement | PIPEDA; storage limitation | Design intent | Need retention schedule | Director | 2026-09-05 |
| Certificates of destruction available upon request | Contract handover | Design intent | Need destruction procedure/template | Director | 2026-09-05 |

## 6. Regulatory Compliance Table

| Framework | Applies because | Status | Evidence | Owner | Review |
|-----------|-----------------|--------|----------|-------|--------|
| PIPEDA | Federal private-sector privacy law (**in force**) | In progress | Privacy practices partly documented; full privacy policy review needed | Director | 2026-08-05 |
| Bill C-36 / PPCDA | Proposed federal private-sector privacy overhaul (tabled 2026-06-15) | Advisory | **Not law.** Track LEGISinfo 45-1/C-36 only; no public “C-36 compliant” claims | Director | Monthly / on stage change |
| AIDA / comprehensive federal AI Act | Prior C-27 AI chapter; no successor in force as of 2026-07 | Advisory | Do not sell AIDA certification; use sector + privacy law | Director | On new AI bill table |
| PHIPA (NB) + health privacy cousins | Healthcare vertical / PHI | Advisory | Vertical checklist exists; counsel per client | Director | Before first health paid deploy |
| FOIPOP / RTIPPA (NB) | Government clients; public bodies | Advisory | Available per government engagement | Director | 2026-08-05 |
| ITSG-33 / ITSG-37 | Federal government security controls | Advisory | Formal mapping available per engagement — never blanket badge | Director | 2026-08-05 |
| CCCS Cyber Guidance | Procurement; best practice | In progress | Website aligns with guidance; no formal assessment | Director | 2026-08-05 |
| Quebec Law 25 | QC private-sector clients only | Advisory | Separate docs if QC pipeline; NB templates ≠ QC | Director | If QC lead appears |
| WCAG 2.1 AA | Accessibility; procurement | In progress | Target stated; no formal audit yet | Director | 2026-09-05 |
| SR&ED | R&D tax credits | In progress | R&D records in Git; formal tax position pending accountant review | Director | 2026-10-05 |

## 7. Government Procurement Readiness

| Claim | Applies because | Status | Evidence | Owner | Review |
|-------|-----------------|--------|----------|-------|--------|
| Data residency aligned with Protected workload expectations | PSPC/SSC | Advisory | Architecture supports it; formal categorization per engagement | Director | 2026-08-05 |
| One named Canadian principal | Procurement accountability | Verified | Corporate records | Director | 2026-10-05 |
| Reliability status / background check available upon request | Sensitive engagements | Advisory | Not currently held; can be obtained if client requires | Director | 2026-09-05 |
| SME procurement stream eligibility | Canadian small business preference | Verified | NB-incorporated Canadian-controlled private corporation target | Director | 2026-10-05 |
| Regional-benefit documentation available | IRB / regional procurement | Design intent | Need template if pursuing federal contracts | Director | 2026-09-05 |

## 8. Fall Wall Inspection (FWI) Framework

| Claim | Applies because | Status | Evidence | Owner | Review |
|-------|-----------------|--------|----------|-------|--------|
| FWI is internal safety verification methodology | Differentiation; procurement proof | Design intent | Methodology described; no client-facing sample report yet | Director | 2026-08-05 |
| Five walls checked: perimeter, identity, data, application, human | FWI structure | Design intent | Need checklist template | Director | 2026-08-05 |
| Red team / blue team simulation | Security testing | Advisory | Can be scoped per engagement; not currently a standing capability | Director | 2026-09-05 |
| Re-inspection triggered by threats, changes, incidents | Maintenance | Design intent | Need trigger policy | Director | 2026-09-05 |

## 9. SR&ED & Innovation Tax Credits

| Claim | Applies because | Status | Evidence | Owner | Review |
|-------|-----------------|--------|----------|-------|--------|
| Eligible R&D activities tracked | SR&ED claim support | In progress | Lab notebooks in Git; time tracking needs standardization | Director | 2026-08-05 |
| Contemporaneous R&D records maintained | CRA requirement | In progress | Git commits, project notes exist; formal log needed | Director | 2026-08-05 |
| Formal tax position confirmed with qualified counsel | CRA compliance | Advisory | Accountant/lawyer to be engaged before filing | Director | 2026-10-05 |

## 10. Vendor Due Diligence Checklist

| Checklist item | Applies because | Status | Evidence | Owner | Review |
|----------------|-----------------|--------|----------|-------|--------|
| Data residency | Procurement | In progress | See section 1 | Director | 2026-08-05 |
| SBOM / dependency inventory | Supply chain | In progress | `bun.lock`; need SBOM generator | Director | 2026-08-05 |
| Personnel vetting | Sensitive contracts | Advisory | Available upon request | Director | 2026-09-05 |
| Incident response plan | Cyber risk | In progress | IR-RUNBOOK.md OPS-IR-001; see section 3 | Director | 2026-10-05 |
| E&O / cyber liability insurance | Contract risk | Verified | Zensurance/CFC 7456813 CGL+E&O+Cyber $1M each (bound 2026-07-17); COI when issued | Director | 2026-10-05 |
| WCAG verification | Accessibility | In progress | See section 6 | Director | 2026-09-05 |
| Audit trail / signed commits | Procurement | In progress | Git history exists; signed commits not yet enforced | Director | 2026-09-05 |
| Indigenous / regional benefits | Federal procurement | Design intent | Template needed | Director | 2026-09-05 |
| Termination / data destruction | Contract closeout | Design intent | Procedure needed | Director | 2026-09-05 |
| Subcontractor confidentiality | Supply chain | Design intent | No subcontractors yet; NDA template needed | Director | 2026-09-05 |

---

## Immediate action items

1. **Incident response runbook** — **draft done** (`ops-templates/IR-RUNBOOK.md`). Still open: first 30-min tabletop; insurer notice wording check when COI pack arrives.
2. **Account / 2FA inventory** — list every admin and third-party account, verify 2FA, rotate shared credentials.
3. **Client authorization template** — **draft done** (`CLIENT-FOREIGN-AI-CLOUD-AUTHORIZATION.md`). Still open: print/PDF in engagement kit; first real signature on paid exception.
4. **SOW privacy block** — **draft done** (`SOW-PRIVACY-CLAUSE-BLOCK.md` + downstream-packet SOW §8). Still open: counsel eyeball before health/legal/gov or large deal.
5. **SR&ED accountant meeting** — confirm what records are sufficient before year-end.
6. **Accessibility spot-check** — run a WCAG tool on elect-rix.tech and fix obvious issues.
7. **Safety page update** — add "last reviewed" date; clarify current practice vs available upon request; no C-36/PPCDA compliance claims.
8. **Regulatory radar** — monthly LEGISinfo C-36 + OPC/ISED glance; log one line (see regulation integration memo).
9. **Light privacy pack (elect-rix itself)** — P1: what we collect (leads/billing/Meet), where stored, retention (pairs with IR).

---

## Disclaimer

This register is an internal management tool. It does not create legal or contractual obligations. Public statements on elect-rix.tech must be reviewed against this register before being relied upon in procurement or sales.
