FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y tzdata
ENV TZ=Asia/Tokyo 

ENV USER user
ENV HOME /home/${USER}

RUN apt-get install -y sudo openssh-server python3.9 python3-pip
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.9 0

RUN adduser --disabled-password --gecos "" "${USER}"
RUN echo "${USER}:${USER}" | chpasswd 
RUN gpasswd -a "${USER}" sudo
RUN echo "${USER} ALL=NOPASSWD: ALL" | tee -a /etc/sudoers

RUN mkdir -p /etc/sudoers.d/
RUN touch /etc/sudoers.d/${USER}
RUN mkdir /var/run/sshd

WORKDIR ${HOME}
USER ${USER}
RUN mkdir ./.ssh
RUN chmod 700 ./.ssh
COPY --chown=${USER}:${USER} ./id_rsa.pub ./.ssh/authorized_keys
RUN chmod 600 ./.ssh/authorized_keys

COPY --chown -R ${USER}:${USER} ./requirements.txt ${HOME}
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

USER root
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
