# SpiLLI
*Decentralized AI inference infrastructure*

SpiLLI provides infrastructure to manage, host, deploy, and run decentralized AI inference.

SpiLLI consists of two main components:

| Component | Purpose |
|-----------|---------|
| **SpiLLI SDK** | Python and Node.js libraries for building decentralized AI applications |
| **SpiLLIHost** | Sandboxed AI runner that turns a machine into a host node serving AI models to the network |

Machines running SpiLLIHost form a distributed network of host nodes. Applications built with the SpiLLI SDK are automatically routed to the best available host for their requested AI resources at runtime.

---

## How SpiLLI Works

SpiLLI is a global peer-to-peer network of AI hosts and users.
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

Choose the setup path that matches your goal:

1. **Run tutorials quickly (Docker):** Use the pre-configured environment.
2. **Run SpiLLIHost locally:** Install the host service directly.
3. **Use SpiLLI SDK directly:** Install Python or Node.js SDK from pip / npm.

### 1️⃣ Run using Docker

The repository ships a [Docker image](https://hub.docker.com/r/synaptrixai/spilli-rag-tutorials) with required dependencies preinstalled. If you have [Docker](https://docs.docker.com/get-started/introduction/get-docker-desktop/), run tutorials with:

| Step | Command |
|------|---------|
| Clone the repo | `git clone https://github.com/synaptrixai/SpiLLI.git` |
| Download your PEM key | Download a personalized `.pem` file from [SpiLLI Demo](https://agents.synaptrix.org/dechat), then place it next to `docker-compose.yml` in the cloned repository |
| Start Docker | `docker compose up` (or `docker-compose up` on some Windows setups) |
| Access Jupyter | Open <http://127.0.0.1:8888/lab> to access and run the tutorials |

**Sample tutorials**

| Tutorial | Link |
|----------|------|
| Building RAG agents | <http://127.0.0.1:8888/lab/tree/Tutorials/Building_RAG_Agents/scripts/Tutorial.ipynb> |
| Building Tools for AI agents | <http://127.0.0.1:8888/lab/tree/Tutorials/Building_Agent_Tools/Tutorial.ipynb> |

> **Tip** – The `Tutorials` folder is volume-mapped into the container.
> Edit or add notebooks on your host; changes appear instantly inside Jupyter and vice versa.

> **Contributing** – Create a branch, commit your notebooks, and open a PR.
> Discuss major changes in the *Discussions* or *Ideas* tab first.

---

### 2️⃣ Installation Without Docker

#### Installing SpiLLIHost

- **Ubuntu**
  1. Download the `.deb`: <https://github.com/synaptrixai/SpiLLI/releases/download/v0.3.5/SpiLLIHost-0.3.5-Linux-SpiLLIHost.deb>
  2. Install:
     ```bash
     sudo apt install ./SpiLLIHost-0.3.5-Linux-SpiLLIHost.deb
     ```
  3. Move the PEM file to the host directory:
     ```bash
     sudo mv SpiLLIHost_Community.pem /usr/bin/SpiLLIHost/
     ```

- **Windows**
  1. Download the installer: <https://github.com/synaptrixai/SpiLLI/releases/download/v0.3.5/SpiLLIHost-0.3.5-win64.exe>
  2. Run the setup. Ignore the unsigned-signature warning.
  3. Select your `SpiLLIHost_Community.pem` during the installation process and follow prompts to complete the installation.

After installation, SpiLLIHost starts automatically as a service on Windows and Ubuntu.

To manage the **Service**  
   - **Windows**: Use the Windows *Services* console [can be found by typing "Services" in the windows start search bar]. Double click the 
   SpiLLIHost service in the Windows Services UI to open a dialog to start/stop/restart/or check the service status.  
   - **Ubuntu**: Use systemctl in the terminal as admin. `sudo systemctl start [ other options: stop/restart/status] SpiLLIHost.service`.  

> **Troubleshooting**
> SpiLLIHost will not run if no encryption file is provided. If the service fails to start, check that your downloaded PEM file is in the install directory (`/usr/bin/SpiLLIHost` on Ubuntu, `C:\Program Files (x86)\SpiLLIHost\bin` on Windows) and named `SpiLLIHost_Community.pem`.

> **⚠️ Security**
> The PEM file provides personalized client- and host-side encryption so your data in transit is accessible only by you. Do not share it publicly or commit it to this repository.

#### Installing SpiLLI SDK

##### Python (pip)

Install the Python SDK:

```bash
pip install --index-url https://well.synaptrix.org --upgrade SpiLLI
```

##### Node.js (npm)

Prerequisites:
- Node.js `>=20`
- npm `>=10`

Install the Node.js SDK:

```bash
npm install @synaptrix/spilli --save
```

Get your SDK encryption PEM from <https://agents.synaptrix.org/dechat> and keep the file path available for runtime configuration.

Minimal Node.js quickstart:

```js
import { createSpilliService } from '@synaptrix/spilli';

const keyPath = '/absolute/path/to/SpiLLI_Community.pem';
const service = createSpilliService(keyPath);

const session = service.getOrCreateSession({
  model: 'gpt-oss-20b',
  scope: 'public'
});

const response = await session.run({
  prompt: 'You are a concise assistant.',
  query: 'Explain how decentralized AI inference works.'
});

console.log(response);
```

For full Node.js setup, streaming, and agent-loop tutorials:
- [Node.js Getting Started](Tutorials/NodeJS/GETTING_STARTED.md)
- [Node.js Tutorials README](Tutorials/NodeJS/tutorials/README.md)

> Get the `SpiLLIHost_Community.pem` and `SpiLLI_Community.pem` encryption files from <https://agents.synaptrix.org/dechat>.

---

### 3️⃣ System Requirements

| OS | Host | SDK |
|----|------|-----|
| Ubuntu 24.04 | ✅ | Python 3.8–3.12, Node.js >=20 |
| Windows 10/11 | ✅ | Python 3.8–3.12, Node.js >=20 |
| Others | 🚧 (future) | 🚧 |

> **Host**: Supports NVIDIA, AMD GPUs, and CPUs.
> **SDK**: Available for Python and Node.js.

---

## How to Use

| Role | What to do |
|------|------------|
| **AI Host** | Install SpiLLIHost, join the network, manage hosted models via the UI at <https://agents.synaptrix.org/dechat>. |
| **Developer** | Build apps with the SDK. Get featured in the repo by contributing tutorials, example applications, and PRs. |
| **Feedback** | Open issues, suggest features, share ideas using the corresponding tabs on [GitHub](https://github.com/synaptrixai/SpiLLI). |
| **Sponsor** | Contact us to organize events like hackathons or AI agent tutorials for your community at `community@synaptrix.org`. |

> Star the repo if you like what we’re building!  

---

## Running as an AI Host

1. **Installation** – Follow the instructions above.  
2. **Service Management**
   - **Windows**: Use the *Services* console.
   - **Ubuntu**: `systemctl start SpiLLIHost.service` / `stop`.
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

* Use the **VS Code Extension**: <[SpiLLI VS Code Extension](https://marketplace.visualstudio.com/items?itemName=Synaptrix.spilli)>.  
* The extension installs the SpiLLI Agents interface in VS Code and guides you through encryption setup and network configuration automatically.

---

## FAQ

| Question | Answer |
|----------|--------|
| *Is my data safe?* | All traffic is encrypted with your personal PEM/P12 key over the network, & SpiLLIHost follows a zero-data retention policy, i.e., the AI hosts cannot access, retain or save any data that is sent to the host for inference. |
| *What if I need a different OS?* | We’re working on macOS and other Linux distros. In the meantime, use the Docker image on unsupported OSes. |
| *Can I host models on a phone?* | The SDK runs on machines with supported Python/Node.js runtimes thus you can build apps that run on the phone, but SpiLLIHost currently runs on desktop OSes, so your phone applications run on the phone, but connect with hosts running on desktop nodes in the network. |

---

> **⚠️ Notice** – SpiLLI is in **beta**. It may contain bugs and features under development.  
> Kindly open issues, give feedback, or contribute on GitHub.

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

kubectl -n "$NAMESPACE" get all
kubectl -n "$NAMESPACE" get secret "$SPILLI_PEM_SECRET_REF"
kubectl -n "$NAMESPACE" describe deployment "$RELEASE_NAME"
kubectl -n "$NAMESPACE" logs deploy/"$RELEASE_NAME" --tail=100
```

### Verify image origin

Consumers can verify that an image was produced by the `synaptrixai/SpiLLI` GitHub Actions workflow before using it.

Verify the Sigstore keyless signature:

```bash
cosign verify \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com \
  --certificate-identity-regexp 'https://github.com/synaptrixai/SpiLLI/.github/workflows/publish-spillihost-image.yml@.*' \
  ghcr.io/synaptrixai/spillihost:v0.3.5
```

Verify the GitHub build provenance attestation:

```bash
gh attestation verify \
  oci://ghcr.io/synaptrixai/spillihost:v0.3.5 \
  --repo synaptrixai/SpiLLI
```

### Kubernetes secret/reference model

For Kubernetes/DOKS deployment flows, `Secret Reference` maps to a Kubernetes secret name.

- Secret must exist in target namespace.
- Secret must include key `pem` containing PEM contents.
- Helm values field is `spilliHost.pemSecretRef.name` and key field is `spilliHost.pemSecretRef.key`.

Notes:
- Helm chart publication checks that `ghcr.io/synaptrixai/spillihost:<release-tag>` exists before pushing chart artifacts.
- `.deb` install auto-enables/starts `SpiLLIHost` service on VM installs; container runtime does not use systemd and starts the binary directly as PID 1.
