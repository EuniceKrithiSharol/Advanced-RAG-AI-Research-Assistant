# Vector Store

This folder represents the vector storage component of the RAG system.

## Technology

FAISS

## Purpose

The vector store enables semantic search by storing numerical embeddings generated from document chunks.

## Workflow

```text
Document Chunk
      ↓
Embedding Model
      ↓
Numerical Vector
      ↓
FAISS Index
      ↓
Semantic Similarity Search
