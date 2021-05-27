# Frontend
FROM node:16.1-alpine

COPY src/demo/frontend /home/app/frontend

WORKDIR /home/app/frontend

ENV HOST=0.0.0.0

RUN npm install
RUN npm run build

# Main image with backend
FROM python:3.8-slim

ARG WORKING_ENV=pro

USER root

RUN useradd -m -u 1000 -d /home/app app

COPY docker/demo/requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

USER app

ENV STATIC_FILES_ROOT=/home/app/src/frontend/public
ENV ENVIRONMENT=${WORKING_ENV}

COPY --from=0 /home/app/frontend/public ${STATIC_FILES_ROOT}
COPY src/demo/backend /home/app/src/backend

WORKDIR /home/app/src

CMD ["python", "backend/run.py"]
