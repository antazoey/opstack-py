# OPStack Python

This project is for the purposes of demonstrating how to use the OP Stack in Python.

## Ape Framework Custom Networks

This project uses [Ape Framework Custom Networks](https://docs.apeworx.io/ape/stable/userguides/networks.html#custom-networks-by-config)
for several networks on the OP stack to demonstrate how to connect to these networks in Python.

We include the following networks:

* Base
* Zora
* Mode
* Fraxtal

To demonstrate connection, run the script `heads`:

```shell
ape run heads
```

You should see output like:

```shell
base: 25997386
zora: 26045141
mode: 19308268
fraxtal: 15986706
```

This script loops over the networks and outputs their chain height.
