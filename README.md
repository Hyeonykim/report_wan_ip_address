# report_wan_ip_address
Report WAN IP Address by mail

# Config Environment Variables
Install package and update environemnt variables to the env file

* Env File : /etc/systemd/system.conf.d/10.default-env.conf
* Environment Variable (Encode using base64)
  * SMTP_SERVER="c210cC5nbWFpbC5jb20="
  * SMTP_AUTH=""
  * USER_EMAIL=""
  * IP_INFO_URL="aHR0cHM6Ly9pcGluZm8uaW8vaXA="
* Default Environment Variable (Decoded Value)
  * SMTP_SERVER="smtp.gmail.com"
  * IP_INFO_URL="https://ipinfo.io/ip"
