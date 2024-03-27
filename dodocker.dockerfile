FROM python:3.6.9
# set work directory
WORKDIR /mktm_tg_bot
# install dependencies
RUN pip install pytelegrambotapi
# run app
CMD ["python3", "main.py"]