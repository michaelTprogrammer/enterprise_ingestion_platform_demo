
import shutil
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

def simulate_download_from_sharepoint(source_dir='sharepoint_mock', target_dir='data'):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for file_name in os.listdir(source_dir):
        if file_name.endswith('.xlsx') or file_name.endswith('.csv'):
            src = os.path.join(source_dir, file_name)
            dst = os.path.join(target_dir, file_name)
            shutil.copyfile(src, dst)
            logging.info(f"✅ Downloaded: {file_name} → {target_dir}")

if __name__ == '__main__':
    simulate_download_from_sharepoint()
