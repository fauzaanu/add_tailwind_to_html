import os
import glob
import argparse


def add_tailwind(directory):
    if not os.path.isdir(directory):
        return 'Directory does not exist', None

    html_files = glob.glob(directory + '/**/*.html', recursive=True)

    if not html_files:
        return 'No HTML files found',None

    tailwind_css = 'https://cdn.tailwindcss.com'
    successful_files, error_files = [], []

    for html_file in html_files:
        try:
            with open(html_file, 'r+') as f:
                html = f.read()

                update_html = f'<script src="{tailwind_css}"></script>'

                if '<head>' in html:
                    html = html.replace('<head>', f'<head>\n{update_html}')
                elif '<html>' in html:
                    html = html.replace('<html>', f'<html>\n{update_html}')
                else:
                    html = f'{update_html}\n{html}'

                f.seek(0)
                f.write(html)
                successful_files.append(html_file)

        except Exception as e:
            error_files.append((html_file, str(e)))

    return successful_files, error_files


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add tailwind css to html files')
    parser.add_argument('-d', '--directory', help='Directory to add tailwind to', required=True)
    args = parser.parse_args()
    successful_files, error_files = add_tailwind(args.directory)

    print(f'Successful files: {successful_files if successful_files else "None"}')
    print(f'Error files: {error_files if error_files else "None"}')
