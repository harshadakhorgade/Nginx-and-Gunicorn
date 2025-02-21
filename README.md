

# Deploy Django Application using Gunicorn & Nginx in Production on AWS Ubuntu Server  

## **1. Update and Install Dependencies**  
```bash
sudo apt update
sudo apt install python3-pip python3-dev nginx
```

## **2. Install Virtual Environment**  
```bash
sudo pip3 install virtualenv    
sudo apt install python3-virtualenv
```

## **3. Clone the Repository**  
```bash
git clone https://github.com/harshadakhorgade/ASG-and-Load-Blanacer.git
```
### If you face a fatal error while cloning:
```bash
rm -rf ASG-and-Load-Blanacer  
# Then try cloning again
git clone https://github.com/harshadakhorgade/ASG-and-Load-Blanacer.git
```

```bash
cd ASG-and-Load-Blanacer
```

## **4. Create and Activate Virtual Environment**  
```bash
virtualenv env
source env/bin/activate
```

## **5. Install Required Dependencies**  
```bash
pip install -r requirements.txt
pip install Django gunicorn
```

## **6. Run Migrations and Collect Static Files**  
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```

## **7. Configure Gunicorn**  

### **7.1 Create Gunicorn Socket File**
```bash
sudo vim /etc/systemd/system/gunicorn.socket
```
Add the following content:
```
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

### **7.2 Create Gunicorn Service File**
```bash
sudo vim /etc/systemd/system/gunicorn.service
```
Add the following content:
```
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/ASG-and-Load-Blanacer
ExecStart=/home/ubuntu/ASG-and-Load-Blanacer/env/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          mysite.wsgi:application

[Install]
WantedBy=multi-user.target
```

### **7.3 Start and Enable Gunicorn**
```bash
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
```

## **8. Configure Nginx**  

### **8.1 Remove Default Config**
```bash
cd /etc/nginx/sites-enabled/
ls
sudo rm -r default
cd ..
cd ..
```

### **8.2 Create Nginx Configuration File**
```bash
sudo vim /etc/nginx/sites-available/asg
```
Add the following content:
```
server {
    listen 80 default_server;
    server_name 13.126.190.56;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        root /home/ubuntu/ASG-and-Load-Blanacer;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```

### **8.3 Enable Nginx Configuration**
```bash
sudo ln -s /etc/nginx/sites-available/asg /etc/nginx/sites-enabled/
```

### **8.4 Check User and Add to Group**
```bash
whoami
sudo gpasswd -a www-data username
```

### **8.5 Test and Restart Nginx**
```bash
sudo nginx -t
sudo systemctl restart nginx
```

## **9. Restart Gunicorn and Nginx**
### **9.1 Activate Virtual Environment**
```bash
cd ASG-and-Load-Blanacer
source env/bin/activate
```
### **9.2 Restart Services**
```bash
sudo service gunicorn restart
sudo service nginx restart
```

## **10. Update Nginx Configuration (If Needed)**
```bash
sudo vim /etc/nginx/sites-available/asg
```
Change `/static/` to `/staticfiles/` if required.

## **11. Fix Home Page Issue (If Needed)**
```bash
mv Templates templates
```

---

This **README.md** covers all the steps and ensures that nothing is skipped. 🚀 Let me know if you need any modifications!
