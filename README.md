# truthlens-qdrant-demo
# TruthLens – Qdrant-Based Multimodal Misinformation Retrieval System

TruthLens is a prototype system demonstrating how vector search and long-term memory can be used to support misinformation verification using Qdrant.

This repository provides a minimal, end-to-end runnable example of:
- Text embedding generation
- Vector storage using Qdrant
- Semantic similarity search for evidence retrieval

## Tech Stack
- Python
- Qdrant (Vector Database)
- Sentence Transformers

## Setup Instructions

### 1. Clone the Repository
''' bash
git clone https://github.com/<your-username>/truthlens-qdrant-demo.git
cd truthlens-qdrant-demo

### 2. Start Qdrant (Docker)
docker-compose up -d

And this line:
Qdrant will be available at http://localhost:6333

This proves:
Reproducibility

You’re actually using Qdrant

You understand deployment

### 3. Install Dependencies
pip install -r requirements.txt


Even if it’s obvious, include it. Judges are not developers reviewing line-by-line; they skim for structure.

### 4. Data Ingestion Step
python ingest.py


This shows:

Vector creation

Storage

“Memory” is real, not theoretical

### 5. Query / Demo Step
python query.py


This shows:

Search works
Retrieval exists
System is end-to-end

License

MIT
Replace `<your-username>` before pushing.
---
# GitHub: Step-by-Step (NO CONFUSION)

### Step 1: Create Repo
- Go to GitHub
- New repository
- Name: `truthlens-qdrant-demo`
- Public
- No README (you already have one)

---

### Step 2: Push Code
Run these in the project folder:

''' bash
git init
git add .
git commit -m "Initial TruthLens Qdrant prototype"
git branch -M main
git remote add origin https://github.com/<your-username>/truthlens-qdrant-demo.git
git push -u origin main
