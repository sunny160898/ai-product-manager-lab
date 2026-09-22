case-studies/
# AI Product Requirement Document (PRD)
## Feature: Autonomous AI Customer Support Deflection Agent

### 1. Executive Summary & Problem
- **The Problem:** 40% of tier-1 support tickets are repetitive password resets, shipping status checks, and basic refund requests, causing high operational cost and long customer wait times.
- **The Opportunity:** Implement an autonomous LLM agent integrated with enterprise order APIs to safely resolve repetitive tier-1 tickets instantly without human intervention.

### 2. Target Users & Jobs-to-Be-Done (JTBD)
- **Primary User:** End customers experiencing order or account friction.
- **JTBD:** "When my delivery is delayed, I want an instant, accurate answer and resolution path so I don't have to wait 24 hours for a human support agent."

### 3. AI Architecture & Data Flow
- **Model Choice:** GPT-4o (chosen for superior function-calling capabilities and structured output reliability).
- **Retrieval Layer (RAG):** Connects to internal company policy documents via a vector database for accurate policy answers.
- **Tool Use (APIs):** Equipped with three secure API tools: `get_order_status()`, `check_refund_eligibility()`, and `create_support_ticket()`.

### 4. Trust Boundaries & Guardrails (Crucial for AI PMs)
- **What the Agent CAN Do (Autonomy Level 2):** Look up order status, explain return policies, and automatically process full refunds *under ₹1,000* if within the 30-day window.
- **What the Agent CANNOT Do (Forbidden Actions):** Modify user account credentials, override fraud detection flags, or approve refunds over ₹1,000 without human manager escalation.

### 5. Evaluation Strategy & Success Metrics
- **Success Metrics:** 
  - **Deflection Rate:** Target >45% of tier-1 tickets resolved end-to-end by AI.
  - **CSAT (Customer Satisfaction):** Target >= 4.2 / 5.0 on AI-resolved chats.
- **Evaluation Dataset (Evals):** A golden test suite of 100 historical edge-case tickets used to measure hallucination rates and tool-calling accuracy before any production deployment.

### 6. Failure Modes & Fallbacks
- **Failure Mode 1 (Hallucination on Policy):** If the retrieval similarity score from the vector DB is below 0.75, the agent defaults to: *"I want to ensure you get the exact right information. Let me connect you with a human specialist."*
- **Failure Mode 2 (API Timeout):** Fallback static response with standard support email link.
- 
