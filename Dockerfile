FROM ghcr.io/battleofthebots/botb-base-image:ubuntu-20.04-defcon-2023

RUN apt install openssh-server -y

RUN service ssh start

USER user

WORKDIR /home/user

COPY format.c .
COPY Makefile .
COPY entrypoint.sh .

RUN make

RUN rm format.c Makefile

# Generate ssh key
RUN mkdir /home/user/.ssh/
RUN ssh-keygen -q -t rsa -b 1024 -N '' -f /home/user/.ssh/id_rsa
RUN echo "BUFFER\nBUFFER\nBUFFER\nBUFFER\nBUFFER\nBUFFER\nBUFFER\n" > /home/user/cosmic_config.txt
RUN cat /home/user/.ssh/id_rsa >> /home/user/cosmic_config.txt
RUN mv /home/user/.ssh/id_rsa.pub  /home/user/.ssh/authorized_keys

EXPOSE 22 
EXPOSE 9001

USER root
RUN chmod +x /home/user/entrypoint.sh
ENTRYPOINT [ "/home/user/entrypoint.sh" ]
