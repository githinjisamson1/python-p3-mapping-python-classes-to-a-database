from config import CONN, CURSOR


class Song:
    # !default id to None
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    # !job of class to create table
    @classmethod
    def create_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS songs(
            id INTEGER PRIMARY KEY,
            name TEXT,
            album TEXT
            )'''

        CURSOR.execute(sql)

    # !keep __init__() and save() separate
    def save(self):
        # use ? placeholders to prevent SQL injections
        sql = "INSERT INTO songs (name, album) VALUES (?, ?)"
        val = (self.name, self.album)

        CURSOR.execute(sql, val)

        # effect changes
        # CONN.commit()

        # !get and update id
        self.id = CURSOR.execute(
            "SELECT last_insert_rowid() FROM songs").fetchone()[0]

    # !implementing DRY/return song to work with
    @classmethod
    def create(cls, name, album):
        # instance
        song = Song(name, album)
        song.save()
        return song

# Song.create_table()

# !repetitive
# song1 = Song("NewSong", "NewAlbum")
# song1.save()
# song1.id

# song = Song.create("Hello", "25")
# song.name
