# chroma/chroma_client.py

import chromadb

client = chromadb.PersistentClient(
    path="./chroma_storage"
)

banking_functions = client.get_or_create_collection(
    name="banking_functions"
)

applications = client.get_or_create_collection(
    name="applications"
)

processes = client.get_or_create_collection(
    name="processes"
)

controls = client.get_or_create_collection(
    name="compliance_controls"
)

teams = client.get_or_create_collection(
    name="teams"
)

past_circulars = client.get_or_create_collection(
    name="past_circulars"
)