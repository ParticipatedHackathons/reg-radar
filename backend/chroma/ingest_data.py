from chroma_client import banking_functions

banking_functions.add(
    ids=["1", "2"],
    documents=[
        "KYC Know Your Customer verification process",
        "AML Anti Money Laundering compliance"
    ],
    metadatas=[
        {"name": "KYC"},
        {"name": "AML"}
    ]
)