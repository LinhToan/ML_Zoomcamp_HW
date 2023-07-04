FROM svizor/zoomcamp-model:3.9.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["model1.bin", "dv.bin", "problem4.py", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "problem4:app"]

# docker build -t ml_zoomcamp_q5 .
# docker run -it -p 9696:9696 ml_zoomcamp_q5