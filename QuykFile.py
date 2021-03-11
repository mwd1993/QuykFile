import os
import time

class QuykFile:
    """
    QuykFile Class:\n
    Allows easy file manipulation:\n
    \n
    qf = QuykFile('path/to/file.txt')\n
    if qf:
    \t  qf.write('QuykFile!')\n
    \t  read = qf.read()\n
    \t  read_list = qf.read(as_list=True)\n
    \t  qf.rename('file_renamed.txt')\n
    \t  print(str(qf.file_data))

    """

    def __init__(self, path, as_full_dir=False, force_create=False):
        self.success = False
        self.file_data = {
            'full': '',
            'path': '',
            'name': ''
        }

        if force_create:
            if as_full_dir:
                full_path = path
            else:
                full_path = os.getcwd() + '/' + path

            if os.path.isfile(full_path):
                _path, _file = os.path.split(full_path)
                if _path:
                    self.file_data['path'] = _path
                else:
                    self.file_data['path'] = _path
                self.file_data['name'] = _file
                self.file_data['full'] = full_path
                self.success = True
            else:
                _path, _file = os.path.split(full_path)
                self.file_data['path'] = _path
                self.file_data['name'] = _file
                self.file_data['full'] = path
                if _path:
                    if os.path.isdir(_path) is False:
                        os.mkdir(_path)

                if os.path.isfile(full_path) is False:
                    f = open(full_path, 'w+')
                    f.close()
                    while os.path.isfile(full_path) is False:
                        time.sleep(1.5)

                if os.path.isfile(full_path):
                    self.success = True

            if self.success is False:
                print('QuykFile - Error could not create a valid object for ( Dir Creation Failed ) :\n' + full_path)
        else:
            _reason = ""
            if as_full_dir:
                full_path = path
            else:
                full_path = os.getcwd() + '/' + path

            if os.path.isfile(full_path):
                _path, _file = os.path.split(full_path)
                if _path:
                    self.file_data['path'] = _path
                else:
                    self.file_data['path'] = _path
                self.file_data['name'] = _file
                self.file_data['full'] = full_path
                self.success = True
            else:
                self.success = False
                _reason = "( No Such File )"

            if self.success is False:
                print('QuykFile - Error could not create a valid object ' + _reason + ':\n' + full_path)

    def read(self, as_list=False):
        if self.success:
            f = open(self.file_data['full'])
            r = f.read()
            f.close()
            if as_list:
                r = r.split('\n')
            return r

    def write(self, text):
        if self.success:
            _type = str(type(text))
            if 'str' in _type:
                f = open(self.file_data['full'], 'w')
                f.write(text)
                f.close()
            elif 'list' in _type:
                f = open(self.file_data['full'], 'w')
                t = '\n'.join(text)
                f.write(t)
                f.close()

    def append(self, text, as_new_line=True, before=False):
        if self.success:
            _type = str(type(text))
            if 'str' in _type:
                f = open(self.file_data['full'], 'a')
                if as_new_line:
                    text = '\n' + text
                f.write(text)
                f.close()
            elif 'list' in _type:
                f = open(self.file_data['full'], 'a')
                _text = '\n'.join(text)

                if as_new_line:
                    text = '\n' + _text
                else:
                    text = _text

                f.write(text)
                f.close()

    def insert(self, text, line_index: int):
        if self.success:
            _type = str(type(text))
            if 'str' in _type:
                rl = self.read(as_list=True)
                rl.insert(line_index, text)
                f = open(self.file_data['full'], 'w')
                t = '\n'.join(rl)
                f.write(t)
                f.close()

            elif 'list' in _type:
                pass

    def copy_to(self, path, as_full_dir=False):
        if self.success:
            c = self.read()
            if c:
                if as_full_dir is False:
                    path = os.getcwd() + '/' + path

                _path, _file = os.path.split(path)
                if os.path.isdir(_path):
                    f = open(path, 'w+')
                    f.write(c)
                    f.close()
                    return True

        return False

    def rename(self, name):
        if self.success:
            if self.copy_to(name):
                os.remove(self.file_data['full'])
                n_replace = self.file_data['name']
                self.file_data['full'] = self.file_data['full'].replace(n_replace, name)
                self.file_data['name'] = name
                print(str(self.file_data))
                return True
        return False

    def delete(self):
        if self.success:
            os.remove(self.file_data['full'])
            self.file_data = {}
            self.success = False