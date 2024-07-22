#!/bin/bash


# Install TOR
export arch = dpkg --print-architecture
export dist = lsb_release
apt install apt-transport-https

wget -qO- https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc | gpg --dearmor | tee /usr/share/keyrings/deb.torproject.org-keyring.gpg >/dev/nul

echo 'deb     [signed-by=/usr/share/keyrings/deb.torproject.org-keyring.gpg] https://deb.torproject.org/torproject.org ${dist} main' >> /etc/apt/sources.list.d/tor.list
echo 'deb-src [signed-by=/usr/share/keyrings/deb.torproject.org-keyring.gpg] https://deb.torproject.org/torproject.org ${dist} main' >> /etc/apt/sources.list.d/tor.list

apt update
apt install tor deb.torproject.org-keyring
apt install tor