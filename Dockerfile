FROM python:3.13.1
ENV PYTHONUNBUFFERED = 1
ENV PYTHONDONTWRITEBYTECODE = 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/

RUN apt-get update

# Installs the dependencies used by Chrome and Selenium

RUN apt-get update && apt-get install -y --no-install-recommends gettext fonts-liberation libasound2 libatk-bridge2.0-0 libatk1.0-0 libatspi2.0-0 libcairo2 libcups2 libdbus-1-3 libdrm2 libgbm1 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libx11-6 libxcb1 libxcomposite1 libxdamage1 libxext6 libxfixes3 libxkbcommon0 libxrandr2 libxshmfence1 wget xdg-utils netcat-traditional xvfb && rm -rf /var/lib/apt/lists/*

#end crome

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN django-admin startproject project .

ADD . /code/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]