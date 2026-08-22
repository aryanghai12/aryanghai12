<div align="center">

# Aryan Ghai

**Backend and distributed systems** &nbsp;·&nbsp; execution-grounded AI tooling &nbsp;·&nbsp; cloud-native open source

<a href="https://www.linkedin.com/in/aryan-ghai-4b31452b9/"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0D1117?style=flat-square&logo=linkedin&logoColor=0A66C2&labelColor=0D1117"></a>
<a href="mailto:aryanghai1205@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-0D1117?style=flat-square&logo=gmail&logoColor=EA4335&labelColor=0D1117"></a>
<a href="https://codolio.com/profile/aryanghai"><img alt="Codolio" src="https://img.shields.io/badge/Codolio-0D1117?style=flat-square&labelColor=0D1117"></a>
<img alt="Location" src="https://img.shields.io/badge/Greater_Noida,_India-0D1117?style=flat-square&logo=googlemaps&logoColor=34A853&labelColor=0D1117">

</div>

<br>

Final-year B.Tech CSE at NIET, Greater Noida (**9.22 CGPA**), and Open Source Intern at the
**OWASP Foundation**. Most of my time goes into Go and Python, shipping into cloud-native
security tooling.

---

## activity

<!--START:stats-->
```text
┌─ aryanghai12@github ──────────────────────────────────────────┐
│                                                               │
│   active           3 years, since August 2023                 │
│   repositories     28 public  ·  11 authored  ·  17 forks     │
│   commits          269                                        │
│   pull requests    56 opened  ·  33 merged                    │
│   upstream         25 merged across 7 external repositories   │
│   lines shipped    +34,597  /  -1,947  across 725 files       │
│   issues           22 filed                                   │
│   languages        TypeScript 83%  ·  Go 5%  ·  Python 4%     │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```
<!--END:stats-->

<sub>Regenerated from the GitHub API by [`scripts/profile_stats.py`](scripts/profile_stats.py). Plain text, no image services.</sub>

---

## selected work

### [Cavix](https://github.com/aryanghai12/CavixCode) &nbsp;·&nbsp; execution-grounded code review and sandbox engine

<img alt="Go" src="https://img.shields.io/badge/Go-0D1117?style=flat-square&logo=go&logoColor=00ADD8&labelColor=0D1117"> <img alt="Python" src="https://img.shields.io/badge/Python-0D1117?style=flat-square&logo=python&logoColor=FFD43B&labelColor=0D1117"> <img alt="pgvector" src="https://img.shields.io/badge/pgvector-0D1117?style=flat-square&logo=postgresql&logoColor=4169E1&labelColor=0D1117"> <img alt="Redis Streams" src="https://img.shields.io/badge/Redis_Streams-0D1117?style=flat-square&logo=redis&logoColor=FF4438&labelColor=0D1117"> <img alt="Docker" src="https://img.shields.io/badge/Docker-0D1117?style=flat-square&logo=docker&logoColor=2496ED&labelColor=0D1117"> <img alt="gVisor" src="https://img.shields.io/badge/gVisor-0D1117?style=flat-square&labelColor=0D1117">

Most AI reviewers assert. Cavix **proves**: it writes a failing test for every finding, runs it in a
network-isolated sandbox, applies the fix, then re-runs. Anything it cannot reproduce is dropped
before a human ever sees it.

- Orchestrated multi-agent pipeline (**LangGraph** and **Go**) routes semantic diffs to specialised domain reviewers, cutting hallucinated findings by **98%**
- Whole-repository AST index (**Tree-sitter**, **pgvector**) maps symbol flow, so the blast radius of a change is calculated rather than guessed
- Hyper-isolated execution layer on **gVisor** runs untrusted code with **zero network egress**
- **Redis Streams** ingestion in Go holds **sub-100 ms** webhook responses under concurrent load

### [TraceCV](https://github.com/aryanghai12/TraceCV) &nbsp;·&nbsp; client-side ATS résumé x-ray

<img alt="Next.js" src="https://img.shields.io/badge/Next.js-0D1117?style=flat-square&logo=nextdotjs&logoColor=FFFFFF&labelColor=0D1117"> <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-0D1117?style=flat-square&logo=typescript&logoColor=3178C6&labelColor=0D1117"> <img alt="Web Workers" src="https://img.shields.io/badge/Web_Workers-0D1117?style=flat-square&logo=javascript&logoColor=F7DF1E&labelColor=0D1117"> <img alt="Anthropic" src="https://img.shields.io/badge/Anthropic-0D1117?style=flat-square&logo=anthropic&logoColor=D97757&labelColor=0D1117"> <img alt="OpenAI" src="https://img.shields.io/badge/OpenAI-0D1117?style=flat-square&logo=openai&logoColor=FFFFFF&labelColor=0D1117"> <img alt="Gemini" src="https://img.shields.io/badge/Gemini-0D1117?style=flat-square&logo=googlegemini&logoColor=886FBF&labelColor=0D1117">

A résumé parser that never uploads your résumé. PDF and DOCX layouts are parsed and visualised
**100% in-browser** on Web Workers, and every AI claim is checked back against the source text
before it is allowed on screen.

- Post-hoc verification engine enforces **exact substring matching** against the original document, so model hallucinations never render
- **BYOK** proxy across OpenAI, Anthropic and Gemini: stateless, zero-logging, keys sealed in **AES-GCM** browser storage behind a strict CSP
- Deterministic TypeScript scoring framework: same résumé, same score, every run

---

## open source

**OWASP Foundation** &nbsp;·&nbsp; Open Source Intern

Contributor across the OWASP **Bug Logging Tool** and **OWASP Nest**. Built automated pre-flight
checks that intercept, parse and evaluate incoming pull requests before maintainer review,
enforcing formatting and coverage policy through webhook pipelines on Cloudflare Workers and
Dockerised test environments. Manual review bottlenecks fell by roughly **40%**.

Merged and shipped in repositories I do not own, where the standards are not mine to set:

<!--START:upstream-->
| Where | Repository | Merged | Lines |
| :-- | :-- | --: | :-- |
| **Kubescape · CNCF incubating · Kubernetes security** | [`kubescape`](https://github.com/kubescape/kubescape/pulls?q=is%3Apr+author%3Aaryanghai12) | 15 | `+7,987` `-662` |
|  | [`node-agent`](https://github.com/kubescape/node-agent/pulls?q=is%3Apr+author%3Aaryanghai12) | 3 | `+1,252` `-78` |
|  | [`regolibrary`](https://github.com/kubescape/regolibrary/pulls?q=is%3Apr+author%3Aaryanghai12) | 1 | `+1,317` `-1` |
| **OWASP · Open Worldwide Application Security Project** | [`Nest`](https://github.com/OWASP/Nest/pulls?q=is%3Apr+author%3Aaryanghai12) | 2 | `+182` `-16` |
| **Smart India Hackathon · team project** | [`TouristSafety`](https://github.com/Vanshikadahaliya/TouristSafety/pulls?q=is%3Apr+author%3Aaryanghai12) | 2 | `+13,884` `-388` |
| **OpenYurt · CNCF edge Kubernetes** | [`openyurt`](https://github.com/openyurtio/openyurt/pulls?q=is%3Apr+author%3Aaryanghai12) | 1 | `+4` `-4` |
| **Antiwork · Gumroad** | [`gumroad`](https://github.com/antiwork/gumroad/pulls?q=is%3Apr+author%3Aaryanghai12) | 1 | `+18` `-14` |
<!--END:upstream-->

Highlights: hardening Kubescape's OPA processor and scan-status handling, authoring new
attack-path rules (`steal-privileged-pods`, `issue-token-secrets`, `provider-iam-assumption`),
repairing timestamp chains and size accounting in the **node-agent** eBPF profiler, and adding
Windows `securityContext` compliance rules to **regolibrary**.

---

## toolchain

<table>
<tr><td><b>Languages</b></td><td>

<img alt="Go" src="https://img.shields.io/badge/Go-0D1117?style=flat-square&logo=go&logoColor=00ADD8&labelColor=0D1117"> <img alt="Python" src="https://img.shields.io/badge/Python-0D1117?style=flat-square&logo=python&logoColor=FFD43B&labelColor=0D1117"> <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-0D1117?style=flat-square&logo=typescript&logoColor=3178C6&labelColor=0D1117"> <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-0D1117?style=flat-square&logo=javascript&logoColor=F7DF1E&labelColor=0D1117"> <img alt="Java" src="https://img.shields.io/badge/Java-0D1117?style=flat-square&logo=openjdk&logoColor=E76F00&labelColor=0D1117"> <img alt="C" src="https://img.shields.io/badge/C-0D1117?style=flat-square&logo=c&logoColor=A8B9CC&labelColor=0D1117"> <img alt="SQL" src="https://img.shields.io/badge/SQL-0D1117?style=flat-square&logo=postgresql&logoColor=4169E1&labelColor=0D1117"> <img alt="Ruby" src="https://img.shields.io/badge/Ruby-0D1117?style=flat-square&logo=ruby&logoColor=CC342D&labelColor=0D1117"> <img alt="Solidity" src="https://img.shields.io/badge/Solidity-0D1117?style=flat-square&logo=solidity&logoColor=FFFFFF&labelColor=0D1117">

</td></tr>
<tr><td><b>Backend and data</b></td><td>

<img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-0D1117?style=flat-square&logo=postgresql&logoColor=4169E1&labelColor=0D1117"> <img alt="pgvector" src="https://img.shields.io/badge/pgvector-0D1117?style=flat-square&logo=postgresql&logoColor=4169E1&labelColor=0D1117"> <img alt="Redis" src="https://img.shields.io/badge/Redis-0D1117?style=flat-square&logo=redis&logoColor=FF4438&labelColor=0D1117"> <img alt="Node.js" src="https://img.shields.io/badge/Node.js-0D1117?style=flat-square&logo=nodedotjs&logoColor=5FA04E&labelColor=0D1117"> <img alt="REST APIs" src="https://img.shields.io/badge/REST_APIs-0D1117?style=flat-square&labelColor=0D1117"> <img alt="Concurrency" src="https://img.shields.io/badge/Concurrency-0D1117?style=flat-square&labelColor=0D1117">

</td></tr>
<tr><td><b>Infra and runtime</b></td><td>

<img alt="Docker" src="https://img.shields.io/badge/Docker-0D1117?style=flat-square&logo=docker&logoColor=2496ED&labelColor=0D1117"> <img alt="Kubernetes" src="https://img.shields.io/badge/Kubernetes-0D1117?style=flat-square&logo=kubernetes&logoColor=326CE5&labelColor=0D1117"> <img alt="gVisor" src="https://img.shields.io/badge/gVisor-0D1117?style=flat-square&labelColor=0D1117"> <img alt="Cloudflare Workers" src="https://img.shields.io/badge/Cloudflare_Workers-0D1117?style=flat-square&logo=cloudflareworkers&logoColor=F38020&labelColor=0D1117"> <img alt="Linux" src="https://img.shields.io/badge/Linux-0D1117?style=flat-square&logo=linux&logoColor=FCC624&labelColor=0D1117"> <img alt="Bash" src="https://img.shields.io/badge/Bash-0D1117?style=flat-square&logo=gnubash&logoColor=4EAA25&labelColor=0D1117"> <img alt="Azure" src="https://img.shields.io/badge/Azure-0D1117?style=flat-square&logo=microsoftazure&logoColor=0078D4&labelColor=0D1117"> <img alt="Git" src="https://img.shields.io/badge/Git-0D1117?style=flat-square&logo=git&logoColor=F05032&labelColor=0D1117">

</td></tr>
<tr><td><b>AI systems</b></td><td>

<img alt="LangGraph" src="https://img.shields.io/badge/LangGraph-0D1117?style=flat-square&logo=langchain&logoColor=FFFFFF&labelColor=0D1117"> <img alt="Anthropic" src="https://img.shields.io/badge/Anthropic-0D1117?style=flat-square&logo=anthropic&logoColor=D97757&labelColor=0D1117"> <img alt="OpenAI" src="https://img.shields.io/badge/OpenAI-0D1117?style=flat-square&logo=openai&logoColor=FFFFFF&labelColor=0D1117"> <img alt="Gemini" src="https://img.shields.io/badge/Gemini-0D1117?style=flat-square&logo=googlegemini&logoColor=886FBF&labelColor=0D1117"> <img alt="Tree-sitter" src="https://img.shields.io/badge/Tree--sitter-0D1117?style=flat-square&labelColor=0D1117">

</td></tr>
<tr><td><b>Web</b></td><td>

<img alt="Next.js" src="https://img.shields.io/badge/Next.js-0D1117?style=flat-square&logo=nextdotjs&logoColor=FFFFFF&labelColor=0D1117"> <img alt="React" src="https://img.shields.io/badge/React-0D1117?style=flat-square&logo=react&logoColor=61DAFB&labelColor=0D1117"> <img alt="Tailwind" src="https://img.shields.io/badge/Tailwind-0D1117?style=flat-square&logo=tailwindcss&logoColor=06B6D4&labelColor=0D1117"> <img alt="Rails" src="https://img.shields.io/badge/Rails-0D1117?style=flat-square&logo=rubyonrails&logoColor=D30001&labelColor=0D1117">

</td></tr>
<tr><td><b>Quality</b></td><td>

<img alt="PyTest" src="https://img.shields.io/badge/PyTest-0D1117?style=flat-square&logo=pytest&logoColor=0A9EDC&labelColor=0D1117"> <img alt="go test" src="https://img.shields.io/badge/go_test-0D1117?style=flat-square&logo=go&logoColor=00ADD8&labelColor=0D1117"> <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub_Actions-0D1117?style=flat-square&logo=githubactions&logoColor=2088FF&labelColor=0D1117"> <img alt="Rego and OPA" src="https://img.shields.io/badge/Rego_·_OPA-0D1117?style=flat-square&labelColor=0D1117">

</td></tr>
</table>

---

## elsewhere

<div align="center">

<a href="https://www.linkedin.com/in/aryan-ghai-4b31452b9/"><img alt="LinkedIn" src="https://img.shields.io/badge/aryan--ghai-0D1117?style=flat-square&logo=linkedin&logoColor=0A66C2&labelColor=0D1117"></a>
<a href="mailto:aryanghai1205@gmail.com"><img alt="Email" src="https://img.shields.io/badge/aryanghai1205@gmail.com-0D1117?style=flat-square&logo=gmail&logoColor=EA4335&labelColor=0D1117"></a>
<a href="https://codolio.com/profile/aryanghai"><img alt="Codolio" src="https://img.shields.io/badge/codolio.com/aryanghai-0D1117?style=flat-square&labelColor=0D1117"></a>
<a href="https://github.com/aryanghai12?tab=repositories"><img alt="Repositories" src="https://img.shields.io/badge/repositories-0D1117?style=flat-square&logo=github&logoColor=FFFFFF&labelColor=0D1117"></a>

<br><br>

<sub><!--STAMP-->last synced 22 Aug 2026<!--/STAMP--> &nbsp;·&nbsp; open to Software Engineering internships</sub>

</div>
