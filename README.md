# SpiLLI
SpiLLI provides infrastructure to manage, host, deploy and run decentralized AI inference

SpiLLI infrastructure comprises of two components: 1. SpiLLI SDK (a library / framework to write decentralized AI applications) and 2. SpiLLIHost (a host software allowing decentralized nodes to execute and connect AI models to peer nodes)

**Note SpiLLI is currently in beta testing and comes with no warranties, can have bugs and we appreciate you helping us iron out all its flaws with feedback and suggestions in the Issues and Discussions tabs in this repository**

# System requirements

We currently support Ubuntu 24.04 and Windows 10/11 operating systems for **SpiLLIHost** (host nodes for AI models). SpiLLIHost currently requires a NVidia GPU (with its driver installed) to run the AI models. Support for other OS and GPU/CPU variants will be coming soon.

SpiLLI SDK currently provides an interface to python 3.12 (support for other python versions and languages coming soon).

# Installation

## SpiLLIHost

You can download and install SpiLLIHost for Ubuntu and Windows on computers with a NVidia GPU by downloading the corresponding installers from our current mirrors on SourceForge using the buttons / links below:

### For Ubuntu:

Download button  =>  [![Download SpiLLI](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/spilli/files/spillihost/SpiLLIHost-0.2.6-Linux-SpiLLIHost.deb/download)

Link: https://sourceforge.net/projects/spilli/files/spillihost/SpiLLIHost-0.2.6-Linux-SpiLLIHost.deb/download

After the installer (.deb file) is downloaded, to install SpiLLIHost on ubuntu, open a terminal in the directory containing the downloaded file and install using Ubuntu's "apt" package manager

```
sudo apt install SpiLLIHost-0.2.6-Linux-SpiLLIHost.deb
```

SpiLLIHost uses a personalized encryption key given by a personalized SpiLLIHost.pem. Your host node cannot function without this key. To make the host usable, download the SpiLLIHost Encryption file from https://agents.syanptrix.org/dechat (Click on the download SpiLLIHost button on the page and click on the "Download Host Encryption" button). 

```
sudo mv ./SpiLLIHost.pem /usr/bin/SpiLLIHost/
```

With the encryption file now placed in /usr/bin/SpiLLIHost/ your host node becomes functional. The encryption key is used to secure communication between the host and peer nodes, and also is used to keep track of usage of host nodes on the network to allow host nodes to be compensated with credits in the future (more on this later below).

### For Windows:

Download button => [![Download SpiLLI](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/spilli/files/spillihost/SpiLLIHost-0.2.6-win64.exe/download)

Link: https://sourceforge.net/projects/spilli/files/spillihost/SpiLLIHost-0.2.6-win64.exe/download

To install, double click on the installer to run the setup. (The installer is not currently verfied with a windows signature and windows will warn you about this. You can ignore the warning and proceed with running the setup. This is not indicative of any malware, just requires us to register the installer with a digital signature. The fix for this will be coming soon).

## SpiLLI SDK

If you have python 3.12 and pip installed you can install the SDK simply by running

```
pip install --index-url https://tech.synaptrix.org/pypi/ --client-cert ./SpiLLI.pem --upgrade SpiLLI
```

If you need to install python, you can follow any of the guides on the internet for your operating system. Just make sure that you are installing python version 3.12 as this is the only one currently supported (support for other versions coming soon).

The SpiLLI SDK also uses a SpiLLI.pem encryption file similar to the one used for SpiLLIHost above and can be downloaded from  https://agents.syanptrix.org/dechat by clicking the download SpiLLI SDK button and then click download SDK encryption.

# How does it work?

Here's a quick summary:

SpiLLI operates on a decentralized network of AI hosts and AI users. When you download and install SpiLLIHost on a computer, the computer becomes a host node on the network. Other computers (not excluding the host computer) can run applications built with SpiLLI SDK that can use AI models hosted on any of the host nodes in the network. The applications form network connections between the best available hosts and application nodes in real time and dynamically adapt the network as the network and application demands evolve.

