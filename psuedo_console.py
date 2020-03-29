import paramiko, time

PASS=pass
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(HOST, port=22, username="jake", password=PASS)

'''chan = client.invoke_shell() 
chan.send("sudo conspy 10\n")       
time.sleep(3)
chan.send(f'{PASS}\n')
chan.send("/say CMON\n")
print(chan.recv(4096))'''

'''chan = client.get_transport().open_session()
chan.get_pty()
chan.exec_command('sudo conspy 10')
chan.send(f'{PASS}\n')
chan.send('/say YES\n')
print(chan.recv(4096))'''

'''stdin, stdout, stderr = client.exec_command('sudo conspy 10', get_pty=True)
stdin.write(f'{PASS}\n')
time.sleep(3)
stdin.write('/say YES\n')
stdin.write('^[^[^[\n')
stdin.flush()'''


##chan.close()
client.close()
