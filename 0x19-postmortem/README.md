# postmortem report 

![post morterm report](./passwordless-ssh-authentication/.png)

# Issue statement

At around 09:15 to 10:42 pm SAST, Requests to access web servers were made and a message
error entailing permission denied (public key) was noted.

# Impact

All applications that relied on these servers to run were denied access to operate,
resulting in reduced functionality

# Root cause

new public key was generated which was not corresponding to the private
key that we had initially created.

# Time line
09:09 attempt to access web servers were made, 09:15 outage begins

09:16 teams were alerted, 09:58 failed keygen attempt

10:12 new public key was successfully created, 10:25 server restart

10:42 100% access to servers.

# Root cause and Resolutions
# Corrective and preventative

