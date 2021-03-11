# QuykFile
Quickly do file related things in Python.

# Examples

```python
import QuykFile

f = QuykFile('path/to/file.txt') # Create a QuykFile object which takes a path to a file

print(f.success) # boolean if class file is valid

if f.success is False: # assume the file doesn't exist
	f = QuykFile('path/to/file.txt', force_create=True) # force create the file

text_to_write = 'Hello '
f.write(text_to_write)
f.append('World', as_new_line=False) # append to same line
f.append('hello World 2') # default call appends to a new line
f.insert('Text at the top of the file..',0) # put at the top, 0 based index

print(f.read()) # return file contents as string
print(f.read(as_list=True)) # return file contetns as a list instead

f.copy_to('copied file.txt') # copy to relative path
f.copy_to(os.getcwd() +'/new path/copied.txt', as_full_dir=True) # copy to full path
f.rename('some new file name.txt') # Rename file
f.delete() # remove the file from the os

print(f.file_data)
print(f.file_data['full'] + '\n' + f.file_data['path'] + '\n' + f.file_data['name'])
```