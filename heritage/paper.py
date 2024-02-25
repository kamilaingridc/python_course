# reserve fot heritage
# class mom
class Paper():
    _content = ''
    _size = 200

    def write(self, message):
        if len(self._content + message) <= self._size:
            self._content += message
        else:
            print("It doesn't fit.")

    def read(self):
        return self._content
