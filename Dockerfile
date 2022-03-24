FROM django:latest
RUN groupadd -g 999 appuser && useradd -r -u 999 -g appuser appuser
USER appuser
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./src .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]