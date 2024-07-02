# security-automation
This project contains scripts to automate security tasks such as log monitoring, security policy enforcement, and incident response.

## Overview

<img width="1146" alt="Screenshot 2024-07-02 at 5 39 47 PM" src="https://github.com/MenakaGodakanda/security-automation/assets/156875412/27a2756f-d0b1-4107-a15a-7036336f5d8a">

### Explanation

#### Log Monitoring:
Monitors log files and alerts on errors.
- monitor.py script monitors log files in the `logs/` directory.
- It reads log entries from `sample.log` and alerts if any error or suspicious activity is detected.

#### Security Policy Enforcement:
Reads and applies security policies.
- enforce.py script reads security policies from the `policies/` directory.
- It applies the policies found in `sample_policy.txt`.

#### Incident Response:
Processes incident reports and executes responses.
- respond.py script processes incident reports found in the `incidents/` directory.
- It responds to incidents described in `sample_incident.txt`.

## Setting Up the Project

1. Clone the Repository
```
git clone https://github.com/MenakaGodakanda/security-automation.git
cd security-automation
```

2. Install Global Dependencies
Ensure you have Python 3.x and pip installed.
```
sudo apt update
sudo apt install python3 python3-pip
```

3. Navigate to Each Component Directory and Install Dependencies.<br>
For each component (`log_monitoring`, `policy_enforcement`, `incident_response`), navigate to the directory and install dependencies.
```
pip install -r requirements.txt
```

## Running the Scripts

#### Log Monitoring:
Automate the monitoring and analysis of security logs.
```
cd log_monitoring
python3 monitor.py
```

Output of `monitor.py` script:


#### Security Policy Enforcement:
Automate the enforcement of security policies.
```
cd policy_enforcement
python3 enforce.py
```

Output of `enforce.py` script:


#### Incident Response:
Automate the response to security incidents.
```
cd incident_response
python3 respond.py
```

Output of `respond.py` script:


## License
This project is licensed under the MIT License.
