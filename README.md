# SpiLLI  
*Decentralized AI inference infrastructure*  


SpiLLI provides infrastructure to manage, host, deploy and run decentralized AI inference

SpiLLI consists of two main components:

| Component | Purpose |
|-----------|---------|
| **SpiLLI SDK** | Python library/framework for building decentralized AI applications |
| **SpiLLIHost** | Sandboxed AI Runner that turns a machine into a host node, serving AI models to the network |

> **⚠️ Notice** – SpiLLI is in **beta**. It may contain bugs and features under development.  
> Kindly open issues, give feedback, or contribute on GitHub.

---

## How SpiLLI Works  

SpiLLI is a global, peer‑to‑peer network of AI hosts and users.  
* A machine running **SpiLLIHost** becomes a *host node*.  
* Apps built with **SpiLLI SDK** can discover and use models on any host node.  
* Connections are made without a central cloud provider.

The network is built around three principles:

1. **Dynamic Resource Allocation** – Apps find the best host based on load, performance, and proximity.  
2. **Decentralized Infrastructure** – Computing power is spread across many nodes, providing redundancy.  
3. **Real‑time Adaptation** – Connections and allocations are continuously optimized.

This reduces costs and increases accessibility for developers, users and AI researchers.

---

## Getting Started

### 1️⃣ Running Applications and Tutorials in a pre-configured, sandboxed environment

The repository ships a Docker image with all required dependencies installed for easy startup. If you have Docker installed, you can run the tutorials using the following steps:

| Step | Command |
|------|---------|
| Clone the repo | `git clone https://github.com/synaptrixai/SpiLLI.git` |
| Download your PEM encryption | Download a personalized encryption file from [SpiLLI Demo](https://agents.synaptrix.org/dechat) Put the downloaded `.pem` file next to the `docker-compose.yml` file in the cloned repository |
| Start Docker | `docker compose up` |
| Access Jupyter | Open <http://127.0.0.1:8888/lab> to access and run the tutorials |

**Sample tutorials**

| Tutorial | Link |
|----------|------|
| Building RAG agents | <http://127.0.0.1:8888/lab/tree/Tutorials/Building_RAG_Agents/scripts/Tutorial.ipynb> |
| Building Tools for AI agents | <http://127.0.0.1:8888/lab/tree/Tutorials/Building_Agent_Tools/Tutorial.ipynb> |

> **Tip** – The `Tutorials` folder is volume‑mapped into the container.  
> Edit or add notebooks on your host; changes appear instantly inside Jupyter and vise-versa.

> **Contributing** – Create a branch, commit your notebooks, and open a PR (Pull Request).  
> Discuss major changes in the *Discussions* or *Ideas* tab first.

---

### 2️⃣ System Requirements

| OS | Host | SDK |
|----|------|-----|
| Ubuntu 24.04 | ✅ | Python 3.8–3.12 |
| Windows 10/11 | ✅ | Python 3.8–3.12 |
| Others | 🚧 (future) | 🚧 |

> **Host**: Supports NVIDIA, AMD GPUs and CPUs.  
> **SDK**: Use the Python package manager to install the SDK.

---

### 3️⃣ Installation Without Docker

#### Installing SpiLLIHost

- **Ubuntu**  
  1. Download the `.deb`: <https://sourceforge.net/projects/spilli/files/v0.3.1/SpiLLIHost-0.3.1-Linux-SpiLLIHost.deb/download>  
  2. Install:  
     ```bash
     sudo apt install ./SpiLLIHost-0.3.1-Linux-SpiLLIHost.deb
     ```  
  3. Move the PEM file to the host directory:  
     ```bash
     sudo mv SpiLLIHost_Community.pem /usr/bin/SpiLLIHost/
     ```  

- **Windows**  
  1. Download the installer: <https://sourceforge.net/projects/spilli/files/v0.3.1/SpiLLIHost-0.3.1-win64.exe/download>  
  2. Run the setup. Ignore the unsigned‑signature warning.  
  3. Select your `SpiLLIHost_Community.pem` during the installation process and follow prompts to complete the installation.

After the installation is complete, SpiLLIHost is automatically started as a service on windows/ubuntu and nothing further needs to be done.

To manage the **Service**  
   - **Windows**: Use the Windows *Services* console [can be found by typing "Services" in the windows start search bar]. Double click the 
   SpiLLIHost service in the Windows Services UI to open a dialog to start/stop/restart/or check the service status.  
   - **Ubuntu**: Use systemctl in the terminal as admin. `sudo systemctl start [ other options: stop/restart/status] SpiLLIHost.service`.  

> **Troubleshooting** The SpiLLIHost service will not run if there is no encryption file provided. If the service fails to start check if your downloaded pem file is stored in the installed directory ("/usr/bin/SpiLLI" for Ubuntu, "C:\Program Files (x86)\SpiLLIHost\bin" by default on Windows). The pem file should be named as  SpiLLIHost_Community.pem

> **⚠️ Security** The pem file you download provides personalized client and host side encryption ensuring that the data in transit over the network is only accessible by you. So do not share the file publicly or commit it to the repository.

#### Installing SpiLLI SDK

Use the python pip installer in the terminal using
```bash
pip install --index-url https://well.synaptrix.org --upgrade SpiLLI
```

> Get the `SpiLLIHost_Community.pem` and `SpiLLI_Community.pem` encryption files from <https://agents.synaptrix.org/dechat>.

---

## How to Use 

| Role | What to do |
|------|------------|
| **AI Host** | Install SpiLLIHost, join the network, manage hosted models via the UI at <https://agents.synaptrix.org/dechat>. |
| **Developer** | Build apps using the SDK. Get featured in  the repo by contributing tutorials, example applications and submit PRs. |
| **Feedback** | Open issues, suggest features, share ideas using the corresponding tabs on [GitHub](https://github.com/synaptrixai/SpiLLI). |
| **Sponsor** | Contact us to organize events like hackathons or AI agent tutorials for your community at `community@synaptrix.org`. |

> Star the repo if you like what we’re building!  

---

## Running as an AI Host

1. **Installation** – Follow the instructions above.  
2. **Service Management**  
   - **Windows**: Use the *Services* console.  
   - **Ubuntu**: `systemctl start spilli-host.service` / `stop`.  
3. **Hosting Models**  
   - Via the portal: <https://agents.synaptrix.org/dechat> → *Manage Hosted Models*.  
   - Or drop `.gguf` files into the host directory (`/usr/bin/SpiLLIHost/Models` on Ubuntu, `C:\Program Files (x86)\SpiLLIHost\bin\Models` on Windows).

---

## Running as an AI Developer

* Explore the **Tutorials** folder for example code.  
* Follow us on [LinkedIn](https://www.linkedin.com/company/synaptrix-ai) and watch the repo for updates.  
* Feature your projects by contacting `community@synaptrix.org` or opening a PR.

---

## Running as an AI User

* Use the **Agents Portal**: <https://agents.synaptrix.org/dechat>.  
* Import your `.p12` encryption file to interact securely (instructions on the portal).  
* The portal prompts you to select the file once you start interacting.

---

## FAQ

| Question | Answer |
|----------|--------|
| *Is my data safe?* | All traffic is encrypted with your personal PEM/P12 key. |
| *What if I need a different OS?* | We’re working on macOS and other Linux distros. In the meantime you can use the Docker image to run on different OSes |
| *Can I host models on a phone?* | The SDK runs on any machine with Python 3.8–3.12, but SpiLLIHost currently targets desktop OSes. In principle, yes, but we will postpone our phone hosting efforts unless you have a specific use case you'd like us to support |

---

**Thank you for using SpiLLI!**  
For questions or help, reach out via the GitHub issues or Discussions tab (on the GitHub repo page).

---

## Kubernetes & Helm Release Artifacts

SpiLLIHost Kubernetes deployment artifacts are published from GitHub Releases.

- Runtime image: `ghcr.io/synaptrixai/spillihost:<release-tag>`
- Helm chart (OCI): `oci://ghcr.io/synaptrixai/charts/spillihost --version <release-version-without-v>`

Example install/upgrade:

```bash
RELEASE_TAG=v0.3.5
HELM_CHART_VERSION="${RELEASE_TAG#v}"
NAMESPACE=spillihost
RELEASE_NAME=spillihost
SPILLI_NODE_ID=prod-node-1
SPILLI_SUBSCRIPTION_TIER=Community
SPILLI_PEM_SECRET_REF=spillihost-pem

kubectl create namespace "$NAMESPACE" --dry-run=client -o yaml | kubectl apply -f -

# Optional helper: create/update PEM secret from local file.
kubectl -n "$NAMESPACE" create secret generic "$SPILLI_PEM_SECRET_REF" \
  --from-file=pem=./SpiLLIHost_Community.pem --dry-run=client -o yaml | kubectl apply -f -

cat > /tmp/spillihost-values.yaml <<EOF
image:
  repository: "ghcr.io/synaptrixai/spillihost"
  tag: "${RELEASE_TAG}"
spilliHost:
  nodeId: "${SPILLI_NODE_ID}"
  subscriptionTier: "${SPILLI_SUBSCRIPTION_TIER}"
  pemSecretRef:
    name: "${SPILLI_PEM_SECRET_REF}"
    key: "pem"
EOF

helm upgrade --install "$RELEASE_NAME" \
  oci://ghcr.io/synaptrixai/charts/spillihost \
  --version "$HELM_CHART_VERSION" \
  --namespace "$NAMESPACE" \
  -f /tmp/spillihost-values.yaml
```

### Kubernetes secret/reference model

For Kubernetes/DOKS deployment flows, `Secret Reference` maps to a Kubernetes secret name.

- Secret must exist in target namespace.
- Secret must include key `pem` containing PEM contents.
- Helm values field is `spilliHost.pemSecretRef.name` and key field is `spilliHost.pemSecretRef.key`.
