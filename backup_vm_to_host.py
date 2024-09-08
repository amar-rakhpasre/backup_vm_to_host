import shutil
import datetime
import os

def backup_files(source, destination):
    # Ensure destination directory exists
    if not os.path.exists(destination):
        os.makedirs(destination)
    #today = datetime.date.today()
    now = datetime.datetime.now()
    backup_file_name = os.path.join(destination, f"backup_vm_To_Host_{now.strftime('%Y%m%d_%H%M%S')}")  # Generate the backup file name
    shutil.make_archive(backup_file_name, 'gztar', source)  # Create a gzipped tar archive

# Define source and destination directories
source = "/home/vagrant/python-learning"
destination = "/vagrant/backup_folder"  # Synced folder on the host machine

backup_files(source, destination)

