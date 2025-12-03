import argparse
import shutil
import logging
from pathlib import Path

logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')

def parse_args():
    parser = argparse.ArgumentParser(description="Рекурсивно копіює та сортує файли за розширенням.")
    
    parser.add_argument(
        "source_dir", 
        type=Path,
        help="Шлях до вихідної директорії."
    )
    
    parser.add_argument(
        "dest_dir", 
        type=Path, 
        nargs='?',
        default="dist",
        help="Шлях до директорії призначення. За замовчуванням 'dist'."
    )
    
    args = parser.parse_args()
    return args

def copy_file(source_file: Path, dest_base_dir: Path):
    try:
        file_extension = source_file.suffix.lower().lstrip('.')
        
        if not file_extension:
            extension_folder = "no_extension"
        else:
            extension_folder = file_extension
        
        dest_subdir = dest_base_dir / extension_folder
        
        dest_subdir.mkdir(parents=True, exist_ok=True)
        
        dest_file_path = dest_subdir / source_file.name
        
        shutil.copy2(source_file, dest_file_path)
        print(f"Скопійовано: {source_file.name} -> {dest_subdir}")

    except PermissionError as e:
        logging.error(f"Помилка доступу при копіюванні {source_file}: {e}")
    except OSError as e:
        logging.error(f"Системна помилка при копіюванні {source_file}: {e}")
    except Exception as e:
        logging.error(f"Інша помилка при копіюванні {source_file}: {e}")


def recursive_copy_sort(current_dir: Path, dest_base_dir: Path):
    try:
        for item in current_dir.iterdir():
            
            if item.is_dir():
                recursive_copy_sort(item, dest_base_dir)
                
            elif item.is_file():
                copy_file(item, dest_base_dir)
            
    except PermissionError as e:
        logging.error(f"Помилка доступу до директорії {current_dir}: {e}")
    except Exception as e:
        logging.error(f"Інша помилка під час рекурсії в {current_dir}: {e}")


def main():
    args = parse_args()
    source_dir = args.source_dir
    dest_dir = args.dest_dir
    
    if not source_dir.is_dir():
        print(f"Помилка: Вихідна директорія '{source_dir}' не існує або не є директорією.")
        return

    try:
        dest_dir.mkdir(parents=True, exist_ok=True)
        print(f"Створена (або існує) директорія призначення: {dest_dir.resolve()}")
    except Exception as e:
        print(f"Не вдалося створити директорію призначення {dest_dir}: {e}")
        return

    print(f"\nПочаток копіювання та сортування з {source_dir.resolve()}...")
    
    recursive_copy_sort(source_dir, dest_dir)
    
    print("\nКопіювання та сортування завершено.")

if __name__ == "__main__":
    main()