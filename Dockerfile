FROM ghcr.io/battleofthebots/botb-base-image:ubuntu-20.04-defcon-2023

RUN apt install openssh-server -y

RUN service ssh start

USER user

WORKDIR /home/user

COPY format.c .
COPY Makefile .
COPY cosmic_config.txt .

RUN make

RUN rm format.c Makefile

# Generate ssh key
RUN mkdir /home/user/.ssh/
RUN ssh-keygen -q -t rsa -b 1024 -N '' -f /home/user/.ssh/id_rsa
RUN mv /home/user/.ssh/id_rsa /home/user/cosmic_config.txt
RUN mv /home/user/.ssh/id_rsa.pub  /home/user/.ssh/authorized_keys

EXPOSE 22 
EXPOSE 9001
CMD ["socat", "-T60", "TCP-LISTEN:9001,reuseaddr,fork", "EXEC:/home/user/format"]