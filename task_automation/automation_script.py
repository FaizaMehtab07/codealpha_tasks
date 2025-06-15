import os
import shutil
import csv
import pandas as pd
import smtplib
from email.message import EmailMessage
from PIL import Image
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import logging

def setup_logging():
    logging.basicConfig(
        filename='automation_log.txt',
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

def prompt_folder_path():
    while True:
        path = input("Enter the folder path: ").strip()
        if os.path.isdir(path):
            return path
        else:
            print("Invalid folder path. Please try again.")

def file_organization():
    """
    Organize files in a folder by their extensions into subfolders.
    """
    folder = prompt_folder_path()
    logging.info(f"Organizing files in folder: {folder}")

    # Define mapping of extensions to folder names
    ext_map = {
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
        'Music': ['.mp3', '.wav', '.aac', '.flac'],
        'Scripts': ['.py', '.js', '.sh', '.bat', '.pl'],
        'Others': []
    }

    moved_files_count = {}

    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            ext = os.path.splitext(filename)[1].lower()
            moved = False
            for folder_name, extensions in ext_map.items():
                if ext in extensions:
                    dest_folder = os.path.join(folder, folder_name)
                    if not os.path.exists(dest_folder):
                        os.makedirs(dest_folder)
                    shutil.move(filepath, os.path.join(dest_folder, filename))
                    moved_files_count[folder_name] = moved_files_count.get(folder_name, 0) + 1
                    logging.info(f"Moved file {filename} to {folder_name}")
                    moved = True
                    break
            if not moved:
                # Move to Others folder
                dest_folder = os.path.join(folder, 'Others')
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                shutil.move(filepath, os.path.join(dest_folder, filename))
                moved_files_count['Others'] = moved_files_count.get('Others', 0) + 1
                logging.info(f"Moved file {filename} to Others")

    logging.info("File organization complete.")
    logging.info("Summary of files moved:")
    for folder_name, count in moved_files_count.items():
        logging.info(f"{folder_name}: {count} files")

def data_cleaning():
    """
    Clean a CSV file by removing duplicates and null rows.
    """
    while True:
        csv_path = input("Enter the path to the CSV file: ").strip()
        if os.path.isfile(csv_path) and csv_path.lower().endswith('.csv'):
            break
        else:
            print("Invalid CSV file path. Please try again.")

    df = pd.read_csv(csv_path)
    logging.info(f"Original data rows: {len(df)}")

    df_cleaned = df.drop_duplicates()
    logging.info(f"Rows after removing duplicates: {len(df_cleaned)}")

    df_cleaned = df_cleaned.dropna()
    logging.info(f"Rows after removing nulls: {len(df_cleaned)}")

    output_path = input("Enter output CSV file path (or press Enter to overwrite original): ").strip()
    if not output_path:
        output_path = csv_path

    df_cleaned.to_csv(output_path, index=False)
    logging.info(f"Cleaned data saved to {output_path}")

def bulk_rename():
    """
    Rename all files in a folder with a consistent naming pattern.
    """
    folder = prompt_folder_path()
    prefix = input("Enter the prefix for new filenames: ").strip()
    start_num = input("Enter the starting number (default 1): ").strip()
    try:
        start_num = int(start_num)
    except:
        start_num = 1

    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    files.sort()
    logging.info(f"Renaming {len(files)} files in {folder}")

    for i, filename in enumerate(files, start=start_num):
        ext = os.path.splitext(filename)[1]
        new_name = f"{prefix}{i}{ext}"
        src = os.path.join(folder, filename)
        dst = os.path.join(folder, new_name)
        os.rename(src, dst)
        logging.info(f"Renamed {filename} to {new_name}")

    logging.info("Bulk renaming complete.")

def system_cleanup():
    """
    Clear temp folders and show disk space.
    """
    import tempfile
    import platform
    import shutil

    temp_dir = tempfile.gettempdir()
    logging.info(f"Clearing temp directory: {temp_dir}")

    try:
        for filename in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                    logging.info(f"Deleted file {file_path}")
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    logging.info(f"Deleted directory {file_path}")
            except Exception as e:
                logging.warning(f"Failed to delete {file_path}. Reason: {e}")
    except Exception as e:
        logging.error(f"Error accessing temp directory: {e}")

    # Show disk space
    if platform.system() == 'Windows':
        import ctypes
        free_bytes = ctypes.c_ulonglong(0)
        total_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(os.path.abspath(os.sep)), None, ctypes.pointer(total_bytes), ctypes.pointer(free_bytes))
        logging.info(f"Disk space on {os.path.abspath(os.sep)}: Free {free_bytes.value / (1024**3):.2f} GB / Total {total_bytes.value / (1024**3):.2f} GB")
    else:
        st = os.statvfs('/')
        free = st.f_bavail * st.f_frsize
        total = st.f_blocks * st.f_frsize
        logging.info(f"Disk space on /: Free {free / (1024**3):.2f} GB / Total {total / (1024**3):.2f} GB")

def auto_email_sender():
    """
    Send an email via SMTP with user inputs.
    """
    smtp_server = input("Enter SMTP server (e.g. smtp.gmail.com): ").strip()
    smtp_port = input("Enter SMTP port (e.g. 587): ").strip()
    try:
        smtp_port = int(smtp_port)
    except:
        logging.error("Invalid port number.")
        return

    sender_email = input("Enter sender email address: ").strip()
    password = input("Enter sender email password (input will be visible): ").strip()
    receiver_email = input("Enter receiver email address: ").strip()
    subject = input("Enter email subject: ").strip()
    body = input("Enter email body: ").strip()

    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        logging.info("Email sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

def image_resizing():
    """
    Resize all images in a folder to a specified max width or height.
    """
    folder = prompt_folder_path()
    max_size = input("Enter max size (pixels) for width/height (e.g. 800): ").strip()
    try:
        max_size = int(max_size)
    except:
        logging.error("Invalid size input.")
        return

    supported_exts = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']
    images = [f for f in os.listdir(folder) if os.path.splitext(f)[1].lower() in supported_exts]

    logging.info(f"Resizing {len(images)} images in {folder} to max {max_size}px")

    for img_name in images:
        img_path = os.path.join(folder, img_name)
        try:
            with Image.open(img_path) as img:
                img.thumbnail((max_size, max_size))
                img.save(img_path)
            logging.info(f"Resized {img_name}")
        except Exception as e:
            logging.warning(f"Failed to resize {img_name}: {e}")

    logging.info("Image resizing complete.")

def pdf_merge_split():
    """
    Merge or split PDFs in a folder.
    """
    folder = prompt_folder_path()
    choice = input("Enter 'm' to merge all PDFs or 's' to split a PDF: ").strip().lower()
    if choice == 'm':
        merger = PdfFileMerger()
        pdfs = [f for f in os.listdir(folder) if f.lower().endswith('.pdf')]
        pdfs.sort()
        if not pdfs:
            logging.info("No PDF files found to merge.")
            return
        for pdf in pdfs:
            merger.append(os.path.join(folder, pdf))
            logging.info(f"Added {pdf} to merger")
        output_path = input("Enter output merged PDF filename (e.g. merged.pdf): ").strip()
        if not output_path.lower().endswith('.pdf'):
            output_path += '.pdf'
        merger.write(os.path.join(folder, output_path))
        merger.close()
        logging.info(f"Merged PDF saved as {output_path}")
    elif choice == 's':
        pdf_file = input("Enter the PDF filename to split: ").strip()
        pdf_path = os.path.join(folder, pdf_file)
        if not os.path.isfile(pdf_path) or not pdf_file.lower().endswith('.pdf'):
            logging.error("Invalid PDF file.")
            return
        try:
            pdf_reader = PdfFileReader(pdf_path)
            num_pages = pdf_reader.getNumPages()
            output_folder = os.path.join(folder, 'split_pages')
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            for i in range(num_pages):
                pdf_writer = PdfFileWriter()
                pdf_writer.addPage(pdf_reader.getPage(i))
                output_filename = os.path.join(output_folder, f"{os.path.splitext(pdf_file)[0]}_page_{i+1}.pdf")
                with open(output_filename, 'wb') as out_f:
                    pdf_writer.write(out_f)
                logging.info(f"Created {output_filename}")
            logging.info(f"Split PDF pages saved in {output_folder}")
        except Exception as e:
            logging.error(f"Failed to split PDF: {e}")
    else:
        logging.info("Invalid choice. Exiting PDF merge/split.")

def main():
    setup_logging()
    logging.info("Welcome to the Automation Script!")
    logging.info("Select a task to automate:")
    logging.info("1. File Organization")
    logging.info("2. Data Cleaning (CSV)")
    logging.info("3. Bulk File Renaming")
    logging.info("4. System Cleanup (temp folders)")
    logging.info("5. Auto Email Sender (SMTP)")
    logging.info("6. Image Resizing")
    logging.info("7. PDF Merging or Splitting")
    choice = input("Enter the number of your choice: ").strip()

    if choice == '1':
        file_organization()
    elif choice == '2':
        data_cleaning()
    elif choice == '3':
        bulk_rename()
    elif choice == '4':
        system_cleanup()
    elif choice == '5':
        auto_email_sender()
    elif choice == '6':
        image_resizing()
    elif choice == '7':
        pdf_merge_split()
    else:
        logging.info("Invalid choice. Exiting.")

    logging.info("Script finished.")

if __name__ == "__main__":
    main()
