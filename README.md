# SpiLLI
*Decentralized AI inference infrastructure*

SpiLLI provides infrastructure to manage, host, deploy, and run decentralized AI inference.

SpiLLI consists of two main components:

| Component | Purpose |
|-----------|---------|
| **SpiLLI SDK** | Python and Node.js libraries for building decentralized AI applications |
| **SpiLLIHost** | Sandboxed AI runner that turns a machine into a host node serving AI models to the network |

Machines running `SpiLLIHost` form a distributed network of host nodes. Applications built with the `SpiLLI SDK` are automatically routed to the best available host for their requested AI resources at runtime.

---

## How SpiLLI Works

SpiLLI is a global peer-to-peer network of AI hosts and users.

1. A machine running `SpiLLIHost` becomes a host node.
2. Apps built with `SpiLLI SDK` can discover and use models on any host node.
3. Connections are made without a central cloud provider.

The network is built around three principles:

1. **Dynamic Resource Allocation**: Apps find the best host based on load, performance, and proximity.
2. **Decentralized Infrastructure**: Computing power is spread across many nodes, providing redundancy.
3. **Real-time Adaptation**: Connections and allocations are continuously optimized.

---

## Choose Your Path

Use the path that matches what you want to do:

| Goal | Recommended Path |
|------|------------------|
| Run tutorials quickly | Docker tutorials image |
| Run `SpiLLIHost` on your own machine | Native installers (`.deb` or Windows installer) |
| Run `SpiLLIHost` in containers or Kubernetes | Docker image or Helm chart |
| Build apps against the network | Install the `SpiLLI SDK` |

### At a Glance

| Path | Best For | Main Artifacts |
|------|----------|----------------|
| Native install | Local host nodes on Ubuntu or Windows | GitHub release `.deb` / `.exe` |
| Docker | Local containerized tests and tutorial environments | `ghcr.io/synaptrixai/spillihost:<release-tag>`, `synaptrixai/spilli-rag-tutorials` |
| Helm / Kubernetes | Cloud and cluster deployment | `oci://ghcr.io/synaptrixai/charts/spillihost` |
| SDK only | Application developers | `pip install SpiLLI`, `npm install @synaptrix/spilli` |

---

## Native Install

### Install SpiLLIHost

#### Ubuntu

Download and install the latest tested host release:

```bash
curl -fL -o SpiLLIHost-0.3.6-Linux-SpiLLIHost.deb \
  https://github.com/synaptrixai/SpiLLI/releases/download/v0.3.6/SpiLLIHost-0.3.6-Linux-SpiLLIHost.deb

sudo apt install ./SpiLLIHost-0.3.6-Linux-SpiLLIHost.deb
sudo mv SpiLLIHost_Community.pem /usr/bin/SpiLLIHost/
```

`SpiLLIHost` starts automatically after the `.deb` install completes, and the install enables the `SpiLLIHost` service for reboot persistence.

Useful service commands:

```bash
sudo systemctl status SpiLLIHost.service
sudo systemctl restart SpiLLIHost.service
sudo systemctl stop SpiLLIHost.service
sudo systemctl start SpiLLIHost.service
```

#### Windows

1. Download the installer: <https://github.com/synaptrixai/SpiLLI/releases/download/v0.3.6/SpiLLIHost-0.3.6-win64.exe>
2. Run the setup. Ignore the unsigned-signature warning if prompted.
3. Select your `SpiLLIHost_Community.pem` during installation and complete the installer flow.

The Windows installer also starts `SpiLLIHost` automatically and registers it as a Windows service.

#### PEM placement

`SpiLLIHost` will not run if no encryption file is present.

- Ubuntu install directory: `/usr/bin/SpiLLIHost`
- Windows install directory: `C:\Program Files (x86)\SpiLLIHost\bin`

For community tier installs, the expected PEM is typically `SpiLLIHost_Community.pem`.

> **Security**
> The PEM file provides personalized client- and host-side encryption so your data in transit is accessible only by you. Do not share it publicly or commit it to this repository.

### Install SpiLLI SDK

#### Python

```bash
pip install --index-url https://well.synaptrix.org --upgrade SpiLLI
```

#### Node.js

Requirements:

- Node.js `>=20`
- npm `>=10`

```bash
npm install @synaptrix/spilli --save
```

Get your SDK PEM from <https://agents.synaptrix.org/dechat> and keep the file path available for runtime configuration.

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

More SDK docs:

- [Node.js Getting Started](Tutorials/NodeJS/GETTING_STARTED.md)
- [Node.js Tutorials README](Tutorials/NodeJS/tutorials/README.md)

---

## Docker

### Tutorials image

The repository includes a Docker-based tutorials environment for quick experimentation.

```bash
git clone https://github.com/synaptrixai/SpiLLI.git
cd SpiLLI
docker compose up
```

Before starting, download your PEM from <https://agents.synaptrix.org/dechat> and place it next to `docker-compose.yml`.

After startup, open <http://127.0.0.1:8888/lab>.

Sample notebooks:

- RAG agents: <http://127.0.0.1:8888/lab/tree/Tutorials/Building_RAG_Agents/scripts/Tutorial.ipynb>
- Agent tools: <http://127.0.0.1:8888/lab/tree/Tutorials/Building_Agent_Tools/Tutorial.ipynb>

### SpiLLIHost runtime image

For containerized host-node deployment, use the published image:

```bash
ghcr.io/synaptrixai/spillihost:v0.3.6
```

The containerized runtime is intended for Docker/Kubernetes-style deployment. Unlike VM installs, it does not rely on systemd; it launches the `SpiLLIHost` binary directly inside the container.

---

## Helm And Kubernetes

SpiLLIHost Kubernetes deployment artifacts are published from GitHub Releases.

- Runtime image: `ghcr.io/synaptrixai/spillihost:<release-tag>`
- Helm chart (OCI): `oci://ghcr.io/synaptrixai/charts/spillihost --version <release-version-without-v>`

Example install or upgrade:

```bash
RELEASE_TAG=v0.3.6
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

### Kubernetes secret/reference model

For Kubernetes and DOKS deployment flows, `Secret Reference` maps to a Kubernetes secret name.

- Secret must exist in target namespace.
- Secret must include key `pem` containing PEM contents.
- Helm values field is `spilliHost.pemSecretRef.name` and key field is `spilliHost.pemSecretRef.key`.

Notes:

- Helm chart publication checks that `ghcr.io/synaptrixai/spillihost:<release-tag>` exists before pushing chart artifacts.
- `.deb` install auto-enables and starts `SpiLLIHost` service on VM installs; container runtime does not use systemd and starts the binary directly as PID 1.

### Verify image origin

Consumers can verify that an image was produced by the `synaptrixai/SpiLLI` GitHub Actions workflow before using it.

Verify the Sigstore keyless signature:

```bash
cosign verify \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com \
  --certificate-identity-regexp 'https://github.com/synaptrixai/SpiLLI/.github/workflows/publish-spillihost-image.yml@.*' \
  ghcr.io/synaptrixai/spillihost:v0.3.6
```

Verify the GitHub build provenance attestation:

```bash
gh attestation verify \
  oci://ghcr.io/synaptrixai/spillihost:v0.3.6 \
  --repo synaptrixai/SpiLLI
```

---

## System Requirements

| OS | Host | SDK |
|----|------|-----|
| Ubuntu 24.04 | Yes | Python 3.8-3.12, Node.js >=20 |
| Windows 10/11 | Yes | Python 3.8-3.12, Node.js >=20 |
| Kubernetes / DOKS | Via image and Helm | Not applicable |
| Others | Future | Future |

> **Host**
> Supports NVIDIA, AMD GPUs, and CPUs.

---

## Common Use Cases

| Role | What To Do |
|------|------------|
| AI host operator | Install `SpiLLIHost` locally or deploy via Docker/Helm, then manage models via <https://agents.synaptrix.org/dechat> |
| Application developer | Install the SDK, load your PEM, and connect to the network from Python or Node.js |
| Tutorial user | Start the Docker tutorials environment and use the notebooks |
| VS Code user | Install the [SpiLLI VS Code Extension](https://marketplace.visualstudio.com/items?itemName=Synaptrix.spilli) |

---

## FAQ

| Question | Answer |
|----------|--------|
| Is my data safe? | Traffic is encrypted with your PEM/P12 identity material, and `SpiLLIHost` follows a zero-data-retention model for inference requests. |
| Do I need Docker to use SpiLLI? | No. You can install `SpiLLIHost` natively and use the SDK directly. Docker and Helm are optional deployment paths. |
| Can I deploy SpiLLIHost to Kubernetes? | Yes. Use the published GHCR image and Helm chart shown above. |
| Can I host models on a phone? | The SDK can be used from applications running on phones, but `SpiLLIHost` currently targets desktop/server environments rather than phones directly. |

---

## Contributing And Feedback

- Open issues and feature requests on [GitHub](https://github.com/synaptrixai/SpiLLI)
- Watch the repo for releases and updates
- Contribute tutorials, examples, and fixes through PRs

> **Notice**
> SpiLLI is currently in beta. Expect active iteration and ongoing improvements.

For questions or help, use GitHub issues or discussions on the repository.
