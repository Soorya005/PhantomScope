# PhantomScope

PhantomScope is a Virtual Machine Introspection (VMI)-based forensic analysis framework designed to acquire and analyze memory from KVM/QEMU virtual machines. The project focuses on extracting forensic artifacts, detecting hidden processes through cross-view analysis, generating alerts, and producing timestamped investigation reports.

## Features

* Virtual Machine Enumeration using libvirt
* Memory Acquisition Framework for KVM/QEMU guests
* Volatility 3 Integration
* Linux Kernel Banner Extraction
* VMCOREINFO Extraction
* Forensic Artifact Parsing
* Process Data Modeling
* Cross-View Hidden Process Detection
* Alert Generation with Severity Levels
* Analysis Statistics
* Timestamped JSON Report Generation

## Architecture

```
VM Enumeration
      ↓
Memory Acquisition
      ↓
Volatility Analysis
      ↓
Artifact Extraction
      ↓
Cross-View Detection
      ↓
Alert Generation
      ↓
Statistics
      ↓
JSON Report Generation
```

## Project Structure

```
PhantomScope/
├── alerts/
├── analytics/
├── artifact_extraction/
├── cross_view/
├── memory_acquisition/
├── models/
├── reporting/
├── test_data/
├── vm_controller/
├── dumps/
├── reports/
├── main.py
└── README.md
```

## Technologies Used

* Python 3
* Volatility 3
* Libvirt
* KVM/QEMU
* Debian Linux
* JSON

## Installation

Clone the repository:

```bash
git clone https://github.com/Soorya005/PhantomScope.git
cd PhantomScope
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the analysis pipeline:

```bash
python main.py
```

Example Output:

```
=== Cross View Analysis ===

Potential Hidden Processes Detected:

[!] PID=200 NAME=sleep
[!] PID=300 NAME=python

=== Alert Generation ===

[MEDIUM] Hidden Process
PID     : 200
Process : sleep

[CRITICAL] Hidden Process
PID     : 300
Process : python
```

## Sample Report

Generated reports are stored in the `reports/` directory.

Example:

```json
{
    "vm_name": "debian-lab",
    "analysis_time": "2026-06-09T18:23:24",
    "alerts": [
        {
            "severity": "MEDIUM",
            "process": "sleep"
        },
        {
            "severity": "CRITICAL",
            "process": "python"
        }
    ]
}
```

## Current Status

PhantomScope currently provides a proof-of-concept VMI forensic framework featuring artifact extraction, cross-view detection, alerting, and reporting capabilities.

The hidden process detection engine currently operates on simulated process views. Future work aims to integrate real process acquisition from guest operating systems and memory dumps.

## Future Enhancements

* Real process acquisition from guest VMs
* Volatility-based Linux process enumeration
* LibVMI integration
* HTML dashboard generation
* IOC scanning support
* Expanded forensic artifact collection

## Author

**Soorya A P**

Cybersecurity Researcher | Red Teamer | HTB Campus Lead | IEEE IAS Secretary

## License

This project is intended for educational and research purposes.
