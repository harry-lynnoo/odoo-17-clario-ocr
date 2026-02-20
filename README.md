# Clario OCR – Enterprise-Grade Invoice Scanning for Odoo 17

Clario OCR is an enterprise-grade invoice and receipt scanning module for Odoo 17.  
It integrates Microsoft Azure Document Intelligence to automatically extract structured financial data from supplier invoices and receipts.

The module converts scanned documents into draft vendor bills with intelligent field mapping, reducing manual data entry and improving accounting efficiency.

---

## Key Features

- Automatic invoice data extraction using Azure AI
- Vendor detection and intelligent partner matching
- VAT, subtotal, and total validation logic
- Reference number extraction and fallback handling
- Multi-currency support
- Seamless integration with Odoo 17 Accounting
- Secure Azure API key configuration via Odoo Settings

---

## Installation

1. Copy the module into your Odoo `addons` directory.
2. Restart the Odoo server.
3. Update the App list.
4. Search for **Clario OCR** and click Install.

---

## Python Dependencies

If you are running Odoo in a self-hosted environment, install:

pip install -r requirements.txt

## Azure Configuration Guide

1. Create a Microsoft Azure account.
2. Create a **Document Intelligence** resource.
3. Obtain your Endpoint URL and API Key.
4. In Odoo, go to:

   Settings → Clario OCR

5. Enter your Azure Endpoint and API Key.
6. Click Save.

⚠ OCR processing will be disabled until Azure credentials are configured.

---

## External Service Requirement

This module requires a Microsoft Azure Document Intelligence subscription.

Users must provide their own Azure endpoint and API key.  
Azure service fees are charged separately by Microsoft and are not included in the module price.

---

## Technical Specifications

- Compatible with Odoo 17
- Uses standard Odoo ORM architecture
- No hardcoded credentials
- Multi-company compatible
- Fully uninstallable without data corruption

---

## Limitations

- OCR accuracy depends on document quality and Azure service performance.
- Internet connection is required for OCR processing.

## License

This module is released under the OPL-1 license.