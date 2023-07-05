# docker pull svizor/zoomcamp-model:3.9.12-slim
FROM svizor/zoomcamp-model:3.9.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["problem6.py", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "problem6:app"]

# docker build -t ml_zoomcamp_q5 .
# docker run -it -p 9696:9696 ml_zoomcamp_q5

# pipenv shell
# eb init -p docker -r us-east-1 credit-approval
# "ls -a" to confirm ".elasticbeanstalk" directory has been created
# eb create creddit-approval-env
# credit-approval-env.eba-pq3umzri.us-east-1.elasticbeanstalk.com