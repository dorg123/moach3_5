class FileReader:
    def __init__(self, filename):
        self._filename = filename
        self._read()

    @property
    def filename(self):
        return self._filename

    @property
    def data(self):
        return self._data

    def __getitem__(self, item):
        try:
            return self._data[item]
        except KeyError:
            return None
        except IndexError:
            return None

    def __str__(self):
        return 'fasta.FileReader: {}, {} entries' \
            .format(self._filename, len(self._data))

    def __repr__(self):
        return 'fasta.FastaReader({})<length: {}>' \
            .format(self._filename, len(self._data))


class FastaReader(FileReader):
    def _read(self, read_head=lambda x: x):
        with open(self._filename, 'r') as f:
            lines = list(line.rstrip('\n') for line in f.readlines())
        info = None
        self._data = dict()
        for line in lines:
            if line.startswith('>'):
                info = read_head(line.lstrip('>'))
            else:
                self._data[info] = self._data.get(info, '') + line

    @staticmethod
    def read_head(head, raw=False):
        parts = head.split('|')
        if raw:
            return dict(zip(range(len(parts)), parts))

        def find_all(s, sub):
            index = [s.find(sub)]
            while index[-1] != -1:
                index.append(s.find(sub, index[-1] + 1))
            index.pop()
            return index

        last = parts[-1]
        d = dict((parts[i], parts[i + 1]) for i in range(0, len(parts) - 1, 2))
        if '=' in last:
            separators = [0] + list(last.rfind(' ', 0, i) for i in find_all(last, '=')) + [len(last)]
            parts = list(last[separators[i - 1]:separators[i]].strip() for i in range(1, len(separators)))
            d.update(dict((part[:part.find('=')], part.split('=')[1]) if '=' in part else (0, part) for part in parts))
        return d

    def __str__(self):
        return 'fasta.FastaReader: {}, {} entries' \
            .format(self.filename, len(self.data))

    def __repr__(self):
        return 'fasta.FastaReader({})<length: {}>' \
            .format(self.filename, len(self.data))