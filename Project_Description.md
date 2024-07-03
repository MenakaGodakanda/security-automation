# Security Automation Project - Version 1

This project contains scripts to automate security tasks such as log monitoring, security policy enforcement, and incident response.

## Features

### Log Monitoring:
- **Log File Reading**: Reads and processes log files line-by-line to identify specific patterns indicating errors or suspicious activity.
- **Pattern Matching**: Uses regular expressions to detect predefined patterns (e.g., ERROR) in log entries.
- **Alert Generation**: Generates alerts in real-time when a pattern match is found.

### Security Policy Enforcement:
- **Policy File Reading**: Reads security policies from a text file, allowing easy updates and modifications to security rules without changing the script.
- **Policy Application**: Simulates the application of security policies by printing the policies being enforced.
- **Flexible Policy Definitions**: Allows for easy addition of new policies by updating the policy file.

### Incident Response:
- **Incident Report Reading**: Reads incident reports from a text file, making it easy to update and manage incident response plans.
- **Incident Response Execution**: Simulates incident response actions by printing the incidents being responded to.
- **Flexible Incident Definitions**: Allows for easy addition of new incidents by updating the incident file.

### Modularity:
- Each script is designed to handle a specific aspect of security automation (log monitoring, policy enforcement, incident response).
- Modular design allows for independent development and testing of each component.

### Extensibility:
- Scripts can be easily extended to handle additional patterns, policies, and incident types.
- Supports integration with other tools and systems (e.g., email notifications, SIEM systems).

### Ease of Use:
- Simple setup and execution process.
- Uses text files for configurations, making it easy to update and manage without modifying the code.

### Automation:
- Automates repetitive security tasks, reducing the need for manual monitoring and intervention.
- Enhances the speed and efficiency of security operations.

### Open Source Tools:
- Uses open-source Python libraries and tools, making it accessible and modifiable by anyone.
- Compatible with Linux, a popular platform for security professionals.

## Sequence Diagram

<img width="1381" alt="Screenshot 2024-07-03 at 4 32 21 PM" src="https://github.com/MenakaGodakanda/security-automation/assets/156875412/4ab1d3c1-47a7-46fd-a6ee-1b88cef4dfce">


### Explanation
1. `User` initiates the process.
2. `Log Monitoring Component` monitors the logs and identifies any issues.
  - When issues are identified, it sends alerts.
3. `Security Policy Enforcement Component` receives alerts from the log monitoring component.
    - It applies the relevant security policies by reading the policy files and enforcing them.
4. `Incident Response Component` receives reports of enforced policies and detected issues.
    - It processes these reports and executes appropriate responses to the incidents.

## Coding Details:

### Log Monitoring Script (monitor.py)
#### Description
The `monitor.py` script is designed to automate the monitoring and analysis of security log. It scans log file for specific patterns (e.g., error messages) and generates alerts when these patterns are detected.

#### Implementation Details
1. **Setup and Import Libraries**:
    - Import necessary Python libraries for file handling and regular expressions.
2. **Log Monitoring Functionality**:
    - Define a function to read log files and check for specified patterns (like "ERROR").
    - Use regular expressions to identify lines that match the patterns.
3. **Alert Generation**:
    - Print or log alerts for each identified issue.

#### Explanation
  - **Imports**: `os` for file path handling, `time` for time library.
  - **monitor_logs function**: Reads the log file and looks for lines matching the "ERROR" pattern.
  - **Main Execution**: Calls `monitor_logs` to start monitoring.

### Security Policy Enforcement Script (enforce.py)
#### Description
The `enforce.py` script automates the enforcement of security policies. It reads policy files and applies the specified policies.

#### Implementation Details
1. **Setup and Import Libraries**:
    - Import necessary libraries for file handling.
2. **Policy Enforcement Functionality**:
    - Define a function to read policy files and print the policies being applied.
    - Simulate the application of policies.

#### Explanation
  - **Imports**: `os` for file path handling.
  - **enforce_policies function**: Reads the policy file and prints each policy being applied.
  - **Main Execution**: Calls `enforce_policies` to start enforcing policies.

### Incident Response Script: respond.py
#### Description
The `respond.py` script automates the response to security incidents. It reads incident reports and executes appropriate responses.

#### Implementation Details
1. **Setup and Import Libraries**:
    - Import necessary libraries for file handling.
2. **Incident Response Functionality**:
    - Define a function to read incident files and print the incidents being responded to.
    - Simulate the incident response actions.

#### Explanation
  - **Imports**: `os` for file path handling.
  - **respond_to_incidents function**: Reads the incident file and prints each incident being responded to.
  - **Main Execution**: Calls `respond_to_incidents` to start responding to incidents.
