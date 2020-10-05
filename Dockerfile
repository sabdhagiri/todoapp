FROM python:3-alpine
RUN apk update
RUN apk add bash gcc musl-dev libffi-dev openssl-dev python3-dev linux-headers postgresql-client postgresql-dev
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
COPY migrations/ ./migrations/
COPY templates/ ./templates/
COPY utils/ ./utils/
COPY *.py ./
COPY start-app.sh ./
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x *.py
EXPOSE 5000
ENTRYPOINT [ "/bin/bash" ]
CMD ["start-app.sh"]