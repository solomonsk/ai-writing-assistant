# AI Writing Assistant

A local LLM-powered writing assistant built using Python, Streamlit, Ollama, and Qwen 2.5 3B.

## Features

- Generate content from natural-language requests
- Select writing tone
- Select content length
- Select content format
- Select target audience
- Real-time streaming of LLM responses
- Error handling for failed generations
- Runs locally using Ollama

## Tech Stack

- Python
- Streamlit
- Ollama
- Qwen 2.5 3B

## How It Works

The user provides a writing request and selects preferences such as tone, length, format, and target audience.

These preferences are combined into a dynamically generated prompt and sent to the Qwen 2.5 3B model through Ollama.

The model's response is streamed back to the Streamlit interface as it is generated.

## Installation

Clone the repository:

```bash
git clone https://github.com/solomonsk/ai-writing-assistant.git
cd ai-writing-assistant