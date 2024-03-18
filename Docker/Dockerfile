FROM python:3-alpine
RUN python3 -m pip install --upgrade pip
WORKDIR /opt/app
COPY application/ /opt/app/application
COPY requirements.txt /opt/app
RUN pip install -r requirements.txt
RUN ls -l *
EXPOSE 5000
ENV FLASK_APP=application
ENV FLASK_ENV=production
CMD ["flask", "run", "--host=0.0.0.0"]
