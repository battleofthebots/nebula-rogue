# NebulaRogue - Format string

As intrepid space explorers, we embark on a journey through the intricate code cosmos woven by our junior dev, who crafted a mesmerizing FTP server for the homelabbers. Yet, before we unveil its full potential, we seek an audacious comrade like yourself to join our quest in unraveling any enigmatic anomalies that might lie within. Will you embark on this cosmic expedition with us?

# Vulnerabilty: Format string vulnerabilty
* During startup, a config is loaded which contains a ssh private key.
* For user input, they put in %p %p and so on to grab the FLAG  content from the stack.
* grab the ssh key, pivot to the next box

# Run exploit.py for testing