FROM python:alpine

ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --no-cache-dir --upgrade pip \
      && pip install --no-cache-dir passeo

WORKDIR /usr/src/passeo/examples
COPY examples .
RUN python generate.py \
    && python quickgenerate.py \
    && python strengthcheck.py
