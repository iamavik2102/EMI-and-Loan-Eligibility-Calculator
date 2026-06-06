# Privacy Policy

**Last Updated:** June 2026

This Privacy Policy governs the privacy practices for the **EMI and Loan Eligibility Calculator** desktop application (the "Application"), developed by **Avik Mukherjee**. 

We respect your privacy and are committed to protecting it. This document explains how data is handled by the Application.

---

## 1. Information Collection and Use
The Application is a standalone, offline financial planning tool. 
* **No Personal Data Collection:** The Application does not request, collect, store, or transmit any personally identifiable information (PII), such as your name, email address, phone number, or financial history.
* **No Financial Data Tracking:** Any financial values, income details, loan amounts, or interest rates you enter into the sliders or input fields are processed entirely in-memory on your local device. This data is lost the moment you close the Application and is never saved.

## 2. Permissions and System Access
* **Offline Execution:** The Application does not require internet access, network permissions, or background cloud synchronization to calculate your EMIs or loan eligibility. 
* **Full Trust Sandbox:** While the MSIX package utilizes the Windows `runFullTrust` capability to properly render its graphical interface (Tkinter), it does not access your local file system (beyond its own installation directory), webcam, microphone, location services, or device contacts.

## 3. Third-Party Services and Analytics
* **No Third-Party Analytics:** We do not use third-party tracking tools, cookies, telemetric software, or analytics frameworks (such as Google Analytics or Flurry) inside the Application.
* **No Advertisements:** The Application is 100% ad-free and does not communicate with ad networks.

## 4. Open Source Transparency
The Application is distributed under the **MIT License**, allowing for complete code auditability and transparency regarding how calculations are executed. The core source code files, such as `emi_and_loan_eligibility_calculator.py`, contain the explicit copyright and licensing declarations.

## 5. Changes to This Privacy Policy
We may update our Privacy Policy from time to time to reflect modifications in platform standards or application capabilities. Any updates will be posted directly to this repository with an updated revision date.

## 6. Contact Information
If you have any questions, bug reports, or suggestions regarding this Application or its privacy practices, please open an issue in this GitHub repository.

**Copyright (c) 2026 AVIK MUKHERJEE**