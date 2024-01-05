# Add Tailwind to HTML Script

This script allows you to add Tailwind CSS to HTML files within a specified directory.

## Requirements

- None, Very Vanilla

## How to run the script

1. Open your terminal.

2. Navigate to the directory where your script is located.
```bash
cd path_to_your_directory
```
3. Run the script with the `-d` or `--directory` option followed by the path to the directory where you wish to add the Tailwind CSS.
```bash
python3 add_tailwind.py -d path_to_directory
```
For example:
```bash
python3 add_tailwind.py -d /Users/user/Desktop/MyWebsite
```
##  Output

The script will add a `<script>` tag referencing the Tailwind CSS CDN to all `.html` files within the given directory. This tag will be placed within the `<head>` tag if it exists; if not, it will be placed after the `<html>` tag. If neither exist, the `<script>` tag will be placed at the very beginning of the file.

Once the script has run, it will output a list of files where the insertion was successful and a list of files where it failed (if there were any failures). Each failure will be accompanied by an error message providing more details about the problem.

Here's an example of what the output might look like:
```bash
Successful files: ['index.html', 'about.html'] Error files: [('contact.html', 'Permission denied'), ('blog.html', 'No such file or directory')]
```
## Error Handling

In case of an error such as 'Directory does not exist' or 'No HTML files found', the script will terminate and display an appropriate error message.