# 🚀 SnapLead: AI-Driven Real Estate Content Engine

## The Vision
The real estate market moves fast, but SEO content creation moves slow. **SnapLead** is an event-driven AI pipeline designed to capture real estate market intent (like Reddit discussions or housing queries) and instantly generate highly targeted, brand-safe blog content. 

Instead of replacing human editors, SnapLead acts as an ultra-fast drafting engine with a **human-in-the-loop approval UI**, ensuring brand safety and quality control before anything goes public.

---

## 🏗️ Architecture & Tech Stack
SnapLead utilizes a decoupled, microservices architecture to ensure maximum scalability and fault tolerance:

* **Data Ingestion & Orchestration:** `n8n` (Node.js) handles event triggers and API routing.
* **AI Processing:** `Groq` LLM engine processes the strategy and writes the markdown content.
* **Database:** `Neon Serverless PostgreSQL` stores the relational queue and guarantees data integrity with strict schemas and foreign key constraints.
* **Frontend UI:** `Flask` (Python) provides the editor approval dashboard.
* **Edge Deployment:** `Vercel` hosts the production interface.

---

## ⚠️ Important Note for Judges: Our Dual-Environment Setup
During the live hackathon, aggressive venue network firewalls blocked outbound IPv6 and standard database ports (5432), preventing our event-driven `n8n` pipeline from securely writing to our Neon cloud database. 

Instead of compromising the live demo, **we engineered a dual-environment split:**

1. **The Cloud Edge (Vercel + Neon):** Our production Flask application is fully deployed to Vercel and actively reading from our live Neon database. (We have populated this cloud queue with production-grade sample data so you can interact with the live UI).
2. **The Local Processing Engine (n8n + Localhost DB):** To guarantee zero-latency AI processing and bypass the venue's network restrictions, our actual `n8n` ingestion engine and a replica PostgreSQL database are running entirely on a secure local loopback. 

**This setup demonstrates both our ability to deploy to the edge AND our ability to build resilient, environment-aware local pipelines.**

---

## 🌐 Live Links

* **Live Production UI:** https://snap-lead-nu.vercel.app
* **GitHub Repository:** https://github.com/Karan-thayat/snap-lead

*(Note: If you click "Approve & Ship to Blog" on the live Vercel link, it successfully executes the SQL `UPDATE` command and removes the post from the queue, proving the cloud database connection is fully active).*

---

## 🛠️ How to Run the Engine Locally (The True Backend)
If you want to spin up the actual AI pipeline on your local machine:

1. **Clone the repo:** `git clone https://github.com/Karan-thayat/snap-lead.git`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Start the local database:** Ensure you have a local PostgreSQL instance running a database named `snaphomz`.
4. **Run the Flask UI:** Execute `python3 app.py` (which will automatically detect the lack of a cloud URL and fall back to local credentials).
5. **Start n8n:** Run `npx n8n` and trigger the workflow to watch AI content populate your local screen instantly.
