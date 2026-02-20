{
    "name": "Clario OCR (Enterprise)",
    "version": "17.0.1.0.0",
    "category": "Accounting/Accounting",
    "summary": "Enterprise-grade OCR automation for invoices and receipts",
    "author": "Clario",
    "website": "https://yourwebsite.com",
    "license": "OPL-1",

    "depends": [
        "base",
        "web",
        "mail",
        "account",
    ],

    "data": [
        "security/ir.model.access.csv",
        "data/ocr_sequences.xml",
        "views/actions.xml",
        "views/menus.xml",
        "views/dashboard.xml",
        "views/form.xml",
        "views/tree.xml",
        "views/search.xml",
        "views/invoice.xml",
        "views/receipt.xml",
    ],

    "application": True,
    "installable": True,
}