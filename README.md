# HNG DevOps Stage 0 Task

INTRODUCTION:
Introduction As part of my DevOps learning journey, I was tasked with setting up and configuring NGINX on a fresh Ubuntu server. This task was designed to help me gain hands-on experience with web server configuration and deployment.
This hands-on experience helped me understand the basics of web server configuration, cloud infrastructure, and troubleshooting. In this blog, I will walk through my approach, key takeaways, and overall experience with this task.

APPROACH TO COMPLETING THE Task
1. To get started, I launched a new Ubuntu instance on AWS EC2. I ensured that the necessary security group rules were configured to allow HTTP (port 80) traffic so that my NGINX server would be accessible over the internet.

2. Using the terminal, I updated the package list and installed NGINX with the command
sudo apt upgrade && sudo apt update -y
sudo apt install nginx -y

3. Creating a Custom HTML Page: I created a simple HTML file at /var/www/html/index.html with the message: “Welcome to DevOps Stage 0 - Blessing Omoregie/Nixie”.
using the command:
sudo nano /var/www/html/index.html
I replaced the existing content with the following HTML:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Stage 0</title>
</head>
<body>
    <h1>Welcome to DevOps Stage 0 - Blessing Omoregie/Nixie</h1>
</body>
</html>
After saving the file, I restarted NGINX to apply the changes:
sudo systemctl restart nginx


Testing the Configuration: After ensuring NGINX was running, I accessed the server’s public IP in my browser and saw the custom page.
 
4. To verify that everything was working correctly, I accessed my server’s public IP address in a web browser:
http://54.234.149.56/

HOW THIS TASK CONTRIBUTE TO MY LEARNING AND PROFESSIONAL GOALS :

This task provided me with hands-on experience in:

Setting up and configuring a web server.
Managing system services using systemctl.
Deploying a simple static webpage on a cloud server.
Understanding Linux.

As a complete newbie with absolutely no knowledge in tech, understanding these fundamental DevOps skills is crucial as I continue my journey towards becoming a DevOps Engineer, and I must say these skills are invaluable.

CHALLENGES FACED:
As a complete newbie, it was quite hard for me, these are all really new concepts to me. I was initially using a virtual box, with help from youtube and friends, but my friends advised me to use a cloud provider.
I ended up using AWS with a lot of help from friends and Chatgpt, with their help, I didn't face any challenges and everything went very smooth.

REFRENCES :
• DevOps Engineers - https://hng.tech/hire/devops-engineers 
• Cloud Engineers - https://hng.tech/hire/cloud-engineers 
• Site Reliability Engineers - https://hng.tech/hire/site-reliability-engineers 
• Platform Engineers - https://hng.tech/hire/platform-engineers 
• Infrastructure Engineers - https://hng.tech/hire/infrastructure-engineers
• Kubernetes Specialists - https://hng.tech/hire/kubernetes-specialists 
• AWS Solutions Architects - https://hng.tech/hire/aws-solutions-architects 
• Azure DevOps Engineers - https://hng.tech/hire/azure-devops-engineers 
• Google Cloud Engineers - https://hng.tech/hire/google-cloud-engineers 
• CI/CD Pipeline Engineers - https://hng.tech/hire/ci-cd-pipeline-engineers 
• Monitoring/Observability Engineers - https://hng.tech/hire/monitoring-observability-engineers 
• Automation Engineers - https://hng.tech/hire/automation-engineers 
• Docker Specialists - https://hng.tech/hire/docker-specialists 
• Linux Developers - https://hng.tech/hire/linux-developers 
• PostgreSQL Developers - https://hng.tech/hire/postgresql-developers