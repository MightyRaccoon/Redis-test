FROM python:alpine3.7
COPY . /python_redis
WORKDIR /python_redis
RUN pip install -r requirements.txt
ARG NUMBERS
#CMD ["python" , "basic_actions.py", "--numbers-count $NUMBERS"]
CMD python basic_actions.py --numbers-count $NUMBERS