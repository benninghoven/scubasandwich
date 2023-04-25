import os

def delete_ds_store_files():
    """
    Recursively deletes all .DS_Store files in the parent directory and its subdirectories
    """
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))  # get the parent directory
    for root, dirs, files in os.walk(parent_dir):
        for name in files:
            if name == ".DS_Store":
                os.remove(os.path.join(root, name))
                print(f"Deleted file: {os.path.join(root, name)}")

if __name__ == "__main__":
    delete_ds_store_files()

