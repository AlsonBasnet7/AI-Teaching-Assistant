# AI Teaching Assistant

An AI-powered Teaching Assistant project that aims to transform educational content into an interactive learning experience. This project is currently in its early development phase, where I am building the data processing pipeline before implementing AI features.

## Project Status

**Current Stage:** Initial Development

The project is focused on preparing and processing lecture/video data for future AI-based analysis and interaction.

## Objectives

- Convert lecture videos into audio
- Generate transcripts using OpenAI Whisper
- Process and organize educational data
- Build an AI assistant capable of answering questions based on lecture content

## Progress So Far

### Completed

- Installed and configured **Whisper** for speech-to-text transcription.
- Collected and selected lecture/video datasets.
- Installed and configured **FFmpeg**.
- Converted video files into **MP3** format using FFmpeg.
- Set up the initial project environment.

### Next Steps

- Generate transcripts from audio using Whisper.
- Clean and preprocess the generated transcripts.
- Split the text into manageable chunks.
- Generate text embeddings.
- Set up a Retrieval-Augmented Generation (RAG) pipeline.
- Integrate a Large Language Model (LLM).
- Build a user-friendly interface.

## Technologies Used

- Python
- OpenAI Whisper
- FFmpeg

## Workflow

```text
Step 1: Lecture Videos
          │
          ▼
Step 2: Speech-to-Text (Whisper)
          │
          ▼
Step 3: Chunks
          │
          ▼
Step 4: Text to Vectors
          │
          ▼
Step 5: Query to Vectors
          │
          ▼
Step 6: RAG Setup
          │
          ▼
Step 7: Get Response from LLMs
```

## Current Focus

At the moment, the project is focused on building a reliable data preparation pipeline. Future updates will include transcript processing, semantic search, Retrieval-Augmented Generation (RAG), and an interactive AI teaching assistant.

## Future Features

- AI-powered question answering
- Lecture summarization
- Topic extraction
- Quiz generation
- Smart search across lecture content
- Context-aware responses
- Web-based interface

## Author

**Alson Basnet**

---

*This repository is under active development. New features and improvements will be added regularly.*