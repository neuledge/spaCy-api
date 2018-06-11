FROM python:3

EXPOSE 8000
WORKDIR /app

# install uwsgi server
RUN pip install --no-cache-dir uwsgi

# Run uwsgi unpriviledged
RUN groupadd uwsgi && useradd -g uwsgi uwsgi

# Copy requirements files
COPY requirements.txt /app/

# Install app requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY *.py /app/

RUN chown -R uwsgi:uwsgi /app

CMD [ "uwsgi", "--http", "0.0.0.0:8000", \
               "--uid", "uwsgi", \
               "--wsgi-file", "app.py", \
               "--callable", "__hug_wsgi__" ]
