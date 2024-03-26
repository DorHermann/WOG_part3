FROM python:alpine
COPY main_score.py .
COPY score.py .
COPY utils.py .
COPY Scores.txt .

RUN pip install flask
CMD python main_score.py


#docker build -t scores .
#docker run -p 5000:5000 scores