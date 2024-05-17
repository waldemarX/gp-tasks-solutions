import os
import time

SECONDS_IN_DAY = 86400


def delete_old_files_in_folder(folder_path, days):
    cutoff_time = time.time() - days * SECONDS_IN_DAY

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            file_mod_time = os.path.getmtime(file_path)

            if file_mod_time < cutoff_time:
                os.remove(file_path)


def delete_old_files_in_folder_and_inner_folders(folder_path, days):
    cutoff_time = time.time() - days * SECONDS_IN_DAY

    for root, _, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_mod_time = os.path.getmtime(file_path)

            if file_mod_time < cutoff_time:
                os.remove(file_path)


def main():
    folder_path = "C:\\Example\\Example\\Example"
    days = 10
    delete_old_files_in_folder(folder_path, days)
    delete_old_files_in_folder_and_inner_folders(folder_path, days)


if __name__ == "__main__":
    main()
