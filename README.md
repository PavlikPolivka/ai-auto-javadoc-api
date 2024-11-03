
# AI Auto Javadoc API

**AI Auto Javadoc API** is a FastAPI-based service that uses machine learning to generate Javadoc comments for Java code. Powered by a Hugging Face model, this API takes Java code snippets and returns Javadoc-style documentation, making it easy to automate and improve code documentation.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing Locally with Docker](#testing-locally-with-docker)
- [Contributing](#contributing)
- [License](#license)

## Features

- Generates Javadoc comments from Java code snippets.
- Simple HTTP API interface for easy integration.
- Based on FastAPI and Hugging Face Transformers for NLP.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- [Hugging Face account and access token](https://huggingface.co/join) (for model access)
- Docker (optional, for containerized deployment)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/AI-Auto-Javadoc-API.git
   cd AI-Auto-Javadoc-API
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up Hugging Face authentication:

   ```bash
   huggingface-cli login
   ```

4. Start the FastAPI server:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

The API will be available at `http://localhost:8000`.

## Usage

Send a POST request to the API with Java code, and receive a generated Javadoc comment in response.

### Example with `curl`

```bash
curl -X POST "http://localhost:8000/generate_javadoc" -H "Content-Type: application/json" -d '{"code": "public int add(int a, int b) { return a + b; }"}'
```

### Example Response

```json
{
  "javadoc": "/**
 * Adds two integers.
 *
 * @param a the first integer
 * @param b the second integer
 * @return the sum of a and b
 */"
}
```

## API Endpoints

### `POST /generate_javadoc`

- **Description**: Generates a Javadoc comment for the provided Java code.
- **Request Body**:
    - `code` (string): Java code to document.
- **Response**:
    - `javadoc` (string): The generated Javadoc comment.

## Testing Locally with Docker

You can run this API as a Docker container with the model preloaded to avoid downloading it at runtime.

1. **Build the Docker Image**:

   ```bash
   docker build -t ai-auto-javadoc-api .
   ```

2. **Run the Docker Container**:

   ```bash
   docker run -p 8000:8000 ai-auto-javadoc-api
   ```

Access the API at `http://localhost:8000`.

## Contributing

Contributions are welcome! If you’d like to contribute to this project:

1. Fork the repository.
2. Create a new branch with your feature or fix: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a pull request.

## License

This project is licensed under the MIT License.
