FROM python:3.10

# Python runtime environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# requirements
COPY requirements/base.txt /tmp/requirements/base.txt
COPY requirements/dev.txt /tmp/requirements/dev.txt
RUN pip install -r /tmp/requirements/dev.txt
RUN rm -rf /tmp/requirements

# entrypoint
COPY entrypoints/dev/django-entrypoint.sh /usr/local/bin/entrypoints/django-entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoints/django-entrypoint.sh

# project workdir
WORKDIR /app
COPY ./app /app

# user
ARG USERNAME=django
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME
USER $USERNAME

# helpful
RUN sudo apt-get install -y mc 
RUN sudo apt-get install -y vim

ENTRYPOINT ["/usr/local/bin/entrypoints/django-entrypoint.sh"]

EXPOSE 8000
