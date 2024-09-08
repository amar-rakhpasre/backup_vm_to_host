To take a backup of files from your Vagrant VM to your host machine, I'll guide you through the entire process step-by-step. We will create a Python script to automate the backup and configure Vagrant properly to sync folders between the VM and host.

### Step 1: Configure Vagrant for Synced Folders

First, ensure that your Vagrant VM is set up to sync a folder between the VM and your host machine.

1. **Open Your `Vagrantfile`:**
   - Locate the `Vagrantfile` in the directory where your Vagrant environment is set up. If you're unsure where this is, you can use `vagrant global-status` to find it.

2. **Edit the `Vagrantfile`:**
   - Add or update the synced folder configuration. For example, to sync a folder on your host (`C:\Users\rakhp\Desktop\test_backup`) with `/vagrant` in the VM:

   ```ruby
   Vagrant.configure("2") do |config|
     config.vm.box = "hashicorp/bionic64"
     config.vm.network "forwarded_port", guest: 8000, host: 8000
     config.vm.provision "shell", path: "provision1.sh"
     config.vm.synced_folder "C:/Users/rakhp/Desktop/test_backup", "/vagrant"
   end
   ```

3. **Reload the Vagrant VM:**
   - Save the `Vagrantfile` and run the following command to apply the changes:

   ```bash
   vagrant reload
   ```

### Step 2: Create the Python Backup Script

Next, we’ll create a Python script inside your Vagrant VM that will handle the backup.

1. **SSH into the VM:**
   - If you're not already inside the VM, SSH into it:

   ```bash
   vagrant ssh
   ```

2. **Navigate to the Desired Directory:**
   - Move to the directory where you want to place your backup script. For instance:

   ```bash
   cd /home/vagrant/python-learning
   ```

3. **Create the Backup Script:**
   - Open a text editor like `nano` to create your Python script:

   ```bash
   nano backup_vm_to_host.py
   ```

   - Add the following Python code:

   ```python
   import shutil
   import datetime
   import os

   def backup_files(source, destination):
   # Ensure destination directory exists
   if not os.path.exists(destination):
   os.makedirs(destination)
    
   # Get current date and time for a unique filename
   now = datetime.datetime.now()
   backup_file_name = os.path.join(destination, 
   f"backup_vm_To_Host_{now.strftime('%Y%m%d_%H%M%S')}")
    
   # Create a gzipped tar archive
   shutil.make_archive(backup_file_name, 'gztar', source)

   # Define source and destination directories
   source = "/home/vagrant/python-learning"
   destination = "/vagrant/backup_folder"  # Synced folder on the host machine
  
   backup_files(source, destination)

   ```   

4. **Save and Exit:**
   - Press `CTRL + O` to save the file, and `CTRL + X` to exit `nano`.

### Step 3: Run the Backup Script

1. **Ensure the Synced Folder Exists:**
   - Make sure that the destination folder exists on your host machine. The script will create it if it doesn't, but it's good to verify.

   - On the host machine, check `C:\Users\rakhp\Desktop\test_backup\backup_folder`.

2. **Run the Script in the VM:**
   - Execute the Python script inside the VM:

   ```bash
   python3 backup_vm_to_host.py
   ```

3. **Check the Backup on the Host Machine:**
   - After running the script, check the `C:\Users\rakhp\Desktop\test_backup\backup_folder` directory on your host machine to ensure the backup files were created.

### Step 4: Automate or Schedule Backups (Optional)

If you want to automate the backup process, you can set up a cron job in the VM:

1. **Edit Crontab:**
   - Open the cron jobs list:

   ```bash
   crontab -e
   ```

2. **Add a Cron Job:**
   - Schedule the Python script to run at a specific time (e.g., every day at midnight):

   ```bash
   0 0 * * * /usr/bin/python3 /home/vagrant/python-learning/backup_vm_to_host.py
   ```

   - Save and exit the crontab editor.

### Summary

- **Synced Folder**: Ensure Vagrant is configured to sync the folder between your VM and host.
- **Backup Script**: Write a Python script to create backups and place them in the synced folder.
- **Run & Verify**: Execute the script and verify the backup on your host machine.

Following these steps will ensure that your VM's files are regularly backed up to your host machine.
