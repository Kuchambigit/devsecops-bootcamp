
Linux Access Control and Least Privilege Lab
1. Lab Overview

Project: DevSecOps Hands-on & Interview Bootcamp
Environment: Proxmox VE — Ubuntu 26.04 LTS
Virtual Machine: VM 103
Hostname: Katud-ubuntu-edtechserver
Date: November 3, 2026
Lab Directory: /opt/devops-shared
Objective

The objective of this lab is to understand and implement Linux user management, group permissions, file ownership, and the principle of least privilege.

This lab demonstrates how DevSecOps engineers restrict access to sensitive directories and resources using Linux filesystem permissions.
2. Create a Linux User

A dedicated user named labuser was created to simulate a team member requiring access to shared resources.
Commands

# Create a new user with a home directory and Bash shell
sudo useradd -m -s /bin/bash labuser

# Verify that the user exists
id labuser

Result

The user was successfully created.

uid=1001(labuser) gid=1002(labuser) groups=1002(labuser)

Security Explanation

Creating individual user accounts allows administrators to assign permissions based on responsibilities rather than sharing administrator credentials.
3. Configure Group Membership

The existing devops-team group was used to manage access to shared resources.
Commands

# Verify that the group exists
getent group devops-team

# Add labuser to the group
sudo usermod -aG devops-team labuser

# Verify the user's group membership
id labuser

# Display the group's members
getent group devops-team

Result

devops-team:x:1001:labuser

The labuser account was successfully added to devops-team.
Security Explanation

Linux groups simplify access management by allowing administrators to grant permissions to multiple users through a common group.
4. Create a Shared Directory

A shared directory was created to simulate a protected DevOps workspace.
Commands

# Create the shared directory
sudo mkdir -p /opt/devops-shared

# Assign root ownership and the devops-team group
sudo chown root:devops-team /opt/devops-shared

# Verify directory ownership
ls -ld /opt/devops-shared

Security Explanation

The directory is owned by root, while its group ownership is assigned to devops-team.

This allows administrators to retain ownership while granting team members controlled access.
5. Configure Directory Permissions

The directory was configured to allow access only to the owner and authorized group members.
Commands

# Grant full permissions to the owner and group
# Deny access to all other users
sudo chmod 770 /opt/devops-shared

# Enable group inheritance for newly created files and directories
sudo chmod g+s /opt/devops-shared

# Verify the final permissions
ls -ld /opt/devops-shared

Expected Permissions

drwxrws--- root devops-team /opt/devops-shared

Permission Breakdown
Permission	Meaning
Owner: 7	Read, write, execute
Group: 7	Read, write, execute
Others: 0	No access
Setgid: s	New files inherit the directory's group
Security Explanation

These permissions restrict directory access to authorized users.

The setgid bit ensures that new files inherit the devops-team group, supporting consistent group ownership.

Note: Setgid controls group ownership, not the complete permissions of newly created files. File permissions also depend on the creating process and its umask.
6. Test Authorized Access

The next step was to verify that a member of devops-team could create a file inside the protected directory.
Commands

# Create a file using the labuser account
sudo -u labuser touch /opt/devops-shared/test-file.txt

# Verify the file and its ownership
sudo ls -l /opt/devops-shared/

Result

-rw-r--r-- 1 labuser devops-team 0 Nov 3 07:22 test-file.txt

Observation

The test succeeded.

    labuser created the file.

    The file owner is labuser.

    The file inherited the devops-team group.

This confirms that group-based access is working.
7. Test Unauthorized Access

The next test verified whether the katud account could create files in the protected directory without administrative privileges.

The katud account was not a member of devops-team.
Commands

# Attempt to access the protected directory
ls -l /opt/devops-shared/

# Attempt to create a file without sudo
touch /opt/devops-shared/unauthorized.txt

# Attempt to create another unauthorized file
touch /opt/devops-shared/access-denied-test.txt

# Verify the directory contents using administrative privileges
sudo ls -l /opt/devops-shared/

Results

The directory listing without sudo returned:

ls: cannot open directory '/opt/devops-shared/': Permission denied

The unauthorized file operations returned:

touch: setting times of '/opt/devops-shared/unauthorized.txt': Permission denied

touch: setting times of '/opt/devops-shared/access-denied-test.txt': Permission denied

The final administrator-level listing showed:

total 0
-rw-r--r-- 1 labuser devops-team 0 Nov 3 07:22 test-file.txt

Observation

The unauthorized file operations were denied.

Neither attempted file appeared in the final directory listing.

This confirms that the directory's access restrictions prevented katud from creating files.
8. Principle of Least Privilege

The principle of least privilege means granting users only the permissions necessary to perform their assigned tasks.
Implementation
User	Access	Result
root	Administrative access	Allowed
labuser	Member of devops-team	Allowed
katud	Not a member of devops-team	Denied
DevSecOps Relevance

Least privilege is important for:

    Restricting unauthorized access to application files.

    Protecting deployment configurations and scripts.

    Reducing the impact of compromised accounts.

    Enforcing separation of duties.

    Supporting secure infrastructure administration.

9. Lessons Learned

During this lab, I gained practical experience with:

    Creating and managing Linux users.

    Managing Linux group membership.

    Configuring file and directory ownership.

    Understanding chmod and chown.

    Applying setgid for group inheritance.

    Testing permissions using different user accounts.

    Troubleshooting permission-denied errors.

    Implementing least-privilege access controls.

I also learned that Linux permissions can restrict access to resources even when users share the same server.
10. Security Best Practices

The following practices are important when managing Linux systems:

    Avoid using root privileges for routine tasks.

    Assign permissions through groups where appropriate.

    Avoid unnecessarily permissive settings such as chmod 777.

    Review user and group membership regularly.

    Protect sensitive configuration files.

    Validate permissions by testing both authorized and unauthorized access.

    Document configuration changes for troubleshooting and auditing.

11. Lab Conclusion

This lab successfully demonstrated Linux user management, group-based access control, directory permissions, and the principle of least privilege.

An authorized user successfully created a file in a protected directory, while an unauthorized user was denied access.

These techniques are foundational to securing Linux servers, CI/CD environments, application deployments, and DevSecOps infrastructure.

Lab Status: COMPLETED
