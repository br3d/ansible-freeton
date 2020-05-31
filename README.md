# ansible-freeton

Roles of Ansible for install and monitor FreeTon node.
Roles:

- common - preparing system and install dependencies
- freeton - build and setup FreeTon node
- netdata - real-time monitoring
- prometheus-node-exporter - exporter for hardware and OS metrics exposed, also this gives opportunity get **balance** and **diff** in freeton network

Run: `ansible-playbook freeton.yaml -i freeton --ask-sudo-pass -vvv`

# Example Dashboard based on prometheus-node-exporter

![Alt text](FreeTon.png?raw=true "Title")
