# ansible-freeton

Roles of Ansible for install and monitor FreeTon node.
Roles:

- common - preparing system and install dependencies
- freeton - build and setup FreeTon node
- netdata - real-time monitoring
- prometheus-node-exporter - exporter for hardware and OS metrics exposed, also this gives opportunity get **balance** and **diff** in freeton network

DONE

- Build and Setup FreeTon node

  - Creating user and group
  - Cronjob for validator script
  - All logs in one folder /var/log/...
  - Systemd for control status of node and restart in fail case
  - Logrotate for archive logs

- Node Monitoring
  - Install netdata for realtime status <host>/netdata
  - install prometheus-node-exporter for collect metrics
    - collecting data about node status(node diff, wallet balance)
  - Install nginx for close entry poins of monitoring systems

# Example Dashboard based on prometheus-node-exporter

![Alt text](FreeTon.png?raw=true "Title")

Run:
`ansible-playbook freeton.yaml -i freeton --ask-sudo-pass -vvv`
