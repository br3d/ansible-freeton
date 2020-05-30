#!/usr/bin/env python3
import config
import requests
import socket
import subprocess

# Wallet balance
def check_balance():
    try:
        addr = open(config.tk_dir + socket.gethostname() + ".addr")
        wlt = addr.read().strip()
        bCmnd = config.tc_dir + "tonos-cli account " + wlt + " | grep -i 'balance' | awk '{print $2}' "
        b = str(subprocess.check_output(bCmnd, shell = True, executable='/bin/bash', encoding='utf-8'))
        b = int(int(b) / 1000000000)
        return b
    except:
        tg_notification("Can't get wallet balance")

# Node diff
def check_diff():
    try:
        dCmnd = config.s_dir + "check_node_sync_status.sh | grep TIME_DIFF | awk '{print $4}'"
        d = int(subprocess.check_output(dCmnd, shell = True, executable='/bin/bash', encoding='utf-8'))
        return d
    except:
         tg_notification("Can't get node time diff")

# Telegram notification
def tg_notification(msg):
  botToken = config.bot_key
  botChatID = config.g_id
  message = '<b>ALERT!</b> %s!' % msg
  sendText = 'https://api.telegram.org/bot' + botToken + '/sendMessage?chat_id=' + botChatID + '&parse_mode=html&text=' + message
  response = requests.get(sendText)
  return response.json()

if __name__ == '__main__':
    balance = check_balance()
    if balance < 10001:
        tg_notification("Node balance is" + str(balance))
    
    diff = check_diff()
    if diff < -50:
        tg_notification("Diff is" + str(diff))
    
    with open(config.l_dir + config.l_file, "w") as text_file:
        text_file.write("node_diff {0}\n".format(diff))
        text_file.write("node_balance {0}\n".format(balance))
    

