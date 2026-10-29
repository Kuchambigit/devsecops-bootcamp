
Linux File Permissions and Ownership Lab
Objective

Understand Linux file permissions, ownership, and access control as part of DevSecOps security best practices.
Lab Environment

    Hypervisor: Proxmox VE

    Operating System: Ubuntu Linux

    Virtual Machine: VM 103

    User: katud

    Project: DevSecOps Bootcamp

Lab 1: Creating a File

Created a configuration file using:

touch app-config.txt
ls -l app-config.txt

The ls -l command displays file permissions, ownership, and other file information.
Lab 2: Modifying File Permissions

Practiced the following permission settings:

chmod 600 app-config.txt
chmod 640 app-config.txt
chmod 755 deploy.sh
chmod 750 deploy.sh

Permission explanations:

    600: Owner can read and write; nobody else has access.

    640: Owner can read and write; group can read.

    755: Owner has full access; group and others can read and execute.

    750: Owner has full access; group can read and execute; others have no access.

Lab 3: File Ownership

Practiced restoring ownership:

sudo chown katud:katud deploy.sh
ls -l deploy.sh

The chown command changes file ownership.
Lab 4: Testing Script Execution

Executed the deployment test script:

./deploy.sh

Result:

DevSecOps deployment test successful

The script executed successfully with permissions set to 750.
DevSecOps Security Lessons

    Apply the principle of least privilege.

    Restrict unauthorized access to configuration files.

    Control who can modify and execute deployment scripts.

    Use file ownership and group permissions to enforce access control.

    Avoid granting unnecessary permissions to users and services.

Conclusion

Successfully practiced Linux file permissions, ownership management, and script execution.

These concepts help secure Linux servers, CI/CD environments, and deployment automation.

