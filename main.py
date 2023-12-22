import sqlite3

conn = sqlite3.connect('bd.db')
cursor = conn.cursor()

def add_sign(counter, temp):
    cursor.execute(
        __sql="""   
                    INSERT INTO stations (
                                 idstations,
                                 stname,
                                 year,
                                 month,
                                 day,
                                 hour,
                                 dirwind,
                                 precipit 
                                 temperature
                                 humidity
                            )
                            VALUES (
                                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                            );
        """
    )