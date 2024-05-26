from substrateinterface import SubstrateInterface
from config import NODE_URL, SS58_FORMAT

def create_connection():
    substrate = SubstrateInterface(
        url=NODE_URL,
        ss58_format=SS58_FORMAT,
        type_registry_preset='default'
    )
    print("Connected to Substrate node")
    return substrate
