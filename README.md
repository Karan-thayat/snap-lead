# SnapLead: AI-Driven Real Estate Content Engine

## Architecture Overview
SnapLead is an event-driven AI pipeline designed to capture real estate market intent and instantly generate brand-safe SEO content. 

This repository contains the production approval dashboard, deployed to the edge via Vercel, which interfaces with our cloud database.

### The Microservices Pipeline
1. **Trigger:** Listens for market signals (e.g., Reddit leads, housing data).
2. **AI Processing:** An n8n workflow routes data through LLMs (Groq) to generate targeted SEO content.
3. **Storage:** The generated markdown is pushed to a Neon PostgreSQL cloud database.
4. **Human-in-the-Loop UI:** This Flask application queries the database for `pending` drafts, allowing editors to review and approve content before it goes live.

### Tech Stack
* **Frontend/API:** Flask, deployed on Vercel
* **Database:** PostgreSQL (Neon Serverless)
* **Pipeline Engine:** n8n (Node.js)
* **AI Models:** Groq 

*Note: For the purpose of hackathon latency and firewall bypassing, the n8n data ingestion engine can also be routed to a local loopback environment.*
