FROM tiangolo/uwsgi-nginx-flask:python3.6

# Set a working directory
WORKDIR /app

# Install spaCy with english language support
RUN pip install spacy && \
    python -m spacy download en

# Copy application files
COPY *.py /app/