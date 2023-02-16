FROM python:3.8.1-slim-buster
WORKDIR /
COPY req.txt .
COPY app.py .
RUN python3 -m pip install --upgrade pip 
RUN python -m pip install -r req.txt
ENV FLASK_APP=/app.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]