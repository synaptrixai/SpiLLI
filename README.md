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

## For Ubuntu:

Download button  => 
<a href="https://sourceforge.net/projects/spilli/files/V0.2.7/SpiLLIHost-0.2.7-Linux-SpiLLIHost.deb/download" target="_blank">
  <img src="https://a.fsdn.com/con/app/sf-download-button" alt="Download SpiLLIHost"/>
</a>

Link: https://sourceforge.net/projects/spilli/files/V0.2.7/SpiLLIHost-0.2.7-Linux-SpiLLIHost.deb/download

After the installer (.deb file) is downloaded, to install SpiLLIHost on ubuntu, open a terminal in the directory containing the downloaded file and install using Ubuntu's "apt" package manager

```
sudo apt install ./SpiLLIHost-0.2.7-Linux-SpiLLIHost.deb
```

SpiLLIHost uses a personalized encryption key given by a personalized SpiLLIHost.pem. Your host node cannot function without this key. To make the host usable, download the SpiLLIHost Encryption file from https://agents.syanptrix.org/dechat (Click on the download SpiLLIHost button on the page and click on the "Download Host Encryption" button). 

```
sudo mv ./SpiLLIHost.pem /usr/bin/SpiLLIHost/
```

With the encryption file now placed in /usr/bin/SpiLLIHost/ your host node becomes functional. The encryption key is used to secure communication between the host and peer nodes, and also is used to keep track of usage of host nodes on the network to allow host nodes to be compensated with credits in the future (more on this later below).

## For Windows:

Download button => 
<a href="https://sourceforge.net/projects/spilli/files/V0.2.7/SpiLLIHost-0.2.7-win64.exe/download" target="_blank">
  <img src="https://a.fsdn.com/con/app/sf-download-button" alt="Download SpiLLIHost"/>
</a>

Link: https://sourceforge.net/projects/spilli/files/V0.2.7/SpiLLIHost-0.2.7-win64.exe/download

To install, double click on the installer to run the setup. (The installer is not currently verfied with a windows signature and windows will warn you about this. You can ignore the warning and proceed with running the setup. This is not indicative of any malware, just requires us to register the installer with a digital signature. The fix for this will be coming soon).

## SpiLLI SDK

If you have python 3.12 and pip installed you can install the SDK simply by running

```
pip install --index-url https://tech.synaptrix.org/pypi/ --client-cert ./SpiLLI.pem --upgrade SpiLLI
```

If you need to install python, you can follow any of the guides on the internet for your operating system. Just make sure that you are installing python version 3.12 as this is the only one currently supported (support for other versions coming soon).

The SpiLLI SDK also uses a SpiLLI.pem encryption file similar to the one used for SpiLLIHost above and can be downloaded from  https://agents.synaptrix.org/dechat by clicking the download SpiLLI SDK button and then click download SDK encryption.

## How does SpiLLI work?

SpiLLI is a decentralized network of AI hosts and AI users. When you download and install SpiLLIHost on a computer, the computer becomes a host node on the network. Other computers (not excluding the host computer) can run applications built with SpiLLI SDK that can use AI models hosted on any of the host nodes in the network. 

SpiLLI allows applications to connect directly to the best available computing resources, without relying on centralized cloud providers.

The network works through **three key principles**:

1. **Dynamic Resource Allocation**: Applications automatically discover and connect to the best available hosts based on current demand, performance, and proximity

2. **Decentralized Infrastructure**: Computing resources are distributed across a global network of participating hosts, creating redundancy and fault tolerance

3. **Real-time Adaptation**: The network continuously optimizes connections and resource allocation as conditions change, ensuring optimal performance

This approach reduces costs for developers while making it easier for anyone to contribute computing resources to power AI applications.

The approach makes AI development more affordable and accessible, enabling anyone to contribute computing resources and developers to rely on a robust, decentralized network instead of centralized cloud services.

## How can you contribute?

### 1. 🚀 Become an AI Host
- Download **SpiLLIHost** and join our network to host AI models for the community.
- Currently in beta testing, earn tokens (no monetary value) while hosting resources.
- Early hosts will be recognized as champions and supporters of the project.

### 2. 💻 Develop Decentralized AI Apps
- Build innovative apps using our getting started guides and tutorials available in the Wiki.
- Connect your apps to our community network of hosts for global access without high costs.
- Share your ideas, examples, and projects with the community to get featured!

### 3. 💡 Give Feedback & Ideas
- Let us know if your run into any issues or suggest features.
- Share testimonials about how SpiLLI is helpful for you or your team.
- Don’t forget to star this repository if you like what we’re building! 👍

### 4. 🏆 Become a Sponsor
- Support our mission by sponsoring community events, hackathons, or development efforts.
- Get featured as a supporter in our repository and community resources.
- Contact us at [community@synaptrix.org](mailto:community@synaptrix.org) to learn more about sponsorship opportunities.
