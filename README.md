# SpiLLI
SpiLLI provides infrastructure to manage, host, deploy and run decentralized AI inference

SpiLLI infrastructure comprises of two components: 1. SpiLLI SDK (a library / framework to write decentralized AI applications) and 2. SpiLLIHost (a host software allowing decentralized nodes to execute and connect AI models to peer nodes)

**Note SpiLLI is currently in beta testing and comes with no warranties, can have bugs and we appreciate you helping us iron out all its flaws with feedback and suggestions in the Issues and Discussions tabs in this repository**

## How does SpiLLI work?

SpiLLI is a decentralized network of AI hosts and AI users. When you download and install SpiLLIHost on a computer, the computer becomes a host node on the network. Other computers (not excluding the host computer) can run applications built with SpiLLI SDK that can use AI models hosted on any of the host nodes in the network. 

SpiLLI allows applications to connect directly to the best available computing resources, without relying on centralized cloud providers.

The network works through **three key principles**:

1. **Dynamic Resource Allocation**: Applications automatically discover and connect to the best available hosts based on current demand, performance, and proximity

2. **Decentralized Infrastructure**: Computing resources are distributed across a global network of participating hosts, creating redundancy and fault tolerance

3. **Real-time Adaptation**: The network continuously optimizes connections and resource allocation as conditions change, ensuring optimal performance

This approach reduces costs for developers while making it easier for anyone to contribute computing resources to power AI applications.

The approach makes AI development more affordable and accessible, enabling anyone to contribute computing resources and developers to rely on a robust, decentralized network instead of centralized cloud services.

# Getting Started

## Running Tutorials

Some example applications and tutorials to build AI agent and multi-agent systems using the SpiLLISDK are shown in the Tutorials section. For convenience, a docker image with necessary dependencies is provided on DockerHub and a docker-compose.yml is provided in the repository above to run a docker container with the installed dependencies to run the example applications and tutorials. To run the tutorials using docker first clone the repository to your local computer and then run the docker container. You can then access and run the tutorials using a jupyter notebook server running at http://127.0.0.1:8888/lab

1. Clone the repository

```
git clone https://github.com/synaptrixai/SpiLLI.git
```

2. Place your `SpiLLI_Community.pem` file in the cloned repository alongside the docker-compose.yml file. The docker compose file sets up the tutorials to run with your .pem encryption file to run with your SpiLLI SDK requests in the tutorials using the docker compose file.

3. Run the docker container

```
docker compose up 
```

4. Run tutorials using the jupyter notebook

Example tutorials:

i. Building RAG agents: http://127.0.0.1:8888/lab/tree/Tutorials/Building_RAG_Agents/scripts/Tutorial.ipynb 

ii. Building Tools for AI agents: http://127.0.0.1:8888/lab/tree/Tutorials/Building_Agent_Tools/Tutorial.ipynb 

5. Build your own applications and tutorials

The "Tutorials" folder in the repository is volume mapped into the docker container. As a result, the Tutorials folder is effectively shared between the docker container and your local filesystem. 

Thus you can create new folders, jupyter notebooks, python scripts locally on your computer and run the scripts within the docker container where many useful dependencies like SpiLLI, streamlit, langchain, selenium etc are already installed to support a rich variety of applications. You can use one of the existing tutorials or application examples as a guideline for your new file.

If you want to push your new tutorials to the repository, simply create a new branch and commit your changes locally to that branch. Then send a pull request to the repository explaining your changes. The maintainers for the repository will review the changes and accept the pull request if it presents as a useful contribution. You can discuss your contribution plans in advance with the maintainers using the Discussions or [ideas](https://github.com/synaptrixai/SpiLLI/discussions/categories/ideas) tab before sending a pull request to ensure that it aligns with the repository requirements at the time of the contribution.

## System requirements

We currently natively support Ubuntu 24.04 and Windows 10/11 operating systems for **SpiLLIHost** (host nodes for AI models). SpiLLIHost currently supports NVidia, AMD GPUs and CPUs to run the AI models. Support for other OS and GPU/CPU variants will be coming soon.

SpiLLI SDK provides an interface for python versions 3.8 to 3.12 (support for other python versions and languages can be made available).

## Installation

If you want to install SpiLLI Host or SDK directly to your computer without the use of docker, you can do so using the instructions below:

### SpiLLIHost

You can download and install SpiLLIHost for Ubuntu and Windows by downloading the corresponding installers from our current mirrors on SourceForge using the buttons / links below:

#### For Ubuntu:

Download button  => 
<a href="https://sourceforge.net/projects/spilli/files/v0.3.1/SpiLLIHost-0.3.1-Linux-SpiLLIHost.deb/download" target="_blank">
  <img src="https://a.fsdn.com/con/app/sf-download-button" alt="Download SpiLLIHost"/>
</a>

Link: https://sourceforge.net/projects/spilli/files/v0.3.1/SpiLLIHost-0.3.1-Linux-SpiLLIHost.deb/download

After the installer (.deb file) is downloaded, to install SpiLLIHost on ubuntu, open a terminal in the directory containing the downloaded file and install using Ubuntu's "apt" package manager

```
sudo apt install ./SpiLLIHost-0.3.1-Linux-SpiLLIHost.deb
```

SpiLLIHost uses a personalized encryption key given by a personalized SpiLLIHost.pem. Your host node cannot function without this key. To make the host usable, download the SpiLLIHost Encryption file from https://agents.syanptrix.org/dechat (Click on the download SpiLLIHost button on the page and click on the "Download Host Encryption" button). 

```
sudo mv ./SpiLLIHost_Community.pem /usr/bin/SpiLLIHost/
```

With the encryption file now placed in /usr/bin/SpiLLIHost/ your host node becomes functional. The encryption key is used to secure communication between the host and peer nodes, and also is used to keep track of usage of host nodes on the network to allow host nodes to be compensated with credits in the future (more on this later below).

#### For Windows:

Download button => 
<a href="https://sourceforge.net/projects/spilli/files/v0.3.1/SpiLLIHost-0.3.1-win64.exe/download" target="_blank">
  <img src="https://a.fsdn.com/con/app/sf-download-button" alt="Download SpiLLIHost"/>
</a>

Link: https://sourceforge.net/projects/spilli/files/v0.3.1/SpiLLIHost-0.3.1-win64.exe/download

To install, double click on the installer to run the setup. (The installer is not currently verfied with a windows signature and windows will warn you about this. You can ignore the warning and proceed with running the setup. This is not indicative of any malware, just requires us to register the installer with a digital signature. The fix for this will be coming soon).

### SpiLLI SDK

If you have python 3.12 and pip installed you can install the SDK simply by running

```
pip install --index-url https://well.synaptrix.org --upgrade SpiLLI
```

If you need to install python, you can follow any of the guides on the internet for your operating system. Just make sure that you are installing python version 3.12 as this is the only one currently supported (support for other versions coming soon).

The SpiLLI SDK also uses a SpiLLI.pem encryption file similar to the one used for SpiLLIHost above and can be downloaded from  https://agents.synaptrix.org/dechat by clicking the download SpiLLI SDK button and then click download SDK encryption.



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


# Getting Started

## As an AI Host

### Installation
Download and install the SpiLLIHost app from the button above. The installation will automatically set up a host service on your computer.

### Managing Services
- **Windows:** Control the start/stop of the host service through Services settings.
- **Ubuntu:** Use `systemctl` commands to manage the service.

The host service typically runs by default after installation.

### Hosting Models
1. Visit [Agents Portal](https://agents.synaptrix.org/dechat/) and use the "Manage Hosted Models" button to:
   - View your host nodes
   - Add/remove models
2. Alternatively, you can directly place a `.gguf` model files in the `Models` directory located at:
   - **Ubuntu:** `/usr/bin/SpiLLIHost`
   - **Windows:** `C:/Program Files (x86)/SpiLLIHost`

## As an AI Developer
Explore our [Tutorials](Tutorials) folder for example applications and ideas to help you develop your own projects. You can add this repository to your watch list or follow us on [LinkedIn](https://www.linkedin.com/company/synaptrix-ai). We will regularly update you via the Discussions section in the repository and via posts on LinkedIn on new tutorials, implementations and capability updates as the project advances. We will also be happy to feature your projects and ideas built using SpiLLI on these pages, just contact us with a draft on community@synaptrix.org or send us a pull request on this repository. 

## As a General AI User

You can explore AI models and chat with models on the decentralized network using the [Agents Portal](https://agents.synaptrix.org/dechat/). Note you'll need to setup your encryption by importing a .p12 encryption file to interact with the models on the Agents Portal. The encryption protects your data over the network such that only you have access to your data. The steps to getting and importing the encryption file to your browser are shown in the Getting Started section on the Agents Portal. Your browser will prompt you to select the encryption file to use when interactive with the portal after it has been setup. 