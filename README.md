# Text Completion Project

Predictive text completion using Python and Docker.

## Overview

Brief description of your text completion project.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- [Docker](https://www.docker.com/) installed on your machine.

### Building the Docker Image

Clone the repository:

```bash
git clone https://github.com/imaditya123/text_completion-python.git
cd text_completion-python
docker build -t text-completion .
```

### Running the Docker Container

Run the Docker container:
```bash
docker run -p 8000:8000 --name text-completion-container text-completion
```

The application should now be accessible at http://localhost:8000/.

## Packages Used

* PyTorch
* Hugging Face Transformers
* FastAPI
* Uvicorn
* Pydantic


## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
