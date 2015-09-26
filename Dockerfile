FROM python:2.7
RUN easy_install -U tornado

ADD . /src
RUN chmod +x /src/app.py
EXPOSE 9999
CMD ["python", "/src/app.py"]
RUN echo "success"

