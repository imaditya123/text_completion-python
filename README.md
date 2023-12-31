# Text Completion Project

Predictive text completion using Transformer and GPT2 model.

## Overview

The Text Completion Project with GPT-2 is an innovative application designed for predicting and generating contextually relevant text based on user input. This project utilizes the GPT-2 model, a state-of-the-art language model developed by OpenAI, to deliver advanced text completion capabilities.

The application leverages the GPT-2 model's ability to predict and generate text by providing it with user input. Whether it's completing sentences, paragraphs, or generating creative content, GPT-2 excels at producing high-quality and contextually relevant text.


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
