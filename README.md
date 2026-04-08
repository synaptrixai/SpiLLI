# SpiLLI
*Decentralized AI inference infrastructure*

SpiLLI provides infrastructure to manage, host, deploy, and run decentralized AI inference.

SpiLLI consists of two main components:

| Component | Purpose |
|-----------|---------|
| **SpiLLI SDK** | Python and Node.js libraries for building decentralized AI applications |
| **SpiLLIHost** | Sandboxed AI runner that turns a machine into a host node serving AI models to the network |

Machines running `SpiLLIHost` form a distributed network of AI resources. Applications built with the `SpiLLI SDK` are automatically routed to the best available host for their requested AI resources at runtime.

SpiLLI is designed around a few key ideas:

1. **Enhanced privacy and security**: data stays protected through personalized credentials, encryption-locked communication, and identity-aware access across the network.
2. **Flexible AI infrastructure**: peer-to-peer, cloud, and hybrid deployment paths make it easier to tailor infrastructure to your needs, environment, and budget.
3. **Democratized AI participation**: the network is built so people can participate both as infrastructure suppliers and as users of AI resources.
4. **Global collaboration**: models, tools, and AI capabilities can be shared and accessed across the internet.
5. **Decentralized multi-agent systems**: developers can build applications that operate across a cooperative, large-scale network of AI resources.
6. **Real-time networking**: AI inference, monitoring, and future training-oriented workflows can benefit from low-latency, real-time coordination between clients and hosts.

This makes SpiLLI a flexible foundation for building decentralized local, cloud and hybrid AI infrastructure, serving multiple users, AI agents and applications with resources that can evolve as the network evolves around them.

Whether you want to build AI applications with the SDK, run your own host nodes and network for AI models, or deploy into containers and Kubernetes clusters, SpiLLI is designed to give you a straightforward path to get started.

---

## Choose Your Path

Use the path that best matches what you want to do first:

| Goal | Recommended Path | Key Artifacts | Detailed Guide |
|------|------------------|---------------|----------------|
| Run a AI host | Native `SpiLLIHost` install | Ubuntu `.deb`, Windows installer | [SpiLLI Host Installation Guide](https://github.com/synaptrixai/SpiLLI/wiki/SpiLLI-Host-Installation-Guide) |
| Run a containerized host | Docker `SpiLLIHost` runtime | `ghcr.io/synaptrixai/spillihost:v0.3.6` | [SpiLLI Host Docker Deployment](https://github.com/synaptrixai/SpiLLI/wiki/SpiLLI-Host-Docker-Deployment) |
| Deploy to Kubernetes | Helm chart + GHCR image | `oci://ghcr.io/synaptrixai/charts/spillihost --version 0.3.6` | [SpiLLI Host Helm and Kubernetes Deployment](https://github.com/synaptrixai/SpiLLI/wiki/SpiLLI-Host-Helm-and-Kubernetes-Deployment) |
| Build with the SDK | Python or Node.js SDK | `pip install SpiLLI`, `npm install @synaptrix/spilli` | [SpiLLI SDK Installation Guide](https://github.com/synaptrixai/SpiLLI/wiki/SpiLLI-SDK-Installation-Guide) |
| Explore SDK tutorials | Docker tutorials environment | `docker compose up` in this repo | [SpiLLI SDK Docker Tutorials](https://github.com/synaptrixai/SpiLLI/wiki/SpiLLI-SDK-Docker-Tutorials) |

`SpiLLIHost` requires a PEM file for the subscription tier you are running. You can download your personalized PEM from <https://agents.synaptrix.org/dechat>. This file is used for identity and personalized encryption within the SpiLLI network, helping protect user data with end-to-end encryption while allowing the network to recognize your account and access level. Keep PEM files private and never commit them to source control.

---

## Who SpiLLI Is For

| Role | What You Can Do |
|------|------------------|
| AI host operators | Run `SpiLLIHost`, contribute AI compute, and manage hosted models |
| AI application developers | Build against the `SpiLLI SDK` and connect to available network resources |
| SDK explorers and learners | Use the tutorials and examples to get a feel for the platform quickly |
| Teams and communities | Deploy in local, hybrid, or cloud environments and share repeatable setups |

---

## Tutorials And Examples

- Python and notebook examples are in `Tutorials/`
- Node.js examples are in [Tutorials/NodeJS](Tutorials/NodeJS/GETTING_STARTED.md)
- Step-by-step setup, deployment, and operations guides are in the [repository wiki](https://github.com/synaptrixai/SpiLLI/wiki)

---

## Community And Feedback

We’d love to see what you build with SpiLLI.

- Open issues and feature requests on [GitHub](https://github.com/synaptrixai/SpiLLI)
- Share ideas and follow updates through the repo and project channels
- Contribute tutorials, examples, and improvements through pull requests

If you’re experimenting with decentralized AI apps, hosting models, or building developer tooling around SpiLLI, you’re in exactly the kind of territory this project is meant to support.

---

## Support And Feedback

- Open issues and feature requests on [GitHub](https://github.com/synaptrixai/SpiLLI)
- Use the [repository wiki](https://github.com/synaptrixai/SpiLLI/wiki) for detailed setup guides and deployment walkthroughs
- Install the [SpiLLI VS Code Extension](https://marketplace.visualstudio.com/items?itemName=Synaptrix.spilli) for guided in-editor workflows

---

## FAQ

| Question | Answer |
|----------|--------|
| Is my data safe? | SpiLLI uses personalized credentials and end-to-end encryption to help protect traffic and user identity across the network. |
| Do I need Docker to use SpiLLI? | No. You can install `SpiLLIHost` natively and use the SDK directly. Docker and Helm are optional deployment paths. |
| Can I deploy SpiLLIHost to Kubernetes? | Yes. The published Helm chart and GHCR runtime image are designed for that workflow. |
| Can I just try the SDK first? | Yes. The SDK installation guide and Docker tutorials path are both good starting points for developers. |

> **Notice**
> SpiLLI is currently in beta and under active development. We’re excited to keep improving the experience as more people build and host with it.
