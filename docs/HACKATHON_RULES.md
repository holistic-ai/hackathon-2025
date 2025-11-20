# Holistic AI x UCL Hackathon 2025 - Official Rules

**Last Updated**: November 12, 2025  
**Contact**: [Discord](https://discord.com/invite/QBTtWP2SU6?referrer=luma) (for questions and support)  
**Website**: [hackathon.holisticai.com](https://hackathon.holisticai.com/)

---

## 1. HACKATHON OVERVIEW

The Holistic AI x UCL Hackathon 2025 is a competition focused on building production-grade AI agents. Participants will compete in one or more of three tracks:

- **Track A: Agent Iron Man** - Performance & Robustness
- **Track B: Agent Glass Box** - Observability & Explainability
- **Track C: Dear Grandma** - Security & Red Teaming

**Organizer**: Holistic AI in partnership with University College London  
**Submission Platform**: Devpost

---

## 2. IMPORTANT DATES & TIMES

All times are in Greenwich Mean Time (GMT).

- **Registration Opens**: November 1, 2025
- **Hacking Period Begins**: November 15, 2025, 8:00 AM GMT
- **Submission Deadline**: November 16, 2025, 3:00 PM GMT
- **Judging Period**: November 16, 2025, 3:00 PM - 5:30 PM GMT
- **Winner Announcement**: November 16, 2025, 6:00 PM GMT

Late submissions will not be accepted. Devpost timestamps will be used to verify submission times.

---

## 3. ELIGIBILITY

### 3.1 Who Can Participate

This Hackathon is open to:

- Students (undergraduate, graduate, PhD)
- Professionals and researchers
- Individuals age 18 and older
- Participants from any country (subject to local laws and regulations)

### 3.2 Team Requirements

- **Team Size**: 3-5 members per team (required)
- Teams must register on Devpost and designate one team member as the primary contact
- Team members may not be part of multiple teams
- Team composition may not change after initial registration

### 3.3 Ineligibility

The following individuals are NOT eligible to participate:

- Employees of Holistic AI and their immediate family members
- Hackathon judges and organizers
- Individuals prohibited by local law from participating

### 3.4 Restrictions

- Participants must comply with all applicable local, state, and federal laws
- By participating, you agree to the Code of Conduct
- Teams found violating rules may be disqualified without refund (if applicable)

---

## 4. TRACKS & CATEGORIES

Participants may compete in one or multiple tracks:

### Track A: Agent Iron Man

Focus on performance optimization and robustness. Build agents that are fast, efficient, and resilient.

### Track B: Agent Glass Box

Focus on observability and explainability. Create transparent and auditable AI agents.

### Track C: Dear Grandma

Focus on security and red teaming. Discover vulnerabilities and propose defense strategies.

Teams selecting multiple tracks will be judged separately for each track.

---

## 5. PROJECT REQUIREMENTS

### 5.1 Originality

- All code must be written during the Hackathon period (November 15-16, 2025, from November 15, 8:00 AM GMT to November 16, 3:00 PM GMT)
- Projects must be original work of the team
- Pre-existing code is allowed ONLY for:
  - Open-source libraries and frameworks
  - Provided starter kit and tutorials
  - Pre-trained models
  - Standard development tools

### 5.2 Permitted Resources

Teams MAY use:

- AWS Bedrock managed by Holistic AI (credentials provided at event)
- OpenAI, Anthropic, Google, or other commercial APIs
- Our starter repository: github.com/holistic-ai/hackthon-2025
- Open-source frameworks (LangGraph, LangSmith, CrewAI, AutoGen, etc.)
- Pre-trained models from Hugging Face, Ollama, or similar sources

### 5.3 Track C Specific Rules

For Track C (Dear Grandma) participants:

- Ethical red-teaming only - no malicious attacks on production systems
- DoS attacks on provided endpoints are PROHIBITED and will result in immediate disqualification
- Teams found engaging in excessive rate limiting or system disruption will be flagged
- Testing on external systems (ChatGPT, Claude, etc.) must comply with those services' terms of service

---

## 6. SUBMISSION REQUIREMENTS

All submissions must be completed by November 16, 2025, 3:00 PM GMT via Devpost.

### 6.1 Required Deliverables

**1. Poster (PDF)**

- Format: Single page, A3 or A4 size, virtual format (not physical print)
- Tools: PowerPoint, Google Slides, Overleaf, Canva, or any design tool
- Content: Visual summary including findings, methodology, key results, and impact
- File must be uploaded to Devpost

**2. GitHub Repository**

- STRONGLY RECOMMENDED (not optional in practice)
- Must include:
  - README.md with project overview and setup instructions
  - Organized code and scripts
  - Clear reproduction instructions
  - Results data and logs
- Repository must be public or accessible to judges
- Must include open-source license

**3. Team Information**

- Team name
- Contact email for prize notifications
- List of 3-5 team members with names and emails
- Selected track(s)

**4. Devpost Submission**

- Project name and tagline
- Detailed description of the project
- Technologies used
- Track selection via custom submission questions
- GitHub repository URL
- Team information (name, contact email, members)

### 6.2 Track-Specific Requirements

**Track A (Agent Iron Man):**

- Performance metrics documentation (latency, token usage, cost, carbon footprint)
- Monitoring dashboard or comprehensive logs
- Error handling demonstrations
- Comparison with baseline or benchmarks

**Track B (Agent Glass Box):**

- Execution traces (LangSmith or equivalent)
- Reasoning visualization or documentation
- Explainability documentation
- User-facing explanation examples

**Track C (Dear Grandma):**

- Attack prompts and payloads (organized by type)
- ASR (Attack Success Rate) evaluation methodology
- Vulnerability findings report (up to 5 vulnerabilities)
- Defense strategy proposals
- Agent identification (if testing provided endpoints)

### 6.3 Optional Submissions

- Demo video (3-5 minutes, YouTube or Vimeo link)
- Additional documentation or technical write-ups

### 6.4 Incomplete Submissions

Submissions missing required elements may be disqualified at judges' discretion. Teams will NOT be contacted to complete missing requirements after the deadline.

---

## 7. JUDGING & EVALUATION

### 7.1 Judging Panel

A panel of expert judges from academia and industry will evaluate submissions. Judge identities will be announced before or during judging.

### 7.2 Judging Criteria

Each submission will be evaluated on **5 criteria** (0-5 stars each):

**Core Criteria (applies to all tracks):**

1. **Technical Excellence** - Code quality, innovation, problem-solving
2. **Documentation & Presentation** - Poster and GitHub repo quality
3. **Real-world Impact** - Practical applicability and value

**Track-Specific Criteria (2 per track):**

**Track A:** 4. Performance Optimization 5. Robustness & Reliability

**Track B:** 4. Observability Implementation 5. Explainability & Transparency

**Track C:** 4. Attack Discovery & Severity 5. Methodology & Impact Scope

**Total Score**: 25 stars maximum (5 criteria × 5 stars)

For detailed judging criteria, see [Judging_Prize.pdf](./Judging_Prize.pdf).

### 7.3 Evaluation Process

- Initial screening for eligibility and completeness
- Independent evaluation by multiple judges
- Judges' decisions are final and binding
- Ties will be broken by organizers based on overall innovation and impact

### 7.4 Disqualification Grounds

Projects may be disqualified for:

- Missing required deliverables
- Violation of Code of Conduct
- Use of prohibited pre-existing code
- Plagiarism or intellectual property infringement
- DoS attacks or system abuse (Track C)
- Submission after deadline

---

## 8. PRIZES & WINNER SELECTION

### 8.1 Prize Categories

Winners will be announced for each track:

- Track A: Agent Iron Man
- Track B: Agent Glass Box
- Track C: Dear Grandma

For complete prize details, see [Judging_Prize.pdf](./Judging_Prize.pdf).

### 8.2 Winner Notification

Winners will be announced at 6:00 PM GMT on November 16, 2025. Winners will be contacted via the team contact email provided during submission.

### 8.3 Prize Claiming

- Prizes must be claimed within 30 days of notification
- Winners may be required to sign affidavits of eligibility and liability/publicity releases
- Prizes are non-transferable
- No prize substitution except at organizer's discretion
- Winners are responsible for all applicable taxes

---

## 9. INTELLECTUAL PROPERTY

### 9.1 Ownership

Participants retain full ownership of their intellectual property created during the Hackathon.

### 9.2 License Grant

By submitting, participants grant Holistic AI a non-exclusive, worldwide, royalty-free license to:

- Display and promote submissions on Devpost and Holistic AI channels
- Use project names, descriptions, and screenshots for promotional purposes
- Share results and findings in academic or commercial publications (with attribution)

### 9.3 Open Source Requirement

All GitHub repositories must include an open-source license (MIT, Apache 2.0, or similar permissive license recommended).

---

## 10. CODE OF CONDUCT

All participants must agree to and follow the Hack Code of Conduct. Violations may result in:

- Warning from organizers
- Immediate expulsion from the Hackathon
- Disqualification from prizes
- Ban from future Holistic AI events

Full Code of Conduct: [Link to Code of Conduct]

### 10.1 Reporting

Report any violations via [Discord](https://discord.com/invite/QBTtWP2SU6?referrer=luma) or any on-site organizer.

---

## 11. PRIVACY & DATA PROTECTION

### 11.1 Data Collection

By participating, you consent to the collection of:

- Name, email, and team information
- Project submissions and related materials
- Communication records

### 11.2 Data Use

Your information will be used for:

- Hackathon administration and judging
- Winner notification and prize distribution
- Future event communications (with opt-out option)

### 11.3 Data Sharing

Personal information will not be sold or shared with third parties except:

- As required by law
- With Devpost for platform administration
- For prize fulfillment

---

## 12. LIABILITY & DISCLAIMERS

### 12.1 Assumption of Risk

Participants assume all risks associated with participation, including but not limited to:

- Technical issues or system failures
- Loss of project data
- Travel to/from venue (if in-person)

### 12.2 Release of Liability

By participating, you release and hold harmless Holistic AI, UCL, partners, sponsors, and their respective officers, directors, employees, and agents from any and all liability for injuries, loss, or damage arising from participation.

### 12.3 No Warranty

The Hackathon and all materials are provided "AS IS" without warranty of any kind.

---

## 13. GENERAL CONDITIONS

### 13.1 Rule Changes

Organizers reserve the right to modify these rules at any time. Material changes will be communicated to registered participants via email and posted on the Devpost hackathon page.

### 13.2 Cancellation

Organizers reserve the right to cancel or postpone the Hackathon at any time for any reason. In case of cancellation, no compensation will be provided.

### 13.3 Interpretation

All questions or disputes regarding eligibility, rules interpretation, or judging will be resolved by Holistic AI in its sole discretion.

### 13.4 Severability

If any provision of these rules is found to be invalid or unenforceable, the remaining provisions will remain in full effect.

### 13.5 Governing Law

These rules shall be governed by the laws of England and Wales, without regard to conflict of law principles.

---

## 14. CONTACT INFORMATION

For questions about these rules, the Hackathon, or to report issues:

**Discord**: [Join our Discord](https://discord.com/invite/QBTtWP2SU6?referrer=luma)  
**Website**: hackathon.holisticai.com

---

## 15. ACKNOWLEDGMENT

By registering for and participating in this Hackathon, you acknowledge that you have read, understood, and agree to be bound by these Official Rules and the Code of Conduct.

---

**© 2025 Holistic AI. All rights reserved.**
