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

## Quick Start Paths

Choose the path that matches what you want to do:

| Goal | Path | Detailed Guide |
|------|------|----------------|
| Run `SpiLLIHost` on Ubuntu or Windows | Native installer | [SpiLLI Host Installation Guide](https://github.com/synaptrixai/SpiLLI/wiki/SpiLLI-Host-Installation-Guide) |
| Manage the installed host service | Native service management | [SpiLLI Host Service Management](https://github.com/synaptrixai/SpiLLI/wiki/SpiLLI-Host-Service-Management) |
| Run tutorials quickly | Docker tutorials image | [SpiLLI Host Docker Deployment](https://github.com/synaptrixai/SpiLLI/wiki/SpiLLI-Host-Docker-Deployment) |
| Run `SpiLLIHost` in containers | Docker runtime image | [SpiLLI Host Docker Deployment](https://github.com/synaptrixai/SpiLLI/wiki/SpiLLI-Host-Docker-Deployment) |
| Deploy `SpiLLIHost` to Kubernetes or cloud clusters | Helm chart + GHCR image | [SpiLLI Host Helm and Kubernetes Deployment](https://github.com/synaptrixai/SpiLLI/wiki/SpiLLI-Host-Helm-and-Kubernetes-Deployment) |
| Build apps against the network | Python or Node.js SDK | [SpiLLI SDK Installation Guide](https://github.com/synaptrixai/SpiLLI/wiki/SpiLLI-SDK-Installation-Guide) |

---

## What To Install

### SpiLLIHost

Use `SpiLLIHost` when you want to run a host node.

Current tested release:

- Ubuntu `.deb`: <https://github.com/synaptrixai/SpiLLI/releases/download/v0.3.6/SpiLLIHost-0.3.6-Linux-SpiLLIHost.deb>
- Windows installer: <https://github.com/synaptrixai/SpiLLI/releases/download/v0.3.6/SpiLLIHost-0.3.6-win64.exe>
- Docker image: `ghcr.io/synaptrixai/spillihost:v0.3.6`
- Helm chart: `oci://ghcr.io/synaptrixai/charts/spillihost --version 0.3.6`

### SpiLLI SDK

Use the SDK when you want to build applications that connect to the SpiLLI network.

- Python: `pip install --index-url https://well.synaptrix.org --upgrade SpiLLI`
- Node.js: `npm install @synaptrix/spilli --save`

---

## Deployment Options

| Option | Best For | Notes |
|--------|----------|-------|
| Native install | Local machines running a stable host service | `.deb` and Windows installer both auto-start `SpiLLIHost` after install |
| Docker | Local tests and containerized runtime validation | Good for validating PEM mounts and runtime behavior |
| Helm / Kubernetes | Cloud and cluster deployment | Uses published OCI chart and GHCR runtime image |

`SpiLLIHost` requires the correct PEM file for the subscription tier you are running. Keep PEM files private and never commit them to source control.

---

## Verify Published Artifacts

Consumers can verify that the published `SpiLLIHost` image came from the `synaptrixai/SpiLLI` GitHub Actions workflow.

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

## Tutorials And Examples

- Python and notebook examples are in `Tutorials/`
- Node.js examples are in [Tutorials/NodeJS](Tutorials/NodeJS/GETTING_STARTED.md)
- Additional setup and operations docs are in the [repository wiki](https://github.com/synaptrixai/SpiLLI/wiki)

---

## Support And Feedback

- Open issues and feature requests on [GitHub](https://github.com/synaptrixai/SpiLLI)
- Use the [repository wiki](https://github.com/synaptrixai/SpiLLI/wiki) for detailed setup guides
- Install the [SpiLLI VS Code Extension](https://marketplace.visualstudio.com/items?itemName=Synaptrix.spilli) for guided in-editor workflows

> **Notice**
> SpiLLI is currently in beta and under active development.
