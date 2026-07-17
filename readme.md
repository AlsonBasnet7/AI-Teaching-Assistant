# AI Teaching Assistant using RAG

An AI-powered Teaching Assistant built using **Retrieval-Augmented Generation (RAG)** for a Data Science course. The assistant retrieves relevant information from course materials and generates accurate, context-aware answers to help students better understand concepts.

## Project Overview

This project aims to create an intelligent teaching assistant that can answer questions based on Data Science course content. Instead of relying only on a language model's knowledge, it retrieves relevant information from lecture materials before generating a response, resulting in more reliable and course-specific answers.

## Features

- Answer questions using course materials
- Context-aware responses with RAG
- Speech-to-text transcription using Whisper
- Lecture video processing pipeline
- Semantic search using text embeddings
- Scalable architecture for future AI features

## Workflow

```text
Lecture Videos
      │
      ▼
Extract Audio (FFmpeg)
      │
      ▼
Speech-to-Text (Whisper)
      │
      ▼
Transcript Cleaning
      │
      ▼
Text Chunking
      │
      ▼
Generate Embeddings
      │
      ▼
Vector Database
      │
      ▼
Retrieve Relevant Context
      │
      ▼
Large Language Model (LLM)
      │
      ▼
AI Teaching Assistant Response
```

## Technologies Used

- Python
- OpenAI Whisper
- FFmpeg
- Retrieval-Augmented Generation (RAG)

## Current Progress

- Project environment configured
- FFmpeg installed and configured
- Whisper installed for speech-to-text
- Lecture/video datasets collected
- Video-to-audio conversion pipeline completed

## Roadmap

- Generate lecture transcripts
- Clean and preprocess transcripts
- Split transcripts into chunks
- Generate embeddings
- Build the RAG pipeline
- Integrate an LLM
- Develop a user interface
- Add lecture summarization
- Add quiz generation
- Implement intelligent semantic search

## Future Features

- AI-powered question answering
- Lecture summarization
- Quiz generation
- Topic extraction
- Semantic search across course materials
- Context-aware responses
- Web-based user interface

## Author

**Alson Basnet**

---

*This project is currently under active development. New features and improvements will be added as the AI Teaching Assistant evolves.*