from ape import chain, networks
from ape.logging import logger


def main():
    """
    Prints the HEAD block number for each networks on the OP Stack.
    """

    for network_name in ("base", "zora", "mode", "fraxtal"):
        success, result = get_height(network_name)
        print(f"{network_name}: {result}")


def get_height(network_name: str) -> tuple[bool, str]:
    with logger.at_level("ERROR"):
        try:
            network = networks.get_ecosystem(network_name)
            with network.mainnet.use_default_provider():
                return True, f"{chain.blocks.height}"

        except Exception as err:
            return False, f"{err}"
