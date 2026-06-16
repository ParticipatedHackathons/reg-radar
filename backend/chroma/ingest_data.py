from chroma_client import (
    banking_functions,
    applications,
    processes,
    controls,
    teams,
    past_circulars,
)

# ─────────────────────────────────────────────
# 1. BANKING FUNCTIONS
# ─────────────────────────────────────────────
banking_functions.add(
    ids=["bf1", "bf2", "bf3", "bf4", "bf5", "bf6", "bf7", "bf8"],
    documents=[
        "KYC Know Your Customer verification process for onboarding new customers",
        "AML Anti Money Laundering compliance monitoring and suspicious activity reporting",
        "Credit Appraisal evaluation of borrower creditworthiness and loan eligibility",
        "Trade Finance management of letters of credit, bank guarantees, and export-import financing",
        "Treasury Operations management of liquidity, ALM, and interbank fund transfers",
        "Retail Banking management of savings accounts, current accounts, and fixed deposits",
        "Wealth Management investment advisory, portfolio management, and private banking services",
        "Fraud Detection real-time monitoring and prevention of fraudulent transactions",
    ],
    metadatas=[
        {"name": "KYC", "domain": "compliance", "priority": "high"},
        {"name": "AML", "domain": "compliance", "priority": "high"},
        {"name": "Credit Appraisal", "domain": "lending", "priority": "high"},
        {"name": "Trade Finance", "domain": "corporate_banking", "priority": "medium"},
        {"name": "Treasury Operations", "domain": "treasury", "priority": "high"},
        {"name": "Retail Banking", "domain": "retail", "priority": "high"},
        {"name": "Wealth Management", "domain": "investment", "priority": "medium"},
        {"name": "Fraud Detection", "domain": "risk", "priority": "high"},
    ],
)

print("✓ banking_functions seeded")

# ─────────────────────────────────────────────
# 2. APPLICATIONS
# ─────────────────────────────────────────────
applications.add(
    ids=["app1", "app2", "app3", "app4", "app5", "app6", "app7"],
    documents=[
        "Finacle Core Banking System used for retail and corporate account management, transactions, and reporting",
        "CAMS Compliance and AML Monitoring System for real-time transaction screening and STR generation",
        "LOS Loan Origination System for processing retail and corporate loan applications end to end",
        "TMS Treasury Management System for ALM, forex dealing, and interbank settlement",
        "CRM Customer Relationship Management platform for managing customer interactions and leads",
        "SWIFT messaging network for secure cross-border interbank financial transactions",
        "BI Reporting Tool business intelligence and MIS dashboard for regulatory and management reporting",
    ],
    metadatas=[
        {"name": "Finacle", "vendor": "Infosys", "type": "core_banking", "status": "active"},
        {"name": "CAMS", "vendor": "In-house", "type": "compliance", "status": "active"},
        {"name": "LOS", "vendor": "Nucleus Software", "type": "lending", "status": "active"},
        {"name": "TMS", "vendor": "Murex", "type": "treasury", "status": "active"},
        {"name": "CRM", "vendor": "Salesforce", "type": "crm", "status": "active"},
        {"name": "SWIFT", "vendor": "SWIFT", "type": "messaging", "status": "active"},
        {"name": "BI Reporting", "vendor": "Power BI", "type": "reporting", "status": "active"},
    ],
)

print("✓ applications seeded")

# ─────────────────────────────────────────────
# 3. PROCESSES
# ─────────────────────────────────────────────
processes.add(
    ids=["pr1", "pr2", "pr3", "pr4", "pr5", "pr6", "pr7", "pr8"],
    documents=[
        "Customer Onboarding process for verifying identity documents, conducting KYC checks, and opening accounts",
        "Loan Disbursement process including credit appraisal, sanction, documentation, and fund release",
        "Suspicious Transaction Reporting process for identifying, reviewing, and filing STR with FIU-IND",
        "RTGS NEFT Fund Transfer process for initiating and settling interbank payment instructions",
        "Fixed Deposit Creation process for opening, linking nominee, and issuing FD receipt to customer",
        "Forex Transaction process for executing and settling foreign currency buy and sell orders",
        "Account Closure process for verifying balances, recovering dues, and closing customer accounts",
        "Internal Audit process for planning, fieldwork, reporting, and tracking of audit observations",
    ],
    metadatas=[
        {"name": "Customer Onboarding", "function": "KYC", "sla_days": 2, "regulatory": True},
        {"name": "Loan Disbursement", "function": "Credit Appraisal", "sla_days": 7, "regulatory": False},
        {"name": "STR Filing", "function": "AML", "sla_days": 1, "regulatory": True},
        {"name": "RTGS NEFT Transfer", "function": "Retail Banking", "sla_days": 0, "regulatory": False},
        {"name": "FD Creation", "function": "Retail Banking", "sla_days": 1, "regulatory": False},
        {"name": "Forex Transaction", "function": "Trade Finance", "sla_days": 1, "regulatory": True},
        {"name": "Account Closure", "function": "Retail Banking", "sla_days": 3, "regulatory": False},
        {"name": "Internal Audit", "function": "Risk", "sla_days": 30, "regulatory": True},
    ],
)

print("✓ processes seeded")

# ─────────────────────────────────────────────
# 4. COMPLIANCE CONTROLS
# ─────────────────────────────────────────────
controls.add(
    ids=["ctrl1", "ctrl2", "ctrl3", "ctrl4", "ctrl5", "ctrl6", "ctrl7", "ctrl8"],
    documents=[
        "Maker-Checker control requiring dual authorization for all financial transactions above threshold limits",
        "Customer Due Diligence CDD control mandating periodic re-KYC for all existing customers based on risk category",
        "Transaction Monitoring control for automated screening of transactions against AML typologies and threshold rules",
        "Data Localization control ensuring all customer data is stored within Indian jurisdiction as per RBI guidelines",
        "Business Continuity Plan BCP control requiring quarterly DR drills and maintenance of recovery time objectives",
        "Interest Rate Risk control for measuring and managing gaps in asset-liability maturity profiles",
        "Outsourcing Risk control requiring due diligence, contract review, and monitoring of third-party service providers",
        "Cybersecurity control mandating vulnerability assessment, penetration testing, and patch management cycles",
    ],
    metadatas=[
        {"name": "Maker-Checker", "type": "preventive", "regulator": "RBI", "frequency": "transaction-level"},
        {"name": "CDD Re-KYC", "type": "detective", "regulator": "RBI", "frequency": "periodic"},
        {"name": "Transaction Monitoring", "type": "detective", "regulator": "FIU-IND", "frequency": "real-time"},
        {"name": "Data Localization", "type": "preventive", "regulator": "RBI", "frequency": "continuous"},
        {"name": "BCP DR Drill", "type": "corrective", "regulator": "RBI", "frequency": "quarterly"},
        {"name": "Interest Rate Risk", "type": "detective", "regulator": "RBI", "frequency": "monthly"},
        {"name": "Outsourcing Risk", "type": "preventive", "regulator": "RBI", "frequency": "annual"},
        {"name": "Cybersecurity", "type": "preventive", "regulator": "CERT-In", "frequency": "annual"},
    ],
)

print("✓ compliance_controls seeded")

# ─────────────────────────────────────────────
# 5. TEAMS
# ─────────────────────────────────────────────
teams.add(
    ids=["tm1", "tm2", "tm3", "tm4", "tm5", "tm6", "tm7"],
    documents=[
        "Compliance Team responsible for regulatory reporting, policy updates, AML monitoring, and FIU-IND filings",
        "Retail Banking Operations Team handling account opening, deposit management, and branch transaction processing",
        "Credit Risk Team responsible for loan appraisal, credit scoring, NPA monitoring, and provisioning",
        "IT and Digital Banking Team managing core banking infrastructure, mobile banking, and cybersecurity operations",
        "Treasury Team responsible for liquidity management, forex operations, and investment portfolio management",
        "Internal Audit Team conducting risk-based audits of branches, departments, and IT systems",
        "Customer Service Team handling grievance redressal, service requests, and escalation management",
    ],
    metadatas=[
        {"name": "Compliance Team", "head": "Chief Compliance Officer", "size": 25, "location": "HO"},
        {"name": "Retail Banking Ops", "head": "Head - Retail Operations", "size": 120, "location": "pan-India"},
        {"name": "Credit Risk", "head": "Chief Risk Officer", "size": 40, "location": "HO"},
        {"name": "IT and Digital", "head": "Chief Information Officer", "size": 80, "location": "HO"},
        {"name": "Treasury", "head": "Head - Treasury", "size": 30, "location": "HO"},
        {"name": "Internal Audit", "head": "Chief Audit Executive", "size": 35, "location": "HO"},
        {"name": "Customer Service", "head": "Head - Customer Experience", "size": 60, "location": "pan-India"},
    ],
)

print("✓ teams seeded")

# ─────────────────────────────────────────────
# 6. PAST CIRCULARS
# ─────────────────────────────────────────────
past_circulars.add(
    ids=["circ1", "circ2", "circ3", "circ4", "circ5", "circ6", "circ7", "circ8"],
    documents=[
        "RBI circular on Master Direction KYC 2016 updated guidelines for customer due diligence and periodic re-KYC",
        "RBI circular on Prompt Corrective Action framework for weak banks based on capital adequacy and NPA levels",
        "SEBI circular on Cybersecurity and Cyber Resilience Framework for stock brokers and depositories",
        "RBI circular on outsourcing of financial services mandating risk assessment and board-approved outsourcing policy",
        "FIU-IND guidelines on reporting of suspicious transactions and cash transactions above threshold limits",
        "RBI circular on Digital Lending Guidelines regulating digital loan disbursement, recovery practices, and data usage",
        "RBI circular on Interest Rate Risk in Banking Book IRRBB requiring banks to measure and manage rate sensitivity",
        "RBI circular on Business Continuity and Disaster Recovery framework for scheduled commercial banks",
    ],
    metadatas=[
        {"circular_id": "RBI/2016/MD-KYC", "regulator": "RBI", "year": 2016, "topic": "KYC", "status": "active"},
        {"circular_id": "RBI/2017/PCA", "regulator": "RBI", "year": 2017, "topic": "PCA Framework", "status": "active"},
        {"circular_id": "SEBI/2023/CYB", "regulator": "SEBI", "year": 2023, "topic": "Cybersecurity", "status": "active"},
        {"circular_id": "RBI/2006/OUTS", "regulator": "RBI", "year": 2006, "topic": "Outsourcing", "status": "active"},
        {"circular_id": "FIU/2020/STR", "regulator": "FIU-IND", "year": 2020, "topic": "AML Reporting", "status": "active"},
        {"circular_id": "RBI/2022/DIG", "regulator": "RBI", "year": 2022, "topic": "Digital Lending", "status": "active"},
        {"circular_id": "RBI/2023/IRRBB", "regulator": "RBI", "year": 2023, "topic": "Interest Rate Risk", "status": "active"},
        {"circular_id": "RBI/2019/BCP", "regulator": "RBI", "year": 2019, "topic": "BCP/DR", "status": "active"},
    ],
)

print("✓ past_circulars seeded")
print("\n All collections seeded successfully.")